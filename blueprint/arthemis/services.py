"""
Arthemis - Services
"""

import pandas as pd
from django.contrib.postgres.search import SearchVector

from .models import EmailClassification
from .models import EmailContent


def classify_email_contents_with_pandas(criteria: str = "unsubscribe"):
    """
    Classify email contents using pandas,
    by converting the queryset to a pandas DataFrame.
    """
    dataset = pd.DataFrame(
        EmailContent.objects.filter(email_classification__isnull=True).values(),
    )

    newsletter_dataset = dataset[dataset["body"].str.contains(criteria, case=False)]

    if not newsletter_dataset.empty:
        for _, row in newsletter_dataset.iterrows():
            EmailClassification.objects.create(
                email_id=row["id"],
                is_newsletter=True,
            )

        dataset.drop["id"].subtract(newsletter_dataset["id"])

    for _, row in dataset.iterrows():
        EmailClassification.objects.create(
            email_id=row["id"],
            is_newsletter=False,
        )


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