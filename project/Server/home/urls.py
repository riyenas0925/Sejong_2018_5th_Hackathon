from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.check, name='check'),
    url(r'^$', views.list, name='list'),
    url('signup', views.signup),
    url('prepare', views.prepare),
]