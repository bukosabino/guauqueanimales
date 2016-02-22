from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from dogs.viewsets import *
from rest_framework.routers import DefaultRouter
from dogs import views

router = DefaultRouter()
router.register(r'adopteds', AdoptedViewSet, base_name='adopteds-list')
router.register(r'losteds', LostedViewSet, base_name='losteds-list')
router.register(r'findeds', FindedViewSet, base_name='findeds-list')
router.register(r'receptions', ReceptionViewSet, base_name='receptions-list')
router.register(r'abuses', AbusedViewSet, base_name='abuses-list')

urlpatterns = patterns('',

    url(r'^dogs/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contacto/$', views.contact, name='contact'),
    url(r'^(?P<section_name>\w+)/$', views.index, name='index'),
    url(r'^detalle/(?P<animal_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^nuevo/en_adopcion/$', views.new_dog_adopted, name='new_dog_adopted'),
    url(r'^nuevo/en_acogida/$', views.new_dog_recepted,name='new_dog_recepted'),
    url(r'^nuevo/encontrado/$', views.new_dog_finded, name='new_dog_finded'),
    url(r'^nuevo/perdido/$', views.new_dog_losted, name='new_dog_losted'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
