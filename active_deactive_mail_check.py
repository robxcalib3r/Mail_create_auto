## core modules
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

## Supporting modules
from login import login
from searchByDept import searchByDept
from retrieveInfo import retrieveInfo
from credentials import credentials
from searchMailbox import search
from modifyMail import modify

class init_driver():
    def setup_method(self, method=None):
        self.driver = webdriver.Chrome()
        return self.driver
    
    def teardown_method(self, method=None):
        self.driver.quit()

def check_inactive(filename, save_inactives):
    ## Initializing webdriver for HRMS
    init = init_driver()
    ## Initializing webdriver for Exchange
    driverEx = init.setup_method()

    # Logging in to Exchange
    _uE, _pE = credentials('credentials.txt', 5, 6)
    signInEx_ = login(driverEx)
    signInEx_.loginExchange(_uE, _pE)

    active = open(filename, 'r')

    s = search(driverEx, 0.2)
    for line in active:
        _, enabled = s.disabledMailCheck(line)
        if not enabled:
            # print(f'{line} not found!')
            with open(save_inactives, 'a') as file:
                file.writelines(f'{line}')

def check_active(filename, save_actives):
    ## Initializing webdriver for HRMS
    init = init_driver()
    ## Initializing webdriver for Exchange
    driverEx = init.setup_method()

    # Logging in to Exchange
    _uE, _pE = credentials('credentials.txt', 5, 6)
    signInEx_ = login(driverEx)
    signInEx_.loginExchange(_uE, _pE)

    active = open(filename, 'r')

    s = search(driverEx, 0.2)
    for line in active:
        _, enabled = s.disabledMailCheck(line)
        if enabled:
            # print(f'{line} not found!')
            with open(save_actives, 'a') as file:
                file.writelines(f'{line}')

if __name__ == '__main__':
    check_active('inactive_employees_from_shell.txt', 'active_employees_from_shell.txt')