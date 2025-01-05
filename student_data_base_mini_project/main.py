import os
import json
from tabulate import tabulate
import textwrap


class student:

    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def __repr__(self):
        grades_table = [[subject + 1, score]
                        for subject, score in enumerate(self.grades)]
        table = tabulate(grades_table +
                         [["Avg", sum(self.grades) / len(self.grades)]],
                         headers=["Subject", "Score"],
                         tablefmt="fancy_grid",
                         colalign=("center", "center"))
        return ("Student Name is: {}\n".format(self.name) +
                "Age is: {}\n".format(self.age) + "Grades:\n{}".format(table))

    def __str__(self):
        return str(self.__dict__)

    def to_dict(self):
        # Convert the instance attributes into a dictionary
        return {
            "name": self.name,
            "age": self.age,
            "grades": self.grades,
        }

    def printSummary(self):
        if (len(self.grades) == 0):
            print("No grades to show")
        else:
            print(
                """\n\nStudent: {} did register : {} Subjects with the following average: {}
        """.format(self.name, len(self.grades),
                   sum(self.grades) / len(self.grades)))


# Handle the location of the text file dynamically to be in same folder that contains the running python script
current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)

# Name the file that will be used to store the data
file_name = "database.json"
FILEPATH = f"{current_file_dir}/{file_name}"


# Function to write the data to the file
def write_data(data: list):
    data_dict = {"students": [student.to_dict() for student in data]}
    with open(FILEPATH, "w") as myFile:
        json.dump(data_dict, myFile, indent=4)


def read_data():
    myFile = open(FILEPATH, "r")
    text = myFile.read()
    data = json.loads(text)
    myFile.close()
    students = []
    for student_data in data.get("students", []):
        # Recreate the student object from the dictionary data
        student_obj = student(student_data["name"], student_data["age"],
                              student_data["grades"])
        students.append(student_obj)
    return students


# write_data(students)
students = read_data()


def add_student(data: list):
    try:
        std_name = input("Enter your name: ")
        if not std_name.isalpha():
            raise ValueError("Name should only contain letters.")

        std_age = input("Enter your age: ")
        if not std_age.isdigit():
            raise ValueError("Age should be a number.")

        std_grade = []
        print("Enter grades one by one. Type 'done' when finished:")

        while True:
            # Prompt the user for each grade input
            grade_input = input("Enter grade (or 'done' to finish): ").strip()
            # Allow user to exit the loop if they are finished
            if grade_input.lower() == 'done':
                if not std_grade:  # Check if no grades were entered
                    raise ValueError("At least one grade must be entered.")
                break
            # Validate and convert the grade to an integer
            try:
                if grade_input.isdigit():
                    thisGrade = float(grade_input)
                    if thisGrade > 100 or thisGrade < 0:
                        raise ValueError(
                            "Grade should be between 0 - 100 Please Enter Correct Grade"
                        )
                    else:
                        std_grade.append(thisGrade)
                else:
                    raise (ValueError(
                        f"Invalid input: '{grade_input}' is not a number. Please enter a valid grade."
                    ))
            except Exception as e:
                print(e)
        data.append(student(std_name, int(std_age), std_grade))
        write_data(data)
        print("Student added successfully")
    except Exception as e:
        print(e)


def read_note(data: list):
    if not print_students(data):
        return
    student_id = input("Enter the index of the Student you want: ")
    if not student_id.isdigit():
        print("Please enter a valid index.")
        return
    student_id = int(student_id)
    if student_id > 0 and student_id < len(data):
        student = data[student_id - 1]
        student.printSummary()
    # if note_id in data.keys():
    #     print(data[0])
    # else:
    #     print("Note not found")


def print_students(data: list):
    if len(data) > 0:
        # Wrap long text
        index = 1
        for dict in data:
            wrapped_data = [("Index", index)
                            ] + [(key, textwrap.fill(str(value), width=20))
                                 for key, value in dict.__dict__.items()]
            print(tabulate(wrapped_data, tablefmt="fancy_grid"))
            index += 1
        return True
    else:
        print("\nNo Notes Found Enter your First Note\n")
        return False


def delete_student(data: list):
    if not print_students(data):
        return
    student_id = input("Enter the index of the Student you want: ")
    if not student_id.isdigit():
        print("Please enter a valid index.")
        return
    student_id = int(student_id)
    if student_id > 0 and student_id < len(data):
        student = data[student_id - 1]
        data.remove(student)


def main():
    students = read_data()
    while True:
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Read Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_student(read_data())
                students = read_data()

            case "2":
                delete_student(students)
                write_data(students)
            case "3":
                read_note(students)
                students = read_data()
            case "4":
                return
            case _:
                print("Invalid choice")
        print()
        print()
        print()


if __name__ == "__main__":
    main()
