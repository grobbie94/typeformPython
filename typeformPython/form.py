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

    def getAllCompletedResponses(self):
        return self.getCompletedResponsesBefore(datetime.now())

    #untilTime must be a dateTime Object

    def getCompletedResponsesBefore(self, untilTime):
        answerDict = {}
        responses = self.json['responses']
        for response in responses:
            responseTime = datetime.strptime(response['metadata']['date_submit'], "%Y-%m-%d %H:%M:%S")
            if response['completed'] == "1" and responseTime < untilTime:
                answerDict[response['token']] = response['answers']
        return answerDict

    def getAverageRating(self, questionToken):
        #TODO throw exception if not a rating question
        answers = self.getAnswersByQuestion(questionToken)
        total = 0.0
        count = 0
        for response in answers:
            total += int(response)
            count += 1
        return total/count

    def getAnswersByQuestion (self, questionToken):
        #Responses is a dict of form
        #{responseToken: {questionToken: answer, questionToken: answer ...}}
        answers = []
        responses = self.getAllCompletedResponses()
        for response in responses:
            answers.append(responses[response][questionToken])
        return answers
