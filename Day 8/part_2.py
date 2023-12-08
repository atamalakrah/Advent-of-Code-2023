import re
import math

file_path = "./Day 8/input_file.txt"
directions = ""
path = []
destination = []
break_loop = False
final_steps = []

def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip()
    path.append(line)

with open(file_path) as input_file:
    [parse_line(line) for line in input_file]

directions = path.pop(0)
path = [item.replace('(', '').replace(')', '').replace('=', '').replace(',', '').split() for item in path]
path.pop(0)

for e in path:
    if e[0][2] == "A":
        destination.append(path.index(e))

def steps_to_first_z(start_node, nodes, directions):
    destination = start_node
    destination_found = False
    distance_traveled = 0
    while destination_found == False:
        for c in directions:
            if c == "L":
                d = 1
            elif c == "R":
                d = 2
            for e in nodes:
                if path[destination][d] == e[0]:
                    destination = path.index(e)
                    break
            distance_traveled += 1
            if path[destination][0][2] ==  "Z":
                destination_found = True
    return distance_traveled

for i in range(len(destination)):
    final_steps.append(steps_to_first_z(destination[i], path, directions))


print(math.lcm(*final_steps))