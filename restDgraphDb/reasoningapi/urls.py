__author__ = 'mpetyx'

from django.conf.urls import patterns, url
from django.contrib import admin

import views


admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^(?P<kb>\w+)/reasoning/explain/$', views.explain),
                       url(r'^(?P<kb>\w+)/reasoning/cosistency/$', views.consistency),
                       url(r'^(?P<kb>\w+)/reasoning/explain/incosistency/$', views.explain_incosistency),

                       # transaction based requests are handled here
                       url(r'^(?P<kb>\w+)/reasoning/(?P<tid>\w+)/explain/$', views.tid_explain),
                       url(r'^(?P<kb>\w+)/reasoning/(?P<tid>\w+)/explain/incosistency/$',
                           views.tid_explain_incosistency),


)
