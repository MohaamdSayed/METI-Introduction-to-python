import os
import json
from tabulate import tabulate
import textwrap

#handle the location of the text file dynamically to be in same folder that contain the running python script
currnt_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(currnt_file_path)

# Name the file of that will be used to store the data
file_name = "personal_diary.json"
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


def add_note(data: dict):
  note_id = input("Enter the note id: ")
  note = input("Enter your note: ")
  data[str(note_id)] = note
  write_data(data)
  print("Note added successfully")


def delete_note(data: dict):
  if not print_notes(data):
    return
  note_id = input("Enter the note id to delete: ")
  if note_id in data:
    del data[note_id]
    write_data(data)
    print("Note deleted successfully")
  else:
    print("Note not found")


def read_note(data: dict):
  if not print_notes(data):
    return
  note_id = input("Enter the note id to read: ")
  if note_id in data.keys():
    print(data[note_id])
  else:
    print("Note not found")


def print_notes(my_dict: dict):

  if len(my_dict) > 0:
    # Wrap long text
    wrapped_data = [(key, textwrap.fill(str(value), width=20))
                    for key, value in my_dict.items()]

    print(
        tabulate(wrapped_data,
                 headers=["Note ID", "Note"],
                 tablefmt="fancy_grid"))
    return True
  else:
    print("\nNo Notes Found Enter your First Note\n")
    return False


def main():
  notes = read_data()
  while True:
    print("1. Add note")
    print("2. Delete note")
    print("3. Read Note")
    print("4. Exit")
    choice = input("Enter your choice: ")
    match choice:
      case "1":
        add_note(read_data())
        notes = read_data()

      case "2":
        delete_note(notes)
        notes = read_data()

      case "3":
        read_note(notes)
        notes = read_data()
      case "4":
        return
      case _:
        print("Invalid choice")
    print()
    print()
    print()


if __name__ == "__main__":
  main()
