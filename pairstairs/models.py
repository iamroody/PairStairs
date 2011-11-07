from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField
from django.db.models.fields.related import ForeignKey

class Programmer(models.Model):
    name = CharField(max_length=200)

class Pair(models.Model):
    programmer_1 = ForeignKey(Programmer, related_name="programmer_1")
    programmer_2 = ForeignKey(Programmer, related_name="programmer_2")
    count = IntegerField(default=0)
