from django.db import models


class Alert(models.Model):
    message = models.TextField()
    currencie = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

class Rule(models.Model):
    currencie = models.CharField(max_length=30, unique=True)
    value_min = models.FloatField(null=True)
    value_max = models.FloatField(null=True)
