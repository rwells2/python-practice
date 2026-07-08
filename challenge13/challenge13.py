"""
Challenge 13

Given the following:

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

Save that data into

people.json

Then load it back and print it.
"""

import json

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
    person1 = people[0]
    person2 = people[1]

    with open("challenge13/people.json", "w") as file:
        file.write(f'{{"people": [{json.dumps(person1)}, {json.dumps(person2)}]}}')

    with open("challenge13/people.json", "r") as this_file:
        data = json.load(this_file)
        for person in data["people"]:
            print(person["name"], "is", person["age"])


if __name__ == "__main__":
    main()