for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 9):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Enter your number of stars : "))
for i in range(0, stars, 1):
    print("*", end='')
print()

stars = int(input("Enter your number of stars : "))
for i in range(1, stars+1):
    print("*" * i)
print()


