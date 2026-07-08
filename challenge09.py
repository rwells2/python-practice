"""
Challenge 9: Password Checker

Write

def is_valid(password):

Rules

at least 8 characters
contains a number
contains a capital letter

Return True or False.
"""

def main():
    password = input("Please enter a password. Passwords must be at least 8 characters long, contain a number, and contain an uppercase letter: ")
    while not(is_valid(password)):
        password = input("Invalid password. Passwords must be at least 8 characters long, contain a number, and contain an uppercase letter: ")
    print(f"Password has been set! Your password is {password}")


def is_valid(p_word):
    return len(p_word) >= 8 and any(char.isdigit() for char in p_word) and any(char.isupper() for char in p_word)

if __name__ == "__main__":
    main()