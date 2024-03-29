from django.db import models
from django.template.defaultfilters import truncatechars as tr


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class EmailContent(BaseModel):
    subject = models.CharField(max_length=255, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.body

    @property
    def short_body(self):
        return tr(self.body, 100)


class EmailClassification(BaseModel):
    email = models.OneToOneField(
        EmailContent,
        related_name="email_classification",
        on_delete=models.CASCADE,
    )
    is_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - {self.is_newsletter}"

    @property
    def short_body(self):
        return tr(self.email.body, 100)
