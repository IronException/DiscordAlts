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


class FirstReaction(Question):

    def react(self, data):
        super().reaction(data)

    def generate_next_question(self):
        return FirstReaction()


current_question

def react(message, viewers): # get next question somehow
    current_question.react(message, viewers)

def load_questions(json):
    current_question = Question(json["0"])
    
    
