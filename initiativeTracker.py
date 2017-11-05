import collections
import diceRoller
import re

initiative = collections.namedtuple('initiative', 'name roll temp')
tracker = []

def addInit(inp):
    print (inp)
    info = re.match(r"^(\w+)\s*(.+)\s*(T*)",inp,flags=re.IGNORECASE)
    iName = info.group(1)
    iRoll = info.group(2)
    temporary = info.group(3).find("T") >= 0
    tracker.append(Initiative(iName,float(iRoll),temporary))
    writeToConsole()

def clearInit():
    for entry in tracker:
        if entry.temporary == True:
            tracker.remove(entry)

def fixOrder():
    tracker.sort(cmp=lambda x,y: cmp(y.roll, x.roll))
    writeToConsole()

def nextInit():
    tracker.append(tracker.pop(0))
    writeToConsole()

def removeInit(inp):
    tracker.pop(int(inp) - 1)

def writeToConsole():
    i = 0
    for entry in tracker:
        i+=1
        print (str(i) + ". " + str(entry.name) + " (" + str(entry.roll) + ")")

class Initiative:
    name = ""
    roll = 0
    temporary = True
    def __init__(self, name, roll, temporary):
        self.name = name
        self.roll = roll
        self.temporary = temporary