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
    if serial % 2 == 1:
      tag = 'even'
    else:
      tag = 'odd'
      
    _id = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class3").text
    _name = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class4").text
    _desig = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class5").text.split("\n")[0]
    _loc = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class5").text.split("\n")[1]
    _ou = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class9").text.split("\n")[0]
    _dept = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class9").text.split("\n")[2]
    _mobile = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class13").text.split("\n")[0]
    _status = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class15b").text.split("\n")[0].strip()
    try:
      _email = self.driver.find_element(By.CSS_SELECTOR, f".{tag}:nth-child({serial}) > .class13").text.split("\n")[1]
    except Exception:
      _email = None


    return [_id, _name, _desig, _ou, _dept, _mobile, _email, _loc, _status]
