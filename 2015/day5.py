with open('./inputs/day5.txt','r') as file:
    input = file.read().splitlines()

# ------ part 1 -------

def threeVowels(string):
    sumVowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for caractere in string:
        if caractere in vowels:
            sumVowels += 1
    if sumVowels > 2:  
        return True
    else:
        return False

def doubleLetter(string):
    oldLetter = ""
    
    for caractere in string:
        if caractere == oldLetter:
            return True
        oldLetter = caractere
    
    return False

def disallowedSubstrings(string):
    subStrings = ['ab', 'cd', 'pq', 'xy']
    
    for sub in subStrings:
        if sub in string:
            return False
        
    return True

def validateString(string):
    if threeVowels(string) and doubleLetter(string) and disallowedSubstrings(string) :
        return True
    else:
        return False

niceStrings = 0

for string in input:
    if validateString(string):
        niceStrings += 1
print(niceStrings)  

# ------ part 2 -------

# Functions

def compairArray(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i]["data"] == array[j]["data"]:
                if abs(array[i]["x"] - array[j]["x"]) >= 2:
                    return True
    return False

def betweenString(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
        
def doublePair(string):
    datas = []
    for i in range(len(string)-1):
    #agrupar por dupla e pegar as coordenadas de cada letra
        pair = string[i]+string[i+1]
        x = i
        y = i + 1

        data = {
            "data": pair,
            "x": x,
            "y": y
        }
        datas.append(data)
    return compairArray(datas)

def validateString2(string):
    return betweenString(string) and doublePair(string)

niceStrings2 = 0

for string in input:
    if validateString2(string):
        niceStrings2 += 1
print(niceStrings2)  