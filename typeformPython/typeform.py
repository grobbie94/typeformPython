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
        apiAddress = "https://api.typeform.com/v0/form/{0}?key={1}".format(formKey, self.API_KEY)
        form = requests.get(apiAddress)
        statusCode = form.status_code
        redirectAddress = "https://api.typeform.com/login/"
        if statusCode == 200 and form.url != redirectAddress:
            formJson = form.json()
            return form(formJson)
        elif statusCode == 404:
            try:
                raise NetworkError("404 Not Found - Check Form Key")
            except NetworkError, instance:
                print "NetworkError: " + instance.par

        else:
            try:
                raise NetworkError("NetworkError -  Check API_KEY")
            except NetworkError, instance:
                print "NetworkError: " + instance.par
