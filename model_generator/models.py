from django.db import models
from django.utils.translation import gettext_lazy as _

from . import constants


class BaseApp(models.Model):
    '''
    Model for app
    '''
    name = models.CharField(max_length=255, verbose_name=_('App Name'))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)


class BaseModel(models.Model):
    '''
    Model for "Model"

    @todo
    1. Plan how to implement adding meta class
    '''
    app = models.ForeignKey(to=BaseApp, verbose_name=_(
        'App'), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('Model Name'))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)


class ModelField(models.Model):
    '''
    Model to create fields for model
    '''
    model = models.ForeignKey(to=BaseModel, verbose_name=_(
        'Model'), on_delete=models.CASCADE, related_name='model_fields')

    name = models.CharField(max_length=255, verbose_name=_('Field Name'))
    type = models.IntegerField(
        default=constants.FieldType.CharField,
        choices=constants.FieldType.choices, verbose_name=_('Field Type')
    )
    parameters = models.OneToOneField(
        to='FieldParameter', on_delete=models.CASCADE, related_name='field_parameters')

    class Meta:
        ordering = ('name',)


class FieldParameter(models.Model):
    '''
    Model for setting parameters

    @todo
    1. plan how to add choices
    '''
    verbose_name = models.CharField(
        max_length=200, verbose_name=_("Verbose Name"))
    primary_key = models.BooleanField(verbose_name=_("Primary Key?"))
    unique = models.BooleanField(verbose_name=_("Unique?"))
    max_length = models.IntegerField(verbose_name=_("Max Length"))
    blank = models.BooleanField(verbose_name=_("Blank?"))
    null = models.BooleanField(verbose_name=_("Nullable?"))
    default = models.CharField(max_length=255, verbose_name=_("Default"))
    editable = models.BooleanField(verbose_name=_("Editable?"))
    # choices = models.
    db_index = models.BooleanField(verbose_name=_("Db Index?"))
    db_column = models.CharField(
        max_length=255, verbose_name=_("DB Column Name"))
    db_comment = models.CharField(max_length=255, verbose_name=_("DB Comment"))
