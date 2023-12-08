import re

file_path = "./Day 8/input_file.txt"
directions = ""
path = []
distance_traveled = 0
destination_found = False
destination = 0

def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip()
    path.append(line)

with open(file_path) as input_file:
    [parse_line(line) for line in input_file]

directions = path.pop(0)
path = [item.replace('(', '').replace(')', '').replace('=', '').replace(',', '').split() for item in path]
path.pop(0)

for e in path:
    if e[0] == "AAA":
        destination = path.index(e)
       
while destination_found == False:
    for c in directions:
        if c == "L":
            d = 1
        elif c == "R":
            d = 2
        for e in path:
            if path[destination][d] == e[0]:
                destination = path.index(e)
                break
        distance_traveled += 1
        if path[destination][0] ==  "ZZZ":
            destination_found = True
 
print(distance_traveled)