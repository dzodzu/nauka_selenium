# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time

class WsbPlSelectors(unittest.TestCase):

    # Instrukcje, które zostaną automatycznie wykonane przed każdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.wsb.pl")

    def test_find_element(self):
    # Instrukcje, które zostaną automatycznie wykonane po każdym teście
        #Wyszukuję ciało strony (body)
        self.driver.find_element_by_tag_name("body")
        #Wyszukuję ikonę wyszukiwania
        self.driver.find_element_by_class_name("search-icon")
        #Wyszukuję link 'Studia podyplomowe'
        #link = self.driver.find_element_by_link_text("Studia podyplomowe")
        #link.click()
        link2 = self.driver.find_element_by_partial_link_text("dia podyplomowe")
        link2.click()

    def tearDown(self):
        self.driver.quit()

# Początek mojego programu
# wywołuję funkcję main() z modułu unittest,
# która w automatyczny sposób będzie już wiedziała
# co dalej robić z utworzoną wyżej klasą
if __name__ == "__main__":
    unittest.main(verbosity=2)
