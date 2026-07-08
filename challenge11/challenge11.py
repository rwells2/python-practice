"""
Challenge 11: Read the Journal

Read

journal.txt

Print every journal entry.
"""

def main():
    with open("challenge10/journal.txt", "r") as this_file:
        print(this_file.read())


if __name__ == "__main__":
    main()