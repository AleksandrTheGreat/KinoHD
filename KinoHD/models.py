from django.db import models

class Character(models.Model):
    title = models.CharField(max_length=100, )