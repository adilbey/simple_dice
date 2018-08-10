import random

question = input('Would you like to roll the dice?\n')

while question != 'no':
    if question == 'yes':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        question = input('Would you like to roll the dice again?\n')
    else:
        print('Invalid response. Please respond with "yes" or "no".')
        question = input('Would you like to roll the dice?\n')

print('Thank you, have a nice day!')
