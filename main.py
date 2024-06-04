# core modules
from selenium import webdriver

# Supporting modules
from login import login
from searchByDept import searchByDept
from retrieveInfo import retrieveInfo
from credentials import credentials

class init_driver():
    def setup_method(self, method=None):
        self.driver = webdriver.Chrome()
        return self.driver
    
    def teardown_method(self, method=None):
        self.driver.quit()

def main():
    init = init_driver()
    driver = init.setup_method()

    _u, _p = credentials('credentials.txt')
    signIn = login(driver)
    signIn.loginHRMS(_u, _p)

    search = searchByDept(driver)
    search.searchByDept('Corporate Affairs')

    ID = retrieveInfo(driver)
    _id, _desig, _mobile = ID.info(1)
    print(f'ID: {_id}, Designation: {_desig}, Mobile: {_mobile}')
    # ID.teardown_method()

if __name__ == '__main__':
    main()