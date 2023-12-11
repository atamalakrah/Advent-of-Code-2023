import re

file_path = './day 10/test_input_file_2.txt'
path = []
#index 0 is the row location, index 1 is the column location, index 3 is the current location type - see comment below
current_location = [0,0,""]
previous_location = [0,0,""]
distance_traveled = 0
valid_connections = {"L":['7','F','-','|','north', 'east'],
                     "J":['7','F','-','|', 'north', 'west'],
                     "7":['L','J','-','|', 'west', 'south'],
                     "F":['L','J','-','|', 'east', 'south'],
                     "|":['L','J','7','F','|', 'north', 'south'],
                     "-":['L','J','7','F','-', 'east', 'west'],
                     "S":['L','J','7','F','-','|', 'north', 'south', 'east', 'west'],
                     ".":[]}
visited = set()
starting_location = [0,0,""]
traveled_locations = {"distance_traveled":int,
                      "location":[],
                      "valid_destinations": []}

#| is a vertical pipe connecting north and south.
#- is a horizontal pipe connecting east and west.
#L is a 90-degree bend connecting north and east.
#J is a 90-degree bend connecting north and west.
#7 is a 90-degree bend connecting south and west.
#F is a 90-degree bend connecting south and east.
#. is ground; there is no pipe in this tile.
#S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip()
    path.append(line)


with open(file_path) as input_file:
    [parse_line(line) for line in input_file]

#find starting position
for i, row in enumerate(path):
    if "S" in row:
        current_location[0] = i
        current_location[1] = row.index("S")
        current_location[2] = "S"
        starting_location = current_location

previous_location = current_location

def next_tile(current_location):
    rows, cols = len(path), len(path[0])
    temp_location = []
    #check east conditional
    if current_location[1] + 1 < cols:
        temp_location = [current_location[0], current_location[1] + 1]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("west" in proposed_destination_dictionary and "east" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            return temp_location
    #check west conditional
    if current_location[1] - 1 >= 0:
        temp_location = [current_location[0], current_location[1] - 1]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("east" in proposed_destination_dictionary and "west" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            return temp_location
    #check north conditional    
    if current_location[0] - 1 >= 0:
        temp_location = [current_location[0] - 1, current_location[1]]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("south" in proposed_destination_dictionary and "north" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            return temp_location
    #check south conditional
    if current_location[0] + 1 < rows:
        temp_location = [current_location[0] + 1, current_location[1]]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("north" in proposed_destination_dictionary and "south" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            return temp_location

#def determine_next_location(current_location):
    #print(current_location)
#    nearby_tile = find_nearby_tiles(current_location)
#    if nearby_tile[2] in valid_connections[current_location[2]] and (nearby_tile[0],nearby_tile[1]) not in visited:
    #        #print("current location: ",current_location,"nearby tile: ", n)
    #        traveled_locations['distance_traveled'] = distance_traveled
    #        traveled_locations['location'] = current_location
#        return n
             
    #traveled_locations['valid_destinations'] = valid_dest

visited.add((current_location[0],current_location[1]))
current_location = next_tile(current_location)
distance_traveled += 1

while current_location[2] != "S":
    #print("2", current_location)
    current_location = next_tile(current_location)
    #print("3", current_location)
    #print("current location: ", current_location)
    distance_traveled += 1
    if current_location == None:
        break
    #print(traveled_locations, visited)
    # Check if the next location has been visited before
    if (current_location[0], current_location[1]) in visited:
        print("Stuck in a loop!")
        break
    visited.add((current_location[0],current_location[1]))
    #print(current_location)

print(len(visited))
print(visited)
