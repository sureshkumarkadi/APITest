#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     21-07-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
import os
import sys

dir_path = os.getcwd()
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

class readjson():
    def jsonread(self,filename):         # run time will provide the filepath
        with open(filename) as jsonfile: # opens the json object
            value = json.load(jsonfile)  # converts json object into python object
            return value                 # returns value

    def readingmultiplejsonfiles(self):
        path_to_jsonfiles=folder_path+'\Data'
        data_json_files=[json_file for json_file in os.listdir(path_to_jsonfiles) if json_file.endswith('.json')]
        return data_json_files

    def readingmultiplejsonfiles1(self):
        path_to_jsonfiles=folder_path+'\Env'
        data_json_files=[json_file for json_file in os.listdir(path_to_jsonfiles) if json_file.endswith('.json')]
        return data_json_files




