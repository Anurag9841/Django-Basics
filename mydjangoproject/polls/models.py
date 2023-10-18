from django.db import models
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    is_true = models.BooleanField()

class Friends(models.Model):
    name = models.CharField(max_length=100)
    details_friends = models.CharField(max_length=200)
