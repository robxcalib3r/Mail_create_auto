import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class switchNav():
    def __init__(self, driver, waitTime) -> None:
        self.driver = driver
        self.waitTime = waitTime

        while True:
            try:
                ## Switching to initial exchange window
                self.driver.switch_to.window(self.driver.window_handles[0])
                break
            except:
                time.sleep(self.waitTime)
                print('------TimeOutException occurred in switching-------')
                self.driver.refresh()

    def secNav(self, xpathToClick):
        ## switch to given XPATH
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpathToClick))).click()
        time.sleep(self.waitTime)
        
