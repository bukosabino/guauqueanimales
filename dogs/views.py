# -*- encoding: utf-8 -*-

from django.http import (HttpResponse, HttpResponseNotModified,
                    HttpResponseRedirect)
from django.shortcuts import (render, redirect, get_object_or_404,
                        render_to_response)
from dogs.models import *
from dogs.forms import *
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request, section_name=None, form_contact=None,
            option_selected='adopted', forms=None):

    adopteds = Adopted.objects.order_by('-id')[:50]
    losteds = Losted.objects.order_by('-id')[:50]
    findeds = Finded.objects.order_by('-id')[:50]
    receptions = Reception.objects.order_by('-id')[:50]

    if not forms:
        form_adopted = AdoptedForm()
        form_finded = FindedForm()
        form_losted = LostedForm()
        form_recepted = ReceptedForm()
    else:
        form_adopted = forms['form_adopted']
        form_finded = forms['form_finded']
        form_losted = forms['form_losted']
        form_recepted = forms['form_recepted']

    context = {
        'adopteds': adopteds,
        'losteds': losteds,
        'findeds': findeds,
        'receptions': receptions,
        'form_adopted': form_adopted,
        'form_finded': form_finded,
        'form_losted': form_losted,
        'form_recepted': form_recepted,
        'section_name': section_name,
        'form_contact': form_contact,
        'option_selected': option_selected,
    }
    return render(request, 'dogs/index.html', context)


def contact(request):

    form_contact = {
        'email': '',
        'name': '',
        'phone': '',
        'message': ''
    }

    if request.POST:
        try:
            asunto = "Aviso a la Administración de Guau! qué animales"
            cuerpo = u"Desde " + unicode(request.POST['email']) + u" \
                        --  Mensaje: " + unicode(request.POST['message'])

            form_contact['email'] = unicode(request.POST['email'])
            form_contact['message'] = unicode(request.POST['message'])

            if 'animal_id' in request.POST:
                cuerpo += u'\n Animal ID: ' + unicode(request.POST['animal_id'])

            if 'name' in request.POST:
                cuerpo += u'\n Nombre: ' + unicode(request.POST['name'])
                form_contact['name'] = unicode(request.POST['name'])

            if 'phone' in request.POST:
                cuerpo += u'\n Teléfono: ' + unicode(request.POST['phone'])
                form_contact['phone'] = unicode(request.POST['phone'])

            email = EmailMessage(subject=asunto, body=cuerpo,
                                    from_email= ['bukosabino@gmail.com',
                                                'lecrintechnologies@gmail.com',
                                                ],
                                    to=('Bukosabino@gmail.com',))

            email.send()
            message = u'Ha sido enviado un mensaje a la Administración de \
                        Guau! qué animales.'
            messages.add_message(request, messages.SUCCESS, message)

        except:
            message = u'Ha habido algún problema en el envío del correo \
                        electrónico. Revise los datos que ha introducido.'
            messages.add_message(request, messages.ERROR, message)

    if 'animal_id' in request.POST:
        return detail(request, int(request.POST['animal_id']))
    else:
        return index(request, 'contact', form_contact)


def detail(request, animal_id):
    animal = Adopted.objects.filter(id=animal_id)
    aux_type = u'En Adopción'
    aux_type2 = u'En %23Adopción'

    if animal.count() == 0:
        animal = Losted.objects.filter(id=animal_id)
        aux_type = u'Perdido'
        aux_type2 = u'%23Perdido'

    if animal.count() == 0:
        animal = Finded.objects.filter(id=animal_id)
        aux_type = u'Encontrado'
        aux_type2 = u'%23Encontrado'

    if animal.count() == 0:
        animal = Reception.objects.filter(id=animal_id)
        aux_type = u'En Acogida'
        aux_type2 = u'En %23Acogida'

    if animal:
        animal = animal[0]
        animal.type = aux_type
        animal.next_id = animal.get_next()
        animal.prev_id = animal.get_prev()
        v = Vieweb(dog=animal)
        v.save()
        aux_desc2 = u'Animal ' + unicode(aux_type) + u' en ' +\
                        unicode(animal.state)
        aux_desc3 = u'Animal ' + unicode(aux_type2) + u' en ' +\
                        unicode(animal.state)
        if animal.city:
            aux_desc2 += ', ' + unicode(animal.city)
            aux_desc3 += ', %23' + unicode(animal.city)
        if animal.town:
            aux_desc2 += ', ' + unicode(animal.town)
            aux_desc3 += ', %23' + unicode(animal.city)

        animal.description2 = aux_desc2 + u'\n'
        animal.description3 = aux_desc3 + u'\n'

    context = {
    	'animal': animal,
    }
    return render(request, 'dogs/detail.html', context)


def validate_form(request, form):
    instance = form.save()
    message = u'El animal ha sido añadido a la base de datos. ¡No olvides usar\
                los botones para compartir en redes sociales!'
    messages.add_message(request, messages.SUCCESS, message)
    return HttpResponseRedirect(reverse('detail', args=[instance.id]))


def new_dog_adopted(request):
    if request.method == 'POST':
        form_adopted = AdoptedForm(data=request.POST, files=request.FILES)
        if form_adopted.is_valid():
            return validate_form(request, form_adopted)
        else:
            forms = {
                'form_adopted': form_adopted,
                'form_finded': FindedForm(),
                'form_losted': LostedForm(),
                'form_recepted': ReceptedForm(),
            }
            return index(request, option_selected='adopted', forms=forms)
        return render(request, 'dogs/index.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))


def new_dog_recepted(request):
    if request.method == 'POST':
        form_recepted = ReceptedForm(data=request.POST, files=request.FILES)
        if form_recepted.is_valid():
            return validate_form(request, form_recepted)
        else:
            forms = {
                'form_adopted': AdoptedForm(),
                'form_finded': FindedForm(),
                'form_losted': LostedForm(),
                'form_recepted': form_recepted,
            }
            return index(request, option_selected='recepted', forms=forms)
        return render(request, 'dogs/index.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))


def new_dog_finded(request):
    if request.method == 'POST':
        form_finded = FindedForm(data=request.POST, files=request.FILES)
        if form_finded.is_valid():
            return validate_form(request, form_finded)
        else:
            forms = {
                'form_adopted': AdoptedForm(),
                'form_finded': form_finded,
                'form_losted': LostedForm(),
                'form_recepted': ReceptedForm(),
            }
            return index(request, option_selected='finded', forms=forms)
        return render(request, 'dogs/index.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))


def new_dog_losted(request):
    if request.method == 'POST':
        form_losted = LostedForm(data=request.POST, files=request.FILES)
        if form_losted.is_valid():
            return validate_form(request, form_losted)
        else:
            forms = {
                'form_adopted': AdoptedForm(),
                'form_finded': FindedForm(),
                'form_losted': form_losted,
                'form_recepted': ReceptedForm(),
            }
            return index(request, option_selected='losted', forms=forms)
        return render(request, 'dogs/index.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))
