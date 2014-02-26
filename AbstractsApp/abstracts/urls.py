__author__ = 'ian'

from django.conf.urls import patterns, include, url

from abstracts import views

urlpatterns = patterns('',
    url(r'^$', views.get_all_abstracts, name='get_all_abstracts')
)
