from blueprint.arthemis.services import classify_email_contents_with_orm
from config import celery_app


@celery_app.task(
    bind=True,
)
def classify_email_contents_task(self, criteria: str = "unsubscribe"):
    classify_email_contents_with_orm(criteria)
    return "Emails classified"
