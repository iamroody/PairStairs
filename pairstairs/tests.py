"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from pairstairs.models import Programmer, Pair

class ModelTest(TestCase):
    def add_programmer(self):
        self.programmer_1 = Programmer(name="programmer_1")
        self.programmer_2 = Programmer(name="programmer_2")
        self.programmer_3 = Programmer(name="programmer_3")

        self.programmer_1.save()
        self.programmer_2.save()
        self.programmer_3.save()

    def setUp(self):
        self.add_programmer()

    def test_should_add_programmer_to_DB(self):
        self.assertTrue(Programmer.objects.filter(name="programmer_1").__contains__(self.programmer_1))
        self.assertTrue(Programmer.objects.filter(name="programmer_2").__contains__(self.programmer_2))
        self.assertTrue(Programmer.objects.filter(name="programmer_3").__contains__(self.programmer_3))
        self.assertEqual(Programmer.objects.all().count(),3)

    def test_return_count_1_when_programmer1_pair_with_programmer2(self):
        Pair.make_pair(self.programmer_1, self.programmer_2)
        self.assertEqual(self.get_pair_count(self.programmer_1, self.programmer_2), 1)

