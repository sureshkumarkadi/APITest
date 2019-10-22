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

tf = 'test_TestcaseNo100004'

#Test case No : 100004
@pytest.mark.smoke
#@unittest.skip("not for this release")
class TestcaseNo100004(unittest.TestCase):
    def test_TestcaseNo100004(self) :
        data_json_files=jsonread1.readingmultiplejsonfiles()
        print(data_json_files)
        i=0
        while i<len(data_json_files):
            try:
                browser = application.intializebrowser()
                application.inputurl(browser)
                registrationform_testdata=jsonread1.jsonread(folder_path+'\Data'+'/'+data_json_files[i])
                registrationform_locator = application.registrationform_locators()
                #registrationform_testdata=application.registrationform_testdata1()
                application.website_login(browser,registrationform_locator)
                application.enter_email(browser,registrationform_locator,registrationform_testdata)
                application.register_login(browser,registrationform_locator)
                time.sleep(3)

                personalinfo=browser.find_element_by_xpath(registrationform_locator['personal_info'])
                self.assertEqual(personalinfo.text,'YOUR PERSONAL INFORMATION')
                time.sleep(3)

            except Exception:
                traceback.print_exc()
                browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
                self.fail("Test case No : 100004 is failed")
            finally:
                application.closebrower(browser)
                i=i+1

if __name__ == '__main__':
   unittest.main()

