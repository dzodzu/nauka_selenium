# -*- coding: utf-8 -*-

#Zaimportiowanie bibliotek
from selenium import webdriver
import time

#Stwórz nowy sterownik do Chrome
driver = webdriver.Chrome()
driver.get("http://www.wsb.pl")
#Poczekaj 5 sekund
time.sleep(5)
#Zamknij sterownik
driver.quit()
