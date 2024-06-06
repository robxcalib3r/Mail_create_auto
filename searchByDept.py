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

class searchByDept():
  def __init__(self, driver):
    self.driver = driver

  def searchByDept(self, deptOption):
    # self.driver.get("https://hrms.waltonbd.com/HRMS/discoverEmp/index")
    # self.driver.set_window_size(788, 816)

    # Basic operation to retrieve certain options (Bug from e-services page)
    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstOperatingUnitId"))).click()
    dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstOperatingUnitId")))
    WebDriverWait(dropdown, 5).until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'Walton Electrocom Ltd.']"))).click()
    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstOperatingUnitId"))).click()
    dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstOperatingUnitId")))
    WebDriverWait(dropdown, 5).until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'All']"))).click()
    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstProductId"))).click()
    dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstProductId")))
    WebDriverWait(dropdown, 5).until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'Automobile']"))).click()
    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstProductId"))).click()
    dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstProductId")))
    WebDriverWait(dropdown, 5).until(EC.element_to_be_clickable((By.XPATH, "//option[. = 'ALL']"))).click()
    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstDepartmentId"))).click()
    dropdown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "allOrgMstDepartmentId")))

    # Select the Department where you want to copy the information
    WebDriverWait(dropdown, 5).until(EC.element_to_be_clickable((By.XPATH, f"//option[. = '{deptOption}']"))).click()

    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "SearchButton"))).click()

    # element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(1) > .class3")
    # actions = ActionChains(self.driver)
    # actions.double_click(element).perform()

    time.sleep(0.5)
