from import_export import resources

from blueprint.arthemis.tasks import classify_email_contents_task

from .models import EmailContent


class EmailContentResource(resources.ModelResource):
    body = resources.Field(column_name="text", attribute="body")

    class Meta:
        model = EmailContent

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        super().after_import(dataset, result, using_transactions, dry_run, **kwargs)
        if not dry_run:
            classify_email_contents_task.apply_async(countdown=120)
