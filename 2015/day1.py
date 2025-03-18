floor = 0
position = 0
firstDown = 0

with open('./inputs/day1.txt','r') as file:
    input = file.read().strip()

for x in input:
    position += 1
    if x == "(":
        floor += 1
    else:
        floor -= 1
    
    if floor == -1 and firstDown == 0:
        firstDown = position


print("Part 1: ",floor)
print("Part 2: ",firstDown)