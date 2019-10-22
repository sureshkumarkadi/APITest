#-------------------------------------------------------------------------------
# Name:        RESTAPI
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     12-05-2016
# Update:      22-03-2017
# Copyright:   (c) causeway 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests
import json
import time
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))


sys.path.insert(0,folder_path+"\Library")
sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Data")

from datadriven import DataDriver

APIDetails = DataDriver()

time.sleep(3)

class ReopentenderusingRESTAPIclass():
      def AuthunticateAPI(self):
            time.sleep(1)
            #APIDetails = DataDriver()
            Username =APIDetails.readfromXML(folder_path+'\Data\APIdetails.xml','eTender','username')
            Password =APIDetails.readfromXML(folder_path+'\Data\APIdetails.xml','eTender','password')

            url = 'http://bg-etender-ser:8080/tenderservices/api/signin'

            Login = {'email':Username,'password':Password}

            headers = {'Content-type': 'application/x-www-form-urlencoded'}

            response = requests.post(url,data=Login,headers=headers)


            accesstoken = response.text
            return accesstoken


      def ReopentenderusingRESTAPI(self,accesstoken):
            # Reopen tender 19034

            TenderID =APIDetails.readfromXML(folder_path+'\Data\APIdetails.xml','eTender','tenderID')
            TendererReferenceID =APIDetails.readfromXML(folder_path+'\Data\APIdetails.xml','eTender','tendererReferenceID')

            url = 'http://bg-etender-ser:8080/tenderservices/api/tender/{0}/notify/reopentender'.format(TenderID) # {0} - Passing tender ID = 19034

            data1 = {
                      "tendererList": [
                        0
                             ],
                       "tendererReferenceList": [
                         TendererReferenceID
                            ]
                    }

            headers = {'Content-type': 'application/json', 'Accept': 'text/plain','access-token':accesstoken}

            response = requests.post(url, json=data1,headers=headers)


            time.sleep(2)

#create project

      def Createproject(self,accesstoken):
            time.sleep(2)

            Projectname =APIDetails.readfromXML(folder_path+'\Data\APIdetails.xml','eTender','projectname')
            Projectdescription =APIDetails.readfromXML(folder_path+'\Data\APIdetails.xml','eTender','projectdescription')
            ProjectRef =APIDetails.readfromXML(folder_path+'\Data\APIdetails.xml','eTender','projectRef')

            url = 'http://bg-etender-ser:8080/tenderservices/api/project'

            data1 = {
                      "id": 0,
                      "name": "ProjectfromRESTAPI",
                      "description": "Projectdescription",
                      "reference": "ProjectRef",
                      "address": {
                        "streetNumber": "",
                        "route": "",
                        "county": "",
                        "country": "",
                        "postalCode": "560017",
                        "formattedAddress": "MurugeshPalya,bangalore",
                        "vicinity": "",
                        "url": "",
                        "lng": 0,
                        "lat": 0
                      },
                      "projectType": {
                        "id": 1,
                        "type": "None"
                      },
                      "value": 0,
                      "approxValue": "4875000",
                      "status": "",
                      "dueDate": "2017-03-30T 0:00:00",
                      "startDate": "2017-03-15T 0:00:00",
                      "extSystemId": 1026,
                      "organisationId": 85
                    }

            headers = {'Content-type': 'application/json', 'access-token':accesstoken}
            response1 = requests.post(url, json=data1,headers=headers)

            json_data = json.loads(response1.text)
            #fetch project id
            idValue = json_data['id']
            time.sleep(1)
            #return json_data
            return idValue

#delete project

      def Deleteproject(self,idValue,accesstoken):
            time.sleep(2)

            #url = 'http://bg-etender-ser:8080/tenderservices/api/project/'+str(idValue)
            url = 'http://bg-etender-ser:8080/tenderservices/api/project/{0}'.format(idValue) # {0} - Passing project ID = 3176

            headers = {'Content-type': 'application/json', 'access-token':accesstoken}

            deleteresponse = requests.delete(url, headers=headers)


