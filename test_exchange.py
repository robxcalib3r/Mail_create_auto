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
    init = init_driver()
    driver = init.setup_method()

    _u, _p = credentials('credentials.txt', 5, 6)
    signIn = login(driver)
    signIn.loginExchange(_u, _p)

    # Search
    s = search(driver)
    s.searchMailbox(1, "Robin Gope")
    # Modify
    m = modify(driver)
    m.modifyContact(1, "016788609740000")

    time.sleep(5)


if __name__ == '__main__':
    main()