# importing dependencies
import random

# Generating the jackpot number
jackpot = random.randint(1,100)

# taking input from user and storing it in variable "guess"
guess = int(input('Guess a number!'))

#setting a counterto calculate number of attempts
counter = 1

# a while loop that runs until the guessed number equals the jackpot number
while guess != jackpot:
    if guess < jackpot:
        print("Guess higher!")
    else:
        print("Guess lower")
        
    guess = int(input('Again'))
    counter = counter + 1
    
# output   
print("Congrats, you guesssed it correct!")
print('You took ',counter,'attempts!')