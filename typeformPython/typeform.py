'''
Author: Robert Banks
This class connects to typeform and is used to return formatted typeform
responses from the typeform API.
'''

import requests

class typeform:

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def getForm (self, formKey):
        #TODO implement exception for no network etc.
        apiAddress = "https://api.typeform.com/v0/form/%s?key=%s" % formKey, self.API_KEY
        formJson = requests.get(apiAddress).json()
        return form(formJson)
