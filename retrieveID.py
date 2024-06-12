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

class searchFromEservices():
    def __init__(self, driver):
        self.driver = driver

    ## retrieve ID by Email from e-services portal
    def retrieveID(self, _email):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, "search_by"))).click()
        dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, "search_by")))
        WebDriverWait(dropdown, 5).until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'By Mail']"))).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, "search_btn"))).click()
        ## Clear previous input
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "emp_id"))).clear()
        ## Send keys to search input
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "emp_id"))).send_keys(_email)
        _id = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//b[@style='font-size:22px']"))).get_attribute("value")
        input(_id)