import unittest, requests, ast
from typeformPython import form
from datetime import datetime

class testForm(unittest.TestCase):

    def setUp(self):
        with open('./tests/json.txt') as f:
            exampleJsonRaw = f.read()
        exampleJson = ast.literal_eval(exampleJsonRaw)
        self.testForm = form.form(exampleJson)


    def test_get_questions(self):
        questions = self.testForm.getQuestions()
        self.assertEqual(questions["list_17638595_choice"],
                        "Please select the coordinators for your class:")

    def test_get_answers(self):
        answers = self.testForm.getAllCompletedAnswers()
        exampleToken = 'b06f6ae3622afa38822ceb31c3286b14'
        self.assertTrue(exampleToken in answers)
        self.assertEqual(answers[exampleToken]["list_17638595_choice"], 'Rob and Anin')

    def test_get_answers_before(self):
        testDateEarly = datetime(1990,1,1)
        testDateFuture = datetime(2990,1,1)
        exampleToken = 'b06f6ae3622afa38822ceb31c3286b14'
        earlyAnswers = self.testForm.getCompletedAnswersBefore(testDateEarly)
        self.assertFalse(exampleToken in earlyAnswers)
        futureAnswers = self.testForm.getCompletedAnswersBefore(testDateFuture)
        self.assertTrue(exampleToken in futureAnswers)

    def test_get_average_rating(self):
        self.assertEqual(self.testForm.getAverageRating("rating_17638596"), 5)
