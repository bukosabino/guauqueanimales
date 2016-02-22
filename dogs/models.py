# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from dogs.utils import *
from django.conf import settings
import threading
from django.core.mail import EmailMessage
from easy_thumbnails.fields import ThumbnailerImageField, ThumbnailerField
from django.core.urlresolvers import reverse


# send tweets in background
def thread_send_tweet(message, photo):

    if settings.DEBUG:
        pass
    else:
        #deprecated
        settings.TWITTER.update_status_with_media(status=message, media=photo)


def thread_send_email(email):
    email.send()


# resize image in background
def resize_image(path):
    from PIL import Image
    img = Image.open(path)
    ancho = img.size[0]
    alto = img.size[1]
    minus_quality = 0

    while(True):
        if ancho > 750 and alto > 750:
            ancho = ancho / 2
            alto = alto / 2
            if minus_quality < 30:
                minus_quality += 10
        else:
            break

    # New image size
    img = img.resize((ancho, alto))
    img.save(path, quality=50-minus_quality)
    img.close()


class Dog(models.Model):

    race = models.CharField(verbose_name=_(u'Raza'), max_length=200,
                                blank=False, null=False, choices=CH_DOGS_RACES,
                                default='Mestizo')

    age = models.CharField(verbose_name=_(u'Edad'), max_length=200,
                            help_text=_(u'Por ejemplo: 2 meses'), blank=True,
                            null=True)

    image = models.ImageField(upload_to='dogs', verbose_name=_(u'Imagen'),
                                null=False, blank=False, max_length=None)

    thumbnail_url = models.URLField(null=True, blank=True)

    animal = models.CharField(verbose_name=_(u'Tipo de animal'), max_length=60,
                                blank=False, null=False, choices=CH_ANIMAL,
                                default='Perro')

    genre = models.CharField(verbose_name=_(u'Sexo'), max_length=60,
                                blank=False, null=False, choices=CH_GENRE,
                                default='Desconocido')

    state = models.CharField(verbose_name=_(u'País'), max_length=200,
                                blank=False, null=False, choices=CH_STATE,
                                default='España')

    city = models.CharField(verbose_name=_(u'Ciudad'), max_length=200,
                                blank=True, null=True)

    town = models.CharField(verbose_name=_(u'Población'), max_length=200,
                                blank=True, null=True)

    description = models.TextField(verbose_name=_(u'Descripción'), blank=True,
                                        null=True)

    email = models.EmailField(verbose_name=_(u'Correo Electrónico'),
                                blank=True, null=True)

    phone = models.CharField(verbose_name=_(u'Teléfono de Contacto'),
                                max_length=50, blank=True, null=True)

    date_created = models.DateTimeField(null=False, auto_now_add=True)

    date_updated = models.DateTimeField(null=False, auto_now=True)

    def __unicode__(self):

        return (unicode(self.id) + ' - ' + unicode(self.race) + ' - '
                + unicode(self.city))

    def save(self, *args, **kwargs):

        new_dog = False
        if self.pk == None:
            new_dog = True

        super(Dog, self).save(*args, **kwargs)

        if new_dog:

            from easy_thumbnails.files import get_thumbnailer
            options = {'size': (100, 100), 'crop': True} #quality:85
            self.thumbnail_url = get_thumbnailer(self.image)\
                                    .get_thumbnail(options).url
            self.save()

            try:
                # send tweet in background
                photo = open(self.image.path, 'rb')

                if self.race == 'Perro':
                    message = u'Perro'
                elif self.race == 'Gato':
                    message = u'Gato'
                else:
                    message = u'Animal'

                if self.__class__.__name__ == 'Adopted':
                    message += u' en #adopción en '
                elif self.__class__.__name__ == 'Losted':
                    message += u' #perdido en '
                elif self.__class__.__name__ == 'Reception':
                    message += u' en #acogida en '
                else:
                    message += u' #encontrado en '

                if self.state != 'Otro':
                    message += u'#' +unicode(self.state.replace(" ", "")) + u' '

                if self.city != '' and self.city != None:
                    message += u'#' + unicode(self.city.replace(" ", "")) + u' '

                if self.town != '' and self.town != None:
                    message += u'#' + unicode(self.town.replace(" ", "")) + u' '

                if self.race != 'Otra' and self.race != 'Desconocida':
                    message += u'#' + unicode(self.race.replace(" ", "")) + u' '

                message += u'más información en http://guauqueanimales.com' +\
                            reverse('detail', args=[self.id])

                t = threading.Thread(target=thread_send_tweet,
                                        args=[message, photo], kwargs={})
                t.setDaemon(True)
                t.start()

            except:
                pass

            try:
                # resize image in background
                t = threading.Thread(target=resize_image, args=[self.image.path,
                                        ], kwargs={})
                t.setDaemon(True)
                t.start()

            except:
                pass


