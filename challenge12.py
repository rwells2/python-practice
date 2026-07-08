"""
Suppose you have

people = [
    {
        "name":"John",
        "age":24
    },
    {
        "name":"Sarah",
        "age":31
    }
]
Challenge 12

Print

John is 24

Sarah is 31
"""
people = [
    {
        "name":"John",
        "age":24
    },
    {
        "name":"Sarah",
        "age":31
    }
]

def main():
    print(f"{people[0]["name"]} is {people[0]["age"]}\n")
    print(f"{people[1]["name"]} is {people[1]["age"]}")


if __name__ == "__main__":
    main()