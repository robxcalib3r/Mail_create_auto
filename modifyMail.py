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
import re

class modify():
    def __init__(self, driver, _waitTime):
        # self.corpLoc = "Plot-1088,R-80ft.2, Block-I, Khilkhet, Vatara, Bashundhara R/A"
        # self.hqLoc = "Chandra, kaliakoir, Gazipur"
        # self.whiplc = "Walton Hi-Tech Industries PLC."
        # self.wdil = "Walton Digi-Tech Industries Ltd."

        self.ou = {
            'WHIPLC': "Walton Hi-Tech Industries PLC.",
            'WDTIL': "Walton Digi-Tech Industries Ltd.",
            'DPI': "Dream Park International",
            'WMTC': "Walton Micro-Tech Corporation",
            'WEL': "Walton Electrocom Ltd.",
            'WPZT': "Walton Plaza",
            'RBG': "RB Group of Companies Ltd.",
            'WSL': "Walton Shipping & Logistics"
        }

        self.driver = driver
        self.waitTime = _waitTime
        print(f'number of windows: {self.driver.window_handles}')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print(f'Window name: {self.driver.title}')


    def modifyDesig(self, _desig, _dept, _comp):
        # Switch to Organization
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@name='Organization']"))).click()
        time.sleep(self.waitTime)

        # Updates Designation
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxTitle']"))).clear()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxTitle']"))).send_keys(_desig)
        time.sleep(self.waitTime)
        
        # Updates Department
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxDepartment']"))).clear()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxDepartment']"))).send_keys(_dept)
        time.sleep(self.waitTime)
        
        # ## updates Company v1.0
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany']"))).clear()
        # if bool(re.search('WHIPLC', _comp)):
        #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany']"))).send_keys(self.whiplc)
        # elif bool(re.search('WDTIL', _comp)):
        #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany']"))).send_keys(self.wdil)
        # else:
        #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany']"))).send_keys(_comp)
        
        ## updates Company v2.0
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany']"))).clear()
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany']"))).send_keys(self.ou[_comp])
        except Exception:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_Organization_contentContainer_OrganizationPlaceHolder_tbxCompany']"))).send_keys(_comp)

        time.sleep(self.waitTime)


    def modifyContact(self, _phone, _location):
        # Updates contact information

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@name='ContactInformation']"))).click()
        time.sleep(self.waitTime)

        # Updates Phone Number
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_tbxPhone']"))).clear()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_tbxPhone']"))).send_keys(_phone)
        time.sleep(self.waitTime)

        # # Updates Office location
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_tbxPhone']"))).send_keys(Keys.PAGE_DOWN)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_moreOptionsContact_label']"))).click()
        # # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@uid='MoreOptionsContactLabel']"))).send_keys(Keys.PAGE_DOWN)
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_tbxOffice']"))).clear()
        # if bool(re.search('corporate', _location.lower())):
        #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_tbxOffice']"))).send_keys(self.corpLoc)
        # elif bool(re.search('headquarters', _location.lower())):
        #     WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ResultPanePlaceHolder_Mailbox_ContactInformation_contentContainer_ContactInformationPlaceHolder_tbxOffice']"))).send_keys(self.hqLoc)
        # time.sleep(self.waitTime)


    def saveInfo(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ResultPanePlaceHolder_ButtonsPanel_btnCommit']"))).click()
        
    def errorCheck(self):
        try:
            self.driver.find_element(By.XPATH, "//button[@id='dlgModalError_OK']").click()
        except Exception:
            return False
        return True