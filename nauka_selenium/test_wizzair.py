# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

valid_name = "John"
valid_surname = "Doe"
valid_tel = "123456789"
invalid_tel = "qwerty"
valid_mail = "john@doe.pl"
invalid_mail = "johndoe.pl"
valid_password = "tester123"

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
        #profile = webdriver.FirefoxProfile()
        #profile.set_preference("geo.enabled", False)
        self.driver = webdriver.Chrome() #Chrome(), Firefox(firefox_profile = profile)
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
        kod_kraju = driver.find_element_by_class_name('phone-number__calling-code-selector__empty__placeholder')
        kod_kraju.click()
        kod_kraju_input = driver.find_element_by_name('phone-number-country-code')
        kod_kraju_input.send_keys('+48')
        kod_kraju_input.send_keys(Keys.RETURN)

        """
        country_code = driver.find_element_by_css_selector('div[data-test="booking-register-country-code"]')
        country_code.click()
        country_code_internal = driver.find_element_by_name("phone-number-country-code")
        country_code_internal.send_keys("+48")
        country_code_internal.send_keys(Keys.RETURN)
        """

        #7. Wpisz numer telefonu
        tel = driver.find_element_by_xpath('//input[@data-test="booking-register-phone"]')
        tel.click()
        tel.send_keys(valid_tel)

        #8. Wpisz niepoprawny adres e-mail ("brak '@')
        mail = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        mail.click()
        mail.send_keys(invalid_mail)

        # 9. Wpisz hasło
        passwd_input = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        passwd_input.send_keys(valid_password)

        #Przewin do przycisku ZAREJESTRUJ
        zarejestruj_btn =  driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestruj_btn.location_once_scrolled_into_view

        #10. Wybierz kraj
        country_field = driver.find_element_by_name('country-select')
        country_field.click()
        country_to_choose = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]/label[164]')
        country_to_choose.location_once_scrolled_into_view
        country_to_choose.click()

        #11. Zaznacz 'Akceptuję Informację o polityce prywatności'
        privacy_policy_checkbox = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy_checkbox.click()

        #12. Kliknij ZAREJESTRUJ SIĘ
        zarejestruj_btn.click()

        #### Oczekiwany rezultat: ####
        # 2. Użytkownik dostaje informację "Nieprawidłowy adres e-mail"
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices), 1)
        self.assertEqual(visible_error_notices[0].text, u"Nieprawidłowy adres e-mail")


    def test_wrong_tel(self):
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
        kod_kraju = driver.find_element_by_class_name('phone-number__calling-code-selector__empty__placeholder')
        kod_kraju.click()
        kod_kraju_input = driver.find_element_by_name('phone-number-country-code')
        kod_kraju_input.send_keys('+48')
        kod_kraju_input.send_keys(Keys.RETURN)

        """
        country_code = driver.find_element_by_css_selector('div[data-test="booking-register-country-code"]')
        country_code.click()
        country_code_internal = driver.find_element_by_name("phone-number-country-code")
        country_code_internal.send_keys("+48")
        country_code_internal.send_keys(Keys.RETURN)
        """

        #7. Wpisz niepoprawny numer telefonu
        tel = driver.find_element_by_xpath('//input[@data-test="booking-register-phone"]')
        tel.click()
        tel.send_keys(invalid_tel)

        #8. Wpisz poprawny adres e-mail
        mail = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        mail.click()
        mail.send_keys(valid_mail)

        # 9. Wpisz hasło
        passwd_input = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        passwd_input.send_keys(valid_password)

        #Przewin do przycisku ZAREJESTRUJ
        zarejestruj_btn =  driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestruj_btn.location_once_scrolled_into_view

        #10. Wybierz kraj
        country_field = driver.find_element_by_name('country-select')
        country_field.click()
        country_to_choose = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]/label[164]')
        country_to_choose.location_once_scrolled_into_view
        country_to_choose.click()

        #11. Zaznacz 'Akceptuję Informację o polityce prywatności'
        privacy_policy_checkbox = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy_checkbox.click()

        #12. Kliknij ZAREJESTRUJ SIĘ
        zarejestruj_btn.click()

        #### Oczekiwany rezultat: ####
        # 2. Użytkownik dostaje informację "Nieprawidłowy adres e-mail"
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices), 1)
        self.assertEqual(visible_error_notices[0].text, u"Please add a valid mobile phone number")


if __name__ == "__main__":
    unittest.main(verbosity=2)
