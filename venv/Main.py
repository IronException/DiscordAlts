import discord
import Config

import DataBase as db


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # to get all the data so the bot can return something
        await db.load_data(Config.filepath)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        for name in db.get_names():
            if message.content.contains(name):
                await message.channel.send(db.get_embed_for(name, message.author, message.content))


client = MyClient()
client.run(Config.token)
