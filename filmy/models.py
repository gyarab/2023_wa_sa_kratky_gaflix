from django.db import models


class Movie(models.Model):
    title = models.CharFiels(max_lenght=300) 
    year = models.PositioveSmallIntegerField()
