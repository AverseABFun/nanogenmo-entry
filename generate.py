"""the actual generation code"""

import csv
import constants

def parseItems(data):
    """parse the data in EVENTS and EXITS"""
    if not data:
        return {}
    data = data.split(",")
    ret = {}
    for item in data:
        item = item.split(":")
        ret[item[0].lower()] = item[1]
    return ret

inventory = 0
START = (3,1)
(x,y) = START
room = constants.START
map = csv.reader(open("map.csv","r", newline=''))
tmpmap = {}
for i, row in enumerate(map):
    if i==0: continue
    tmpmap[row[0]] = {"description":row[1],"events":parseItems(row[2]),"exits":parseItems(row[3])}
map = tmpmap
del tmpmap

page = constants.MAIN_HTML
eventsActive = []
def HAVE_GOT_ALL(data):
    return data

def setInventory(value):
    global inventory
    if inventory & value != value:
        inventory = inventory + value

def removeInventory(value):
    global inventory
    if inventory & value == value:
        inventory = inventory - value

def generatePageId():
    global inventory
    return f"{inventory}{x}{y}"

def generatePage(room, changes=lambda code : code):
    global page
    code = "<div class=\"page\">"
    code += room["description"]
    code = changes(code)
    for key in room["events"].keys():
        if key in eventsActive:
            code = globals()[room["events"][key]](code)
    code += "</div>\n[[CODE]]"
    page = page.replace("[[CODE]]", code)
    return page

print(generatePage(map["START"]))
