from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    label = 'core'
    name = 'projects.core'
    verbose_name = _('Core')
