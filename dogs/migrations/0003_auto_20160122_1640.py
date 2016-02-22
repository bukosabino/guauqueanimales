# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_auto_20160118_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='genre',
            field=models.CharField(default=b'Desconocido', max_length=60, verbose_name='Sexo', choices=[('Desconocido', 'Desconocido'), ('Hembra', 'Hembra'), ('Macho', 'Macho')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dog',
            name='race',
            field=models.CharField(default=b'Mestizo', max_length=200, verbose_name='Raza', choices=[('Desconocida', 'Desconocida'), ('Affenpinscher', 'Affenpinscher'), ('Airedale Terrier', 'Airedale Terrier'), ('Akita americano', 'Akita americano'), ('Akita Inu', 'Akita Inu'), ('Alaskan Malamute', 'Alaskan Malamute'), ('American Staffordshire Terrier', 'American Staffordshire Terrier'), ('Basenji', 'Basenji'), ('Basset Hound', 'Basset Hound'), ('Beagle', 'Beagle'), ('Beauceron', 'Beauceron'), ('Bichon Frise', 'Bichon Frise'), ('Bodeguero', 'Bodeguero'), ('Borzoi', 'Borzoi'), ('Boston Terrier', 'Boston Terrier'), ('Boxer', 'Boxer'), ('Bret\xf3n', 'Bret\xf3n'), ('Bull Terrier Ingl\xe9s', 'Bull Terrier Ingl\xe9s'), ('Bulldog Franc\xe9s', 'Bulldog Franc\xe9s'), ('Bullmastiff', 'Bullmastiff'), ('Cane Corso', 'Cane Corso'), ('Caniche', 'Caniche'), ('Chihuahua', 'Chihuahua'), ('Chow Chow', 'Chow Chow'), ('Cocker Americano', 'Cocker Americano'), ('Cocker Spaniel', 'Cocker Spaniel'), ('Collie', 'Collie'), ('Collie Barbudo', 'Collie Barbudo'), ('Collie de la Frontera', 'Collie de la Frontera'), ('Dalmata', 'Dalmata'), ('Doberman', 'Doberman'), ('Dogo Argentino', 'Dogo Argentino'), ('Field Spaniel', 'Field Spaniel'), ('Fox Terrier Chileno', 'Fox Terrier Chileno'), ('Fox Terrier Wire', 'Fox Terrier Wire'), ('Foxhound Ingl\xe9s', 'Foxhound Ingl\xe9s'), ('Galgo Espa\xf1ol', 'Galgo Espa\xf1ol'), ('Golden Retrieveer', 'Golden Retrieveer'), ('Gran Dan\xe9s', 'Gran Dan\xe9s'), ('Hovawart', 'Hovawart'), ('Husky siberiano', 'Husky siberiano'), ('Irish water spaniel', 'Irish water spaniel'), ('Jack Russell Terrier', 'Jack Russell Terrier'), ('Komondor', 'Komondor'), ('Kritikos Lagonikos', 'Kritikos Lagonikos'), ('Labrador Retriever', 'Labrador Retriever'), ('Lebrel afgano', 'Lebrel afgano'), ('Leonberger', 'Leonberger'), ('Malt\xe9s', 'Malt\xe9s'), ('Mast\xedn ingl\xe9s', 'Mast\xedn ingl\xe9s'), ('Mestizo', 'Mestizo'), ('Pastor Alem\xe1n', 'Pastor Alem\xe1n'), ('Pastor Catal\xe1n', 'Pastor Catal\xe1n'), ('Pequin\xe9s', 'Pequin\xe9s'), ('Perro de agua espa\xf1ol', 'Perro de agua espa\xf1ol'), ('Pinscher Miniatura', 'Pinscher Miniatura'), ('Podenco', 'Podenco'), ('Pointer', 'Pointer'), ('Rottweiler', 'Rottweiler'), ('Samoyedo', 'Samoyedo'), ('San Bernardo', 'San Bernardo'), ('Schnauzer est\xe1ndar', 'Schnauzer est\xe1ndar'), ('Schnauzer gigante', 'Schnauzer gigante'), ('Schnauzer miniatura', 'Schnauzer miniatura'), ('Setter Ingl\xe9s', 'Setter Ingl\xe9s'), ('Shar Pei', 'Shar Pei'), ('Shiba Inu', 'Shiba Inu'), ('Shih Tzu', 'Shih Tzu'), ('Terrier Irland\xe9s', 'Terrier Irland\xe9s'), ('West Highland White Terrier', 'West Highland White Terrier'), ('Whippet', 'Whippet'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Otra', 'Otra')]),
            preserve_default=True,
        ),
    ]
