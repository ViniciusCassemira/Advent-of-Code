import re

with open('./inputs/day6.txt','r') as file:
    input = file.read().splitlines()

matriz = [[0 for _ in range(1000)] for _ in range(1000)]
brightness_matriz = [[0 for _ in range(1000)] for _ in range(1000)]

def toggle(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matriz[x][y] = 0 if matriz[x][y] == 1 else 1
            brightness_matriz[x][y] += 2

def turn_on(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matriz[x][y] = 1
            brightness_matriz[x][y] += 1

def turn_off(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matriz[x][y] = 0
            if brightness_matriz[x][y] > 0:
                brightness_matriz[x][y] -= 1

def find_coord(string):
    values = re.findall(r"\d+,\d+", string)
    return values

def sum_on():
    total = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if matriz[x][y] == 1:
                total += 1
    return total  

def sum_brightness():
    total = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            total += brightness_matriz[x][y]
    return total  

for linha in input:
    coords = find_coord(linha)
    x1, y1 = map(int, coords[0].split(','))
    x2, y2 = map(int, coords[1].split(','))
    
    if "turn on" in linha:
        turn_on(x1, y1, x2, y2)
    elif "toggle" in linha:
        toggle(x1, y1, x2, y2)
    elif "turn off" in linha:
        turn_off(x1, y1, x2, y2)
    else:
        print("error to exec command")

print("Part 1:", sum_on())
print("Part 2:", sum_brightness())