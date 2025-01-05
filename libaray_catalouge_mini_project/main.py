import os
import json
from tabulate import tabulate
import textwrap


class Book:

    def __init__(self, title: str, author: str, isAvaialbe: bool):
        self.title = title
        self.author = author
        self.isAvaialbe = isAvaialbe

    def __repr__(self):
        table = tabulate(
            [[self.title, self.author, "Yes" if self.isAvaialbe else "No"]],
            # headers=["Title", "Author", "avaialbe"],
            tablefmt="fancy_grid",
            colalign=("center", "center"))
        return (table)

    def __str__(self):
        return str(self.__dict__)

    def toList(self):
        return [self.title, self.author, "Yes" if self.isAvaialbe else "No"]

    def change_availability(self):
        self.isAvaialbe = not self.isAvaialbe
        print(self.title,
              "is now " + ("avaialbe" if self.isAvaialbe else "Booked"))


# Handle the location of the text file dynamically to be in same folder that contains the running python script
current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)

# Name the file that will be used to store the data
file_name = "database.json"
FILEPATH = f"{current_file_dir}/{file_name}"


# Function to write the data to the file
def write_data(data: list):
    data_dict = {"books": [book.__dict__ for book in data]}
    with open(FILEPATH, "w") as myFile:
        json.dump(data_dict, myFile, indent=4)


def print_books(data: list):
    if (len(data) == 0):
        print("No Books Exist Please add your first Book")
        return False

    rows = []
    index = 1
    for book in data:
        # rows.append([book.title, book.author, book.isAvaialbe])
        rows.append([index] + book.toList())
        index += 1
    table = tabulate(rows,
                     headers=["Index", "Title", "Author", "Availability"],
                     tablefmt="fancy_grid",
                     colalign=("center", "center", "center"))

    print(table)
    return True


def read_data():
    myFile = open(FILEPATH, "r")
    text = myFile.read()
    data = json.loads(text)
    myFile.close()
    students = []
    for student_data in data.get("books", []):
        # Recreate the student object from the dictionary data
        student_obj = Book(student_data["title"], student_data["author"],
                           student_data["isAvaialbe"])
        students.append(student_obj)
    return students


def add_book(data: list):
    try:
        book_title = input("Enter book title: ")
        if not book_title.isalpha():
            raise ValueError("Title should only contain letters.")

        book_author = input("Enter book auther name: ")
        if not book_title.isalpha():
            raise ValueError("Author Name should only contain letters.")
        #since book is added then it will be avaialble by default
        book = Book(book_title, book_author, True)
        data.append(book)
        write_data(data)
        print("book added successfully")
    except Exception as e:
        print(e)


def delete_book(data: list):
    if not print_books(data):
        return
    book_id = input("Enter the index of the Book you want: ")
    if not book_id.isdigit():
        print("Please enter a valid index.")
        return
    book_id = int(book_id)
    if book_id > 0 and book_id <= len(data):
        book = data[book_id - 1]
        print(book.title, "is deleted")
        data.remove(book)


def change_availability(data: list):
    if not print_books(data):
        return
    book_id = input("Enter the index of the Book you want: ")
    if not book_id.isdigit():
        print("Please enter a valid index.")
        return
    book_id = int(book_id)
    if book_id > 0 and book_id <= len(data):
        book = data[book_id - 1]
        book.change_availability()


def main():
    Books = read_data()
    while True:
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Change Book Avaialbilty")
        print("4. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_book(read_data())
                Books = read_data()

            case "2":
                delete_book(Books)
                write_data(Books)
            case "3":
                change_availability(Books)
                write_data(Books)
            case "4":
                return
            case _:
                print("Invalid choice")
        print()
        print()
        print()


if __name__ == "__main__":
    main()
