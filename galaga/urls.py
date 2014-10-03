from django.conf.urls import patterns, include, url
from django.contrib import admin
from rsi_app.views import *

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','rsi_app.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', founder_detail),
    url(r'^founders', founders_list)
)
