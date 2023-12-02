cal_array = []

with open("./input_file.txt") as cal_file:
    for line in cal_file:
        cal_array.append(line)

def parse_cal_text(a):
    total = 0  # Initialize total within the function
    for l in a:
        l = update_text(l.lower())
        first_number = ""
        second_number = ""
        for c in l:
            if c.isdigit() and first_number == "":
                first_number = c
            elif c.isdigit() and first_number != "":
                second_number = c
        if second_number == "":
            second_number = first_number
        #print(first_number + second_number)
        combined_number = first_number + second_number
        total = total + int(combined_number)  # Indentation corrected
    return total   

def update_text(word):
    new_string = ""
    for c in range(len(word)):
        if word[c:c+3] == "one":
            new_string = new_string + "1"
        elif word[c:c+3] == "two":
            new_string = new_string + "2"
        elif word[c:c+5] == "three":
            new_string = new_string + "3"
        elif word[c:c+4] == "four":
            new_string = new_string + "4"
        elif word[c:c+4] == "five":
            new_string = new_string + "5"
        elif word[c:c+3] == "six":
            new_string = new_string + "6"
        elif word[c:c+5] == "seven":
            new_string = new_string + "7"
        elif word[c:c+5] == "eight":
            new_string = new_string + "8"
        elif word[c:c+4] == "nine":
            new_string = new_string + "9"           
        elif word[c].isdigit():
            new_string = new_string + word[c]
    return new_string
total = parse_cal_text(cal_array)
print(total)

