'''
Created on Nov 24, 2017

@author: sandhya.palla
'''
from selenium.webdriver.common.by import By
 
from time import sleep
import datetime


class library_func():

    def __init__(self, driver):
        self.driver = driver
        self.WelcomeIcon = (By.ID, 'welcome')
        self.logoutIcon = (By.LINK_TEXT, 'Logout')
        
    def logout(self):
        self.driver.find_element(*self.WelcomeIcon).click()
        sleep(1)
        self.driver.find_element(*self.logoutIcon).click()

    def take_screenShot(self, testName):
        d = str(datetime.datetime.now())
        path = str('C:\\Users\sandhya.palla\Selenium_Python\\automating_OrangeHRM\Libraries\screenshots\img') + testName + ''.join(e for e in d if e.isalnum())
        self.driver.save_screenshot(path + '.png')
        
#         
