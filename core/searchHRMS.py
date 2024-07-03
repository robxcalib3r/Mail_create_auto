import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class search():
    def __init__(self, driver):
        self.driver = driver

    def searchFromHRMS(self, strToSearch):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "anyField"))).click()
        dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "anyField")))
        WebDriverWait(dropdown, 5).until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'Walton Electrocom Ltd.']"))).click()