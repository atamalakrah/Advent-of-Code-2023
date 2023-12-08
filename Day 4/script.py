import re

file_path = "./test_input_file.txt"
total = 0
total_scratchcards = 0
scratchcards_to_process = []
card_location = 0

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

#Returns number of winning numbers
def scratchcard_winnings(winning_numbers, selected_numbers):
    winnings = 0
    for number in winning_numbers:
        if number in selected_numbers:
            winnings += 1
    return winnings

#Returns score calculation for pt1
def calculate_score(winning_numbers, selected_numbers):
    winnings = scratchcard_winnings(winning_numbers, selected_numbers)
    score = 0
    for i in range(winnings):
        if i == 0:
            score = 1
        elif i == 1:
            score = 2
        else:
            score = score * 2

    return score

#calculates total winnings for pt1
for ticket in lottery_data:
    total = total + calculate_score(ticket['winning_numbers'], ticket['selected_numbers'])

#print(total)

def continued_card_winnings(lottery_cards):
    for i in range(len(lottery_cards)):
        winnings = scratchcard_winnings(lottery_data[i]['winning_numbers'], lottery_data[i]['selected_numbers'])
        print()
        for j in range(winnings):
            current_card = card_location + 1
            print(current_card)
            #for j in range(winnings):
             #   scratchcards_to_process.append
                
            
            

continued_card_winnings(lottery_data)
