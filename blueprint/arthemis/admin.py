from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import EmailClassification
from .models import EmailContent
from .resources import EmailContentResource
from .services import classify_email_contents_with_orm

# Register your models here.


@admin.register(EmailContent)
class EmailContentAdmin(ImportExportModelAdmin):
    resource_class = EmailContentResource
    list_display = ("id", "subject", "short_body")
    search_fields = ("subject", "body")
    actions = ["classify_email_contents"]

    def classify_email_contents(self, request, queryset):
        classify_email_contents_with_orm()


@admin.register(EmailClassification)
class EmailClassificationAdmin(admin.ModelAdmin):
    list_display = ("id", "short_body", "is_newsletter")
    search_fields = ("email__body", "is_newsletter")
    list_filter = ("is_newsletter",)
