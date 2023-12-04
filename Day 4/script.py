import re

file_path = "./input_file.txt"
total = 0

def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip()
    id, winning_numbers, selected_numbers = re.split(r'[:,|]', line)
    winning_numbers = [num.strip() for num in re.split(r'\s+', winning_numbers)]
    selected_numbers = [num.strip() for num in re.split(r'\s+', selected_numbers)]
    for c in winning_numbers:
        if c == "":
            winning_numbers.remove(c)
    for c in selected_numbers:
        if c == "":
            selected_numbers.remove(c)
    
    return {"id": id, "winning_numbers":winning_numbers, "selected_numbers":selected_numbers}

with open(file_path) as input_file:
    lottery_data = [parse_line(line) for line in input_file]

def calculate_winnings(winning_numbers, selected_numbers):
    winnings = 0
    score = 0
    for number in winning_numbers:
        if number in selected_numbers:
            winnings += 1
    for i in range(winnings):
        if i == 0:
            score = 1
        elif i == 1:
            score = 2
        else:
            score = score * 2

    return score

for ticket in lottery_data:
    total = total + calculate_winnings(ticket['winning_numbers'], ticket['selected_numbers'])

print(total)

