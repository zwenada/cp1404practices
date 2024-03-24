class Vehicle:
    """Represent a Vehicle object."""

    def __init__(self, fuel=0, name='Vehicle'):
        """Initialize a Vehicle instance.

        Parameters:
        - fuel (float): One unit of fuel drives one kilometre.
        - name (str): The name of the vehicle.
        """
        self.fuel = fuel
        self.name = name
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the vehicle's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the vehicle a given distance.

        Drive given distance if the vehicle has enough fuel
        or drive until fuel runs out and return the distance actually driven.
        """
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
    """Create a new Vehicle object called "limo" with 100 units of fuel.
    Add 20 more units of fuel to this new vehicle object using the add_fuel method.
    Attempt to drive the vehicle 115 km using the drive method."""
    limo = Vehicle(100, "Limousine")

    limo.add_fuel(20)
    print(f"The {limo.name} has {limo.fuel} units of fuel.")

    distance_driven = limo.drive(115)
    print(f"The {limo.name} drove {distance_driven} km.")

    print(limo)


if __name__ == "__main__":
    main()



