'''
Created on Nov 24, 2017

@author: sandhya.palla
'''

import unittest
from selenium import webdriver
# from Libraries import reading_xlsx  as xl
from Pages.Login_Page import Login
from Pages.UserManagement import UserManagement
from Pages.AddUesr_Page import AddUser
from Libraries.applicationLibrary import library_func
# from Pages.LeaveList_page import SearchLeaveList

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
           
    def test_addUser(self):
        self.driver.get('https://orangehrm-demo-6x.orangehrmlive.com')
        self.assertIn("OrangeHRM", self.driver.title)
        libFunc=library_func(self.driver)
        try:
            login_page=Login(self.driver)
            login_page.login_admin()
            libFunc.take_screenShot('Pass_login_')
        except :
            print 'unable to login'
            libFunc.take_screenShot('fail_login_')
             
  
        admin_user=UserManagement(self.driver)
        admin_user.navigate_to_add_user()           
       
        add=AddUser(self.driver)
        add.addNewUser()
        try:
            libFunc.logout()
        except:
            print 'Failed to Logout'
        self.driver.close()

#     def test_leaveList(self):
#         self.driver.get('https://orangehrm-demo-6x.orangehrmlive.com/')
#         self.assertIn("OrangeHRM", self.driver.title)
#         libFunc=library_func(self.driver)
#         try:
#             login_page=Login(self.driver)
#             login_page.login_admin()
#             libFunc.take_screenShot('Pass_login_')
#         except :
#             print 'unable to login'
#             libFunc.take_screenShot('fail_login_')
#             
#         try:
#             search=SearchLeaveList(self.driver)
#             search.searchLeaves()
#             libFunc.take_screenShot('Pass_seachLeaves_')
#         except:
#             print 'Unable to search'
#             libFunc.take_screenShot('Fail_seachLeaves_')   
#         
#         try:
#             libFunc.logout()
#         except:
#             print 'Failed to Logout'
#         self.driver.close()
        
    
if __name__ == "__main__":
    unittest.main()    
