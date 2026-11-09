import json


class file_handle:
    def __init__(self) -> None:
        pass

    def __read_file(self, filename: str) -> list[dict]:
        try:
            with open(filename, mode="r") as file:
                products = json.load(file)
                print("\ninventory.json found.")
                print("Inventory loaded successfully.\n")
        except (FileNotFoundError, ValueError):
            products = []
        return products

    def __write_file(self, filename: str, inventory: list[dict]) -> None:
        with open(filename, mode="w") as file:
            json.dump(inventory, file, indent=4)

    def load_inventory(self) -> list[dict]:
        return self.__read_file("inventory.json")

    def save_inventory(self, products: list[dict]) -> None:
        self.__write_file("inventory.json", products)
