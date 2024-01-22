from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=255)

class Level(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, related_name='levels')
    level = models.IntegerField(null=True)
    effect = models.CharField(max_length=255, null=True)
    lock = models.BooleanField(default=False, null=True)
    state = models.CharField(max_length=255, null=True)

class Coin(models.Model):
    coin = models.IntegerField()