# -*- coding: utf-8 -*-

from django import forms
from dogs.models import *


class DogForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(DogForm, self).clean()
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")

        if not email and not phone:
            # Only do something if both fields are valid so far.
            raise forms.ValidationError(
                u"Rellena el campo de 'Correo Electrónico' o el 'Teléfono', para que alguien pueda contactar contigo!"
            )


class AdoptedForm(DogForm):

    class Meta:
        model = Adopted
        exclude = ['thumbnail_url']


class LostedForm(DogForm):

    class Meta:
        model = Losted
        exclude = ['thumbnail_url']


class FindedForm(DogForm):

    class Meta:
        model = Finded
        exclude = ['thumbnail_url']


class ReceptedForm(DogForm):

    class Meta:
        model = Reception
        exclude = ['thumbnail_url']
