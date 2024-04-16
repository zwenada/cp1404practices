from prac_09.taxi import Taxi

class SilverStarTaxi(Taxi):
    service_fee = 5.00  # Updated service fee

    def __init__(self, name, fuel, star_rating):
        """Initialize a SilverStarTaxi instance."""
        super().__init__(name, fuel)
        self.star_rating = star_rating
        self.price_per_km *= star_rating

    def __str__(self):
        """Return a string representation of the taxi."""
        return f"{super().__str__()}, plus a service fee of ${self.service_fee:.2f}"

    def get_fare(self):
        """Calculate and return the total fare, including service fee."""
        return super().get_fare() + self.service_fee
