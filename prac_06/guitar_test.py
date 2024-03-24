# instrument.py module content
import datetime

class Instrument:
    """Represent an instrument object."""

    def __init__(self, name, year, cost):
        """Initialize an Instrument instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the instrument."""
        current_year = datetime.date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the instrument is considered vintage, False otherwise."""
        return self.get_age() >= 50

    def __str__(self):
        """Return a string representation of the Instrument."""
        return f"{self.name}, Year={self.year}, Cost=${self.cost}"


def main():
    """Demo test code to show how to use Instrument class.
    Create instances of Instruments"""
    current_year = datetime.date.today().year

    vintage_instrument = Instrument("Gibson L-5 CES", 1922, 16035.40)
    new_instrument = Instrument("Another Instrument", 2013, 2499.95)

    print(f"{vintage_instrument.name} get_age() - Expected {current_year - 1922}. Got {vintage_instrument.get_age()}")
    print(f"{new_instrument.name} get_age() - Expected {current_year - 2013}. Got {new_instrument.get_age()}")
    print(f"{vintage_instrument.name} is_vintage() - Expected True. Got {vintage_instrument.is_vintage()}")
    print(f"{new_instrument.name} is_vintage() - Expected False. Got {new_instrument.is_vintage()}")


if __name__ == "__main__":
    main()
