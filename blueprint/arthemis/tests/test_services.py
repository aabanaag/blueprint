"""
Test cases for the services module.
"""

from django.test import TestCase
from factory.faker import faker

from blueprint.arthemis.factories import EmailContentFactory
from blueprint.arthemis.models import EmailClassification
from blueprint.arthemis.models import EmailContent
from blueprint.arthemis.services import classify_email_contents_with_orm

faker = faker.Faker()


class TestClassifyEmailContents(TestCase):
    """
    Test case for the classify_email_contents service.
    """

    def setUp(self):
        super().setUp()

        EmailContentFactory.create_batch(
            20,
        )

    def test_should_classify_email_contents(self):
        """
        Test the classify_email_contents service.
        """
        email = EmailContent.objects.create(
            subject=faker.sentence(),
            body=f"{faker.paragraph()} Unsubscribe to stop receiving emails.",
        )

        classify_email_contents_with_orm()

        assert (
            EmailClassification.objects.filter(
                email=email,
                is_newsletter=True,
            ).exists()
            is True
        )

    def test_should_classify_email_contents_with_criteria(self):
        """
        Test the classify_email_contents service with a criteria.
        """
        email = EmailContent.objects.create(
            subject=faker.sentence(),
            body=f"{faker.paragraph()}, this is a newsletter.",
        )

        classify_email_contents_with_orm("newsletter")

        assert (
            EmailClassification.objects.filter(
                email=email,
                is_newsletter=True,
            ).exists()
            is True
        )

    def test_should_not_classify_email_contents(self):
        """
        Test the classify_email_contents service without any criteria.
        """
        email = EmailContent.objects.create(
            subject=faker.sentence(),
            body=f"{faker.paragraph()}",
        )

        classify_email_contents_with_orm()

        assert (
            EmailClassification.objects.filter(
                email=email,
                is_newsletter=True,
            ).exists()
            is False
        )
