import unittest, requests, ast
from typeformPython import form
from datetime import datetime

class testForm(unittest.TestCase):

    def setUp(self):
        with open("./tests/json.txt") as f:
            exampleJsonRaw = f.read()
        exampleJson = ast.literal_eval(exampleJsonRaw)
        self.testForm = form(exampleJson)


    def test_get_questions(self):
        questions = self.testForm.getQuestions()
        self.assertEqual(questions["list_17638595_choice"],
                        "Please select the coordinators for your class:")

    def test_get_responses(self):
        answers = self.testForm.getAllCompletedResponses()
        exampleToken = "b06f6ae3622afa38822ceb31c3286b14"
        self.assertTrue(exampleToken in answers)
        self.assertEqual(answers[exampleToken]["list_17638595_choice"], "Rob and Anin")

    def test_get_responses_before(self):
        testDateEarly = datetime(1990,1,1)
        testDateFuture = datetime(2990,1,1)
        exampleToken = "b06f6ae3622afa38822ceb31c3286b14"
        earlyAnswers = self.testForm.getCompletedResponsesBefore(testDateEarly)
        self.assertFalse(exampleToken in earlyAnswers)
        futureAnswers = self.testForm.getCompletedResponsesBefore(testDateFuture)
        self.assertTrue(exampleToken in futureAnswers)

    def test_get_average_rating(self):
        self.assertEqual(self.testForm.getAverageRating("rating_17638596"), 5)

    def test_get_answer_by_question(self):
        answers = self.testForm.getAnswersByQuestion("textfield_17638598")
        self.assertTrue(answers[0] == "This is a test file")
