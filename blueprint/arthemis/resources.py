from import_export import resources
from .models import EmailContent


class EmailContentResource(resources.ModelResource):
    body = resources.Field(column_name='text', attribute='body')

    class Meta:
        model = EmailContent


