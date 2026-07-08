"""
Challenge 7: Word Counter

Ask for a sentence.

Count how many times each word appears.

Example

hello world hello python

Output

hello: 2

world: 1

python: 1

You'll use a dictionary for this.
"""


# word_counter = {}
# words = input("Enter a word string: ").split()

# word_iterator = iter(words)

# current_word = next(word_iterator) 

# while current_word is not None:
#     if word_counter.__contains__(current_word):
#         word_counter.get(current_word) += 1
#     else:
#         word_counter.update({current_word, 1})
#     current_word = next(word_iterator)

word_counter = {}
words = input("Enter a word string: ").split()

for w in words:
    # returns the value at key w... if the value does not exist, assign a new value to 0
    word_counter[w] = word_counter.get(w, 0) + 1

print(word_counter)
