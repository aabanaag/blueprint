from factory.django import DjangoModelFactory
from factory import RelatedFactory

from factory.faker import Faker

from blueprint.users.models import User
from blueprint.arthemis.models import EmailContent, EmailClassification


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    email = Faker("email")


class EmailContentFactory(DjangoModelFactory):
    class Meta:
        model = EmailContent

    subject = Faker("sentence")
    body = Faker("text")


class EmailClassificationFactory(DjangoModelFactory):
    class Meta:
        model = EmailClassification

    email = RelatedFactory(EmailContentFactory)
    is_newsletter = Faker("boolean")


