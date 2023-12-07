import re

file_path = "./input_file.txt"

def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip()
    #input = ' '.join(line.split()).replace(" ", "").split(":")
    print(line)

with open(file_path) as input_file:
    [parse_line(line) for line in input_file]

