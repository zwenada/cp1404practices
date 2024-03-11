import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
QUICK_PICK_SIZE = 6

def main():
    """Main program."""
    try:
        num_quick_picks = int(input("How many quick picks? "))
        if num_quick_picks <= 0:
            print("Please enter a positive number.")
        else:
            display_quick_picks(num_quick_picks)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def generate_quick_pick():
    """Generate quick pick."""
    return sorted(random.sample(range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1), QUICK_PICK_SIZE))

def display_quick_picks(num_picks):
    """Display the specified no. of quick picks."""
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(map(str, quick_pick)))

main()
