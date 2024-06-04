import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class search():
    def __init__(self, driver):
        self.driver = driver

    def searchMailbox(self):
        self.driver.find_element(By.CLASS_NAME, 'ToolBarButtonLnk').click()
        self.driver.find_element(By.CLASS_NAME, 'filterTextBox').send_keys('just a test')