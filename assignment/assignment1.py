"""
Name: Zwe Nada
Date started: 20/3/2024
GitHub URL (of this assignment): https://github.com/zwenada/cp1404practices/tree/master/assignment
Remember to NEVER make this assignment repo public
"""
MENU = """
Menu
D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit
"""
import csv

# Function to load movie data from CSV file
def load_movie_data(file_name):
    try:
        with open(file_name, "r") as file:
            movies = [line.strip().split(",") for line in file.readlines()]
        return movies
    except FileNotFoundError:
        return []

# Function to save movie data to CSV file
def save_movie_data(file_name, movies):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)

def main():
    print(f"MovieMaster 1.0 - Zwe Nada")
    file_name = "movies.csv"  # Using movies.csv file
    movie_data = load_movie_data(file_name)
    num_movies = len(movie_data)
    print(f"{num_movies} movies loaded\n")

    while True:
        print(MENU)
        choice = input("~ ").upper()

        if choice == "D":
            display_movies(movie_data)
        elif choice == "A":
            add_new_movie(movie_data)
        elif choice == "W":
            mark_as_watched(movie_data)
        elif choice == "Q":
            save_movie_data(file_name, movie_data)
            print(f"{len(movie_data)} movies saved to {file_name}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")

def display_movies(movies):
    print("{:<5} {:<5} {:<40} {:<10} {:<20} {:<10}".format("No.", "List", "Movie Title", "Year", "Category", "Status"))

    for idx, movie in enumerate(movies, 1):
        title, year, category, status = movie
        watched = " " if status == "w" else "*"
        print(f"{idx:<5} {watched:<5} {title:<40} {year:<10} {category:<20} {status}")

def add_new_movie(movies):
    title = input("Enter movie title: ").strip()
    while not title:
        print("Title cannot be blank")
        title = input("Enter movie title: ").strip()
    while True:
        try:
            year = int(input("Enter movie year: "))
            if year < 0:
                print("Year must be greater than or equal to 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    category = input("Enter movie category: ").strip()
    while not category:
        print("Category cannot be blank")
        category = input("Enter movie category: ").strip()
    movies.append([title, str(year), category, "u"])
    print(f"{title} ({category} from {year}) added to movie list")

def mark_as_watched(movies):
    unwatched_movies = [idx for idx, movie in enumerate(movies) if movie[3] == "u"]
    if not unwatched_movies:
        print("No more movies to watch!")
        return
    while True:
        try:
            idx = int(input("Enter the number of the movie to mark as watched: "))
            if idx < 1 or idx > len(movies):
                print("Invalid movie number. Please enter a number within the range.")
            elif movies[idx - 1][3] == "w":
                print(f"You have already watched {movies[idx - 1][0]}")
            else:
                movies[idx - 1][3] = "w"
                print(f"{movies[idx - 1][0]} from {movies[idx - 1][1]} marked as watched")
                break
        except ValueError:
            print("Invalid input; enter a valid number")

if __name__ == "__main__":
    main()
