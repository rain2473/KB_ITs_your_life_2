from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class AccountBook(models.Model):
    title = models.TextField()
    choice = (
              ('수입', '수입'),
              ('지출', '지출'),
    )
    contents = models.CharField(max_length=2, choices=choice)
    amount = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)