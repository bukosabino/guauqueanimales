from dogs.models import *
from dogs.serializers import *
from rest_framework.parsers import *
from rest_framework.renderers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class AdoptedViewSet(viewsets.ModelViewSet):

    def update(self, request, pk=None):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, request, pk=None):
        raise NotImplementedError('`destroy()` must be implemented.')

    def partial_update(self, request, pk=None):
        raise NotImplementedError('`partial_update()` must be implemented.')

    serializer_class = AdoptedSerializer

    def list(self, request):
        queryset = Adopted.objects.all()

        city = self.request.QUERY_PARAMS.get('city', None)
        if city is not None and city != 'Todas':
            queryset = queryset.filter(city=city)

        race = self.request.QUERY_PARAMS.get('race', None)
        if race is not None and race != 'Todas':
            queryset = queryset.filter(race=race)

        genre = self.request.QUERY_PARAMS.get('genre', None)
        if genre is not None and genre != 'Ambos':
            queryset = queryset.filter(genre=genre)

        queryset = queryset.order_by('-id')[:30]
        serializer = AdoptedSerializerList(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        dog = get_object_or_404(Adopted, pk=pk)
        serializer = AdoptedSerializer(dog)
        View(dog=dog).save()
        return Response(serializer.data)

    def get_queryset(self):
        if 'pk' in self.kwargs: # view one object
            return Adopted.objects.filter(pk=self.kwargs['pk'])
        else: # list
            return Adopted.objects.order_by('-id')[:30]


class LostedViewSet(viewsets.ModelViewSet):

    def update(self, request, pk=None):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, request, pk=None):
        raise NotImplementedError('`destroy()` must be implemented.')

    def partial_update(self, request, pk=None):
        raise NotImplementedError('`partial_update()` must be implemented.')

    serializer_class = LostedSerializer

    def list(self, request):
        queryset = Losted.objects.all()

        city = self.request.QUERY_PARAMS.get('city', None)
        if city is not None and city != 'Todas':
            queryset = queryset.filter(city=city)

        race = self.request.QUERY_PARAMS.get('race', None)
        if race is not None and race != 'Todas':
            queryset = queryset.filter(race=race)

        genre = self.request.QUERY_PARAMS.get('genre', None)
        if genre is not None and genre != 'Ambos':
            queryset = queryset.filter(genre=genre)

        queryset = queryset.order_by('-id')[:30]
        serializer = LostedSerializerList(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        dog = get_object_or_404(Losted, pk=pk)
        serializer = LostedSerializer(dog)
        View(dog=dog).save()
        return Response(serializer.data)

    def get_queryset(self):
        if 'pk' in self.kwargs: # view one object
            return Losted.objects.filter(pk=self.kwargs['pk'])
        else: # list
            return Losted.objects.order_by('-id')[:30]


class FindedViewSet(viewsets.ModelViewSet):

    def update(self, request, pk=None):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, request, pk=None):
        raise NotImplementedError('`destroy()` must be implemented.')

    def partial_update(self, request, pk=None):
        raise NotImplementedError('`partial_update()` must be implemented.')

    serializer_class = FindedSerializer

    def list(self, request):
        queryset = Finded.objects.all()

        city = self.request.QUERY_PARAMS.get('city', None)
        if city is not None and city != 'Todas':
            queryset = queryset.filter(city=city)

        race = self.request.QUERY_PARAMS.get('race', None)
        if race is not None and race != 'Todas':
            queryset = queryset.filter(race=race)

        genre = self.request.QUERY_PARAMS.get('genre', None)
        if genre is not None and genre != 'Ambos':
            queryset = queryset.filter(genre=genre)

        queryset = queryset.order_by('-id')[:30]
        serializer = FindedSerializerList(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        dog = get_object_or_404(Finded, pk=pk)
        serializer = FindedSerializer(dog)
        View(dog=dog).save()
        return Response(serializer.data)

    def get_queryset(self):
        if 'pk' in self.kwargs: # view one object
            return Finded.objects.filter(pk=self.kwargs['pk'])
        else: # list
            return Finded.objects.order_by('-id')[:30]


class ReceptionViewSet(viewsets.ModelViewSet):

    def update(self, request, pk=None):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, request, pk=None):
        raise NotImplementedError('`destroy()` must be implemented.')

    def partial_update(self, request, pk=None):
        raise NotImplementedError('`partial_update()` must be implemented.')

    serializer_class = ReceptionSerializer

    def list(self, request):
        queryset = Reception.objects.all()

        city = self.request.QUERY_PARAMS.get('city', None)
        if city is not None and city != 'Todas':
            queryset = queryset.filter(city=city)

        race = self.request.QUERY_PARAMS.get('race', None)
        if race is not None and race != 'Todas':
            queryset = queryset.filter(race=race)

        genre = self.request.QUERY_PARAMS.get('genre', None)
        if genre is not None and genre != 'Ambos':
            queryset = queryset.filter(genre=genre)

        queryset = queryset.order_by('-id')[:30]
        serializer = ReceptionSerializerList(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        dog = get_object_or_404(Reception, pk=pk)
        serializer = ReceptionSerializer(dog)
        View(dog=dog).save()
        return Response(serializer.data)

    def get_queryset(self):
        if 'pk' in self.kwargs: # view one object
            return Reception.objects.filter(pk=self.kwargs['pk'])
        else: # list
            return Reception.objects.order_by('-id')[:30]


class AbusedViewSet(viewsets.ModelViewSet):

    def update(self, request, pk=None):
        raise NotImplementedError('`update()` must be implemented.')

    def destroy(self, request, pk=None):
        raise NotImplementedError('`destroy()` must be implemented.')

    def partial_update(self, request, pk=None):
        raise NotImplementedError('`partial_update()` must be implemented.')

    serializer_class = AbusedSerializer

    def get_queryset(self):
        if 'pk' in self.kwargs: # view one object
            return Abuse.objects.filter(pk=self.kwargs['pk'])
        else: # list
            return Abuse.objects.order_by('-id')[:30]
