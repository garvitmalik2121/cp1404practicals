Menu = """(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit
"""
def main():
    print(Menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if Choice == "G":
            valid_score = get_valid_score()
        elif choice == "P":
            print(print_remarks(score))
        elif choice == "S":
            print(show_stars(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")












def get_valid_score():
    score = float(input("Enter Score"))
    if score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter Score"))
    return score
def print_remarks(score):
    if score < 0 or score > 100:
        return "Invalid score"

    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"
def show_stars(score):
    return "*" * score

main()
