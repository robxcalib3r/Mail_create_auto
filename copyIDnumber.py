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

class CopyIDnumber():
  
  def copyIDnumber(self, deptOption = 'Corporate Affairs'):
    # self.driver.get("https://hrms.waltonbd.com/HRMS/discoverEmp/index")
    # self.driver.set_window_size(788, 816)

    # Basic operation to retrieve certain options (Bug from e-services page)
    self.driver.find_element(By.ID, "allOrgMstOperatingUnitId").click()
    dropdown = self.driver.find_element(By.ID, "allOrgMstOperatingUnitId")
    dropdown.find_element(By.XPATH, "//option[. = 'Walton Electrocom Ltd.']").click()
    self.driver.find_element(By.ID, "allOrgMstOperatingUnitId").click()
    dropdown = self.driver.find_element(By.ID, "allOrgMstOperatingUnitId")
    dropdown.find_element(By.XPATH, "//option[. = 'All']").click()
    self.driver.find_element(By.ID, "allOrgMstProductId").click()
    dropdown = self.driver.find_element(By.ID, "allOrgMstProductId")
    dropdown.find_element(By.XPATH, "//option[. = 'Automobile']").click()
    self.driver.find_element(By.ID, "allOrgMstProductId").click()
    dropdown = self.driver.find_element(By.ID, "allOrgMstProductId")
    dropdown.find_element(By.XPATH, "//option[. = 'ALL']").click()
    self.driver.find_element(By.ID, "allOrgMstDepartmentId").click()
    dropdown = self.driver.find_element(By.ID, "allOrgMstDepartmentId")

    # Select the Department where you want to copy the information
    dropdown.find_element(By.XPATH, f"//option[. = {deptOption}]").click()

    self.driver.find_element(By.ID, "SearchButton").click()

    name = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(1) > .class3").text()
    
    # element = self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(1) > .class3")
    # actions = ActionChains(self.driver)
    # actions.double_click(element).perform()

    return name
  
