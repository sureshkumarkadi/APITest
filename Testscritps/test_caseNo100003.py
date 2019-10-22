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
import pytest
import sys
import traceback
import time
from selenium.webdriver.common.keys import Keys

dir_path = os.getcwd()
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Library")

from datadriver import readjson
jsonread1 = readjson()

from Launchapplication import launchapplication
application = launchapplication()

tf = 'test_TestcaseNo100003'

#Test case No : 100003
@pytest.mark.regression
class TestcaseNo100003(unittest.TestCase):
    def test_TestcaseNo100003(self) :
        try:
            browser = application.intializebrowser()
            application.inputurl(browser)
            registrationform_locator = application.registrationform_locators()
            application.website_login(browser,registrationform_locator)
            application.register_login(browser,registrationform_locator)
            validationmessage=browser.find_element_by_xpath(registrationform_locator['validation_message'])
            #time.sleep(5)
            self.assertEqual(validationmessage.text,'Invalid email address.')
            time.sleep(5)

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
            self.fail("Test case No : 100003 is failed")
        finally:
            application.closebrower(browser)

if __name__ == '__main__':
    unittest.main()

