"""
CP1404/CP5632 - Practical
experience using different ways to read files.
"""
# 1 Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.

name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2 (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close
# 3 Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59

in_file = open("numbers.txt", "r")
first_number = int(in_file.readline().strip())
second_number = int(in_file.readline().strip())
result = first_number + second_number
print(result)
in_file.close()


# 4 Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.