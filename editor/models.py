from django.db import models


class Card(models.Model):
    fn = models.TextField(default='')
    n = models.TextField(default='')
    tel = models.TextField(default='')
    version = models.TextField(default='')
    active = models.BooleanField(default=True)
