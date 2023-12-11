import re

file_path = './day 10/test_input_file.txt'
path = []
#index 0 is the row location, index 1 is the column location, index 3 is the current location type - see comment below
current_location = [0,0,""]
#previous_location = [0,0,""]
distance_traveled = 0
valid_connections = {"L":['7','F','-','|','north', 'east'],
                     "J":['7','F','-','|', 'north', 'west'],
                     "7":['L','J','-','|', 'west', 'south'],
                     "F":['L','J','-','|', 'east', 'south'],
                     "|":['L','J','7','F','|', 'north', 'south'],
                     "-":['L','J','7','F','-', 'east', 'west'],
                     "S":['L','J','7','F','-','|', 'north', 'south', 'east', 'west'],
                     ".":[],
                     "P":[]}
visited = set()
not_enclosed = set()
starting_location = [0,0,""]
traveled_locations_dictionary = {"location":[],
                      "connections": []}
traveled_locations = []
counter = 0
exit_paths = []

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

#previous_location = current_location

def next_tile(current_location, counter):
    rows, cols = len(path), len(path[0])
    temp_location = []
    #check east conditional
    if current_location[1] + 1 < cols:
        temp_location = [current_location[0], current_location[1] + 1]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("west" in proposed_destination_dictionary and "east" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            traveled_locations.append({'id':counter,'location' : temp_location, 'connections': ["west"]})
            return temp_location 
    #check west conditional
    if current_location[1] - 1 >= 0:
        temp_location = [current_location[0], current_location[1] - 1]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("east" in proposed_destination_dictionary and "west" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            traveled_locations.append({'id':counter,'location' : temp_location, 'connections': ["east"]})
            return temp_location
    #check north conditional    
    if current_location[0] - 1 >= 0:
        temp_location = [current_location[0] - 1, current_location[1]]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("south" in proposed_destination_dictionary and "north" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            traveled_locations.append({'id':counter,'location' : temp_location, 'connections': ["south"]})
            return temp_location 
    #check south conditional
    if current_location[0] + 1 < rows:
        temp_location = [current_location[0] + 1, current_location[1]]
        current_location_dictionary = valid_connections[current_location[2]]
        proposed_destination_dictionary = valid_connections[path[temp_location[0]][temp_location[1]]]
        if("north" in proposed_destination_dictionary and "south" in current_location_dictionary and (temp_location[0],temp_location[1]) not in visited):
            temp_location.append(path[temp_location[0]][temp_location[1]])
            traveled_locations.append({'id':counter,'location' : temp_location, 'connections': ["north"]})
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
s_location = current_location
traveled_locations.append({'id':counter,'location' : current_location, 'connections': []})
counter += 1
current_location = next_tile(current_location, counter)
counter += 1
distance_traveled += 1



while current_location[2] != "S":
    #print("2", current_location)
    current_location = next_tile(current_location, counter)
    counter += 1
    #print("current location: ", current_location)
    distance_traveled += 1
    if current_location == None:
        break
    
    #print(current_location)
    #print(traveled_locations, visited)
    # Check if the next location has been visited before
    if (current_location[0], current_location[1]) in visited:
        print("Stuck in a loop!")
        break
    visited.add((current_location[0],current_location[1]))

def find_dict_by_id(array, target_id):
    for item in array:
        if item["id"] == target_id:
            return item
    return None  # Return None if not found

def find_dict_by_location(array, location):
    for item in array:
        if item["location"][0] == location[0] and item["location"][1] == location[1]:
            return item
    return None # Return None if not found

def find_exit_path_by_location(array, location):
    for item in array:
        if item["tile"][0] == location[0] and item["tile"][1] == location[1]:
            return item
    return None # Return None if not found

for t in traveled_locations:
    if t['id'] + 1 < len(traveled_locations) and t['location'][2] != 'S':
        s = find_dict_by_id(traveled_locations, t['id']+1)
        if "east" in s['connections']:
            t['connections'].append("west")
        elif "west" in s['connections']:
            t['connections'].append("east")
        elif "north" in s['connections']:
            t['connections'].append("south")
        else:
            t['connections'].append("north")
    elif t['id'] == len(traveled_locations) - 1:
        if t['location'][2] == '|':
            if t['connections'][0] == 'south':
                t['connections'].append('north')
            else:
                t['connections'].append('south')
        elif t['location'][2] == '-':
            if t['connections'][0] == 'east':
                t['connections'].append('west')
            else:
                t['connections'].append('east')
        elif t['location'][2] == 'L':
            if t['connections'][0] == 'east':
                t['connections'].append('north')
            else:
                t['connections'].append('east')
        elif t['location'][2] == 'J':
            if t['connections'][0] == 'west':
                t['connections'].append('north')
            else:
                t['connections'].append('west')   
        elif t['location'][2] == '7':
            if t['connections'][0] == 'west':
                t['connections'].append('south')
            else:
                t['connections'].append('west')
        elif t['location'][2] == 'F':
            if t['connections'][0] == 'east':
                t['connections'].append('south')
            else:
                t['connections'].append('east')     
for t in traveled_locations:
    if t['location'][2] == 'S':
        s = find_dict_by_id(traveled_locations, len(traveled_locations) - 1)
        if s['connections'][1] == "east":
            t['connections'].append("west")
        elif s['connections'][1] == "west":
            t['connections'].append("east")
        elif s['connections'][1] == "north":
            t['connections'].append("south")
        elif s['connections'][1] == "south":
            t['connections'].append("north")
        s = find_dict_by_id(traveled_locations, t['id']+1)
        if s['connections'][0] == "east":
            t['connections'].append("west")
        elif s['connections'][0] == "west":
            t['connections'].append("east")
        elif s['connections'][0] == "north":
            t['connections'].append("south")
        elif s['connections'][0] == "south":
            t['connections'].append("north")
    #print(t)   

def tile_checker(tile, starting_tile):
    #print(tile, starting_tile)
    north_tile = [tile[0], tile[1]-1]
    west_tile = [tile[0]-1, tile[1]]
    east_tile = [tile[0]+1, tile[1]]
    south_tile = [tile[0], tile[1]+1]
    #print(north_tile, west_tile, east_tile, south_tile)
    if  (north_tile[0],north_tile[1]) in not_enclosed or (west_tile[0],west_tile[1]) in not_enclosed or (east_tile[0],east_tile[1]) in not_enclosed or (south_tile[0],south_tile[1]) in not_enclosed:
        not_enclosed.add((tile[0], tile[1]))
        return
    def made_it_to_exit(tile):
        if tile[0] >= 140 or tile[0] < 0 or tile[1] >= 140 or tile[0] < 0:
            return True
        return False
    if made_it_to_exit(north_tile):
        not_enclosed.add((tile[0], tile[1]))
        return
    if made_it_to_exit(west_tile):
        not_enclosed.add((tile[0], tile[1]))
        return
    if made_it_to_exit(east_tile):
        not_enclosed.add((tile[0], tile[1]))
        return
    if made_it_to_exit(south_tile):
        not_enclosed.add((tile[0], tile[1]))
        return
    def valid_direction(tile, direction):
        tile_in_list = find_dict_by_location(traveled_locations, tile)
        
        v_tiles = find_exit_path_by_location(exit_paths, (starting_tile[0],starting_tile[1]))
        #print(tile_in_list)
        if tile_in_list != None:
            movement = tile_in_list['connections']
            if direction == "north" and (movement == ['north', 'south'] or movement == ['south', 'north'] or movement == ['south', 'west'] or movement == ['west', 'south']):
                v_tiles['valid_tiles'].append(tile)
                return
            if direction == "south" and (movement == ['north', 'south'] or movement == ['south', 'north'] or movement == ['north', 'east'] or movement == ['east', 'north']):
                v_tiles['valid_tiles'].append(tile)
                #print("should make it here")
                return
            if direction == "east" and (movement == ['east', 'west'] or movement == ['west', 'east'] or movement == ['south', 'west'] or movement == ['west', 'south']):
                v_tiles['valid_tiles'].append(tile)
                return
            if direction == "west" and (movement == ['east', 'west'] or movement == ['west', 'east'] or movement == ['north', 'west'] or movement == ['west', 'north']):
                v_tiles['valid_tiles'].append(tile)
                return
    
    valid_direction(north_tile, "north")
    valid_direction(west_tile, "west")
    valid_direction(south_tile, "south")
    valid_direction(east_tile, "east")

            
    
    
    




total_tiles_left = (((len(path) + 1) * (len(path[0])) + 1)) - (len(traveled_locations) - 1)
starting_tile = [0,0]

while total_tiles_left > 0:
    if (starting_tile[0],starting_tile[1]) not in visited and (starting_tile[0],starting_tile[1]) not in not_enclosed:
        exit_paths.append({'tile': starting_tile, 'valid_tiles':[]})
        tile_checker(starting_tile, starting_tile)
        current_tile = find_exit_path_by_location(exit_paths, (starting_tile[0],starting_tile[1]))
        while len(current_tile['valid_tiles']) > 0:
            for tile in list(current_tile['valid_tiles']):
                tile_checker(tile, starting_tile)
                current_tile['valid_tiles'].remove(tile)
    else:
        if starting_tile[0] < len(path[0]):
            starting_tile[0] += 1
        elif starting_tile[1] < len(path):
            starting_tile[1] += 1
            starting_tile[0] = 0
        total_tiles_left -= 1
print(not_enclosed)
print("not enclosed: ",len(not_enclosed))
print("number of pipes: ", len(traveled_locations))
#for t in traveled_locations:
#    print(t)
#for v in visited:
#    print(v)
print(len(visited))
print(len(traveled_locations)- len(not_enclosed))
print(((len(path) + 1) * (len(path[0])) + 1))