"""
Arthemis - Services
"""

from django.contrib.postgres.search import SearchVector

from .models import EmailClassification
from .models import EmailContent


def classify_email_contents_with_orm(criteria: str = "unsubscribe"):
    """
    Classify email contents using Django's ORM.
    Use postgres SearchVector to search for the criteria.
    """
    newsletter_query = EmailContent.objects.annotate(
        search=SearchVector("body"),
    ).filter(search=criteria.lower())

    if newsletter_query.exists():
        for email in newsletter_query.iterator():
            EmailClassification.objects.create(
                email=email,
                is_newsletter=True,
            )

    for email in EmailContent.objects.exclude(
        id__in=newsletter_query.values_list("id", flat=True),
    ).iterator():
        EmailClassification.objects.create(
            email=email,
            is_newsletter=False,
        )
