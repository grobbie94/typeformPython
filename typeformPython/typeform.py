import requests

class typeform:
    """
    Class representing one connection to typeform
    Parameters: API_KEY - retrieved from your typeform account settings
    """

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def getForm (self, formKey):
        """
        Returns a form object which can be queried to get
        responses to typeforms
        Parameters: formKey - Check the typeform API docs for info
        """
        #TODO implement exception for no network etc.
        apiAddress = "https://api.typeform.com/v0/form/%s?key=%s" % formKey, self.API_KEY
        formJson = requests.get(apiAddress).json()
        return form(formJson)
