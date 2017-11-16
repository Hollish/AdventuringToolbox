import random
import os
import re

regexDicePattern = re.compile(r"(\d*)d(\d+)",flags=re.IGNORECASE)

def regexRollStr(inpStr):
    resultStr = inpStr
    rolledStr = inpStr
    try:
        for rollArgs in regexDicePattern.finditer(inpStr):
            results = []
            if (rollArgs.group(1) != ""):
                for i in range(int(rollArgs.group(1))):
                    results.append(rollDie(int(rollArgs.group(2))))
            else:
                results.append(rollDie(int(rollArgs.group(2))))

            rolledStr = regexDicePattern.sub(str(results), rolledStr, 1)
            resultStr = regexDicePattern.sub(str(sum(results)), resultStr, 1)

        print (rolledStr)
        print (regexCalc(resultStr))
    except:
        print ""

def rollDie(dSize):
    random.seed(os.urandom(128))
    return random.randint(1,dSize)

def regexCalc(inpStr):
    try: #Brackets | [({\[](.+)[)}\]]
        regexBrackets = re.compile(r"[({\[](.+)[)}\]]",flags=re.IGNORECASE)
        for bracket in regexBrackets.findall(inpStr):
            inpStr = regexBrackets.sub(str(regexCalc(bracket)),inpStr)
            print (inpStr)
    except:
        print ("Bracket Calculation Failed.")

    try: #Exponents | (\d+(?:\.\d+)?)\s*\^\s*(\d+(?:\.\d+)?)
        regexExponent = re.compile(r"(\d+(?:\.\d+)?)\s*\^\s*(\d+(?:\.\d+)?)",flags=re.IGNORECASE)
        for exponent in regexExponent.findall(inpStr):
            inpStr = regexExponent.sub(str(float(exponent[0])**float(exponent[1])),inpStr)
    except:
        print ("Exponent Calculation Failed.")

    try: #Division | (\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)
        regexDivision = re.compile(r"(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)",flags=re.IGNORECASE)
        for divisor in regexDivision.findall(inpStr):
            inpStr = regexDivision.sub(str(float(divisor[0])/float(divisor[1])),inpStr)
    except:
        print ("Division Calculation Failed.")

    try: #Multiplication | (\d+(?:\.\d+)?)\s*\*\s*(\d+(?:\.\d+)?)
        regexMultiplication = re.compile(r"(\d+(?:\.\d+)?)\s*\*\s*(\d+(?:\.\d+)?)",flags=re.IGNORECASE)
        for multiplier in regexMultiplication.findall(inpStr):
            inpStr = regexMultiplication.sub(str(float(multiplier[0])*float(multiplier[1])),inpStr)
    except:
        print ("Multiplication Calculation Failed.")

    try: #Addition | (\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)
        regexMAddition = re.compile(r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)",flags=re.IGNORECASE)
        for adder in regexMAddition.findall(inpStr):
            inpStr = regexMAddition.sub(str(float(adder[0])+float(adder[1])),inpStr)
    except:
        print ("Addition Calculation Failed.")

    try: #Subtraction | (\d+(?:\.\d+)?)\s*\-\s*(\d+(?:\.\d+)?)
        regexSubtraction = re.compile(r"(\d+(?:\.\d+)?)\s*\-\s*(\d+(?:\.\d+)?)",flags=re.IGNORECASE)
        for subtractor in regexSubtraction.findall(inpStr):
            inpStr = regexSubtraction.sub(str(float(subtractor[0])-float(subtractor[1])),inpStr)
    except:
        print ("Subtraction Calculation Failed.")

    return inpStr