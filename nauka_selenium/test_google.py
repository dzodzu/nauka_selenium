# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time

class WsbPlSelectors(unittest.TestCase):

    # Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.google.pl")

    def test_find_element(self):
    # Instrukcje, które zostaną automatycznie wykonane po każdym teście
        #Wyszukuję nazwę elementu (name)
        input_field = self.driver.find_element_by_name("q")
        input_field.send_keys("tester podyplomowe")
        input_field.submit() #Wysyłam formularz
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

# Początek mojego programu
# wywołuję funkcję main() z modułu unittest,
# która w automatyczny sposób będzie już wiedziała
# co dalej robić z utworzoną wyżej klasą
if __name__ == "__main__":
    unittest.main(verbosity=2)
