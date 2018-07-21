'''
Created on Nov 24, 2017

@author: sandhya.palla
'''
from selenium.webdriver.common.by import By

class UserManagement(object):
    def __init__(self,driver):
        self.driver=driver
        self.admin=(By.ID,'txtUsername')
        self.admin_userManagement=(By.ID,'txtPassword')
        self.add_user_button=(By.ID,'btnLogin')
    
#     def getAdmin(self):
#         return self.admin
#     def getUserManagement
    def navigate_to_add_user(self):
        self.driver.find_element(*self.admin).click()
        self.driver.find_element(*self.admin_userManagement).click()
        self.driver.find_element(*self.add_user_button).click()
