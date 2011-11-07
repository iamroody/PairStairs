from time import sleep
from nose.plugins.attrib import attr
from selenium.webdriver.common.by import By
from framework.basetest import BaseTest
from framework.database.sqlite_db_manager import DataBaseManager
from framework.utils.utils import url

class TestPairStairs(BaseTest):

    def prepare_pair_data(self):
        self.driver.get(url('/pairstairs/add'))
        element = self.driver.find_element(By.CSS_SELECTOR, "#programmer_names")
        element.send_keys("Angle,Smile")
        self.driver.find_element(By.CSS_SELECTOR, "#add_programmers").click()

    @attr("function_test")
    def test_should_not_create_pair_stairs_when_there_are_less_2_programmers(self):
        self.driver.get(url('/pairstairs'))
        self.assertEqual(self.driver.title, "Pair Stairs")
        message = self.driver.find_element(By.CSS_SELECTOR,".warning_message").text
        self.assertEqual(message, "There are not enough programmers (less than 2) to create stairs")

    @attr("function_test")
    def test_should_display_pair_stairs(self):
        self.prepare_pair_data()
        self.assertEqual(self.driver.title, "Pair Stairs")
        self.assertIsNotNone(self.driver.find_element(By.CSS_SELECTOR,"#pair_stairs_table"))

    @attr("function_test")
    def test_should_update_count_when_click_one_pair(self):
        self.prepare_pair_data()
        self.driver.get(url('/pairstairs'))
        pair_count = self.driver.find_element(By.CSS_SELECTOR, "")
        self.assertEqual('0', pair_count.text)
        pair_count.click()
        self.assertEqual('1', pair_count.text)

    @attr("function_test")
    def test_should_remove_all_info_of_stairs(self):
        self.prepare_pair_data()
        self.driver.get(url('/pairstairs/reset'))
        message = self.driver.find_element(By.CSS_SELECTOR,".warning_message").text
        self.assertEqual(message, "There are not enough programmers (less than 2) to create stairs")
