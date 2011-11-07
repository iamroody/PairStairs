from nose.plugins.attrib import attr
from selenium.webdriver.common.by import By
from framework.basetest import BaseTest
from framework.utils.utils import url

class TestPairStairs(BaseTest):
    @attr("function_test")
    def test_should_not_create_pair_stairs_when_there_are_less_2_programmers(self):
        self.driver.get(url('/pairstairs'))
        self.assertEqual(self.driver.title, "Pair Stairs")
        message = self.driver.find_element(By.CSS_SELECTOR,".warning_message").text
        self.assertEqual(message, "There are not enough programmers (less than 2) to create stairs")

        