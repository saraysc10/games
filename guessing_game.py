"""Guessing game"""
import random
from operator import truediv

random=random.randint(1,100)
attempts =0



while True:
    try:
        user = int(input("Type a number from 0 to 100: "))
        if isinstance(user, int):
            break
    except ValueError:
        print("Invalid value. Type a valid number!")


while True:
    attempts+=1
    try:
        if user>random:
            print("Your number is higher than the computer's number.")
            user=int(input("Type a number from 0 to 100: "))
        elif user<random:
            print("Your number is lower than the computer's number.")
            user=int(input("Type a number from 0 to 100: "))
        else:
            print(f"Congratulations! You typed the correct number! Attempts: {attempts}")
            break
    except ValueError:
        print("Invalid number. Type a valid number!")
        user = int(input("Type a number from 0 to 100: "))
