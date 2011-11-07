from nose.plugins.attrib import attr
from framework.basetest import BaseTest
from framework.utils.utils import url

class TestPairStairs(BaseTest):
    @attr("function_test")
    def test_should_not_create_pair_stairs_when_there_are_less_2_programmers(self):
        self.driver.get(url('pairstairs'))
        self.assertEqual(self.driver.title, "Pair Stairs")
        