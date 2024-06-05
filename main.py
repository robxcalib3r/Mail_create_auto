# core modules
from selenium import webdriver
import time

# Supporting modules
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

def main():
    # Initializing webdriver for HRMS
    init = init_driver()
    driverHR = init.setup_method()

    # Logging in to HRMS
    _uHR, _pHR = credentials('credentials.txt', 1, 2)
    signInHR_ = login(driverHR)
    signInHR_.loginHRMS(_uHR, _pHR)

    # Initializing webdriver for Exchange
    driverEx = init.setup_method()

    # Logging in to Exchange
    _uE, _pE = credentials('credentials.txt', 5, 6)
    signInEx_ = login(driverEx)
    signInEx_.loginExchange(_uE, _pE)

    # Searching by given Dept.
    s_ = searchByDept(driverHR)
    s_.searchByDept('Corporate Affairs')

    # Retreiving info by Serial No. of individuals
    ID = retrieveInfo(driverHR)
    info_serial = ['id', 'name', 'desig', 'ou', 'dept', 'mobile', 'email', 'loc']
    info = [" "] * 8
    info = ID.info(1)
    # print(f'ID: {info[0]}, Designation: {info[1]}, Mobile: {info[2]}, Email: {info[3]}, Loc: {info[4]}')

    for i in range(len(info)):
        print(f'{info_serial[i]}: {info[i]}')

    time.sleep(5)
    # Modifying exchange mailbox based on email
    if info[6] != None:
        # Search
        s = search(driverEx)
        s.searchMailbox(1, info[6])
        # Modify
        m = modify(driverEx, 2)
        m.modifyContact(info[5], info[7])
        m.modifyDesig(info[2], info[4], info[3])
        time.sleep(2)
        m.saveInfo()
        time.sleep(5)

    # init.teardown_method()

if __name__ == '__main__':
    main()