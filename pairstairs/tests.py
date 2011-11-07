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
