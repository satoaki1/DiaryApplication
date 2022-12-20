from django.db import models
from django.utils import timezone
import uuid


class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    date = models.DateField(verbose_name='Date', default=timezone.now())
    title = models.CharField(verbose_name='Title', max_length=40)
    text = models.CharField(verbose_name='Component', max_length=200)
    created_at = models.DateTimeField(verbose_name='Created at', default=timezone.now())
    updated_at = models.DateTimeField(verbose_name='Updated_at', blank=True, null=True)

# Create your models here.
