def main():
    secret_code = obtain_secret_code()
    display_asterisks(secret_code)

def display_asterisks(secret_code):
    print('*' * len(secret_code))

def obtain_secret_code():
    secret_code = input("Enter your secret code: ")
    while len(secret_code) < 8:
        print("Secret code must be at least 8 characters long.")
        secret_code = input("Enter your secret code: ")
    return secret_code

main()
