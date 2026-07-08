"""

Challenge 4: Grocery List

Start with an empty list.

Let the user type groceries.

Typing

done

ends the program.

Finally print

Your grocery list:

1. Apples
2. Milk
3. Eggs

Practice:

append()
loops
enumerate()

"""

grocery_list = []

item = input("Enter an item that you would like to add to the grocery list: ")
while item.lower() != "done":
    grocery_list.append(item)
    item = input("Enter an item that you would like to add to the grocery list: ")

print("Your grocery list:\n")
for index, this_item in enumerate(grocery_list):
    print(f"{index+1}. {this_item}")
