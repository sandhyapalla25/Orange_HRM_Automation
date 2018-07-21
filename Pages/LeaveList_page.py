'''
Created on Nov 28, 2017

@author: sandhya.palla
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Libraries import reading_xlsx  as xl


class SearchLeaveList:
    def __init__(self,driver):
        self.driver=driver
        self.leave=(By.ID,'menu_leave_viewLeaveModule')
        self.leavelist=(By.ID,'menu_leave_viewLeaveList')
        self.fromDate=(By.ID,'calFromDate')
        self.toDate=(By.ID,'calToDate')
        self.check_all=(By.ID,'leaveList_chkSearchFilter_checkboxgroup_allcheck')
        self.employee=(By.ID,'leaveList_txtEmployee_empName')
        self.subUnit=(By.ID,'leaveList_cmbSubunit')
        self.includePastEmployees=(By.ID,'leaveList_cmbWithTerminated')
        self.searchBtn=(By.ID,'btnSearch')
        self.resetBtn=(By.ID,'btnReset')
             
    def searchLeaves(self):
        valuesDict=xl.read_from_xlsx('searchLeaves')
        self.driver.find_element(*self.leave).click()
        self.driver.find_element(*self.leavelist).click()
        self.driver.find_element(*self.fromDate).clear()
        self.driver.find_element(*self.fromDate).send_keys(valuesDict['fromDate'])
        self.driver.find_element(*self.toDate).clear()
        self.driver.find_element(*self.toDate).send_keys(valuesDict['toDate'])
        self.driver.find_element(*self.check_all).click()
        self.driver.find_element(*self.employee).send_keys(valuesDict['employee'])
        select=Select(self.driver.find_element(*self.subUnit))
        select.select_by_visible_text(valuesDict['subUnit'])
        self.driver.find_element(*self.includePastEmployees).click()
        self.driver.find_element(*self.searchBtn).click()
        
            
        
        
        




