startPosition = (0,0)
positions = []
currentPosition = startPosition

# Iniial gift
positions.append(startPosition)

# Read arrow
with open('./inputs/day3.txt','r') as file:
    input = file.read().strip()

def newGift(p, current):
    currentPosition = (current[0] + p[0], current[1] + p[1])
    positions.append(currentPosition)
    print(f'New gift to {currentPosition[0]},{currentPosition[1]} locate house!')
    return currentPosition

# Using all arrow in file
for arrow in input:
    
    if arrow == ">":
        pos = (0,1)
    elif arrow == "<":
        pos = (0,-1)
    elif arrow == "^":
        pos = (1,0)
    elif arrow == "v":
        pos = (-1,0)

    currentPosition = newGift(pos, currentPosition)

print(positions)

uniquePosition = set(positions)
numUniquePosition = len(uniquePosition)
print(f'Result: {numUniquePosition}')