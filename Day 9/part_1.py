import re

file_path = "./day 9/input_file.txt"
path = []
values = []
total = 0

#Parses input file
def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip()
    path.append(line)

#Calculates the difference between values in an array and returns the new list
def find_diff(l):
    diff_arr = []
    l_len = len(l) - 1
    for value in l:
        while l_len > 0:
            diff_arr.append(int(l[l_len]) - int(l[l_len - 1]))
            l_len -= 1
    diff_arr.reverse()
    return diff_arr

#checks to see if all of the values in an array are 0, if so it returns true. Otherwise returns false.
def check_all_zero (l):
    zero_arr = []
    for value in l:
        if value == 0:
            zero_arr.append(True)
        else:
            zero_arr.append(False)
    if False in zero_arr:
        return False
    else:
        return True

with open(file_path) as input_file:
    [parse_line(line) for line in input_file]
path = [item.split() for item in path]

#Constructs dictionary for value storage
for counter, p in enumerate(path):
    value_dict = {}
    temp_arr = []
    value_dict["id"] = counter
    temp_arr.append([int(value) for value in p])
    value_dict["value_array"] = temp_arr
    values.append(value_dict)

#Calculates all of the difference values until an array returns all zeroes.
for a in values:
    counter = 0
    while check_all_zero(a["value_array"][counter]) == False:
        a["value_array"].append(find_diff(a["value_array"][counter]))
        counter += 1

#calculate the last value for the initial list of numbers
for a in values:
    diff_arr_len = len(a['value_array'])
    while diff_arr_len > 1:
        curr_arr = a['value_array'][diff_arr_len-1]
        next_arr = a['value_array'][diff_arr_len-2]
        new_value = curr_arr[len(curr_arr) - 1] + next_arr[len(next_arr) - 1]
        next_arr.append(new_value)
        diff_arr_len -= 1

for a in values:
    total += a["value_array"][0][len(a["value_array"][0])-1]

print(total)
