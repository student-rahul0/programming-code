# Number Guessing Game in Python

'''
    1. Take a random number and save it in a variable, for simplicity take random number between 0 to 100
'''

# a = 57 
# flag = True 
# while flag :
#     gn = int(input("Guess a number :"))
#     if (gn<a):
#         print("guessing number  greater than gn number: ")
#     elif(gn>a):
#         print("guessing number less than random number: ")
#     else:
#         print("gussing number equal to random number:")
#         flag = False

import random

computer_no = random.randrange(0,100)
flag = True
count = 0
while flag:
    count += 1
    user_input = int(input("Guessin a number ------ :"))
    if(computer_no < user_input):
        print("Your Guessing Number is High ---")
    elif(computer_no > user_input):
        print("Your Guessing Number is low --- ")
    else:
        print("Congratulations! You have successfully Your Guessing The Number",{count},"attempts")
        flag = False

