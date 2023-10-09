from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

from . import models


class ModelFieldParameterAdmin(NestedStackedInline):
    model = models.FieldParameter


class ModelFieldAdmin(NestedTabularInline):
    model = models.ModelField
    inlines = [ModelFieldParameterAdmin,]
    extra = 1


@admin.register(models.BaseModel)
class BaseModelAdmin(NestedModelAdmin):
    model = models.BaseModel
    inlines = [ModelFieldAdmin,]


@admin.register(models.BaseApp)
class BaseAppAdmin(admin.ModelAdmin):
    list_display = ('name',)
