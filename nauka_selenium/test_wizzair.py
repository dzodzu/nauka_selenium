# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

valid_name = "John"
valid_surname = "Doe"

"""
Scenariusz:
Rejestracja nowego użytkownika na polskiej stronie wizzair.com

Przypadek testowy:
I. Rejestracja nowego użytkownika przy użyciu błędnego adresu e-mail (brak znaku '@')

Warunki wstępne:
1. Użytkownik niezalogowany
2. Przeglądarka otwarta na stronie https://wizzair.com/pl-pl#/

Kroki:
1. Klinij ZALOGUJ SIĘ
2. Kliknij REJESTRACJA
3. Wpisz imię
4. Wpisz nazwisko
5. Wybierz płeć
6. Wpisz kod kraju
7. Wpisz numer telefonu
8. Wpisz niepoprawny adres e-mail ("brak '@')
9. Wpisz hasło
10. Wybierz kraj
11. Zaznacz 'Akceptuję Informację o polityce prywatności'
12. Kliknij ZAREJESTRUJ SIĘ

Oczekiwany rezultat:
1. (Rejestracja nie powodzi się)
2. Użytkownik dostaje informację "Nieprawidłowy adres e-mail"
"""

class WizzairRegistration(unittest.TestCase):
    """
    Scenariusz:
    Rejestracja nowego użytkownika na polskiej stronie wizzair.com
    """
    def setUp(self):
        """
        Warunki wstępne:
        1. Użytkownik niezalogowany
        2. Przeglądarka otwarta na stronie https://wizzair.com/pl-pl#/
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        """
        Zakończenie
        """
        self.driver.quit()

    def test_wrong_email(self):
        """
        Przypadek testowy:
        I. Rejestracja nowego użytkownika przy użyciu błędnego adresu e-mail (brak znaku '@')

        Kroki:
        """
        driver = self.driver

        #1. Klinij ZALOGUJ SIĘ
        zaloguj_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]'))
        )
        zaloguj_btn.click()

        #2. Kliknij REJESTRACJA
        rejestracja_btn = driver.find_element_by_xpath('//button[contains(text(), "Rejestracja")]')
        rejestracja_btn.click()

        #3. Wpisz imię
        imie = driver.find_element_by_name('firstName')
        imie.send_keys(valid_name)

        #4. Wpisz nazwisko
        nazwisko = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
        nazwisko.send_keys(valid_surname)

        #5. Wybierz płeć
        #imie.click()
        plec = driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
        driver.execute_script("arguments[0].click();", plec) #Wymuszenie kliknięcia (stosować, gdy inne metody zawiodą)
        plec.click()

        #6. Wpisz kod kraju
        kod_kraju = driver.find_element_by_name('phone-number-country-code')

        sleep(2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
