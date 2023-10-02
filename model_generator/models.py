from collections.abc import Iterable
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.conf import settings

from . import constants as m_consts


class BaseAppManager(models.Manager):
    '''
    '''
    pass



class BaseApps(models.Model):
    '''
    '''
    choices = map(lambda x: (x, x), filter(lambda y: not y.startswith('django.'), settings.INSTALLED_APPS))
    app_name = models.CharField(max_length=255, name='App Name', choices=tuple(choices))
    model_name = models.CharField(max_length=255, name='Model Name')

    # def __str__(self) -> str:
    #     return f"{self.model_name}"

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)


@receiver(post_save, sender=BaseApps)
def create_models_file(sender, instance, **kwargs):
    print("Create")



class BaseModelGenerator(models.Model):
    '''
    '''
    app = models.ForeignKey(BaseApps, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255, name='Field Name')
    field_type = models.IntegerField(
        default=m_consts.FieldType.CharField,
        choices=m_consts.FieldType.choices, verbose_name=_('Field Type'))
