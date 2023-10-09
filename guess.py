from random import *
from os import *

system("clear")

random_number = randint(1,100)

print("Number generated!")

while True:
    inp = int(input("Pick a number from 1 to 100 > "))

    if random_number - inp > 0:
        print("The number you guessed is smaller than the given number")
    
    if random_number - inp < 0:
        print("The number you guessed is bigger than the given number")
    
    if random_number - inp == 0:
        print(f"You guessed the right number, the given number was {random_number}!")
        break
