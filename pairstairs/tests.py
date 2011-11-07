"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test.client import Client
from django.test.testcases import TestCase
from models import Programmer, Pair

NAMES = ['Kitty','Transformer']

def format_names(names):
    return ', '.join(names)

class TestPairStairs(TestCase):
    def test_should_render_page_to_pair_stairs_page(self):
        response = Client().get('/pairstairs/')
        self.assertEqual(response.status_code, 200)

    def test_should_render_page_to_add_programmers_page(self):
        response = Client().get('/pairstairs/add')
        self.assertEqual(response.status_code, 200)

    def test_should_save_pairs(self):
        Client().post('/pairstairs/add', {"programmer_names":format_names(NAMES)})
        for name in NAMES:
            print Programmer.objects.filter(name=name)
            self.assertEqual(Programmer.objects.filter(name=name).count(), 1)

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
        pair = Pair()
        pair.make_pair(self.programmer_1, self.programmer_2)

