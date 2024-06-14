## core modules
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import re

## Support modules
from login import login
from retrieveInfo import retrieveInfo
from credentials import credentials
from retrieveID import searchFromEservices

class init_driver():
    def setup_method(self, method=None):
        self.driver = webdriver.Chrome()
        return self.driver
    
    def teardown_method(self, method=None):
        self.driver.quit()

def main(filename, initLine, endLine):
    ## Initializing webdriver for HRMS
    init = init_driver()
    # driverHR = init.setup_method()
    driverES = init.setup_method()

    # ## Logging in to HRMS
    # _uHR, _pHR = credentials('credentials.txt', 1, 2)
    # signInHR_ = login(driverHR)
    # signInHR_.loginHRMS(_uHR, _pHR)

    ## Load into Eservices
    driverES.get('http://192.168.200.135/pl/')

    mailList = open(filename, 'r')
    mailListLines = mailList.readlines()

    count = 1
    for lineNo in range(initLine, endLine):
        # input(mailListLines[lineNo])
        email = mailListLines[lineNo].split('\t')[1]

        eservice = searchFromEservices(driverES)
        eservice.retrieveID(email)
        # r = retrieveInfo(driverHR)
        # r.info(1)

if __name__ == '__main__':
    main('total_active_inactive_list.txt', 0, 1)