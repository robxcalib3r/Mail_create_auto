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

class login():
  def __init__(self, driver):
    self.driver = driver

  def loginHRMS(self, _user, _pw):
    self.driver.get("https://hrms.waltonbd.com/HRMS/")
    self.driver.set_window_size(1084, 816)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys(_user)
    self.driver.find_element(By.ID, "password").send_keys(_pw)
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    elem = self.driver.find_element(By.LINK_TEXT, "Self Service")
    actions = ActionChains(self.driver)
    actions.move_to_element(elem).perform()
    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Discover Employee"))).click()

  def loginExchange(self, _user, _pw):
    self.driver.get("https://webmail.waltonbd.com/ecp/")
    self.driver.set_window_size(788, 816)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys(_user)
    self.driver.find_element(By.ID, "password").send_keys(_pw)
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    # self.driver.find_element(By.CLASS_NAME, 'ToolBarButtonLnk').click()
    