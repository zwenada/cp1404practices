def extract_name_from_email(email_address):
    # Extracting the part before '@' symbol
    name = email_address.split('@')[0]
    # Capitalizing each word and joining them with space
    name = ' '.join(name.split('.')).title()
    return name

def main():
    user_data = {}
    while True:
        email_address = input("Enter your email: ").strip()
        if email_address == "":
            break
        name = extract_name_from_email(email_address)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation == "" or confirmation == "y":
            user_data[email_address] = name
        else:
            name = input("Enter your name: ").strip().title()
            user_data[email_address] = name

    for email, name in user_data.items():
        print(f"Name: {name} | Email: {email}")

if __name__ == "__main__":
    main()
