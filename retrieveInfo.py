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

class retrieveInfo():
  def __init__(self, driver):
    self.driver = driver

  def info(self, serial):
    _id = self.driver.find_element(By.CSS_SELECTOR, f".even:nth-child({serial}) > .class3").text
    _desig = self.driver.find_element(By.CSS_SELECTOR, f".even:nth-child({serial}) > .class5").text.split("\n")[0]
    _mobile = self.driver.find_element(By.CSS_SELECTOR, f".even:nth-child({serial}) > .class13").text.split("\n")[0]

    return _id, _desig, _mobile
