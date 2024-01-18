from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, null=True)

class Level(models.Model):
    effect = models.CharField(max_length=255)
    lock = models.BooleanField(default=False)
    state = models.CharField(max_length=255)

class Coin(models.Model):
    coin = models.IntegerField()