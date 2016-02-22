import unittest, requests
from typeform import form

class testForm(unittest.TestCase):

    def setUp(self):
        with open('exampleJson.txt') as f:
            exampleJson = f.read()
        self.testForm = form.form(exampleJson)

    def test_get_questions(self):
        questions = self.testFrom.getQuestions()
        self.assertEqual(questions["list_17638595_choice"],
                        "Please select the coordinators for your class:")
