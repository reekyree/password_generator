# This program generates a password
# using alphanumeric characters.
# The user can specify the number of characters used.


import random, string
from random import shuffle # This lets you randomize a list

password = []

def getLength():
    # Get the password length.

    length = int(input("How many alphabetic characters would you like? (Enter a number) "))
    return length

def addNums(password):
    # Add numeric characters if the user chooses 'yes.'

    # Counter provides a stopping point to make sure the
    # password stays within the specified number range.
    counter = 0
    addNums = int(input("Enter the minimum number of numeric characters for the password (0 if none): "))
    if addNums > 0:
        while counter < addNums:
            password.append(random.randint(0, 9))
            counter += 1
    else:
        print("You are adding (0) numbers.")

def addSpecial(password):

    counter = 0
    addSpecial = int(input("Enter the minimum number of special characters for the password (0 if none): "))
    if addSpecial > 0:
        while counter < addSpecial:
            special = random.choice(string.punctuation)
            password.append(special)
            counter += 1
    else:
        print("You are adding (0) special characters.")


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

    addNums(password)

    addSpecial(password)

    shufflePass(password)

    displayPass(password)


if __name__ == "__main__":
    main()
    