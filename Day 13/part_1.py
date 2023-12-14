import time

file_path = "./Day 13/file.txt"
with open(file_path, 'r') as file:
    initial = [line.split() for line in file.read().splitlines()]
groups = [''.join(group) for group in '\n'.join(' '.join(line) for line in initial).split('\n\n')]
result = [group.splitlines() for group in groups]
start_time = time.time()
original_mirror_rows = []
total = 0
hor_ans = 0
ver_ans = 0
index_to_check = []

def determine_mirror_horizontal (x1: int, y1: int, x2: int, y2: int, input: list, type: str, indexes: list):
    #x1 and y1 are coordinate values indicating the row and column of the first element to check
    #x2 and y2 are coordinate values indicating the row and column of the second element to check
    #the input is the array of strings containing the table to review
    while y2 < len(input[x2]) and y1 < len(input[x1]):
        if input[x1][y1] == input[x2][y2]: # or x1 + x2 == len(input):
            if (y2 == len(input[x2]) - 1 and y1 == len(input[x1]) - 1):
                return (x1,y1,x2,y2)
            result = determine_mirror_horizontal(x1, (y1 + 1), x2, (y2 + 1), input, type, indexes)
            if result:
                return result
        if input[x1][y1] != input[x2][y2]:
            if type == "initial":
                while x1 < len(input) - 1 and x2 < len(input) - 1:
                    result = determine_mirror_horizontal(x1 + 1, 0, x2 + 1, 0, input, type, indexes)
                    if result: 
                        indexes.append(result)
                return indexes
            else:
                return ("No mirror found")
    return False

def determine_mirror_vertical (x: int, y1: int, y2: int, input: list, type):
    #x1 and y1 are coordinate values indicating the row and column of the first element to check
    #x2 and y2 are coordinate values indicating the row and column of the second element to check
    #the input is the array of strings containing the table to review
    while x < len(input):
        if input[x][y1] == input[x][y2] or y1 + y2 == len(input[x]):
            if x == len(input) - 1:
                return (x,y1,y2)
            result = determine_mirror_vertical(x + 1, y1, y2, input, type)
            if result:
                return result
        if input[x][y1] != input[x][y2]:
            if y2 < len(input[x]) - 1 and y1 < len(input[x]) - 1 and type == "initial":
                result = determine_mirror_vertical(0, y1 + 1, y2 + 1, input, type)
                if result: 
                    return result
            else:
                return ("No mirror found")
    return False

def confirm_horizontal_mirror (x1,y1,x2,y2,input,original_mirror_rows,type, indexes):
    result = determine_mirror_horizontal(x1,y1,x2,y2,list(i), type, indexes)
    while result != "No mirror found" and result != "Mirror found!":
        if isinstance(result, str):
            return "No mirror found"
        elif isinstance(result, tuple):
            x1, y1, x2, y2 = result
            while (len(i) - x2) > 0 and x1 >= 0:
                original_mirror_rows.append(tuple([x1, x2]))
                if (len(original_mirror_rows) == len(i) // 2 or (x1 - 1 == 0 or x2 + 1 == len(i))) and len(original_mirror_rows) > 1:
                    result = "Mirror found!"
                    break
                elif (x1 - 1 > 0 and x2 + 1 < len(input)):
                    x1 = x1 - 1
                    x2 = x2 + 1
                    y1 = 0
                    y2 = 0
                    result = confirm_horizontal_mirror(x1, y1, x2, y2, input, original_mirror_rows, type="recursive")
                elif len(original_mirror_rows) == 1 and (x1-1 < 0 or x2 + 1 > len(i)):
                    original_mirror_rows = []
                    x1 = x1 + 1
                    x2 = x2 + 1
                    y1 = 0
                    y2 = 0
                    result = determine_mirror_horizontal(x1,y1,x2,y2,list(i), type, indexes)
                if result == "No mirror found" or result == "Mirror found!":
                    return result
        else:
            print("unexpected result", result)
    if result == "No mirror found":
        return "No mirror found"
    else:
        return "Mirror found!"

def confirm_vertical_mirror (x,y1,y2,input,original_mirror_rows,type):
    result = determine_mirror_vertical(x,y1,y2,list(i), type)
    while result != "No mirror found" and result != "Mirror found!":
        if isinstance(result, str):
            return "No mirror found"
        elif isinstance(result, tuple):
            x, y1, y2 = result
            while (len(input[x]) - y2) > 0 and y1 >= 0:
                original_mirror_rows.append(tuple([y1, y2]))
                if (len(original_mirror_rows) == len(i) // 2 or y1 - 1 < 0 or y2 + 1 >= len(input[x])) and len(original_mirror_rows) > 1:
                    result = "Mirror found!"
                    break
                else:
                    x = 0
                    y1 = y1 - 1
                    y2 = y2 + 1
                    result = confirm_vertical_mirror(x, y1, y2, input, original_mirror_rows, type="recursive")
                if result == "No mirror found" or result == "Mirror found!":
                    return result
        else:
            print("unexpected result", result)
    if result == "No mirror found":
        return "No mirror found"
    else:
        return "Mirror found!"

#for i in result:
#    print(determine_mirror_horizontal(0,0,1,0,list(i)))

#for i in result:
#    print(determine_mirror_vertical(0,0,1,list(i)))
for i in result:
    x1, y1, x2, y2 = 0, 0, 1, 0  # resets for the next call
    original_mirror_rows = []  # reset for next call
    mirror = confirm_horizontal_mirror(x1, y1, x2, y2,list(i), original_mirror_rows, "initial", index_to_check)
    if mirror == "Mirror found!":
        hor_ans += (original_mirror_rows[0][1]) * 100
    #print(mirror, total)

for i in result:
    x, y1, y2 = 0, 0, 1
    original_mirror_rows = []
    mirror = confirm_vertical_mirror(x, y1, y2, list(i), original_mirror_rows, "initial")
    if mirror == "Mirror found!":
        ver_ans += original_mirror_rows[0][1]
    

end_time = time.time()
final_time = end_time - start_time
total = hor_ans + ver_ans
print("speed: ", round(final_time, 5))
print("total: ", total, "horizontal:", hor_ans, "vertical:", ver_ans)