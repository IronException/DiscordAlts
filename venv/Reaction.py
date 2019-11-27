class FirstReaction:

    def react_to_message(self, msg):
        for k in keywords.keys():
            if is_in(content, k):
                return keys[k].getReaction()
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


def load_questions(json):
    for j in json.keys():
        questions[j] = Question(json[j])
    current_question = questions["0"]

    """
    1.: change, add / + (asks wether player or where attribute...), delete / remove / rem / -
    then it asks the questions... but define all that there?
    """
