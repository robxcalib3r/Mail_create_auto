# core modules
from selenium import webdriver

# Supporting modules
from login import login
from copyIDnumber import CopyIDnumber



def main():
    signIn = login()
    signIn.setup_method()
    signIn.login()
    ID = CopyIDnumber()
    name = ID.copyIDnumber()
    print(name)
    # ID.teardown_method()

if __name__ == '__main__':
    main()