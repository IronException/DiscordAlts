import discord
import Config

import DataBase as db


def name_in_msg(name, msg):
    if not (name in msg):
        return False
    ind = msg.find(name)

    left = ind - 1 < 0 or not msg[ind - 1].isalpha()
    right = ind + len(name) >= len(msg) or not msg[ind + len(name)].isalpha()
    return left and right


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        for name in db.get_names():
            if name_in_msg(name, message.content):
                await message.channel.send(embed=db.get_embed_for(name, message.author, message.content))


# to get all the data so the bot can return something
db.load_data(Config.file_path)

client = MyClient()
client.run(Config.token)
