cal_array = []
import regex

# Regular expression pattern to match combinations of digits from 0 to 99
number_pattern = regex.compile(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine|(?:ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen)|(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)|[2-9]nine)\b', regex.IGNORECASE)

# Mapping of word representations of numbers to actual numbers
number_mapping = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'ten': '10',
    'eleven': '11',
    'twelve': '12',
    'thirteen': '13',
    'fourteen': '14',
    'fifteen': '15',
    'sixteen': '16',
    'seventeen': '17',
    'eighteen': '18',
    'nineteen': '19',
    'twenty': '20',
    'thirty': '30',
    'forty': '40',
    'fifty': '50',
    'sixty': '60',
    'seventy': '70',
    'eighty': '80',
    'ninety': '90',
}

def replace_numbers(line):
    # Use a function to perform the replacement based on the matched word
    def replace_match(match):
        return number_mapping[match.group().lower()]  # Convert to lowercase to handle case-insensitive matching
    
    # Use sub() with the function to replace all occurrences of the number patterns
    return number_pattern.sub(replace_match, line)

with open("./input_file.txt") as cal_file:
    for line in cal_file:
        cal_array.append(line)

def parse_cal_text(a):
    total = 0  # Initialize total within the function
    for l in a:
        replace_numbers(l)
        #print(l)
        first_number = ""
        second_number = ""
        for c in l:
            if c.isdigit() and first_number == "":
                first_number = c
            elif c.isdigit() and first_number != "":
                second_number = c
        if second_number == "":
            second_number = first_number
        print(first_number + second_number)
        combined_number = first_number + second_number
        total = total + int(combined_number)  # Indentation corrected
    return total   


total = parse_cal_text(cal_array)
print(total)

