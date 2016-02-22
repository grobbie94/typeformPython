from datetime import datetime
class form:
    def __init__(self, json):
        self.json = json

    def getQuestions(self):
        questionDict = {}
        questions = self.json['questions']
        for question in questions:
            questionDict[question['id']] = question['question']
        return questionDict

    def getAllCompletedAnswers(self):
        return self.getCompletedAnswersBefore(datetime.now())

    #untilTime must be a dateTime Object

    def getCompletedAnswersBefore(self, untilTime):
        answerDict = {}
        responses = self.json['responses']
        for response in responses:
            responseTime = datetime.strptime(response['metadata']['date_submit'], "%Y-%m-%d %H:%M:%S")
            if response['completed'] == "1" and responseTime < untilTime:
                answerDict[response['token']] = response['answers']
        return answerDict

    def getAverageRating(self, questionNumber):
        pass
