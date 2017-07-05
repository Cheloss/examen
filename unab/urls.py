from django.conf.urls import url
from unab import views
urlpatterns = [
    url(r'^list/$', views.noticia_list, name='noticia_list'),
    url(r'^edit/(?P<pk>\d+)$', views.noticia_update, name='noticia_edit'),
    url(r'^contacto/$', views.unab_contactos, name='unab_contacto'),
]