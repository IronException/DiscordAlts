import os, json
import discord


class Player:

    def __init__(self, data):
        self.all_data = json.loads(data)

    # contains allvariables

    def add_self(self):
        # we cant ignore if its deleted lol
        print(self.all_data["name"])
        name_depo[self.all_data["name"]["value"]] = self


def get_files(dir):
    json_files = [pos_json for pos_json in os.listdir(dir) if pos_json.endswith('.json')]
    for i, element in enumerate(json_files):
        json_files[i] = dir + "/" + json_files[i]

    folders = [name for name in os.listdir(dir) if os.path.isdir(dir + "/" + name)]
    for f in folders:
        for d in get_files(dir + "/" + f):  # because it returns a list...
            json_files.append(d)

    return json_files


global name_depo
name_depo = {}


def load_data(dir):
    files = get_files(dir)
    print("load these files: ")
    print(files)

    for file in files:
        Player(open(file, "r").read()).add_self()


def get_embed_for(name, author, message):
    embed = discord.Embed(title=name, color=0x008000)

    # find out which attribute here... and give it over as a parameter to the data. also remove it from the msg... so
    # only the new data is in the message..
    # also somehow when the bot is asking questions to add the things eg it should be checked first...

    # TODO somhow do the perms with blacklist + whitelist like in

    # somehow search the db now... test author wether he has acces,..? / actually I have to sptest this for all
    # people that do have access to that channel... test message for more specifications (attribute + embedstyle)
    data = name_depo[name].all_data
    for field in data.keys():
        if not data[field]["deleted"] and data[field]["show"]:
            embed.add_field(name=field, value=data[field]["value"], inline=True)
    return embed
