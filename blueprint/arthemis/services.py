"""
Arthemis - Services
"""

from .models import EmailContent, EmailClassification
from django.contrib.postgres.search import SearchVector


def classify_email_contents(criteria: str = "unsubscribe"):
    newsletter_query = EmailContent.objects.annotate(
        search=SearchVector("subject", "body")
    ).filter(search=criteria)

    if newsletter_query.exists():
        for email in newsletter_query.iterator():
            EmailClassification.objects.create(
                email=email,
                is_newsletter=True
            )
