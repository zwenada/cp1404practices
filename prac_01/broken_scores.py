"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score < 50:
    print("Bad")
else:
    if score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    else:
        print("Passable")



