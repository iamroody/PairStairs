"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test.client import Client
from django.test.testcases import TestCase
from models import Programmer, Pair

class TestPairStairs(TestCase):
    def reset_db(self):
        Programmer.objects.all().delete()
        Pair.objects.all().delete()

    def setUp(self):
        self.reset_db()

    def tearDown(self):
        self.reset_db()

    def test_should_render_page_to_pair_stairs_page(self):
        response = Client().get('/pairstairs/')
        self.assertEqual(response.status_code, 200)

    def test_should_render_page_to_add_programmers_page(self):
        response = Client().get('/pairstairs/add')
        self.assertEqual(response.status_code, 200)

    def test_should_save_pairs(self):
        names = ','.join(['Kitty','Transformer'])
        Client().post('/pairstairs/add', {"programmer_names":names})
        self.assertEqual(Programmer.objects.count(), 2)
        self.assertEqual(Programmer.objects.filter(name="Kitty").count(),1)
        self.assertEqual(Programmer.objects.filter(name="Transformer").count(),1)

    def prepare_data(self):
        self.programmer1 = Programmer(name='Jason')
        self.programmer2 = Programmer(name='David')
        self.programmer1.save()
        self.programmer2.save()

    def test_should_reset_stairs(self):
        self.prepare_data()
        Client().get("/pairstairs/reset")
        self.assertEqual(Programmer.objects.count(), 0)

    def test_should_update_count_of_pair(self):
        self.prepare_data()
        Client().get("/pairstairs/2/1")
        pair = Pair.objects.get(programmer_1=self.programmer2, programmer_2=self.programmer1)
        self.assertEqual(pair.count, 1)

