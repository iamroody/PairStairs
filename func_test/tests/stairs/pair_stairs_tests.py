from time import sleep
from nose.plugins.attrib import attr
from selenium import webdriver
from selenium.webdriver.common.by import By
from framework.basetest import BaseTest
from framework.database.sqlite_db_manager import DataBaseManager
from framework.utils.utils import url

class TestPairStairs(BaseTest):

    def setUp(self):
        self.driver = webdriver.Firefox()
        DataBaseManager().reset_db()

    def tearDown(self):
        self.driver.quit()
        DataBaseManager().reset_db()

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
        self.driver.get(url('/pairstairs'))
        self.assertEqual(self.driver.title, "Pair Stairs")
        self.assertIsNotNone(self.driver.find_element(By.CSS_SELECTOR,"#pair_stairs_table"))

    @attr("function_test")
    def test_should_update_count_when_click_one_pair(self):
        self.prepare_pair_data()
        self.driver.get(url('/pairstairs'))
        pre_pair_count = self.driver.find_element(By.CSS_SELECTOR, ".pair a")
        self.assertEqual('0', pre_pair_count.text)
        pre_pair_count.click()
        update_pair_count = self.driver.find_element(By.CSS_SELECTOR, ".pair a")
        self.assertEqual('1', update_pair_count.text)

    @attr("function_test")
    def test_should_remove_all_info_of_stairs(self):
        self.prepare_pair_data()
        self.driver.get(url('/pairstairs/reset'))
        message = self.driver.find_element(By.CSS_SELECTOR,".warning_message").text
        self.assertEqual(message, "There are not enough programmers (less than 2) to create stairs")
