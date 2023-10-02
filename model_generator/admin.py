from django.contrib import admin

from . import models


class BaseModelAdmin(admin.TabularInline):
    model = models.BaseModelGenerator
    pass

class BaseAppsAdmin(admin.ModelAdmin):
    '''
    '''
    inlines = (BaseModelAdmin,)

admin.site.register(models.BaseApps, BaseAppsAdmin)
