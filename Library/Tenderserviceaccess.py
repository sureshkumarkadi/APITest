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

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os
import sys
import pytest
import unittest

#Getting current working folder
dir_path = os.getcwd()

#Getting parent of current working folder
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

#Navigating to the desired folder
sys.path.insert(0,folder_path+"\Syslibrary")

#Imoprting module from Syslibrary
from datadriver import readjson

#Creating class object and instance of that object
jsonread1 = readjson()

class tenderservices():
    def tenderservices_api(self):
        #from instance object calling function 'jsonread'
        env = jsonread1.jsonread(folder_path+'\Env\prestagURLS.json')
        if env['url']  == 'prestagurl':
            # Intializing prestagURL
            url = env['prestagurl']
            return url
            #print(prestagurl)

        elif env['url']  == 'stagurl':
            # Intializing stagURL
            url = env['stagurl']
            return url
            #print(stagurl)



