# Task 2: Compute averages of 3 grades

grades = [0,0,0]


for i in range(3):
    grades[i] = float(input("Input your grade for test " + str(i + 1) + ": "))

avg = (grades[0] + grades[1] + grades[2]) / grades.__len__()
print(f"Average: {avg:.1f}")

letterGrade = ""
if avg >= 90:
    letterGrade = "A"
elif avg >= 80:
    letterGrade = "B"
elif avg >= 80:
    letterGrade = "C"
elif avg >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print("Letter Grade: " + letterGrade)