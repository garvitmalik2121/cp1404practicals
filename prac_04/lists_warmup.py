""" cp1404 practical 4
warm-up
creator:Garvit Malik"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0]  Answer 3
# numbers[-1]  Answer 2
# numbers[3]   Answer 1
# print(numbers[:-1] ) Answer [3, 1, 4, 1, 5, 9]
# numbers[3:4]    Answer [1]
# 5 in numbers     Answer True
# 7 in numbers      Answer False
# "3" in numbers    Answer True
# numbers + [6, 5, 3]  Answer [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers[0] = "ten"  # Change the first element of numbers to "ten"
numbers[-1] = 1  # Change the last element of numbers to 1
print(numbers[2:])  # Print all the elements from numbers except the first two (slice)
print(9 in numbers)  # Print whether 9 is an element of numbers
