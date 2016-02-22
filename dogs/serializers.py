from rest_framework import serializers
from dogs.models import *


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and (';base64,' in data or ':base64,' in data):
                # Break out the header from the base64 content
                header, data = data.split('base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class DogSerializerList(serializers.ModelSerializer):

    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, instance, validated_data):
        raise NotImplementedError('`destroy()` must be implemented.')

    class Meta:
        fields = ('id', 'name', 'image', 'thumbnail_url', 'race', 'age',
                    'city',)


class DogSerializer(serializers.ModelSerializer):

    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, instance, validated_data):
        raise NotImplementedError('`destroy()` must be implemented.')

    class Meta:

        fields = ('id', 'name', 'image', 'animal', 'race', 'genre', 'age',
                    'state', 'town', 'city', 'description', 'email', 'phone',
                    'date_created', 'date_updated',)


class AdoptedSerializerList(DogSerializerList):

    class Meta:
        model = Adopted


class AdoptedSerializer(DogSerializer):

    class Meta:
        model = Adopted


class LostedSerializerList(DogSerializerList):

    class Meta:
        model = Losted


class LostedSerializer(DogSerializer):

    class Meta:
        model = Losted


class FindedSerializerList(DogSerializerList):

    class Meta:
        model = Finded


class FindedSerializer(DogSerializer):

    class Meta:
        model = Finded


class ReceptionSerializerList(DogSerializerList):

    class Meta:
        model = Reception


class ReceptionSerializer(DogSerializer):

    class Meta:
        model = Reception


class AbusedSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, instance, validated_data):
        raise NotImplementedError('`destroy()` must be implemented.')

    class Meta:
        model = Abuse
        fields = ('id', 'message', 'email', 'dog_id')
