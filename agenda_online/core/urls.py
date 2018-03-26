from django.conf.urls import url
from django.contrib import admin
from agenda_online.core.views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^adicionar/', adicionar, name="adicionar"),
    url(r'^pesquisa/', pesquisa, name="pesquisa")
]