"""CP1404/CP5632 - Practical

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message"""


def main():
    user_name = get_string("Enter name: ").lower()
    display_menu()
    choice = get_string("Enter your choice: ").lower()
    while choice != "q":
        if choice == "h":
            print(f"Hello {user_name}")
        elif choice == "g":
            print(f"Goodbye {user_name}")
        else:
            print("invalid choice")
        display_menu()
        choice = get_string("Enter your choice: ").lower()
    print("Finished")


def get_string(prompt):
    return input(prompt)


def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


main()
