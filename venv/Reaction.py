
class Question:

    def __init__(self, json):
        self.question = json["question"]
        self.next_question = json["nextQuestion"]


    def react(self, message):
        # save message? somehow
        return questions[self.nextquestion]

questions = {}
current_question


def react(message, viewers):
    # bot gets answer from viewer and returns next step. questions or anything have to be asked in there
    current_question = current_question.react(message, viewers)


def load_questions(json):
    for j in json.keys():
        questions[j] = Question(json[j])
    current_question = questions["0"]

    """
    1.: change, add / + (asks wether player or where attribute...), delete / remove / rem / -
    then it asks the questions... but define all that there?
    """

