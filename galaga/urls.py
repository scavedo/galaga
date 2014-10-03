from django.conf.urls import patterns, include, url
from django.contrib import admin
from rsi_app.views import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','rsi_app.views.index'),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^grandison', 'rsi_app.views.grandison'),
    url(r'^bones', 'rsi_app.views.bones'),
    url(r'^events', Event.as_view()),
    #our urls
    url(r'^ghost-stories/', 'rsi_app.views.ghost_stories'),
    url(r'^history/', 'rsi_app.views.history'),
    url(r'^(?P<slug>[\w\-]+)/$', FounderDetail.as_view()),
    url(r'^founders', FoundersList.as_view()),


)

