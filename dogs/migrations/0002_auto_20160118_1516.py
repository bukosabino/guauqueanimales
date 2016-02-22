# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('dog_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dogs.Dog')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Nombre', blank=True)),
            ],
            options={
            },
            bases=('dogs.dog',),
        ),
        migrations.CreateModel(
            name='Vieweb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('dog', models.ForeignKey(related_name='visitas_web', verbose_name=b'Perro visitado', blank=True, to='dogs.Dog', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dog',
            name='animal',
            field=models.CharField(default=b'Perro', max_length=60, verbose_name='Tipo de animal', choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Otro', 'Otro')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dog',
            name='state',
            field=models.CharField(default=b'Espa\xc3\xb1a', max_length=200, verbose_name='Pa\xeds', choices=[('Espa\xf1a', 'Espa\xf1a'), ('M\xe9xico', 'M\xe9xico'), ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Venezuela', 'Venezuela'), ('Per\xfa', 'Per\xfa'), ('Ecuador', 'Ecuador'), ('Guatemala', 'Guatemala'), ('Cuba', 'Cuba'), ('Rep\xfablica Dominicana', 'Rep\xfablica Dominicana'), ('Honduras', 'Honduras'), ('Bolivia', 'Bolivia'), ('El Salvador', 'El Salvador'), ('Nicaragua', 'Nicaragua'), ('Paraguay', 'Paraguay'), ('Costa Rica', 'Costa Rica'), ('Panam\xe1', 'Panam\xe1'), ('Otro', 'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dog',
            name='city',
            field=models.CharField(max_length=200, null=True, verbose_name='Ciudad', blank=True),
            preserve_default=True,
        ),
    ]
