from django.db import models

class Details(models.Model):
    code = models.CharField(max_length=25)
    description = models.TextField(blank=True)


class Keywords(models.Model):
    keyword = models.CharField(max_length=50)
    detail = models.ManyToManyField(Details)
