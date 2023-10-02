"""Constants are stored here."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class FieldType(models.IntegerChoices):
    CharField = 101, _('Char Field')
    IntegerField = 102, _('Integer Field')

