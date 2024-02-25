# Shop_calculator

raw_total = 0

item_number = int(input("Enter your item numbers : "))
while item_number < 0:
    print("Invalid number")
    item_number = int(input("Enter your item numbers : "))
for i in range(1, item_number+1):
    item_price = float(input("Enter your item price " + str(i) + ": "))
    raw_total = raw_total + item_price
if raw_total > 100:
    total_price = raw_total * 0.9
else:
    total_price = raw_total
print(f"Total price for your items is {total_price:.2f}.")