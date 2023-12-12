import re
#utilizing math for creating all of the pairs
import math
#utilziing itertools for creating the pair combinations
import itertools
#utilizing heapq for the A* algorithm function
import heapq

file_path = './Day 11/test_input_file.txt'
#stores the universe - woah!
universe = []
#stores the row numbers for rows with no galaxy
no_galaxy_x = []
#stores the column numbers for columns with no galaxy
no_galaxy_y = []
#stores the locations of all galaxies as an array [row, column]
galaxy_location = []
#galaxy pair storage, stores 2 galaxy arrays in an array [[row, column][row,column]]
galaxy_pair_storage = []
#total distance traveled for all pairs
total_distance_traveled = 0

#def parse_line(line):
#    line = re.sub(r'\n', '', line).lstrip()
#    universe.append(line)

#with open(file_path) as input_file:
#    [parse_line(line) for line in input_file]

universe = open(file_path).read().splitlines()

#for counter, i in enumerate(universe):
#    galaxy_found = False
#    for n in i:
#        if n == "#":
#            galaxy_found = True
#    if galaxy_found == False:
#        no_galaxy_x.append(counter)

#for r in range(len(universe)):
#    galaxy_found = False
#    for i in range(len(universe[r])):
#        if universe[i][r] == "#":
#            galaxy_found = True
#    if galaxy_found == False:
#        no_galaxy_y.append(r)

def get_vertical_expansions(universe):
    amount = 0
    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == '#':
                break
        else:
            amount += 1
 
        yield amount
 
 
def get_horizontal_expansions(universe):
    amount = 0
    for x in range(len(universe[0])):
        for y in range(len(universe)):
            if universe[y][x] == '#':
                break
        else:
            amount += 1
        yield amount


#Input is an array of rows or columns that do not contain a galaxy and will expand, orientation indicates which direction (x or y), and space is the grid that needs to be expanded
#def expand_space(input, orientation, space):
#    new_space = space.copy()
#    if orientation == "x":
##        shift = 0
#        for r in input:
#            row_template = "." * len(space[0])
#            new_space.insert(r + shift, row_template)
#            shift += 1
#    elif orientation == "y":
#        #print(input)
#        for r in range(len(space)):
#            shift = 0
#            for i in input:
#                #print(input, r, i+shift)
#                new_space[r] = new_space[r][:i + shift] + "." + new_space[r][i + shift:]
#                #print(new_space[r])
#                shift += 1
#    else:
#        print("Invalid orientation, please enter x or y")
#        return None
#    return new_space

#print(len(no_galaxy_x), len(no_galaxy_y))
#expands space based for rows/columns that do not have a galaxy
#universe = expand_space(no_galaxy_x, "x", universe)
#universe = expand_space(no_galaxy_y, "y", universe)

#finds all galaxies and stores their location
for row, r in enumerate(universe):
    for loc, i in enumerate(r):
        if i == "#":
            galaxy_location.append([row, loc])

#determing the total amount of pairs based off of the number of galaxies
pairs_needed = math.comb(len(galaxy_location), 2)

#creating the pairs needed to perform the shortest distance calculations
galaxy_pair_storage = list(itertools.combinations(galaxy_location,2))

#Defining the heuristic formula to find the Manhattan distance for use in the A* path algorithm
def heuristic(a,b):
    x1, y1 = a
    x2, y2 = b
 
    return abs(x1 - x2) + abs(y1 - y2)

#Defining the A* search algorithm
def astar(grid, start, end):
    #definding the parameters of the search
    rows, cols = len(grid), len(grid[0])
    #setting the directions, only left/right/up/down
    directions = [(0,1), (0, -1), (1,0), (-1, 0)]
    #setting the starting location and setting a priority of 0
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start,end)}
    while open_set:
        current_f, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            return path
        for dx, dy in directions:
            neighbor = current[0] + dx, current[1] + dy
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                tenative_g = g_score[current] + 1
                if neighbor not in g_score or tenative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tenative_g
                    f_score[neighbor] = tenative_g + heuristic(neighbor, end)
                    heapq.heappush((open_set), (f_score[neighbor], neighbor))
    return None

horizontal_expansions = []
vertical_expansions = []

for counter, x in enumerate(no_galaxy_x):
    horizontal_expansions.append(counter + 1)
for counter, y in enumerate(no_galaxy_y):
    vertical_expansions.append(counter + 1)


 

expansions_horizontal = tuple(expansion for expansion in get_horizontal_expansions(universe))
expansions_vertical = tuple(expansion for expansion in get_vertical_expansions(universe))

g_location_set = set()

for g in galaxy_location:
    g_location_set.add(tuple(g))

print(g_location_set)
print(expansions_horizontal, expansions_vertical)


pairs_to_calculate = len(galaxy_pair_storage) + 1
#print(galaxy_pair_storage)
def adjusted_coordinate(expansion_factor: 1, coordinate: tuple, expansions_horizontal: tuple, expansions_vertical: tuple):
    x, y = coordinate
    #print(expansions_horizontal, expansions_vertical, type(expansions_vertical))
    return x + expansions_horizontal[x] * expansion_factor, y + expansions_vertical[y] * expansion_factor

coordinates_adjusted = (
    adjusted_coordinate(
        1000000 - 1,
        coordinate,
        expansions_horizontal,
        expansions_vertical
    )
    for coordinate in g_location_set
)

distances = (heuristic(coordinate_1, coordinate_2)
        for coordinate_1, coordinate_2 in itertools.combinations(coordinates_adjusted, 2))



print(sum(distances))

 