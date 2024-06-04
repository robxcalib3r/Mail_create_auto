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

class login():
  def setup_method(self, method=None):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
  def teardown_method(self, method=None):
        self.driver.quit()

  def login(self):
    self.driver.get("https://hrms.waltonbd.com/HRMS/")
    self.driver.set_window_size(788, 816)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("I-454")
    self.driver.find_element(By.ID, "password").send_keys("R0b1n_kh!$@")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Self Service").click()
    elem = self.driver.find_element(By.LINK_TEXT, "Discover Employee")
    actions = ActionChains(self.driver)
    actions.move_to_element(elem).perform()
