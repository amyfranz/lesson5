# Question 2
# I'm setting up my own market stall to sell chocolates.
# I need a basic till to check the prices of different chocolates that I sell.
# I've started the program and included the chocolates and their prices.
# Finish the program by asking the user to input an item and then output its price.

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

usersChocolate = input('What chocolate do you want?\n')

print('The prince of {} chocolate is £{}'.format(usersChocolate, chocolates[usersChocolate]))