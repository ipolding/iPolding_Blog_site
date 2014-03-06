__author__ = 'ian'
from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^entry/(?P<entry_id>\d+)$', views.entry, name='blog'),

)