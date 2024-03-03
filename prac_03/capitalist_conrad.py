import random

maximum_increase = 0.175
maximum_decrease = 0.05
minimum_price = 1.0
maximum_price = 100.0
initial_price = 10.0
output_file = "stock_output.txt"

price = initial_price
number_of_days = 0

# Open the file for writing
out_file = open(output_file, 'w')

print(f"Starting price: ${price:,.2f}", file=out_file)

while minimum_price <= price <= maximum_price:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, maximum_increase)
    else:
        price_change = random.uniform(-maximum_decrease, 0)

    price *= (1 + price_change)
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

print(f"Simulation ran for {number_of_days} days.", file=out_file)
out_file.close()
