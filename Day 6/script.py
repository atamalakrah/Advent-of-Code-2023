import re

file_path = "./input_file.txt"
time = []
distance = []
times_beat = []
answer = 1

def parse_line(line):
    line = re.sub(r'\n', '', line).lstrip()
    input = ' '.join(line.split()).replace(" ", "").split(":")
    if input[0] == 'Time':
        time.extend([int(value) for value in input[1:]])
    if input[0] == 'Distance':
        distance.extend([int(value) for value in input[1:]])

with open(file_path) as input_file:
    [parse_line(line) for line in input_file]

# formula to calculate max distance = (time - button_held) * (time - (time - button_held))
for i, t in enumerate(time):
    beat_record = 0
    for j in range(0, t):
        max_distance = (t - j) * (t - (t - j))
        if max_distance > distance[i]:
            beat_record += 1
    times_beat.append(beat_record)

print(times_beat)

for i in times_beat:
    answer = i * answer

print(answer)