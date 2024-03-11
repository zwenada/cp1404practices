persons = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

first_initials = []
for person in persons:
    first_initials.append(person[0])
print(first_initials)

first_initials = [person[0] for person in persons]
print(first_initials)

full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

a_names = [person for person in persons if person.startswith('A')]
print(a_names)

print(" ".join(sorted(persons)))

# TODO: list comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: list comprehension to create a list of integers from the above list of strings
numbers = [int(number) for number in almost_numbers]
print(numbers)

# TODO: list comprehension to create a list of only the numbers that are
numbers_greater_than_9 = [number for number in numbers if number > 9]
print(numbers_greater_than_9)

# TODO: (more advanced) use a list comprehension and the join string method
long_last_names = [name.split()[1] for name in full_names if len(name.split()[1]) > 11]
result_string = ", ".join(long_last_names)
print(result_string)
