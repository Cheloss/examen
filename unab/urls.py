from django.conf.urls import url
from unab import views
urlpatterns = [
    url(r'^contacto/$', views.unab_contactos, name='unab_contacto'),
    url(r'^ver/(?P<pk>\d+)$', views.contacto_ver, name='contacto_ver'),
]