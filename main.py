# This program generates a password
# using upper and lowercase letters.
# The user can specify the number of characters.


import random, string
from random import shuffle # This lets you randomize a list

password = []
nums = False

def getLength():
    # Get the password length.

    length = int(input("How long would you like the password to be? (Enter integer) "))
    return length

def addNums(nums, password):
    
    addNums = input("Do you want to add numbers to the password? (y/n) ")
    if addNums.lower() == "y":
        amount = int(input("How many numbers do you want? "))
        nums = True
    else:
        nums = False

    if nums == True:
        password.append(random.randint(0, 9))


def createPass(password, length):
    while len(password) < length:
        char = random.choice(string.ascii_letters)
        password.append(char)

    # Add code to pick and add random numbers to the list that becomes the password.


def displayPass(password):
    for char in password:
        print(char, end='')


def main():

    length = getLength()

    createPass(password, length)

    addNums(nums, password)

    displayPass(password)


if __name__ == "__main__":
    main()
