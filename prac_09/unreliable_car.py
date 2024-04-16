"""RandomCar Class"""

import random
from prac_09.car import Car

LOW_RANDOM_NUMBER = 0
HIGH_RANDOM_NUMBER = 100


class RandomCar(Car):
    """A car that randomly behaves."""

    def __init__(self, name, fuel, unpredictability):
        """Initialize a RandomCar."""
        super().__init__(name, fuel)
        self.unpredictability = unpredictability

    def drive(self, distance):
        """Drive the car, sometimes behaving unpredictably."""
        random_number = random.uniform(LOW_RANDOM_NUMBER, HIGH_RANDOM_NUMBER)

        if random_number < self.unpredictability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
