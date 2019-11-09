import os, json


class Player:

    def __init__(self, data):
        self.all_data = json.loads(data)

    # contains allvariables

    def add_self(self):
        name_depo[self.all_data["name"]] = self


def get_files(dir):
    json_files = [pos_json for pos_json in os.listdir(dir) if pos_json.endswith('.json')]
    for i, element in enumerate(json_files):
        json_files[i] = dir + "/" + json_files[i]

    folders = [name for name in os.listdir(dir) if os.path.isdir(dir + "/" + name)]
    for f in folders:
        for d in get_files(dir + "/" + f): # because it returns a list...
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


def get_names():
    return name_depo.keys()  # works?


def get_embed_for(name, author, message):
    # somehow search the db now... test author wether he has acces,..? / actually I have to sptest this for all
    # people that do have access to that channel... test message for more specifications (attribute + embedstyle)
    out = name_depo[name].all_data
    print(out)
    return out
