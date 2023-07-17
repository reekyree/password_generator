# This program generates a password
# using alphanumeric characters.
# The user can specify the number of characters used.


import random, string
from random import shuffle # This lets you randomize a list

password = []
nums = False

def getLength():
    # Get the password length.

    length = int(input("How many alphabetic characters would you like? (Enter a number) "))
    return length

def addNums(nums, password):
    # Add numeric characters if the user chooses 'yes.'

    # Counter provides a stopping point to make sure the
    # password stays within the specified number range.
    counter = 0
    addNums = input("Do you want to add numbers to the password? (y/n) ")
    if addNums.lower() == "y":
        amount = int(input("How many numbers do you want? "))
        nums = True
    else:
        nums = False

    if nums == True:
        while counter < amount:
            password.append(random.randint(0, 9))
            counter += 1

def addSpecial():

    counter = 0
    addSpecial = input("Enter the minimum number of special characters for the password (0 if none): ")
    if addSpecial > 0:
        special = random.choice(string.punctuation)


def createPass(password, length):
    # Create a password based on the length entered by the user.

    while len(password) < length:
        char = random.choice(string.ascii_letters)
        password.append(char)

def shufflePass(password):
    # Randomize the password.
    random.shuffle(password)


def displayPass(password):
    # Display the password in a non-list format.
    for char in password:
        print(char, end='')


def main():

    length = getLength()

    createPass(password, length)

    addNums(nums, password)

    shufflePass(password)

    displayPass(password)


if __name__ == "__main__":
    main()
    