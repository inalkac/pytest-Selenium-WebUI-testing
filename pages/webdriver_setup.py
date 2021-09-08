from selenium import webdriver
import os

class WebdriverSetup():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = f"{os.curdir}/webdrivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
    
    def getDriver(self):
        return self.driver