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