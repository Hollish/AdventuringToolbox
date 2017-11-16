import collections
import diceRoller
import re

initiative = collections.namedtuple('initiative', 'name roll hp')
tracker = []

def addInit(inp):
    try:
        info = re.match(r"^(\w+)\s*(\d+(?:\.\d+)?)\s*(T*)",inp,flags=re.IGNORECASE)
        iName = info.group(1)
        iRoll = info.group(2)
        temporary = info.group(3).find("T") >= 0
        tracker.append(Initiative(iName,float(iRoll),temporary))
    except:
        print("Invalid input \"" + inp + "\"")


def clearInit():
    for entry in tracker:
        if entry.temporary == True:
            tracker.remove(entry)

def changeInit(inp):
    try:
        info = re.match(r"^(\d+)\s+(\d+(?:\.\d+)?)",inp,flags=re.IGNORECASE)
        tracker[int(info.group(1)) - 1].roll = float(info.group(2))
    except IndexError:
        print("Entered initiative doesn't exist.")
    except:
        print("Invalid input \"" + inp + "\"")

def fixOrder():
    tracker.sort(cmp=lambda x,y: cmp(y.roll, x.roll))

def nextInit():
    tracker.append(tracker.pop(0))

def removeInit(inp):
    try:
        tracker.pop(int(inp) - 1)
    except IndexError:
        print("Entered initiative doesn't exist.")
    except:
        print("Invalid input \"" + inp + "\"")
    

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