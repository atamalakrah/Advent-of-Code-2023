import regex as re

input_arr = []
game_dict = {}
red_cubes = 12
green_cubes = 13
blue_cubes = 14
split_pattern = re.compile(r'[:;]')
cube_pattern = re.compile(r'[ ]')
total_score = 0
total_power = 0

with open("./input_file.txt") as input_file:
    for line in input_file:
        input_arr.append(line)

for counter, game in enumerate(input_arr):
    value_array = [re.sub(r'\n', '', item).lstrip() for item in split_pattern.split(game)][1:]
    cube_array = [cube_pattern.split(item.lstrip()) for sublist in value_array for item in re.split(r'[,]', sublist)]
    game_dict[counter + 1] = cube_array


for key, value in game_dict.items():
    total_condition = True
    for draw in value:
        if draw[1] == 'red':
            if int(draw[0]) > red_cubes:
                total_condition = False
                next
        elif draw[1] == 'blue':
            if int(draw[0]) > blue_cubes:
                total_condition = False
                next
        elif draw[1] == 'green':
            if int(draw[0]) > green_cubes:
                total_condition = False
                next
    if total_condition == True:
        total_score = key + total_score

for key, value in game_dict.items():
    min_red = 0
    min_blue = 0
    min_green = 0
    for draw in value:
        if draw[1] == 'red':
            if int(draw[0]) > min_red or min_red == 0:
                min_red = int(draw[0])
        if draw[1] == 'blue':
            if int(draw[0]) > min_blue or min_blue == 0:
                min_blue = int(draw[0])
        if draw[1] == 'green':
            if int(draw[0]) > min_green or min_green == 0:
                min_green = int(draw[0])
    cubed_value = min_red * min_blue * min_green
    total_power = total_power + cubed_value

print(total_score)
print(total_power)