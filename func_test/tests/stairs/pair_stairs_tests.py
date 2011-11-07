import unittest
from selenium import webdriver

class TestPairStairs(unittest.TestCase):
    def test_should_not_create_pair_stairs_when_there_are_less_2_programmers(self):
        self.driver=webdriver.Firefox()
        self.driver.get('http://localhost:8000/pairstairs')
        self.assertEqual(self.driver.title, "Pair Stairs")
