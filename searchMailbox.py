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
import time

class search():
    def __init__(self, driver, waitTime):
        self.driver = driver
        self.waitTime = waitTime
        ## Switching to initial exchange window
        self.driver.switch_to.window(self.driver.window_handles[0])
        ## Switching frame to find the objects   
        frameMailbox = self.driver.find_element(By.XPATH, "//iframe[@class='abs0 hw100']")
        self.driver.switch_to.frame(frameMailbox)
        ## Search Button
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ToolBarItem  ToolBarButton ToolBarButton InlineSearchBarCommand  EnabledToolBarItem']"))).click()
        # time.sleep(self.waitTime)

    def searchMailbox(self, _strToSearch):
        actions = ActionChains(self.driver)
        ## Switching to initial exchange window
        self.driver.switch_to.window(self.driver.window_handles[0])
        ## Switching frame to find the objects   
        frameMailbox = self.driver.find_element(By.XPATH, "//iframe[@class='abs0 hw100']")
        self.driver.switch_to.frame(frameMailbox)

        ## Clear previous input
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_SearchBox"))).clear()
        ## Send keys to search input
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_SearchBox"))).send_keys(_strToSearch)
        time.sleep(self.waitTime)
        ## Press enter to search
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_SearchBox"))).send_keys(Keys.ENTER)
        time.sleep(self.waitTime)

        try:
            ## Checks how many rows of table is generated after the search
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//table[@id='ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_contentTable']/tbody/tr")))
            rows = self.driver.find_elements(By.XPATH, "//table[@id='ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_contentTable']/tbody/tr")
            number_of_rows = len(rows)
            print(f'Number of rows: {number_of_rows}')
        except Exception:
            number_of_rows = 0
            time.sleep(self.waitTime)

        # if not bool(WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), 'multiple warnings')]")))):      
        if (number_of_rows == 1):
            selectedRow = self.driver.find_element(By.XPATH, "//table[@id='ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_contentTable']/tbody/tr")
            actions.double_click(selectedRow).perform()
            return True
        elif(number_of_rows == 0):
            print(f"User {_strToSearch} not found")
            return False
        elif(number_of_rows > 1):
            input("Manually Select the User and Enter any key !")
            return True

             