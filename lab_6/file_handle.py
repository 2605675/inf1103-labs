import json

class file_handle:
    def __init__(self):
        pass

    def __read_file(self, filename):
        try:
            with open(filename, mode="r") as file:
                products = json.load(file)
                print("\ninventory.json found.")
                print("Inventory loaded successfully.\n")
        except (FileNotFoundError, ValueError):
            products = []
        return products

    def __write_file(self, filename, inventory):
        with open(filename, mode="w") as file:
            json.dump(inventory, file, indent=4)

    def load_inventory(self):
        return self.__read_file("inventory.json")

    def save_inventory(self, products):
        self.__write_file("inventory.json", products)