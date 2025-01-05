import os
import json
from tabulate import tabulate


class Item:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        table = tabulate([[self.name, self.price, self.quantity]],
                         tablefmt="fancy_grid",
                         colalign=("center", "center", "center"))
        return (table)

    def __str__(self):
        return str(self.__dict__)

    def toList(self):
        return [self.name, self.price, self.quantity]


# Handle the location of the text file dynamically to be in same folder that contains the running python script
current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)

# Name the file that will be used to store the data
file_name = "inventory.json"
FILEPATH = f"{current_file_dir}/{file_name}"


# Function to write the data to the file
def write_data(data: list):
    data_dict = {"items": [book.__dict__ for book in data]}
    with open(FILEPATH, "w") as myFile:
        json.dump(data_dict, myFile, indent=4)


def print_items(data: list):
    if (len(data) == 0):
        print("No Items Exist Please add your first Item")
        return False

    rows = []
    index = 1
    for item in data:
        # rows.append([book.title, book.author, book.isAvaialbe])
        rows.append([index] + item.toList())
        index += 1
    table = tabulate(rows,
                     headers=["Index", "Name", "Price", "Quantity"],
                     tablefmt="fancy_grid",
                     colalign=("center", "center", "center", "center"))

    print(table)
    return True


def read_data():
    myFile = open(FILEPATH, "r")
    text = myFile.read()
    data = json.loads(text)
    myFile.close()
    items = []
    for items_data in data.get("items", []):
        # Recreate the student object from the dictionary data
        item = Item(items_data["name"], items_data["price"],
                    items_data["quantity"])
        items.append(item)
    return items


def add_item(data: list):
    try:
        item_name = input("Enter product name: ")
        if not item_name.isalpha():
            raise ValueError("Name should only contain letters.")

        item_price = input("Enter product price: ")
        if not item_price.isdigit():
            raise ValueError("Price should only contain numbers.")
        item_quantity = input("Enter product quantity: ")
        if not item_price.isdigit():
            raise ValueError("Quantity should only contain numbers.")
        #since book is added then it will be avaialble by default
        item = Item(item_name, float(item_price), int(item_quantity))
        data.append(item)
        write_data(data)
        print("item added successfully")
    except Exception as e:
        print(e)


def delete_item(data: list):
    if not print_items(data):
        return
    item_id = input("Enter the index of the Item you want: ")
    if not item_id.isdigit():
        print("Please enter a valid index.")
        return
    item_id = int(item_id)
    if item_id > 0 and item_id <= len(data):
        item = data[item_id - 1]
        print(item.title, "is deleted")
        data.remove(item)


def main():
    Books = read_data()
    while True:
        print("1. Add Items")
        print("2. Delete Items")
        print("3. List Itmems")
        print("4. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_item(read_data())
                Books = read_data()

            case "2":
                delete_item(Books)
                write_data(Books)
            case "3":
                print_items(Books)
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
