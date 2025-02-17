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
sys.path.insert(0,folder_path+"\Env")

from datadriver import readjson

APIDetails = readjson()

time.sleep(3)

from Tenderserviceaccess import tenderservices
service = tenderservices()

class RESTAPIrequests():
      def test_RESTAPIrequests(self,url):
            time.sleep(1)

            registrationform_testdata = service.registrationform_testdata1()
            print(registrationform_testdata)

            URI = url + '/signin'
            print(URI)

            Login = {'email':registrationform_testdata['username'],'password':registrationform_testdata['password']}

            headers = {'Content-type': 'application/x-www-form-urlencoded'}

            response = requests.post(URI,data=Login,headers=headers)
            return response

            #accesstoken = response.text
            #return accesstoken

      def test_RESTAPItoken(self,response):
            time.sleep(1)
            accesstoken = response.text
            return accesstoken

      def ReopentenderusingRESTAPI(self,accesstoken):
            # Reopen tender 18837

            env = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')

            if env == 'StageURL':
                    TenderID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tenderIDStage')
                    TendererReferenceID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tendererReferenceIDStage')

                    StageURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','StageURL')

                    stageURL = StageURL + 'tenderservices/api/tender/{0}/notify/reopentender'.format(TenderID)  #Passing tender ID = 18837

                    data1 = {
                              "tendererList": [
                                0
                                     ],
                               "tendererReferenceList": [
                                 TendererReferenceID
                                    ]
                            }

                    headers = {'Content-type': 'application/json', 'Accept': 'text/plain','access-token':accesstoken}

                    response = requests.post(stageURL, json=data1,headers=headers)


                    time.sleep(2)

            elif env == 'PreStageURL':
                    PreStageURL = 'http://bg-etender-ser:8080/'

                    TenderID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tenderIDPreStage')
                    TendererReferenceID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tendererReferenceIDPreStage')

                    preStageURL = PreStageURL + 'tenderservices/api/tender/{0}/notify/reopentender'.format(TenderID)  #Passing tender ID = 18837


                    data1 = {
                              "tendererList": [
                                0
                                     ],
                               "tendererReferenceList": [
                                 TendererReferenceID
                                    ]
                            }

                    headers = {'Content-type': 'application/json', 'Accept': 'text/plain','access-token':accesstoken}

                    response = requests.post(preStageURL, json=data1,headers=headers)

                    time.sleep(2)

            elif env == 'MasterURL':
                    TenderID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tenderIDMaster')
                    TendererReferenceID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tendererReferenceIDMaster')

                    MasterURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','MasterURL')

                    masterURL = MasterURL + 'tenderservices/api/tender/{0}/notify/reopentender'.format(TenderID)  #Passing tender ID = 18837

                    data1 = {
                              "tendererList": [
                                0
                                     ],
                               "tendererReferenceList": [
                                 TendererReferenceID
                                    ]
                            }

                    headers = {'Content-type': 'application/json', 'Accept': 'text/plain','access-token':accesstoken}

                    response = requests.post(masterURL, json=data1,headers=headers)

                    time.sleep(2)

#create project

      def Createproject(self,accesstoken):
            time.sleep(2)

            Projectname =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','projectname')
            Projectdescription =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','projectdescription')
            ProjectRef =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','projectRef')

            env = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')

            if env == 'StageURL':

                StageURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','StageURL')

                stageURL = StageURL + 'tenderservices/api/project'

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
                          "extSystemId": 1073,
                          "organisationId": 85
                        }

                headers = {'Content-type': 'application/json', 'access-token':accesstoken}
                response1 = requests.post(stageURL, json=data1,headers=headers)

                json_data = json.loads(response1.text)
                #fetch project id
                idValue = json_data['id']
                time.sleep(1)
                #return json_data
                return idValue

            elif env == 'PreStageURL':
                PreStageURL = 'http://bg-etender-ser:8080/'

                preStageURL = PreStageURL + 'tenderservices/api/project'


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
                          "extSystemId": 1512,
                          "organisationId": 2429
                        }

                headers = {'Content-type': 'application/json', 'access-token':accesstoken}
                response1 = requests.post(preStageURL, json=data1,headers=headers)

                json_data = json.loads(response1.text)
                #fetch project id
                idValue = json_data['id']
                time.sleep(1)
                #return json_data
                return idValue

            elif env == 'MasterURL':

                MasterURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','MasterURL')

                masterURL = MasterURL + 'tenderservices/api/project'


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
                          "extSystemId": 1073,
                          "organisationId": 85
                        }

                headers = {'Content-type': 'application/json', 'access-token':accesstoken}
                response1 = requests.post(masterURL, json=data1,headers=headers)

                json_data = json.loads(response1.text)
                #fetch project id
                idValue = json_data['id']
                time.sleep(1)
                #return json_data
                return idValue

