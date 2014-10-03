from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','rsi_app.views.index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'rsi_app.views.founders_detail'),
)
