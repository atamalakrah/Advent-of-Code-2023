from itertools import product, groupby
from math import factorial
import time
from functools import lru_cache

file_path = "./Day 12/test_file_1.txt"
springs = [spring.split() for spring in open(file_path).read().splitlines()]
total_arrangements = 0

start_time = time.time()

for spring in springs:
    spring[1] = [int(i) for i in spring[1].split(',')]

#helper function to count the total number of springs in the row
def count_total_springs (spring: list): 
     return sum([i for i in spring])

#helper function to  count the springs in a row
def count_value_in_row (spring: str, value):
    return len([i for i, char in enumerate(spring) if char == value])

#takes a string representing the row and returns an array of arrays containing the location of the '?' characters
def find_question_sections(pattern:str):
    sections = []
    current_section = []

    for i, char in enumerate(pattern):
        if char == "?":
            current_section.append(i)
        elif current_section:
            sections.append(current_section)
            current_section = []
    
    if current_section:
        sections.append(current_section)
    return sections
#replaces the ? character sections with # and .
@lru_cache(maxsize=None)
def replace_question_sections(pattern: str, combinations: list, question_sections: list):
    result = list(pattern)
    for i, section in enumerate(question_sections):
        for j, pos in enumerate(section):
            result[pos] = combinations[i][j]

    return "".join(result)


#Validates the combination to ensure it fits with the order provided
@lru_cache(maxsize=None)
def is_valid_combination(combination:list, order:list):
    max_hash_count = count_total_springs(order)
    hash_count = 0
    consecutive_count = 0
    consecutive_non_count = 0
    order_count = 0
    first_hash_found = False

    for counter,char in enumerate(combination):
        if char =='#':
            hash_count += 1
            consecutive_count += 1
            consecutive_non_count = 0
            first_hash_found = True
        else:
            consecutive_count = 0
            if consecutive_non_count == 0 and first_hash_found:
                order_count += 1
            consecutive_non_count += 1

        if order_count > len(order) - 1:
            for char in combination[counter+1:]:
                if char == "#":
                    return False
            if max_hash_count > hash_count:
                return False
            return True
    
        order_condition = order[order_count]
        if consecutive_count > order_condition:
            return False
    if hash_count == max_hash_count:
        return True
    else:
        return False

def valid_pattern_count (question_sections: list, pattern):
    total_combinations = 1
    for section in question_sections:
        section_length = len(section)
        section_combinations = factorial(section_length)
        total_combinations *= section_combinations
    combinations = product(*[list(product('#.', repeat=len(section))) for section in question_sections])
    #follow_up_combinations = product(*[list(product('#.', repeat=len(section))) for section in second_question_sections])
    valid_count = 0
    for combo in combinations:
        #print(type(combo))
        current_combination = tuple(replace_question_sections(pattern, combo, question_sections))
        spring_tuple = tuple(spring[1])
        if is_valid_combination(current_combination, spring_tuple):
            #for recombo in follow_up_combinations:
            #    reoccuring_combination = tuple(replace_question_sections(second_pattern, recombo, second_question_sections))
            #    if(is_valid_combination(reoccuring_combination, spring_tuple)):
            print(current_combination)
            valid_count +=1
    
    return valid_count

for spring in springs:
    pattern = spring[0] + "?" + spring[0]
    #second_pattern =  pattern + "?"
    question_sections = find_question_sections(pattern) + find_question_sections(pattern)
    #second_question_sections = find_question_sections(second_pattern)        
    total_arrangements += valid_pattern_count(question_sections, pattern)

end_time = time.time()


print(round((end_time - start_time), 2), " seconds, ", total_arrangements)
