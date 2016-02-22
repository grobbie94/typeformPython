
class form:
    def __init__(self, json):
        self.json = json

    def getQuestions(self):
        questionDict = {}
        questions = self.json['questions']
        for question in questions:
            questionDict[question['id']] = question['question']
        return questionDict

    def getCompletedAnswers(self):
        pass

    def getAverageRating(self, questionNumber):
        pass
