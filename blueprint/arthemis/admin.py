from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import EmailContent
from .resources import EmailContentResource

# Register your models here.


@admin.register(EmailContent)
class EmailContentAdmin(ImportExportModelAdmin):
    resource_class = EmailContentResource
    list_display = ('id', 'subject', 'created_at', 'updated_at')
    search_fields = ('id', 'subject', 'created_at', 'updated_at')
