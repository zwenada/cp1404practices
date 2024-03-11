FILENAME = "course_info.txt"

def main():
    data = fetch_data()
    show_course_details(data)

def fetch_data():
    """Read data from the file formatted like: course, instructor, number of students."""
    input_file = open(FILENAME)
    course_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        course_data.append(parts)
    input_file.close()
    return course_data

def show_course_details(data):
    """Display the course details."""
    for course in data:
        print(f"{course[0]} is taught by {course[1]} and has {course[2]} students")

main()
