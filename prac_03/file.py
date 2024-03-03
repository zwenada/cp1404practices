user_name_input = input("What is your name? ")
with open("name.txt", "w") as name_file:
    name_file.write(user_name_input)

with open("name.txt", "r") as name_file:
    stored_name = name_file.read().strip()
print(f"Your name is {stored_name}")

with open("numbers.txt", "r") as numbers_file:
    first_num = int(numbers_file.readline().strip())
    second_num = int(numbers_file.readline().strip())
print(f"The sum of the first two numbers is: {first_num + second_num}")

total_sum = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total_sum += int(line.strip())
print(f"The total of all numbers is: {total_sum}")
