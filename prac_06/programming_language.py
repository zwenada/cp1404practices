# vehicle.py module content
class Vehicle:
    """Represent a vehicle object."""

    def __init__(self, fuel=0, name='Vehicle'):
        """Initialise a Vehicle instance with a name and initial fuel quantity."""
        self.fuel = fuel
        self.name = name
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the vehicle's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the vehicle a given distance."""
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self.odometer += distance_driven
        return distance_driven

    def __str__(self):
        """Return a string representation of a Vehicle."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"


def main():
    """Demo test code to show how to use Vehicle class.
    Create a new Vehicle object called "limo" with 100 units of fuel.
    Add 20 more units of fuel to this new vehicle object using the add_fuel method.
    """
    limo = Vehicle(100, 'Limo')

    limo.add_fuel(20)
    print(f"The limo has {limo.fuel} units of fuel.")
    distance_driven = limo.drive(115)
    print(f"The limo drove {distance_driven}km.")
    print(limo)

    # Other vehicle interactions
    my_vehicle = Vehicle(180, 'My Vehicle')
    my_vehicle.drive(30)
    print(f"Vehicle has fuel: {my_vehicle.fuel}")
    print(my_vehicle)


if __name__ == "__main__":
    main()
