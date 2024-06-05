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
    def __init__(self, driver):
        self.driver = driver

    def searchMailbox(self, waitTime, _strToSearch):
        actions = ActionChains(self.driver)

        frameMailbox = self.driver.find_element(By.XPATH, "//iframe[@class='abs0 hw100']")
        self.driver.switch_to.frame(frameMailbox)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ToolBarItem  ToolBarButton ToolBarButton InlineSearchBarCommand  EnabledToolBarItem']"))).click()
        time.sleep(waitTime)
        self.driver.find_element(By.ID, "ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_SearchBox").send_keys(_strToSearch)
        time.sleep(waitTime)
        self.driver.find_element(By.ID, "ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_SearchBox").send_keys(Keys.ENTER)
        time.sleep(waitTime)
        rows = self.driver.find_elements(By.XPATH, "//table[@id='ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_contentTable']/tbody/tr")
        number_of_rows = len(rows)
        print(f'Number of rows: {number_of_rows}')
        time.sleep(waitTime)
        if (number_of_rows == 1):
            selectedRow = self.driver.find_element(By.XPATH, "//table[@id='ResultPanePlaceHolder_ctl00_ctl02_ctl01_MailboxListView_contentTable']/tbody/tr")
            actions.double_click(selectedRow).perform()
        elif(number_of_rows == 0):
            print(f"User {_strToSearch} not found")
        elif(number_of_rows > 1):
            input("Manually Select the User and Enter any key !")
            

             