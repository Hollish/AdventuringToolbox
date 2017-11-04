from math import floor

class Stat:
    score = 10
    def __init__ (self, aScore):
        score = aScore
    def getMod():
        return math.floor((score - 10)/2)


class StatBlock:
    STR,DEX,CON,INT,WIS,CHA
    def __init__ (self, stren, dext, con, intel, wisd, charis):
        STR = Stat(stren)
        DEX = Stat(dext)
        CON = Stat(con)
        INT = Stat(intel)
        WIS = Stat(wisd)
        CHA = Stat(charis)


class NPC:
    name = ""
    characterClass = 
    
