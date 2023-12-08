import re
from collections import Counter
import operator
#borrowed
file_path = "./day 7/input_file.txt"
card_list = []
five_of_a_kind = []
four_of_a_kind = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []
full_house = []
total = 0

def parse_line(line):
    cards = {}
    line = re.sub(r'\n', '', line).lstrip().split()
    cards["hand"] = line[0]
    cards["bid_amount"] = line[1]
    cards["hand_name"] = ""
    card_list.append(cards)

with open(file_path) as input_file:
    [parse_line(line) for line in input_file]


def type_calculator(hand):
    for h in hand:
        value_counts = Counter(h["hand"])
        unique_counts = set(value_counts.values())

        if 5 in unique_counts:
            h["hand_name"] = "five_of_a_kind"
        elif 4 in unique_counts:
            h["hand_name"] = "four_of_a_kind"
        elif 3 in unique_counts and 2 in unique_counts:
            h["hand_name"] = "full_house"
        elif 3 in unique_counts:
            h["hand_name"] = "three_of_a_kind"
        elif 2 in unique_counts:
            h["hand_name"] = "two_pair"
        elif 1 in unique_counts:
            h["hand_name"] = "one_pair"
        else:
            h["hand_name"] = "high_card"

type_calculator(card_list)


def hand_to_number (hand):
    for h in hand:
        split_hand = list(h["hand"])
        for i in range(len(split_hand)):
            value = split_hand[i]
            if value == 'A':
                split_hand[i] = 14
            elif value == 'K':
                split_hand[i] = 13
            elif value == 'Q':
                split_hand[i] = 12
            elif value == 'J':
                split_hand[i] = 11
            elif value == 'T':
                split_hand[i] = 10
            else:
                split_hand[i] = int(value)
        h["hand_number_value"] = split_hand

hand_to_number(card_list)

def split_card_list_by_hand(card_list):
    for card in card_list:
        if card["hand_name"] == "five_of_a_kind":
            five_of_a_kind.append(card)
        elif card["hand_name"] == "four_of_a_kind":
            four_of_a_kind.append(card)
        elif card["hand_name"] == "three_of_a_kind":
            three_of_a_kind.append(card)
        elif card["hand_name"] == "two_pair":
            two_pair.append(card)
        elif card["hand_name"] == "one_pair":
            one_pair.append(card)
        elif card["hand_name"] == "full_house":
            full_house.append(card)
        else:
            high_card.append(card)
    

split_card_list_by_hand(card_list)

def sort_lists(c):
    temp_list = []

    def compare_hands(hand1, hand2):
        for i in range(len(hand1)):
            if hand1[i] > hand2[i]:
                return 1
            elif hand1[i] < hand2[i]:
                return -1
        return 0

    c.sort(key=lambda x: x["hand_number_value"], reverse=True)

    while c:
        best_hand = c[0]
        temp_list.append(c.pop(0))

        i = 0
        while i < len(c):
            comparison_result = compare_hands(best_hand["hand_number_value"], c[i]["hand_number_value"])
            if comparison_result == 0:
                temp_list.append(c.pop(i))
            elif comparison_result == -1:
                best_hand = c.pop(i)
                i = 0  # Start over after finding a better hand
            else:
                i += 1  # Move to the next hand if it's worse
    return temp_list


# Ordering Lists:
five_of_a_kind = sort_lists(five_of_a_kind)
four_of_a_kind = sort_lists(four_of_a_kind)
full_house = sort_lists(full_house)
three_of_a_kind = sort_lists(three_of_a_kind)
two_pair = sort_lists(two_pair)
one_pair = sort_lists(one_pair)
high_card = sort_lists(high_card)

card_list = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pair + one_pair + high_card
counter = len(card_list)
for value in card_list:
    total += int(value["bid_amount"]) * counter
    print(value["hand"], "|", value["hand_name"], " : ", counter, " * ", int(value["bid_amount"]), " = ", total)
    counter = counter - 1

print(total)

#for card in card_list:
#    print(card["hand_name"], card["hand"], card["hand_number_value"], card["bid_amount"])
