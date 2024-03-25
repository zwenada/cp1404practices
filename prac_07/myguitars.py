import csv
from guitar import Guitar

def read_guitars(filename):
    """Read guitar data from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars():
    """Display information about guitars."""
    print("My Guitars!")
    # Read guitar data from the 'guitars.csv' file
    guitars = read_guitars('guitars.csv')

    guitars.sort()

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f}{vintage_string}")


display_guitars()
