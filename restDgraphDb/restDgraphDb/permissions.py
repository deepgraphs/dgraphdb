__author__ = 'mpetyx'

import authority
from authority import permissions
from django.contrib.flatpages.models import FlatPage


class FlatpagePermission(permissions.BasePermission):
    label = 'flatpage_permission'


authority.register(FlatPage, FlatpagePermission)