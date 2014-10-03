from django.db import models

class Founders(models.Model):
    name = models.CharField(max_length=256)
    birth_year = models.PositiveIntegerField(default=1700)
    death_year = models.PositiveIntegerField(default=1700)
    position = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)

