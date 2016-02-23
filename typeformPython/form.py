from datetime import datetime
class form:
    """
    Class representing one form and its associated responses
    Instatiated through typeform object
    """
    def __init__(self, json):
        self.json = json

    def getQuestions(self):
        """
        Returns a dictionary of the form {questionToken: Question Text}
        A question token is a unique key for the question
        """
        questionDict = {}
        questions = self.json["questions"]
        for question in questions:
            questionDict[question["id"]] = question["question"]
        return questionDict

    def getAllCompletedResponses(self):
        """
        Returns all responses in form:
        {responseToken: {questionToken: answerString....}}
        """
        return self.getCompletedResponsesBefore(datetime.now())

    def getCompletedResponsesBefore(self, untilTime):
        """
        Returns responses before untilTime in form:
        {responseToken: {questionToken: answerString....}}
        Parameters: untilTime - a datetime object
        """
        answerDict = {}
        responses = self.json["responses"]
        for response in responses:
            responseTime = datetime.strptime(response["metadata"]["date_submit"], "%Y-%m-%d %H:%M:%S")
            if response["completed"] == "1" and responseTime < untilTime:
                answerDict[response["token"]] = response["answers"]
        return answerDict

    def getAverageRating(self, questionToken):
        """
        Returns the average rating of a rating question from all responses
        Parameters: questionToken
        """
        #TODO throw exception if not a rating question
        answers = self.getAnswersByQuestion(questionToken)
        total = 0.0
        count = 0
        for response in answers:
            total += int(response)
            count += 1
        return total/count

    def getAnswersByQuestion (self, questionToken):
        """
        Returns all answers to a question as a list
        Parameters: questionToken
        """
        return self.getAnswersByQuestionBefore(questionToken, datetime.now())

    def getAnswersByQuestionBefore (self, questionToken, untilTime):
        """
        Returns answers to a question before untilTime
        """
        #Responses is a dict of form
        #{responseToken: {questionToken: answer, questionToken: answer ...}}
        answers = []
        responses = self.getCompletedResponsesBefore(untilTime)
        for response in responses:
            answers.append(responses[response][questionToken])
        return answers
