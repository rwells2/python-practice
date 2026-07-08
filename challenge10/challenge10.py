"""
Challenge 10: Journal

Ask the user

What happened today?

Save the answer to

journal.txt

Run the program multiple times.

Each entry should be added instead of replacing the file.
"""


def main():
    todays_log = input("What happened today?\n")
    with open("challenge10/journal.txt", "a") as this_file:
        this_file.write(f"{todays_log}\n")


if __name__ == "__main__":
    main()