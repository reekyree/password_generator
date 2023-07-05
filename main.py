# This program generates a password
# using upper and lowercase letters.
# The user can specify the number of characters.


import random, string

password = []


def main():

    length = int(input("How long would you like the password to be? (Enter integer) "))

    while len(password) < length:
        char = random.choice(string.ascii_letters)
        password.append(char)

    for char in password:
        print(char, end='')


if __name__ == "__main__":
    main()
