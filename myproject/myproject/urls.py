"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cms_templates import views

urlpatterns = [
    url(r'^$',views.barra, name="Pagina Principal"),
    url(r'^logout$', views.myLogout, name="Hace Un Logout del usuario actual"),
    url(r'^admin', include(admin.site.urls)),
    url(r'^annotated/(.+)', views.plantilla, name="Sirve el contenido pero con plantilla"),
    url(r'^(.+)', views.recurso, name="Ofrece el contenido del recurso"),
]
