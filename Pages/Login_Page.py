'''
Created on Nov 24, 2017

@author: sandhya.palla
'''
from selenium.webdriver.common.by import By
# from Libraries import reading_xlsx  as xl
from Libraries import reading_xlsx as xl
class Login(object):
    def __init__(self,driver):
        self.driver=driver
        
        self.username = (By.ID,'txtUsername')
        self.password =(By.ID,'txtPassword')
        self.login = (By.ID,'btnLogin')
        
    def login_admin(self):
        valuesDict=xl.read_from_xlsx('Login')
        self.driver.find_element(*self.username).send_keys(valuesDict['username'])
        self.driver.find_element(*self.password).send_keys(valuesDict['password'])
        self.driver.find_element(*self.login).click()       