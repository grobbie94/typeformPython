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

    def getAverageRating(self, questionToken):
        #TODO throw exception if not a rating question
        answers = self.getAllCompletedAnswers()
        total = 0.0
        count = 0
        for response in answers:
            total += int(answers[response][questionToken])
            count += 1
        return total/count
