from config import celery_app
from blueprint.arthemis.services import classify_email_contents


@celery_app.task(
    bind=True
)
def classify_email_contents_task(self, criteria: str = "unsubscribe"):
    classify_email_contents(criteria)
    return "Emails classified"
