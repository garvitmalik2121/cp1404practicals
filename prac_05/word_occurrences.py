"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 40 minutes
Actual:  1 hour 30 minutes

"""
text = input("text: ")
words = text.split()  # Split the string into words
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
# Determine the width for aligning the output
length_longest_word = max(len(word) for word in word_to_count)
for word, count in sorted(word_to_count.items()):
    print(f"{word:{length_longest_word}} : {count}")
