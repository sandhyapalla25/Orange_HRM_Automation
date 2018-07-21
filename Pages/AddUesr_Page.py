'''
Created on Nov 24, 2017

@author: sandhya.palla
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Libraries import reading_xlsx  as xl

class AddUser(object):
    def __init__(self,driver):
        self.driver=driver
        self.userRole=(By.ID,'systemUser_userType')
        self.employeeName=(By.ID,'systemUser_employeeName_empName')
        self.userName=(By.ID,'systemUser_userName')
        self.status=(By.ID,'systemUser_status')
        self.password=(By.ID,'systemUser_password')
        self.confirmPassword=(By.ID,'systemUser_confirmPassword')
        self.saveButton=(By.ID,'btnSave')
               
               
    def addNewUser(self):
#         list=xl.read_fro  m_xlsx('addNewUser')
        element=Select(self.driver.find_element_by_id('systemUser_userType'))
        element.select_by_value('1')
        self.driver.find_element(*self.employeeName).send_keys(list['employeeName'])
        self.driver.find_element(*self.userName).send_keys(list['userName'])
        element=Select(self.driver.find_element(*self.status))
        element.select_by_index(list['status'])
        self.driver.find_element(*self.password).send_keys(list['password'])
        self.driver.find_element(*self.confirmPassword).send_keys(list['confirmPassword'])
        self.driver.find_element(*self.saveButton).click()