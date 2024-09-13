# Todo 1: Create a specified class with methods
    
# Initialize Student object
student1 = Student("amx333", "Alice", 21, "Female", "Computer Science")

# Add courses and grades
student1.add_course("Math", 3.5)
student1.add_course("Programming", 4.0)
student1.add_course("Algorithms", 3.7)

# Export student info to a text file
student1.export_info()