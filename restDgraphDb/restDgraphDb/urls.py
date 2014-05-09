from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'restDgraphDb.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url('^coreapi/', include('coreapi.urls')),
                       url('^adminapi/', include('adminapi.urls')),
                       url('^reasoningapi', include('reasoningapi.urls')),
                       url('^adminapi/', include('adminapi.urls')),
)