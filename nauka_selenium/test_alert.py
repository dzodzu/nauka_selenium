# -*- coding: utf-8 -*-

#Import bibliotek
from selenium import webdriver
import unittest
import time
import os

class AlertTest(unittest.TestCase):
    """
    Klasa AlertTest dziedziczy po klasie
    TestCase z modułu unittest
    (to jest jakby scenariusz testowy)
    """

    def setUp(self):
        """
        (Warunki wstępne)
        To, co ma się wykonać przed każdym testem
        """
        self.driver = webdriver.Chrome()
        self.driver.get("file://"+os.getcwd()+"/strona2.html") #os.getcwd() importuje aktualny katalog, w którym znajduje się użytkownik
        self.driver.maximize_window() #lepiej maksymalizować

    def tearDown(self):
        """
        (Zakończenie)
        To, co ma się wykonać po każdym teście
        """
        self.driver.quit()

    def test_simple_alert(self):
        """
        To jest przypadek testowy pierwszy
        (kroki...)
        """
        moj_alert = self.driver.find_element_by_id('zwykly')
        moj_alert.click()
        time.sleep(2)
        simple_alert = self.driver.switch_to.alert
        #simple_alert = self.driver.switch_to_alert() - obecnie przestarzałe
        simple_alert.accept()
        time.sleep(2)

    def test_prompt(self):
        """
        To jest przypadek testowy drugi
        """
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