#delete project

      def Deleteproject(self,idValue,accesstoken):
            time.sleep(2)

            env = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')


            if env == 'StageURL':

                StageURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','StageURL')

                stageURL = StageURL + 'tenderservices/api/project/{0}'.format(idValue) # {0} - Passing project ID = 3176'


                headers = {'Content-type': 'application/json', 'access-token':accesstoken}

                deleteresponse = requests.delete(stageURL, headers=headers)


            elif env == 'PreStageURL':
                PreStageURL = 'http://bg-etender-ser:8080/'

                preStageURL = PreStageURL + 'tenderservices/api/project/{0}'.format(idValue) # {0} - Passing project ID = 3176'


                headers = {'Content-type': 'application/json', 'access-token':accesstoken}

                deleteresponse = requests.delete(preStageURL, headers=headers)


            elif env == 'MasterURL':

                MasterURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','MasterURL')

                masterURL = MasterURL + 'tenderservices/api/project/{0}'.format(idValue) # {0} - Passing project ID = 3176'


                headers = {'Content-type': 'application/json', 'access-token':accesstoken}

                deleteresponse = requests.delete(masterURL, headers=headers)


#create tender

      def Createtender(self,idValue,accesstoken):
        time.sleep(1)

        env = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')

        if env == 'StageURL':

            StageURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','StageURL')

            stageURL = StageURL + 'tenderservices/api/tender'


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
            response2 = requests.post(stageURL, json=data2,headers=headers)

        elif env == 'PreStageURL':
            PreStageURL = 'http://bg-etender-ser:8080/'

            preStageURL = PreStageURL + 'tenderservices/api/tender'


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
                      "id": 2429
                    },
                    "extSystemId": 1512,
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
            response2 = requests.post(preStageURL, json=data2,headers=headers)

        elif env == 'MasterURL':

            MasterURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','MasterURL')

            masterURL = MasterURL + 'tenderservices/api/tender'


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
            response2 = requests.post(masterURL, json=data2,headers=headers)

#create item

      def Additem(self,accesstoken):
            time.sleep(1)

            env = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','env')


            if env == 'StageURL':
                    TenderID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tenderIDStage')

                    StageURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','StageURL')

                    stageURL = StageURL + 'tenderservices/api/tender/{0}/item'.format(TenderID)  #Passing tender ID = 18837


                    data1 = {
                                  "compositeItem": False,
                                  "compositeItemId": "0",
                                  "description": "Unpriced item",
                                  "documentList": [
                                    ""
                                  ],
                                  "extSystemId": "486203",
                                  "extension": True,
                                  "id": 0,
                                  "note": "",
                                  "ownRate": 0,
                                  "position": 12,
                                  "previousItemId": "486202",
                                  "priceIsRequired": True,
                                  "quantity": 3,
                                  "rate": "0",
                                  "reference": "0",
                                  "tenderId": 18837,
                                  "unit": "Hour",
                                  "updateFlag": 0,
                                  "value": "0"
                                }

                    headers = {'Content-type': 'application/json','access-token':accesstoken}

                    response = requests.post(stageURL, json=data1,headers=headers)



                    time.sleep(2)

            elif env == 'PreStageURL':
                    PreStageURL = 'http://bg-etender-ser:8080/'

                    TenderID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tenderIDPreStage')

                    preStageURL = PreStageURL + 'tenderservices/api/tender/{0}/item'.format(TenderID)  #Passing tender ID = 18837

                    data1 = {
                                  "compositeItem": False,
                                  "compositeItemId": "0",
                                  "description": "Unpriced item",
                                  "documentList": [
                                    ""
                                  ],
                                  "extSystemId": "486203",
                                  "extension": True,
                                  "id": 0,
                                  "note": "",
                                  "ownRate": 0,
                                  "position": 12,
                                  "previousItemId": "486202",
                                  "priceIsRequired": True,
                                  "quantity": 3,
                                  "rate": "0",
                                  "reference": "0",
                                  "tenderId": 18837,
                                  "unit": "Hour",
                                  "updateFlag": 0,
                                  "value": "0"
                                }
                    headers = {'Content-type': 'application/json','access-token':accesstoken}

                    response = requests.post(preStageURL, json=data1,headers=headers)


                    time.sleep(2)

            elif env == 'MasterURL':
                    TenderID =APIDetails.readfromXML(folder_path+'\Data\APIdetailsStaging.xml','eTender','tenderIDMaster')

                    MasterURL = APIDetails.readfromXML(folder_path+'\Env\Setup.xml','eTender','MasterURL')

                    masterURL = MasterURL + 'tenderservices/api/tender/{0}/item'.format(TenderID)  #Passing tender ID = 18837


                    data1 = {
                                  "compositeItem": False,
                                  "compositeItemId": "0",
                                  "description": "Unpriced item",
                                  "documentList": [
                                    ""
                                  ],
                                  "extSystemId": "486203",
                                  "extension": True,
                                  "id": 0,
                                  "note": "",
                                  "ownRate": 0,
                                  "position": 12,
                                  "previousItemId": "486202",
                                  "priceIsRequired": True,
                                  "quantity": 3,
                                  "rate": "0",
                                  "reference": "0",
                                  "tenderId": 18837,
                                  "unit": "Hour",
                                  "updateFlag": 0,
                                  "value": "0"
                                }

                    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain','access-token':accesstoken}
                    headers = {'Content-type': 'application/json','access-token':accesstoken}

                    response = requests.post(masterURL, json=data1,headers=headers)



                    time.sleep(2)





