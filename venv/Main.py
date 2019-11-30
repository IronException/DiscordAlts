import discord
import Config

import DataBase as db
from Reaction import FirstReaction


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        global reaction
        print('Message from {0.author}: {0.content}'.format(message))

        reaction = reaction.react_to_discord_message(message)


reaction = FirstReaction()

# to get all the data so the bot can return something
db.load_data(Config.file_path)

client = MyClient()
client.run(Config.token)