class View(models.Model):

    dog = models.ForeignKey(Dog, verbose_name='Perro visitado', blank=True,
                                null=True, related_name='visitas')

    date_created = models.DateTimeField(null=False, auto_now_add=True)

    date_updated = models.DateTimeField(null=False, auto_now=True)

    def __unicode__(self):
        return unicode(self.id) + ' - ' + unicode(self.dog.id) + ' - ' +\
                unicode(self.date_created)


class Vieweb(models.Model):

    dog = models.ForeignKey(Dog, verbose_name='Perro visitado', blank=True,
                                null=True, related_name='visitas_web')

    date_created = models.DateTimeField(null=False, auto_now_add=True)

    date_updated = models.DateTimeField(null=False, auto_now=True)

    def __unicode__(self):
        return unicode(self.id) + ' - ' + unicode(self.dog.id) + ' - ' +\
                    unicode(self.date_created)


class Abuse(models.Model):

    dog_id = models.PositiveIntegerField(verbose_name='Identificador del Perro',
                                            blank=True, null=True)

    message = models.TextField(verbose_name=_(u'Mensaje'), blank=True,
                                        null=True)

    email = models.EmailField(verbose_name=_(u'Correo Electrónico'),
                                blank=True, null=True)

    def __unicode__(self):
        return unicode(self.dog_id) + ' - ' + unicode(self.message)

    def save(self, *args, **kwargs):
        # send emails in background
        super(Abuse, self).save(*args, **kwargs)

        try:
            asunto = "Aviso a la Administración de Guau! qué perros"
            cuerpo = u"Desde " + unicode(self.email) + u"  --  Identificador: "\
                        + unicode(self.dog_id) + u"  --  Mensaje: " +\
                        unicode(self.message)
            email = EmailMessage(subject=asunto, body=cuerpo,
                                    from_email=settings.FROM_ADMIN_EMAIL,
                                    to=settings.TO_ADMIN_EMAIL)

            t = threading.Thread(target=thread_send_email, args=[email,],
                                    kwargs={})
            t.setDaemon(True)
            t.start()

        except:
            pass


# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


@receiver(pre_delete, sender=Dog)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)


# PERROS PARA ADOPTAR
class Adopted(Dog):

    name = models.CharField(verbose_name=_(u'Nombre'), max_length=200,
                                blank=True, null=True)

    def get_next(self):
        try:
            next = Adopted.objects.filter(id__gt=self.id)[0]
            return next.id
        except:
            return False

    def get_prev(self):
        try:
            prev = Adopted.objects.filter(id__lt=self.id).order_by('-id')[0]
            return prev.id
        except:
            return False


# PERROS PERDIDOS
class Losted(Dog):

    name = models.CharField(verbose_name=_(u'Nombre'), max_length=200,
                                blank=True, null=True)

    reward = models.CharField(verbose_name=_(u'Recompensa'), max_length=200,
                                blank=True, null=True)

    def get_next(self):
        try:
            next = Losted.objects.filter(id__gt=self.id)[0]
            return next.id
        except:
            return False

    def get_prev(self):
        try:
            prev = Losted.objects.filter(id__lt=self.id).order_by('-id')[0]
            return prev.id
        except:
            return False


# PERROS ENCONTRADOS
class Finded(Dog):

    name = models.CharField(verbose_name=_(u'Nombre'), max_length=200,
                                blank=True, null=True)

    def get_next(self):
        try:
            next = Finded.objects.filter(id__gt=self.id)[0]
            return next.id
        except:
            return False

    def get_prev(self):
        try:
            prev = Finded.objects.filter(id__lt=self.id).order_by('-id')[0]
            return prev.id
        except:
            return False


# PERROS EN ACOGIDA
class Reception(Dog):

    name = models.CharField(verbose_name=_(u'Nombre'), max_length=200,
                                blank=True, null=True)

    def get_next(self):
        try:
            next = Reception.objects.filter(id__gt=self.id)[0]
            return next.id
        except:
            return False

    def get_prev(self):
        try:
            prev = Reception.objects.filter(id__lt=self.id).order_by('-id')[0]
            return prev.id
        except:
            return False
