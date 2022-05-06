# Question 3
# Write a program that simulates a lottery.
# The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers.
# After comparing the two sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random


def get_random_lottery():
    lottery_ticket = []
    for i in range(7):
        new_num = random.randint(1, 20)
        while str(new_num) in lottery_ticket:
            new_num = random.randint(1, 20)

        new_num = str(new_num)
        lottery_ticket.append(new_num)
    return lottery_ticket

def count_matches(numbers1, numbers2):
    matches = 0
    for num in numbers1:
        if num in numbers2:
            matches += 1
    return matches

def determine_earnings(matches):
    if matches == 3:
        return 20
    elif matches == 4:
        return 40
    elif matches == 5:
        return 100
    elif matches == 6:
        return 10000
    elif matches == 7:
        return 1000000
    else:
        return 0


my_lottery_ticket = get_random_lottery() #[1,2,3,4]
lottery_numbers = get_random_lottery() #[1,2,3,4]

matches = count_matches(my_lottery_ticket, lottery_numbers) #4
earnings = determine_earnings(matches)

print("My lottery numbers are: {}".format(", ".join(my_lottery_ticket)))
print("The lottery numbers are: {}".format(", ".join(lottery_numbers)))
print("You got {} matches".format(matches))
print("You earned ${}".format(earnings))