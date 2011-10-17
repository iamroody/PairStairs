from django.db import models

# Create your models here.
class Programmer(models.Model):
    name = models.fields.CharField(max_length=200)

class Pair(models.Model):
    programmer_1 = models.ForeignKey(Programmer, related_name="programmer_1")
    programmer_2 = models.ForeignKey(Programmer, related_name="programmer_2")
    count = models.fields.IntegerField(null=True, blank=True)
    last_time = models.fields.DateTimeField(auto_now=True)