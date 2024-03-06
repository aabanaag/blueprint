import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArthemisConfig(AppConfig):
    name = "blueprint.arthemis"
    verbose_name = _("Arthemis")
