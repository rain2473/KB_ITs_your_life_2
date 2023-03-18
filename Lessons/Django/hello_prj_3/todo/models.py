from turtle import title
from django.db import models

# Create your models here.
class Todo(models.Model):#쿼리 관리자
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)