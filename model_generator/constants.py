"""Constants are stored here."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class FieldType(models.IntegerChoices):
    AutoField = 101, _('AutoField')
    BigAutoField = 102, _('BigAutoField')
    BigIntegerField = 103, _('BigIntegerField')
    BinaryField = 104, _('BinaryField')
    BooleanField = 105, _('BooleanField')
    CharField = 106, _('CharField')
    DateField = 107, _('DateField')
    DateTimeField = 108, _('DateTimeField')
    DecimalField = 109, _('DecimalField')
    DurationField = 110, _('DurationField')
    EmailField = 111, _('EmailField')
    FileField = 112, _('FileField')
    FilePathField = 113, _('FilePathField')
    FloatField = 114, _('FloatField')
    ImageField = 116, _('ImageField')
    IntegerField = 117, _('IntegerField')
    JSONField = 118, _('JSONField')
    PositiveBigIntegerField = 119, _('PositiveBigIntegerField')
    PositiveIntegerField = 120, _('PositiveIntegerField')
    PositiveSmallIntegerField = 121, _('PositiveSmallIntegerField')
    SlugField = 122, _('SlugField')
    SmallAutoField = 123, _('SmallAutoField')
    SmallIntegerField = 124, _('SmallIntegerField')
    TextField = 125, _('TextField')
    TimeField = 126, _('TimeField')
    URLField = 127, _('URLField')
    UUIDField = 128, _('UUIDField')
