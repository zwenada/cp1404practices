import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def read_programming_languages():
    """Read programming language details from a CSV file and save as objects."""
    languages = []
    with open('languages.csv', 'r') as file:
        next(file)  # Skip the header
        for line in file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[2] == "Yes"  # Variable not used in this code
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
            languages.append(language)
    return languages

def display_languages(languages):
    """Display information about programming languages."""
    for language in languages:
        print(language)

def read_csv_using_csv_module():
    """Read language file using the csv module."""
    with open('languages.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def read_csv_using_namedtuple():
    """Read language file using a named tuple."""
    with open('languages.csv', 'r', newline='') as file:
        file_field_names = next(file).strip().split(',')
        Language = namedtuple('Language', file_field_names)
        reader = csv.reader(file)
        for row in reader:
            language = Language._make(row)
            print(repr(language))

def read_csv_using_csv_and_namedtuple():
    """Read language file using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    with open("languages.csv", "r") as file:
        next(file)
        for language in map(Language._make, csv.reader(file)):
            print(language.name, 'was released in', language.year)
            print(repr(language))

def main():
    """Read file of programming language details, save as objects, and display."""
    languages = read_programming_languages()
    display_languages(languages)

# Uncomment the desired function call to execute the corresponding version
# read_csv_using_csv_module()
# read_csv_using_namedtuple()
# read_csv_using_csv_and_namedtuple()
main()
