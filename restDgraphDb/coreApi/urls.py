__author__ = 'mpetyx'

from django.conf.urls import patterns, url
from django.contrib import admin

import views


admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^(?P<kb>\w+)/size/$', views.kb_size),
                       url(r'^(?P<kb>\w+)/query/$', views.kb_query),

                       url(r'^(?P<kb>\w+)/transaction/begin/$', views.transaction_begin),
                       url(r'^(?P<kb>\w+)/transaction/rollback/(?P<tid>\w+)/$', views.transaction_rollback),
                       url(r'^(?P<kb>\w+)/transaction/commit/(?P<tid>\w+)/$', views.transaction_commit),

                       url(r'^(?P<kb>\w+)/(?P<tid>\w+)/add/$', views.tid_add),
                       url(r'^(?P<kb>\w+)/(?P<tid>\w+)/remove/$', views.tid_remove),
                       url(r'^(?P<kb>\w+)/(?P<tid>\w+)/query/$', views.tid_query),
                       url(r'^(?P<kb>\w+)/(?P<tid>\w+)/clear/$', views.tid_clear),

)
