import os, json


class Player:

    def __init__(self, data):
        allData = json.loads(data)

    # contains allvariables

    def add_self(self, depo):
        depo[self.name] = depo

def get_files(dir):
    json_files = [pos_json for pos_json in os.listdir(dir) if pos_json.endswith('.json')
    print(json_files)  # for me this prints ['foo.json']
    return json_files
        

def load_data(dir):
    files = get_files(dir)
    name_depo = {}
    print("loading")
    for file in files:
        Player(file).add_self()
                  
def get_names():
    return name_depo.keys() # works?
                  
def get_embed_for(name, author, message):
    # somehow search the db now...
                  # test author wether he has acces,..? / actually I have to sptest this for all people that do have access to that channel...
                  # test message for more specifications (attribute + embedstyle)
    return name_depo[name]
 
