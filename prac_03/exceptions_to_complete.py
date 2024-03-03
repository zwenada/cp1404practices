is_done = False
while not is_done:
    try:
        valid_result = int(input("Enter a valid integer: "))
        is_done = True  # This line will be reached only if the input is a valid integer, thus breaking the loop
    except ValueError:  # Catching the ValueError specifically to handle non-integer inputs
        print("Please enter a valid integer.")
print("Valid result is:", valid_result)
