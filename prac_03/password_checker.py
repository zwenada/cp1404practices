min_length = 2
max_length = 6
special_chars_required = False
special_characters = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", min_length, "and", max_length,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if special_chars_required:
        print("\tand 1 or more special characters: ", special_characters)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)} character password is valid: {password}")

def is_valid_password(password):
    """Determine if the provided password is valid."""
    if not (min_length <= len(password) <= max_length):
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in special_characters:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if special_chars_required and count_special == 0:
        return False

    return True

main()
