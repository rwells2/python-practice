"""
Challenge 5: Highest Score

Given

scores = [81, 93, 72, 99, 88]

Print

Highest: 99

Lowest: 72

Average: 86.6

Do it without using max() or min() first. Then try it again using the built-in functions.
"""


scores = [81, 93, 72, 99, 88]

min1 = max1 = scores[0]
sum = 0
for num in scores:
    if num < min1:
        min1 = num
    elif num > max1:
        max1 = num
    sum += num

print(f"Highest: {max1}\n\nMin: {min1}\n\nAverage: {sum/len(scores):.1f}")

print('--------------------')
scores2 = [81, 93, 72, 99, 88]

print(f"Highest: {max(scores2)}\n\nMin: {min(scores2)}\n\nAverage: {sum/len(scores2):.1f}")
