#-------------------------------------------------------------------------------
# Name:        RESTAPI
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     12-05-2016
# Update:      18-08-2017
# Copyright:   (c) causeway 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

url = 'http://bg-etender-ser:8080/tenderservices/api/signin'
url = 'http://bg-etender-ser:8080/tenderservices/api/project'
url = 'http://bg-etender-ser:8080/tenderservices/api/project/projectID'
url = 'http://bg-etender-ser:8080/tenderservices/api/tender'
url = 'http://bg-etender-ser:8080/tenderservices/api/tender/tenderID/notify/reopentender'


import requests
import json
import time
import os
import sys
import unittest
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")
sys.path.insert(0,folder_path+"\Env")

from datadriver import readjson

APIDetails = readjson()

time.sleep(3)

from Tenderserviceaccess import tenderservices
service = tenderservices()


class RESTAPIrequests(unittest.TestCase):
    def test_decorator1(function):
     def wrapper():
        starttime = time.time()
        function()
        endtime = time.time()
        print(endtime - starttime)
     return wrapper

    @test_decorator1
    def test_RESTAPIrequests(self):
            time.sleep(1)

            #registrationform_testdata = service.registrationform_testdata1()
            #print(registrationform_testdata)

            URI = 'https://reqres.in/api/users'
            #print(URI)

            Login = {
                        "name": "morpheus",
                        "job": "leader"
                    }

            #headers = {'Content-type': 'application/json','Accept': 'text/plain'}
            headers = {'Content-type': 'application/json'}

            response = requests.post(URI,json=Login,headers=headers)
            #print(response)
            #print(response.status_code)
            jsonresponse = json.loads(response.text)
            #print(jsonresponse)
            #print(jsonresponse["id"])
            test = re.findall('^[0-9]*$',jsonresponse["id"])
            if test:
                print("ID contains only digits")
            else:
                print("ID contains digits + string")

            #print(jsonresponse)
            #print(response.headers) # content type,content length,server that you were requested for

if __name__ == '__main__':
    unittest.main()





