from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Excellent_Man(models.Model):
    who_recommend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    reason = models.TextField()
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True)
    more_information = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
