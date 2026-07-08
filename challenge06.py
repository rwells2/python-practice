"""
Challenge 6: Student Database

Store students like

students = {
    "Alice":92,
    "Bob":84,
    "Charlie":97
}

Allow the user to type a student's name.

If it exists:

Charlie's grade is 97

Otherwise

Student not found.
"""

students = {
    "Alice":92,
    "Bob":84,
    "Charlie":97
}

name = input("Enter a student name: ")
if students.__contains__(name):
    print(f"{name}'s grade is {students.get(name)}")
else:
    print("Student not found.")
