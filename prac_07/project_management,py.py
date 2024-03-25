import csv
from project_model import Project
import datetime as dt


def load_projects_from_file(filename):
    """Load projects from a CSV file."""
    projects = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            project = Project(row['Name'], row['Start Date'], row['Priority'], row['Cost Estimate'],
                              row['Completion Percentage'])
            projects.append(project)
    return projects


def save_projects_to_file(filename, projects):
    """Save projects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for project in projects:
            writer.writerow({'Name': project.name,
                             'Start Date': project.start_date.strftime('%d/%m/%Y'),
                             'Priority': project.priority,
                             'Cost Estimate': project.cost_estimate,
                             'Completion Percentage': project.completion_percentage})


def display_projects_info(projects):
    """Display information about projects."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    print("\nCompleted projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_start_date(projects, date):
    """Filter projects based on start date."""
    filtered_projects = [p for p in projects if p.start_date > date]
    print(f"Projects starting after {date.strftime('%d/%m/%Y')}:")
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Enter project name: ")
    start_date = input("Enter project start date (dd/mm/yyyy): ")
    priority = input("Enter project priority: ")
    cost_estimate = float(input("Enter project cost estimate: "))
    completion_percentage = float(input("Enter project completion percentage: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project_completion(projects):
    """Update completion percentage of a project."""
    project_name = input("Enter the name of the project to update: ")
    for project in projects:
        if project.name == project_name:
            new_completion = float(input(f"Enter new completion percentage for {project_name}: "))
            project.completion_percentage = new_completion
            print(f"Completion percentage updated for {project_name}.")
            return
    print(f"No project found with the name '{project_name}'.")


def main_menu(projects):
    """Display the main menu and handle user inputs."""
    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by start date")
        print("- (A)dd new project")
        print("- (U)pdate project completion")
        print("- (Q)uit")

        choice = input("Choose an option: ").upper()

        if choice == 'L':
            filename = input("Enter filename to load from: ")
            projects = load_projects_from_file(filename)
            print(f"Loaded projects from {filename}")
        elif choice == 'S':
            filename = input("Enter filename to save to: ")
            save_projects_to_file(filename, projects)
            print(f"Saved projects to {filename}")
        elif choice == 'D':
            display_projects_info(projects)
        elif choice == 'F':
            date_input = input("Enter date (dd/mm/yyyy) to filter projects after: ")
            date = dt.datetime.strptime(date_input, "%d/%m/%Y").date()
            filter_projects_by_start_date(projects, date)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project_completion(projects)
        elif choice == 'Q':
            if input("Save changes to projects.txt? (y/n): ").lower() == 'y':
                save_projects_to_file('projects.txt', projects)
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


def main():
    """Main function to start the program."""
    projects = load_projects_from_file('projects.txt')
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from projects.txt")
    main_menu(projects)


if __name__ == "__main__":
    main()
