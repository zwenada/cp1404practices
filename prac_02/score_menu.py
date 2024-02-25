def obtain_valid_mark():
    """Prompt the user for a valid mark between 0 and 100 inclusive."""
    mark = float(input("Enter a mark between 0 and 100: "))
    while mark < 0 or mark > 100:
        print("Invalid mark. The mark must be between 0 and 100.")
        mark = float(input("Enter a mark between 0 and 100: "))
    return mark


def evaluate_mark(mark):
    """Evaluate the mark and return the result."""
    if mark < 0 or mark > 100:
        return "Invalid mark"
    elif mark >= 90:
        return "Excellent"
    elif mark >= 50:
        return "Passable"
    else:
        return "Bad"


def display_result(mark):
    """Print the result based on the mark."""
    result = evaluate_mark(mark)
    print(f"Result: {result}")


def display_stars(mark):
    """Print stars equal to the mark."""
    print("*" * int(mark))


def main():
    mark = -1  # Initialize mark with an invalid value to enter the loop
    menu = """(G)et a valid mark
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            mark = obtain_valid_mark()
        elif choice == "P":
            if 0 <= mark <= 100:
                display_result(mark)
            else:
                print("Please get a valid mark first.")
        elif choice == "S":
            if 0 <= mark <= 100:
                display_stars(mark)
            else:
                print("Please get a valid mark first.")
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").upper()

    print("Farewell!")


if __name__ == "__main__":
    main()
