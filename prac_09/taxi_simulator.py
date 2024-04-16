from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def show_available_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i + 1} - {taxi}")


def main():
    print("Welcome to the Taxi Service!")
    taxis = [Taxi("Toyota Camry", 100), SilverServiceTaxi("Limousine", 100, 2), SilverServiceTaxi("Hummer H2", 200, 4)]
    selected_taxi = None
    total_bill = 0.0

    while True:
        print("\nWhat would you like to do?")
        print("1. Quit")
        print("2. Choose a taxi")
        print("3. Take a ride")

        choice = input("Enter your choice: ").lower()

        if choice == '1' or choice == 'quit':
            print(f"Total bill so far: ${total_bill:.2f}")
            print("Here are the available taxis:")
            show_available_taxis(taxis)
            break
        elif choice == '2' or choice == 'choose':
            print("Available Taxis:")
            show_available_taxis(taxis)
            try:
                taxi_index = int(input("Enter the taxi number you'd like to choose: ")) - 1
                selected_taxi = taxis[taxi_index]
                print(f"Current bill: ${total_bill:.2f}")
            except (ValueError, IndexError):
                print("Invalid taxi selection. Please enter a valid taxi number.")
        elif choice == '3' or choice == 'ride':
            if selected_taxi is None:
                print("You need to choose a taxi before you can take a ride.")
            else:
                try:
                    distance = float(input("How far would you like to go? (in kilometers): "))
                    cost = selected_taxi.drive(distance)
                    total_bill += cost
                    print(f"Your trip with the {selected_taxi.name} costs: ${cost:.2f}")
                    print(f"Total bill so far: ${total_bill:.2f}")
                except ValueError:
                    print("Invalid distance. Please enter a valid distance.")
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
