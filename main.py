# This program generates a password
# using upper and lowercase letters.
# The user can specify the number of characters.


import random, string

password = []


def getLength():
    
    length = int(input("How long would you like the password to be? (Enter integer) "))
    return length



def main():

    length = getLength()

    while len(password) < length:
        char = random.choice(string.ascii_letters)
        password.append(char)

    for char in password:
        print(char, end='')


if __name__ == "__main__":
    main()
