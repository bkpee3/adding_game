from random import *

answer = ''

number_one = randint(0, 10)
number_two = randint(0, 10)
the_answer = number_one + number_two
number_of_guesses = 0

while answer != the_answer and number_of_guesses < 3:
    print('What is ' + str(number_one) + ' + ' + str(number_two))
    answer = int(input())
    if answer != the_answer and number_of_guesses < 2:
        print('Try Again..')
        number_of_guesses += 1
    else:
        break

if answer == the_answer:
    print('Correct, You Win!')
else:
    print('You Lose, Try Again..')
