import os
import json
from tabulate import tabulate
import textwrap

#handle the location of the text file dynamically to be in same folder that contain the running python script
currnt_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(currnt_file_path)

# Name the file of that will be used to store the data
file_name = "grades.json"
# print(current_file_dir)
FILEPATH = f"{current_file_dir}/{file_name}"


# Function to write the data to the file
def write_data(data: dict):
  myFile = open(FILEPATH, "w")
  json.dump(data, myFile, indent=4)
  myFile.close()


def read_data():
  myFile = open(FILEPATH, "r")
  text = myFile.read()
  data = json.loads(text)
  return data


def add_subject(data: dict):
  try:
    subject_name = input("Enter the subject Name : ")
    if not subject_name.isalpha():
      raise ValueError("Subject name should be a string")
    subject_grade = input("Enter your note: ")
    if not subject_grade.isnumeric():
      raise ValueError("Subject grade should be a number")
    if int(subject_grade) > 100 or int(subject_grade) < 0:
      raise ValueError("Subject grade should be between 0 and 100")
    data[str(subject_name)] = int(subject_grade)
    write_data(data)
    print("Subject added successfully")
  except Exception as e:
    print(e)


def delete_subject(data: dict):
  if not print_grades(data):
    return
  try:
    subject_name = input("Enter the subject Name : ")
    if not subject_name.isalpha():
      raise ValueError("Subject name should be a string")
    if subject_name in data:
      del data[subject_name]
      write_data(data)
      print("Subject deleted successfully")
  except Exception as e:
    print(e)
  else:
    print("Note not found")


def print_grades(my_dict: dict):
  if len(my_dict) > 0:
    # Wrap long text
    wrapped_data = [(key, textwrap.fill(str(value), width=20))
                    for key, value in my_dict.items()]

    print(
        tabulate(wrapped_data,
                 headers=["Subject", "Grade"],
                 tablefmt="fancy_grid"))
    return True
  else:
    print("\nNo Subjects found enter your first subject\n")
    return False


def calculate_avg(data: dict) -> float:
  total = 0
  for key, value in data.items():
    total += data[key]
  return total / len(data)


def main():
  subjetcs = read_data()
  while True:
    print("1. Add subject")
    print("2. Delete subject")
    print("3. List Subjects")
    print("4. Calculate avg")
    print("5. Exit")
    choice = input("Enter your choice: ")
    match choice:
      case "1":
        add_subject(read_data())
        subjetcs = read_data()

      case "2":
        delete_subject(subjetcs)
        subjetcs = read_data()

      case "3":
        print_grades(subjetcs)
        subjetcs = read_data()
      case "4":
        print(calculate_avg(subjetcs))

      case "5":
        return
      case _:
        print("Invalid choice")
    print()
    print()
    print()


if __name__ == "__main__":
  main()
