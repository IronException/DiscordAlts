import discord
import Config

import DataBase as db

# todo move that to helper
def is_in_msg(word, msg):
    if not (word in msg):
        return False
    ind = msg.find(word)

    left = ind - 1 < 0 or not msg[ind - 1].isalpha()
    right = ind + len(word) >= len(msg) or not msg[ind + len(word)].isalpha()
    return left and right


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        reaction.react(message)
        #stop here

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # TODO ignore some channels. or whitelist some


        for name in db.get_names():
            if name_in_msg(name, message.content):
                msg = await message.channel.send(embed=db.get_embed_for(name, message.author, message.content))
                reactions = ['🛋']
                for emoji in reactions:
                    await msg.add_reaction(emoji)
                    
reaction = 
                   
                    
                    
                  
# to get all the data so the bot can return something
db.load_data(Config.file_path)

client = MyClient()
client.run(Config.token)
