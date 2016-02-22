# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abuse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dog_id', models.PositiveIntegerField(null=True, verbose_name=b'Identificador del Perro', blank=True)),
                ('message', models.TextField(null=True, verbose_name='Mensaje', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Correo Electr\xf3nico', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('race', models.CharField(max_length=200, verbose_name='Raza', choices=[('Desconocida', 'Desconocida'), ('Affenpinscher', 'Affenpinscher'), ('Airedale Terrier', 'Airedale Terrier'), ('Akita americano', 'Akita americano'), ('Akita Inu', 'Akita Inu'), ('Alaskan Malamute', 'Alaskan Malamute'), ('American Staffordshire Terrier', 'American Staffordshire Terrier'), ('Basenji', 'Basenji'), ('Basset Hound', 'Basset Hound'), ('Beagle', 'Beagle'), ('Beauceron', 'Beauceron'), ('Bichon Frise', 'Bichon Frise'), ('Bodeguero', 'Bodeguero'), ('Borzoi', 'Borzoi'), ('Boston Terrier', 'Boston Terrier'), ('Boxer', 'Boxer'), ('Bret\xf3n', 'Bret\xf3n'), ('Bull Terrier Ingl\xe9s', 'Bull Terrier Ingl\xe9s'), ('Bulldog Franc\xe9s', 'Bulldog Franc\xe9s'), ('Bullmastiff', 'Bullmastiff'), ('Cane Corso', 'Cane Corso'), ('Caniche', 'Caniche'), ('Chihuahua', 'Chihuahua'), ('Chow Chow', 'Chow Chow'), ('Cocker Americano', 'Cocker Americano'), ('Cocker Spaniel', 'Cocker Spaniel'), ('Collie', 'Collie'), ('Collie Barbudo', 'Collie Barbudo'), ('Collie de la Frontera', 'Collie de la Frontera'), ('Dalmata', 'Dalmata'), ('Doberman', 'Doberman'), ('Dogo Argentino', 'Dogo Argentino'), ('Field Spaniel', 'Field Spaniel'), ('Fox Terrier Chileno', 'Fox Terrier Chileno'), ('Fox Terrier Wire', 'Fox Terrier Wire'), ('Foxhound Ingl\xe9s', 'Foxhound Ingl\xe9s'), ('Galgo Espa\xf1ol', 'Galgo Espa\xf1ol'), ('Golden Retrieveer', 'Golden Retrieveer'), ('Gran Dan\xe9s', 'Gran Dan\xe9s'), ('Hovawart', 'Hovawart'), ('Husky siberiano', 'Husky siberiano'), ('Irish water spaniel', 'Irish water spaniel'), ('Jack Russell Terrier', 'Jack Russell Terrier'), ('Komondor', 'Komondor'), ('Kritikos Lagonikos', 'Kritikos Lagonikos'), ('Labrador Retriever', 'Labrador Retriever'), ('Lebrel afgano', 'Lebrel afgano'), ('Leonberger', 'Leonberger'), ('Malt\xe9s', 'Malt\xe9s'), ('Mast\xedn ingl\xe9s', 'Mast\xedn ingl\xe9s'), ('Mestizo', 'Mestizo'), ('Pastor Alem\xe1n', 'Pastor Alem\xe1n'), ('Pastor Catal\xe1n', 'Pastor Catal\xe1n'), ('Pequin\xe9s', 'Pequin\xe9s'), ('Perro de agua espa\xf1ol', 'Perro de agua espa\xf1ol'), ('Pinscher Miniatura', 'Pinscher Miniatura'), ('Podenco', 'Podenco'), ('Pointer', 'Pointer'), ('Rottweiler', 'Rottweiler'), ('Samoyedo', 'Samoyedo'), ('San Bernardo', 'San Bernardo'), ('Schnauzer est\xe1ndar', 'Schnauzer est\xe1ndar'), ('Schnauzer gigante', 'Schnauzer gigante'), ('Schnauzer miniatura', 'Schnauzer miniatura'), ('Setter Ingl\xe9s', 'Setter Ingl\xe9s'), ('Shar Pei', 'Shar Pei'), ('Shiba Inu', 'Shiba Inu'), ('Shih Tzu', 'Shih Tzu'), ('Terrier Irland\xe9s', 'Terrier Irland\xe9s'), ('West Highland White Terrier', 'West Highland White Terrier'), ('Whippet', 'Whippet'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Otra', 'Otra')])),
                ('age', models.CharField(help_text='Por ejemplo: 2 meses', max_length=200, null=True, verbose_name='Edad', blank=True)),
                ('image', models.ImageField(upload_to=b'dogs', verbose_name='Imagen')),
                ('thumbnail_url', models.URLField(null=True, blank=True)),
                ('genre', models.CharField(max_length=60, verbose_name='Sexo', choices=[('Desconocido', 'Desconocido'), ('Hembra', 'Hembra'), ('Macho', 'Macho')])),
                ('city', models.CharField(max_length=200, verbose_name='Ciudad', choices=[('Otra', 'Otra'), ('Almer\xeda', 'Almer\xeda'), ('Granada', 'Granada'), ('C\xe1diz', 'C\xe1diz'), ('C\xf3rdoba', 'C\xf3rdoba'), ('Huelva', 'Huelva'), ('Ja\xe9n', 'Ja\xe9n'), ('M\xe1laga', 'M\xe1laga'), ('Sevilla', 'Sevilla'), ('Huesca', 'Huesca'), ('Teruel', 'Teruel'), ('Zaragoza', 'Zaragoza'), ('Cantabria', 'Cantabria'), ('\xc1vila', '\xc1vila'), ('Burgos', 'Burgos'), ('Le\xf3n', 'Le\xf3n'), ('Palencia', 'Palencia'), ('Salamanca', 'Salamanca'), ('Segovia', 'Segovia'), ('Soria', 'Soria'), ('Valladolid', 'Valladolid'), ('Zamora', 'Zamora'), ('Albacete', 'Albacete'), ('Ciudad Real', 'Ciudad Real'), ('Cuenca', 'Cuenca'), ('Guadalajara', 'Guadalajara'), ('Toledo', 'Toledo'), ('Barcelona', 'Barcelona'), ('Girona', 'Girona'), ('Lleida', 'Lleida'), ('Tarragona', 'Tarragona'), ('Ceuta', 'Ceuta'), ('Madrid', 'Madrid'), ('Alicante', 'Alicante'), ('Castell\xf3n', 'Castell\xf3n'), ('Valencia', 'Valencia'), ('Badajoz', 'Badajoz'), ('C\xe1ceres', 'C\xe1ceres'), ('A Coru\xf1a', 'A Coru\xf1a'), ('Lugo', 'Lugo'), ('Ourense', 'Ourense'), ('Pontevedra', 'Pontevedra'), ('Baleares', 'Baleares'), ('Las Palmas', 'Las Palmas'), ('Santa Cruz de Tenerife', 'Santa Cruz de Tenerife'), ('La Rioja', 'La Rioja'), ('Melilla', 'Melilla'), ('Navarra', 'Navarra'), ('\xc1lava', '\xc1lava'), ('Guipuzcoa', 'Guipuzcoa'), ('Vizcaya', 'Vizcaya'), ('Asturias', 'Asturias'), ('Murcia', 'Murcia')])),
                ('town', models.CharField(max_length=200, null=True, verbose_name='Poblaci\xf3n', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Descripci\xf3n', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Correo Electr\xf3nico', blank=True)),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='Tel\xe9fono de Contacto', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Adopted',
            fields=[
                ('dog_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dogs.Dog')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Nombre', blank=True)),
            ],
            options={
            },
            bases=('dogs.dog',),
        ),
        migrations.CreateModel(
            name='Finded',
            fields=[
                ('dog_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dogs.Dog')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Nombre', blank=True)),
            ],
            options={
            },
            bases=('dogs.dog',),
        ),
        migrations.CreateModel(
            name='Losted',
            fields=[
                ('dog_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dogs.Dog')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('reward', models.CharField(max_length=200, null=True, verbose_name='Recompensa', blank=True)),
            ],
            options={
            },
            bases=('dogs.dog',),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('dog', models.ForeignKey(related_name='visitas', verbose_name=b'Perro visitado', blank=True, to='dogs.Dog', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
