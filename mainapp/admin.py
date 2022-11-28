# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mainapp.models import SentEmailList, TemplateName, Subscriber


@admin.register(Subscriber)
class SubscriberAdminModel(admin.ModelAdmin):
    pass


@admin.register(TemplateName)
class TemplateNameAdminModel(admin.ModelAdmin):
    pass


@admin.register(SentEmailList)
class SentEmailListAdminModel(admin.ModelAdmin):
    pass
