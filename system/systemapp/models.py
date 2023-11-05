from django.db import models

class client(models.Model):
    id = models.IntegerField(primary_key=7)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
