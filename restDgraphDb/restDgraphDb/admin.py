__author__ = 'mpetyx'

from django.contrib import admin
from models import KnowledgeBase


class KnowledgeBaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(KnowledgeBase, KnowledgeBaseAdmin)