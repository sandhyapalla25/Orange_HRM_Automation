'''
Created on Nov 27, 2017

@author: sandhya.palla
'''
from xlrd import open_workbook
import sys


def read_from_xlsx(testName):
        file_name = 'C:\Users\sandhya.palla\Selenium_Python\\automating_OrangeHRM\Resources\orangeHRM.xlsx'
        try:
            wb = open_workbook(file_name)
        except IOError:
            print 'Could not read file:  ' + file_name
            sys.exit()
        f1 = wb.sheet_by_name(testName)
        list_d = {}
        for i in range(f1.ncols):
            list_d.update({str(f1.cell_value(0, i)):str(f1.cell_value(1, i))})
        return list_d

