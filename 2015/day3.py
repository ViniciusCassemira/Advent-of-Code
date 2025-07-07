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
print(f'Result part1: {numUniquePosition}')

# ----------------  PART 2  ----------------
startPosition2 = (0, 0)
positions2 = set()
currentPosition2 = startPosition2
currentPositionRobot2 = startPosition2

# Initial gift
positions2.add(startPosition2)
positions2.add(currentPositionRobot2)

def newGift(p, current):
    currentPosition = (current[0] + p[0], current[1] + p[1])
    positions2.add(currentPosition)
    return currentPosition

for i, arrow in enumerate(input):
    if arrow == ">":
        pos = (0, 1)
    elif arrow == "<":
        pos = (0, -1)
    elif arrow == "^":
        pos = (1, 0)
    elif arrow == "v":
        pos = (-1, 0)

    if i % 2 == 0:
        currentPosition2 = newGift(pos, currentPosition2)
    else:
        currentPositionRobot2 = newGift(pos, currentPositionRobot2)

print(f'Result part 2: {len(positions2)}')