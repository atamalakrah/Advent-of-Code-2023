import regex as re

input_dict = {}
total_sum = 0

with open("./input_file.txt") as input_file:
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
            for p in position_array:
                # Checking row above
                if counter - 1 >= 0:
                    if p - 1 >= 0 and input_dict[counter - 1][p - 1].isdigit() == False and input_dict[counter - 1][p - 1] != ".":
                        symbol_nearby = True
                    elif input_dict[counter - 1][p].isdigit() == False and input_dict[counter - 1][p] != ".":
                        symbol_nearby = True
                    elif p + 1 < len(value) and input_dict[counter - 1][p + 1].isdigit() == False and input_dict[counter - 1][p + 1] != ".":
                        symbol_nearby = True

                # Checking current row
                if p - 1 >= 0 and input_dict[counter][p - 1].isdigit() == False and input_dict[counter][p - 1] != ".":
                    symbol_nearby = True
                elif p + 1 < len(value) and input_dict[counter][p + 1].isdigit() == False and input_dict[counter][p + 1] != ".":
                    symbol_nearby = True

                # Checking row below
                if counter + 1 <= max_key:
                    if p - 1 >= 0 and input_dict[counter + 1][p - 1].isdigit() == False and input_dict[counter + 1][p - 1] != ".":
                        symbol_nearby = True
                    elif input_dict[counter + 1][p].isdigit() == False and input_dict[counter + 1][p] != ".":
                        symbol_nearby = True
                    elif p + 1 < len(value) and input_dict[counter + 1][p + 1].isdigit() == False and input_dict[counter + 1][p + 1] != ".":
                        symbol_nearby = True

            if symbol_nearby:
                digit_sequence = "".join(input_dict[counter][p] for p in position_array)
                total_sum += int(digit_sequence)

print(total_sum)