#create tender

      def Createtender(self,idValue,accesstoken):
        time.sleep(1)
        url = 'http://bg-etender-ser:8080/tenderservices/api/tender'

        data2 = {
              "system": {
                "id": 1,
                "description": "",
                "name": "Causeway Estimating v3",
                "version": "3.3.25.92"
              },
              "tendererList": [],
              "newTendererList": [
                {
                  "tenderId": 0,
                  "tenderDescription": "Mini Piling",
                  "email": "suresh@etender.com",
                  "name": "Aarsleff Piling",
                  "referenceId": 5783,
                  "code": "PIL011"
                }
              ],
              "tender": {
                "id": 0,
                "estimator": {
                  "id": 85
                },
                "extSystemId": 8371,
                "projectId": idValue,
                "name": "Mini Piling",
                "description": "Mini Piling",
                "reference": "DOMESTIC",
                "status": "PENDING",
                "tenderType": "TRADE",
                "dueDate": "2017-04-27T 0:00:00",
                "startDate": "1980-01-01T 0:00:00",
                "documentList": []
              },
              "tenderItem": [
                {
                  "tenderId": 0,
                  "priceIsRequired": False,
                  "ownRate": 0,
                  "documentList": [],
                  "reference": "",
                  "extension": False,
                  "id": 0,
                  "extSystemId": "310160",
                  "compositeItem": False,
                  "compositeItemId": "0",
                  "position": "1",
                  "previousItemId": "0",
                  "updateFlag": 0,
                  "unit": "",
                  "rate": 0,
                  "description": "PAVING, PLANTING, FENCING & FURNITURE",
                  "value": 0,
                  "quantity": 0
                },
                {
                  "tenderId": 0,
                  "priceIsRequired": False,
                  "ownRate": 0,
                  "documentList": [],
                  "reference": "",
                  "extension": False,
                  "id": 0,
                  "extSystemId": "310161",
                  "compositeItem": False,
                  "compositeItemId": "0",
                  "position": "2",
                  "previousItemId": "310160",
                  "updateFlag": 0,
                  "unit": "",
                  "rate": 0,
                  "description": "Q10: KERBS, EDGINGS, CHANNELS AND PAVING ACCESSORIES",
                  "value": 0,
                  "quantity": 0
                },
                {
                  "tenderId": 0,
                  "priceIsRequired": False,
                  "ownRate": 0,
                  "documentList": [],
                  "reference": "",
                  "extension": False,
                  "id": 0,
                  "extSystemId": "310162",
                  "compositeItem": False,
                  "compositeItemId": "0",
                  "position": "3",
                  "previousItemId": "310161",
                  "updateFlag": 0,
                  "unit": "",
                  "rate": 0,
                  "description": "Kerbs and edgings; Marley concrete block paviors",
                  "value": 0,
                  "quantity": 0
                },
                {
                  "tenderId": 0,
                  "priceIsRequired": False,
                  "ownRate": 0,
                  "documentList": [],
                  "reference": "",
                  "extension": False,
                  "id": 0,
                  "extSystemId": "310163",
                  "compositeItem": False,
                  "compositeItemId": "0",
                  "position": "4",
                  "previousItemId": "310162",
                  "updateFlag": 0,
                  "unit": "",
                  "rate": 0,
                  "description": "Splayed edging units; 100 mm wide; bed and point in cement mortar (1:3); haunching with 10 N/mm2 concrete:",
                  "value": 0,
                  "quantity": 0
                },
                {
                  "tenderId": 0,
                  "priceIsRequired": True,
                  "ownRate": 0,
                  "documentList": [],
                  "reference": "",
                  "extension": False,
                  "id": 0,
                  "extSystemId": "310164",
                  "compositeItem": False,
                  "compositeItemId": "0",
                  "position": "5",
                  "previousItemId": "310163",
                  "updateFlag": 0,
                  "unit": "m",
                  "rate": 0,
                  "description": "65 mm thick",
                  "value": 0,
                  "quantity": 1
                },
                {
                  "tenderId": 0,
                  "priceIsRequired": True,
                  "ownRate": 0,
                  "documentList": [],
                  "reference": "",
                  "extension": False,
                  "id": 0,
                  "extSystemId": "310165",
                  "compositeItem": False,
                  "compositeItemId": "0",
                  "position": "6",
                  "previousItemId": "310164",
                  "updateFlag": 0,
                  "unit": "m",
                  "rate": 0,
                  "description": "65 mm thick; curved work",
                  "value": 0,
                  "quantity": 2
                },
                {
                  "tenderId": 0,
                  "priceIsRequired": True,
                  "ownRate": 0,
                  "documentList": [],
                  "reference": "",
                  "extension": False,
                  "id": 0,
                  "extSystemId": "310166",
                  "compositeItem": False,
                  "compositeItemId": "0",
                  "position": "7",
                  "previousItemId": "310165",
                  "updateFlag": 0,
                  "unit": "m",
                  "rate": 0,
                  "description": "80 mm thick",
                  "value": 0,
                  "quantity": 3
                }
              ]
     }
        headers = {'Content-type': 'application/json','access-token':accesstoken}
        time.sleep(1)
        response2 = requests.post(url, json=data2,headers=headers)





