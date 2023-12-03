input_dict = {}
total_sum = 0

with open("./input_file.txt") as input_file:
    for line, counter in enumerate(input_file):
        input_arr = []
        input_arr.append(line)
        input_dict[counter] = input_arr

for line in input_dict: 
    print(line)

