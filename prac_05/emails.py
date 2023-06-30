def main():
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = find_name(email)
        confirm_name = input(f" Is your name {name}? (Y/n)").lower()
        if confirm_name == "n":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def find_name(email):
    """ extract name from the email address provided"""
    parts = email.split("@")
    username = parts[0]
    name_parts = username.split(".")
    name = " ".join(name_parts).title()
    return name


main()
