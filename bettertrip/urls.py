"""bettertrip URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""



# import sys

# sys.path.append("/users/jizhizili/django/project/bettertrip/bettertrip")


import os

from django.conf.urls import *
from django.contrib import admin

from bettertrip.views import homepage,playtem,vic,act,nsw,wa,sa,tas,nt,qld,service,about,contact


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = os.path.join(os.path.dirname(BASE_DIR), 'bettertrip','static').replace('\\','/')

print (STATIC_URL)


urlpatterns = patterns('',
	url(r'^homepage/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/css'}),
	url(r'^homepage/image/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/image'}),
	url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/css'}),
	url(r'^image/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/image'}),
	
	url(r'^homepage/victoria/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/css'}),
	url(r'^homepage/state/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/state'}),
	url(r'^homepage/state/stateimage/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/state/'+'/stateimage'}),
	url(r'^homepage/js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_URL+'/js'}),
	('^play/$',playtem),
	('^homepage/$',homepage),
	('^homepage/act/$',act),
	('^homepage/vic/$',vic),
	('^homepage/sa/$',sa),
	('^homepage/tas/$',tas),
	('^homepage/nt/$',nt),
	('^homepage/qld/$',qld),
	('^homepage/nsw/$',nsw),
	('^homepage/wa/$',wa),
	('^homepage/service/$',service),
	('^homepage/about/$',about),
	('^homepage/contact/$',contact)
	)

