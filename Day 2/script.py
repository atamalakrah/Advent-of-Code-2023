import regex as re

input_arr = []
game_dict = {}
red_cubes = 12
green_cubes = 13
blue_cubes = 14
split_pattern = re.compile(r'[:;]')
cube_pattern = re.compile(r'[ ]')

with open("./input_file.txt") as input_file:
    for line in input_file:
        input_arr.append(line)

for counter, game in enumerate(input_arr):
    value_array = [re.sub(r'\n', '', item).lstrip() for item in split_pattern.split(game)][1:]
    cube_array = [cube_pattern.split(item.lstrip()) for sublist in value_array for item in re.split(r'[,]', sublist)]
    game_dict[counter + 1] = cube_array


for key, value in game_dict.items():
    for draw in value:
        if draw[1] == 'red':
            print("nice this works")

