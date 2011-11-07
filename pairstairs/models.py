from django.db import models
# Create your models here.
from django.db.models.fields import CharField, IntegerField, DateTimeField
from django.db.models.fields.related import ForeignKey

class Programmer(models.Model):
    name = CharField(max_length=200)

class Pair(models.Model):
    programmer_1 = ForeignKey(Programmer, related_name="programmer_1")
    programmer_2 = ForeignKey(Programmer, related_name="programmer_2")
    count = IntegerField(default=0)
    last_time = DateTimeField(auto_now=True)

    def switch_programmer(self, programmer, another_programmer):
        if programmer.id > another_programmer.id:
            return another_programmer, programmer
        else:
            return programmer, another_programmer

    def make_pair(self, programmer, another_programmer):
        programmer_1, programmer_2 = self.switch_programmer(programmer, another_programmer)

        filter = Pair.objects.filter(programmer_1, programmer_2)

        if(filter.count() > 0):
            filter.update(count=filter.count() + 1)
        else:
            Pair(programmer_1, programmer_2).save()

    def get_pair_count(self, programmer, another_programmer):
        return Pair.objects.filter(programmer_1=programmer, programmer_2=another_programmer).count