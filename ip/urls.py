from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.shortcuts import render_to_response, RequestContext
from django.conf.urls import patterns, url
from ip import views
#try:
#    HOSTNAME = socket.gethostname()
#except:
#    HOSTNAME = 'localhost'
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ip$', views.iplookup_views, name='iplookup_views'),
)
