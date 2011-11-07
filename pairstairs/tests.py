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

    def test_should_update_count_of_pair(self):
        programmer1 = Programmer(name='Jason')
        programmer2 = Programmer(name='David')
        programmer1.save()
        programmer2.save()
        Client().get("/pairstairs/2/1")
        pair = Pair.objects.get(programmer_1=programmer2, programmer_2=programmer1)
        self.assertEqual(1, pair.count)
