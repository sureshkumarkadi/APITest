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

dir_path = os.getcwd()
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Library")

from datadriver import readjson
jsonread1 = readjson()

from Launchapplication import launchapplication
application = launchapplication()

tf = 'test_TestcaseNo100001'

#Test case No : 100001
@pytest.mark.regression                      # Python code
@pytest.mark.smoke
@pytest.mark.hookwrapper                         # Python code
class TestcaseNo100001(unittest.TestCase):   # Python code
    def test_TestcaseNo100001(self) :        # Python code
        try:
            browser = application.intializebrowser()  # Python code
            application.inputurl(browser)             # Python code
            registrationform_locator=application.registrationform_locators() # Python code
            login_locator=application.login_locators() # Python code

            Tabs1= browser.find_element_by_xpath(registrationform_locator['tab1']) # Selenium code
            Tabs2= browser.find_elements_by_xpath(registrationform_locator['tab2'])# Selenium code
            Tabs3= browser.find_elements_by_xpath(login_locator['tab3'])           # Selenium code

            self.assertEqual(Tabs1.text,'WOMEN1')      # Python code
            self.assertEqual(Tabs2[1].text,'DRESSES') # Python code
            self.assertEqual(Tabs3[1].text,'T-SHIRTS')# Python code
            time.sleep(5)

        except Exception:                                                          # Python code
            #traceback.print_exc()                                                  # Python code
            #browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)# Selenium code
            application.pytest_runtest_makereport()
            #application._gather_screenshot(browser,item,report,summary,extra) # Python code
##            screenshot = browser.get_screenshot_as_base64()
##            pytest_html = item.config.pluginmanager.getplugin('html')
##
##            if pytest_html is not None:
##            # add screenshot to the html report
##                extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))
            self.fail("Test case No : 100001 is failed")                           # Python code

        finally: # Python code
            application.closebrower(browser) # Python code

if __name__ == '__main__':
    unittest.main()

