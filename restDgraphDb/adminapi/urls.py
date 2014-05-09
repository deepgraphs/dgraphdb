__author__ = 'mpetyx'

from django.conf.urls import patterns, url
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^/admin/shutdown/$', views.shutdown),
                       url(r'/admin/queries/(?P<queryID>\w+)/$', views.queries_id),
                       url(r'/admin/queries/$', views.queries),

                       url(r'^/admin/databases/$', views.databases),
                       url(r'^admin/databases/(?P<kb>\w+)/options/$', views.databases_kb_options),
                       url(r'^admin/databases/(?P<kb>\w+)/optimize/$', views.databases_kb_optimize),
                       url(r'^admin/databases/(?P<kb>\w+)/copy/$', views.databases_kb_copy),
                       url(r'^admin/databases/(?P<kb>\w+)/delete/$', views.databases_kb_delete),
                       url(r'/admin/databases/(?P<kb>\w+)/migrate/$', views.databases_kb_migrate),
                       url(r'/admin/databases/(?P<kb>\w+)/online$', views.databases_kb_online),
                       url(r'/admin/databases/(?P<kb>\w+)/offline', views.databases_kb_offline),

                       url(r'/admin/permissions/role/(?P<role>\w+)/$', views.permissions_role),
                       url(r'/admin/permissions/user/(?P<user>\w+)/$', views.permissions_user),
                       url(r'/admin/permissions/user/effective/(?P<user>\w+)/$', views.permissions_user_effective),

                       url(r'/admin/roles/$', views.roles),
                       url(r'/admin/roles/(?P<role>\w+)/$', views.role),
                       url(r'/admin/roles/(?P<role>\w+)/users/$', views.roles_users),

                       url(r'/admin/users/$', views.users),
                       url(r'/admin/users/(?P<user>\w+)/roles/$', views.users_roles),
                       url(r'/admin/users/(?P<user>\w+)/roles/(?P<role>\w+)/$', views.users_role_id),
                       url(r'/admin/users/(?P<user>\w+)/$', views.users_id),
                       url(r'/admin/users/(?P<user>\w+)/valid/$', views.users_id_valid),
                       url(r'/admin/users/(?P<user>\w+)/pwd/$', views.users_id_pwd),
                       url(r'/admin/users/(?P<user>\w+)/enabled/$', views.users_id_enabled),
                       url(r'/admin/users/(?P<user>\w+)/superuser/$', views.users_id_superuser),


)
