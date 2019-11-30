import Helper
import DataBase as db


class FirstReaction:

    def __init__(self):
        self.keywords = {"add": TestReaction()}
        # TODO add all reactions from test in here...

    def react_to_discord_message(self, msg):


        for k in self.keywords.keys():
            if Helper.is_in(msg.content, k):
                print("go to next reaction: \"" + str(self.keywords[k]) + "\" with \"" + k + "\" and content: \"" + msg.content + "\"")
                return self.keywords[k]
        return self
        # stop here

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # TODO ignore some channels. or whitelist some

        for name in db.get_names():
            if name_in_msg(name, message.content):
                msg = await
                message.channel.send(embed=db.get_embed_for(name, message.author, message.content))
                reactions = ['🛋']
                for emoji in reactions:
                    await
                    msg.add_reaction(emoji)


class TestReaction:

    def react_to_discord_message(self, msg):
        msg.channel.send(embed=db.get_embed_for("n"))
        return self


def load_questions(json):
    for j in json.keys():
        questions[j] = Question(json[j])
    current_question = questions["0"]

    """
    1.: change, add / + (asks wether player or where attribute...), delete / remove / rem / -
    then it asks the questions... but define all that there?
    """
