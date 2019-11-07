import discord
import Config

from DataBase import load_data


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await load_data()

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith("!test"):
            channel = message.channel
            await channel.send("test")


client = MyClient()
client.run(Config.token)