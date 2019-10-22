#-------------------------------------------------------------------------------
# Name:        Registration Form
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     21-07-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import os
import sys
import traceback
import time
import pytest
from selenium.webdriver.common.keys import Keys

dir_path = os.getcwd()
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Library")

from datadriver import readjson
jsonread1 = readjson()

from Launchapplication import launchapplication
application = launchapplication()

tf = 'test_TestcaseNo100002'

#Test case No : 100002
@pytest.mark.regression
class TestcaseNo100002(unittest.TestCase):
    def test_TestcaseNo100002(self) :
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            registrationform_locator = application.registrationform_locators()
            application.website_login(browser,registrationform_locator)
            submitbutton=browser.find_element_by_xpath(registrationform_locator['submit_button'])
            if submitbutton.is_displayed():
                print("pass")
            else:
                self.fail("Test case is failed")

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No : 100002 is failed")
        finally:
            application.closebrower(browser)

if __name__ == '__main__':
   unittest.main()

