from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^survey/$', views.survey, name='survey'),
    url(r'^$', auth_views.login, name='index'),
    url(r'^login/$', views.login, name='login')
]
