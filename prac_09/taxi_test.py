from prac_09.taxi import Taxi

# 1. Create a new taxi object, my_taxi, with the name "EcoRide", starting fuel of 100 units
my_taxi = Taxi("EcoRide", 100)

# 2. Drive the taxi for 40 kilometers
my_taxi.drive(40)

# 3. Display the taxi's details and the current fare
print("Taxi Details:")
print(my_taxi)
print(f"Current Fare: ${my_taxi.get_fare():.2f}")

# 4. Reset the meter (start a new fare) and then drive the car for 100 kilometers
my_taxi.start_fare()
my_taxi.drive(100)

# 5. Display the updated details and the current fare
print("\nUpdated Taxi Details:")
print(my_taxi)
print(f"Current Fare: ${my_taxi.get_fare():.2f}")
