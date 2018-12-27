from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.check, name='check'),
    url(r'^$', views.list, name='list'),
]