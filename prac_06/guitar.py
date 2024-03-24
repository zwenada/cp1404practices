class Instrument:
    """Represent an Instrument object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise an Instrument with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Instrument."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the instrument is in years."""
        current_year = 2022  # You might want to use datetime module to make it always current
        return current_year - self.year

    def is_vintage(self):
        """Return True if the instrument is 50 or more years old."""
        return self.get_age() >= 50
