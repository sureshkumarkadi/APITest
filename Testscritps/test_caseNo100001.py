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

from Tenderserviceaccess import tenderservices
service = tenderservices()

from RESTAPIRequests import RESTAPIrequests
requests = RESTAPIrequests()

tf = 'test_TestcaseNo100001'

#Test case No : 100001
@pytest.mark.regression                      # Python code
@pytest.mark.smoke                           # Python code
class TestcaseNo100001(unittest.TestCase):   # Python code
    def test_TestcaseNo100001(self) :        # Python code
        try:
            url = service.tenderservices_api()
            response = requests.test_RESTAPIrequests(url)
            accesstoken = requests.test_RESTAPItoken(response)

        except Exception:                                                          # Python code
            #traceback.print_exc()                                                  # Python code
            #browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)# Selenium code
            self.fail("Test case No : 100001 is failed")                           # Python code

        #finally: # Python code
            #application.closebrower(browser) # Python code

if __name__ == '__main__':
    unittest.main()

