import regex as re

input_dict = {}
total_sum = 0
numbers_nearby = []

with open("./Day 3/test_input_file.txt") as input_file:
    for counter, line in enumerate(input_file):
        input_arr = re.sub(r'\n', '', line).lstrip()
        input_dict[counter] = input_arr

for counter, value in input_dict.items():
    for c in range(len(value)):
        position_array = []
        if value[c].isdigit() and (c == 0 or not value[c-1].isdigit()):
            position_array.append(c)
            for j in range(c + 1, len(value)):
                if value[j].isdigit():
                    position_array.append(j)
                else:
                    break
            max_key = max(input_dict)
            symbol_nearby = False
            for c in position_array:
                # Checking row above
                if counter - 1 >= 0:
                    if c - 1 >= 0 and input_dict[counter - 1][c - 1].isdigit() == False and input_dict[counter - 1][c - 1] != ".":
                        symbol_nearby = True
                    elif input_dict[counter - 1][c].isdigit() == False and input_dict[counter - 1][c] != ".":
                        symbol_nearby = True
                    elif c + 1 < len(value) and input_dict[counter - 1][c + 1].isdigit() == False and input_dict[counter - 1][c + 1] != ".":
                        symbol_nearby = True

                # Checking current row
                if c - 1 >= 0 and input_dict[counter][c - 1].isdigit() == False and input_dict[counter][c - 1] != ".":
                    symbol_nearby = True
                elif c + 1 < len(value) and input_dict[counter][c + 1].isdigit() == False and input_dict[counter][c + 1] != ".":
                    symbol_nearby = True

                # Checking row below
                if counter + 1 <= max_key:
                    if c - 1 >= 0 and input_dict[counter + 1][c - 1].isdigit() == False and input_dict[counter + 1][c - 1] != ".":
                        symbol_nearby = True
                    elif input_dict[counter + 1][c].isdigit() == False and input_dict[counter + 1][c] != ".":
                        symbol_nearby = True
                    elif c + 1 < len(value) and input_dict[counter + 1][c + 1].isdigit() == False and input_dict[counter + 1][c + 1] != ".":
                        symbol_nearby = True

            if symbol_nearby:
                digit_sequence = "".join(input_dict[counter][c] for c in position_array)
                total_sum += int(digit_sequence)

print(total_sum)

for counter, value in input_dict.items():
    for c in range(len(value)):
        if value[c] == "*":
            neighbor_value = 0
            max_key = max(input_dict)
            # Checking row above
            if counter - 1 >= 0:
                if c - 1 >= 0 and input_dict[counter - 1][c - 1].isdigit() == True:
                    neighbor_value += 1
                if input_dict[counter - 1][c].isdigit() == True:
                    neighbor_value += 1
                if c + 1 < len(value) and input_dict[counter - 1][c + 1].isdigit() == True:
                    neighbor_value += 1

            # Checking current row
            if c - 1 >= 0 and input_dict[counter][c - 1].isdigit() == True:
                neighbor_value += 1
            if c + 1 < len(value) and input_dict[counter][c + 1].isdigit() == True:
                neighbor_value += 1

            # Checking row below
            if counter + 1 <= max_key:
                if c - 1 >= 0 and input_dict[counter + 1][c - 1].isdigit() == True:
                    neighbor_value += 1
                if input_dict[counter + 1][c].isdigit() == True:
                    neighbor_value += 1
                if c + 1 < len(value) and input_dict[counter + 1][c + 1].isdigit() == True:
                    neighbor_value += 1
            if neighbor_value >= 2:
                numbers_nearby.append([counter, c])
digit_array = []
#print(numbers_nearby)
for num in numbers_nearby:
    if num[0] - 1 >= 0 and num[0] + 1 <= max_key:
        if num[1] - 1 >= 0 and input_dict[num[0] - 1][num[1] - 1].isdigit() == True:
            digit_array.append([num[0] - 1, num[1] - 1, num[0], num[1]])
        if input_dict[num[0] - 1][num[1]].isdigit() == True:
            digit_array.append([num[0] - 1, num[1], num[0], num[1]])
        if num[1] + 1 < len(value) and input_dict[num[0] - 1][num[1] + 1].isdigit() == True:
            digit_array.append([num[0] - 1,num[1] + 1, num[0], num[1]])
    # Checking current row
        if num[1] - 1 >= 0 and input_dict[num[0]][num[1] - 1].isdigit() == True:
            digit_array.append([num[0],num[1] - 1, num[0], num[1]])
        if num[1] + 1 < len(value) and input_dict[num[0]][num[1] + 1].isdigit() == True:
            digit_array.append([num[0],num[1] + 1, num[0], num[1]])
    # Checking row below
        if num[1] - 1 >= 0 and input_dict[num[0] + 1][num[1] - 1].isdigit() == True:
            digit_array.append([num[0] + 1,num[1] - 1, num[0], num[1]])
        if input_dict[num[0] + 1][num[1]].isdigit() == True:
            digit_array.append([num[0] + 1,num[1], num[0], num[1]])
        if num[1] + 1 < len(value) and input_dict[num[0] + 1][num[1] + 1].isdigit() == True:
            digit_array.append([num[0] + 1,num[1] + 1, num[0], num[1]])

grouped_data = {}
clean_digit_array = []

for cor in digit_array:
    key = (cor[2], cor[3])
    if key not in grouped_data:
        grouped_data[key] = []
    grouped_data[key].append(cor)

#duplicate_lists = [group for group in grouped_data.values() if len(group) > 1]

for key, value in grouped_data:
   # print(grouped_data[key, value])
    for i in range(len(grouped_data[key, value])):
       # print(grouped_data[key, value][i][0], grouped_data[key, value][i][1])
#        print(input_dict[grouped_data[key, value][i][0]][grouped_data[key, value][i][1]])
        if input_dict[grouped_data[key, value][i][0]][grouped_data[key, value][i][1]-1].isdigit():
            print(input_dict[grouped_data[key, value][i][0]][grouped_data[key, value][i][1]-1])
#            print(input_dict[grouped_data[(key,value)][0][i]][grouped_data[(key,value)][0][i+1]])


#print(grouped_data)
#print(input_dict)     
#print(grouped_data[(1,121)][0][0], grouped_data[(1,121)][0][1])
#print(input_dict[grouped_data[(1,121)][0][0]][grouped_data[(1,121)][0][1]])