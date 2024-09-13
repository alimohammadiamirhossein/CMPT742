students_grades = {
    "std1": {"a1": 95, "a2": 90, "a3": 85, "a4": 90},
    "std2": {"a1": 90, "a2": 85, "a3": 80, "a4": 85},
    "std3": {"a1": 85, "a2": 80, "a3": 100, "a4": 80},
    "std4": {"a1": 90, "a2": 75, "a3": 70, "a4": 95}
}

# Todo 1: Define a function to add average to each student's grades
def add_avg(grades):
    """Add average to each student's grades"""
    return grades

# Todo 2: Define a function to calculate the average of a student's grades for std1
def calculate_avg(assignments):
    """Calculate the average of the grades"""
    return ...


# Define main function
def main():
    updated_grades = add_avg(students_grades)
    print(updated_grades)


if __name__ == "__main__":
    main()