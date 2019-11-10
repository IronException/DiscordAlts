from abc import ABC, abstractmethod


class Reaction(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def react(self, data):
        setup_next_question(self.generate_next_question())

    @abstractmethod
    def generate_next_question(self):
        return None


class Question:

    def __init__(self, json):


    def react(self, data):
        super().reaction(data)

    def generate_next_question(self):
        return FirstReaction()

questions = {}
current_question


def react(message, viewers):  # get next question somehow
    current_question.react(message, viewers)


def load_questions(json):
    for j in json.keys():
        questions[j] = Question(json[j])
    current_question = questions["0"]

