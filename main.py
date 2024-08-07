## core modules
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import re

## Supporting modules
from core.login import login
from core.searchByDept import searchByDept
from core.retrieveInfo import retrieveInfo
from core.credentials import credentials
from core.searchMailbox import search
from core.modifyMail import modify

class init_driver():
    def setup_method(self, method=None):
        self.driver = webdriver.Chrome()
        return self.driver
    
    def teardown_method(self, method=None):
        self.driver.quit()

def main():
    ## Initializing webdriver for HRMS
    init = init_driver()
    driverHR = init.setup_method()

    ## Logging in to HRMS
    _uHR, _pHR = credentials('credentials.txt', 1, 2)
    signInHR_ = login(driverHR)
    signInHR_.loginHRMS(_uHR, _pHR)

    ## Initializing webdriver for Exchange
    driverEx = init.setup_method()

    # Logging in to Exchange
    _uE, _pE = credentials('credentials.txt', 5, 6)
    signInEx_ = login(driverEx)
    signInEx_.loginExchange(_uE, _pE)

    ## Search pressing search button
    s = search(driverEx, 0.2)

    # ## Searching by given Dept.
    # s_ = searchByDept(driverHR)
    # s_.searchByDept('Sales')

    ## Retreiving info by Serial No. of individuals
    
    info_serial = ['id', 'name', 'desig', 'ou', 'dept', 'mobile', 'email', 'loc']

    ## Page to start retrieving data from HRMS
    k = 2
    # First time opening page (Comment out if not needed)
    WebDriverWait(driverHR, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='pagination']/a[contains(text(), '{k}')]"))).click()
    
    ## Breaks loop if reaches end Page
    _endPage = 999
    while True:
        ## Looping through rows of employees
        for j in range(1, 51):
            ID = retrieveInfo(driverHR)
            info = [" "] * 8
            info = ID.info(j)
            # print(f'ID: {info[0]}, Designation: {info[1]}, Mobile: {info[2]}, Email: {info[3]}, Loc: {info[4]}')

            for i in range(len(info)):
                print(f'{info_serial[i]}: {info[i]}')

            # time.sleep(5)

            whiteList = ['@waltonplc.com', '@waltonbd.com', '@marcelbd.com', '@risingbd.com', '@walcart.com']
            for z in range(len(whiteList)):
                if info[6] == None:
                    break
                elif bool(re.search(whiteList[z], info[6])):
                    _ok = True
                    break
                else:
                    _ok = False

            ## Modifying exchange mailbox based on email
            if info[6] != None and _ok:
                # ## Switching to initial exchange window
                # driverEx.switch_to.window(driverEx.window_handles[0])

                ## Search with keywords
                foundMail = s.searchMailbox(info[6])
                if foundMail:
                    ## Modify
                    m = modify(driverEx, 0.2)
                    error = m.errorCheck()
                    if not error:
                        m.modifyContact(info[5], info[7])
                        m.modifyDesig(info[2], info[4], info[3])
                        time.sleep(0.5)
                    m.saveInfo()
                    # time.sleep(1)
                else:
                    # ## Manual input v1.0
                    # r = input('No mail found!, do you want to continue? "y" or "n": ')
                    # if r == 'y':
                    #     pass
                    # elif r == 'n':
                    #     exit()

                    ## Auto input into non-existent_mails.txt
                    print("No emails found writing into the txt file")
                    with open('non-existent_mails.txt', 'a') as f:
                        f.writelines(f'{info[6]}\n')



            # print(f'number of windows: {driverHR.window_handles}')
            # # driverHR.switch_to.window(driverHR.window_handles[-1])
            # print(f'Window name: {driverHR.title}')

            # for handle in driverHR.window_handles:
            #     driverHR.switch_to.window(handle)
            #     print(driverHR.title)

            
        if k == _endPage:
            break
        k += 1
        WebDriverWait(driverHR, 5).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='pagination']/a[contains(text(), '{k}')]"))).click()
    
    while input("Do you want to close?  ").lower() != ('y'):
        pass
    init.teardown_method()

if __name__ == '__main__':
    main()
