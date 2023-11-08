import csv
import constants

inventory = 0b0
START = (3,1)
(x,y) = START
room = constants.Room.START
map = csv.reader(open("map.csv","r", newline=''))
tmpmap = []
for i, row in enumerate(map):
    if i==0: continue
    tmpmap.append(row[1:])
map = tmpmap
del tmpmap
print(map)

def setInventory(value):
    global inventory
    if inventory & value != value:
        inventory = inventory + value

def removeInventory(value):
    global inventory
    if inventory & value == value:
        inventory = inventory - value

def generatePageId():
    global inventory, room
    return f"{inventory}{x}{y}"