import json
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = int(quantity)

    def display_information(self):
        return (
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )

    @abstractmethod
    def get_fufilment_info(self):
        pass


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight
        self.__cost = self.calculate_shipping_cost()

    def display_information(self):
        return f" {super().display_information()} | Weight: {self.__weight} | Cost: {self.__cost}"

    def get_fufilment_info(self):
        print("Product requires physical shipping")
        return

    def calculate_shipping_cost(self):
        cost = self.__weight * 2
        return cost

    def to_dict(self):
        return {
            "Physical": {
                "product_id": super().get_product_id(),
                "name": super().get_name(),
                "price": super().get_price(),
                "stock": super().get_stock(),
                "weight": self.__weight,
                "cost": self.__cost,
            }
        }


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        return (
            f" {super().display_information()} | Download size: {self.__download_size}"
        )

    def get_fufilment_info(self):
        print("Product is delivered digitally")
        return

    def to_dict(self):
        return {
            "Digital": {
                "product_id": super().get_product_id(),
                "name": super().get_name(),
                "price": super().get_price(),
                "stock": super().get_stock(),
                "download_size": self.__download_size,
            }
        }


class Inventory:
    def __init__(self):
        self.__products = []

    def store_all_products(self, product_list):
        if product_list:
            for item in product_list:
                product_type, details = next(iter(item.items()))

                if product_type == "Physical":
                    product = PhysicalProduct(
                        details["product_id"],
                        details["name"],
                        details["price"],
                        details["stock"],
                        details["weight"],
                    )
                elif product_type == "Digital":
                    product = DigitalProduct(
                        details["product_id"],
                        details["name"],
                        details["price"],
                        details["stock"],
                        details["download_size"],
                    )

                self.__products.append(product)

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_products(self):
        products = self.__products
        if not products:
            print("No products available in inventory.")
            return
        for product in products:
            print(product.display_information())

    def get_inventory(self):
        return [product.to_dict() for product in self.__products]


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


class menu:
    def __init__(self, handle, inventory):
        self.__handle = handle
        self.__inventory = inventory

        products = self.__handle.load_inventory()
        self.__inventory.store_all_products(products)

        self.display_menu()

    def display_menu(self):
        while True:
            print("----------- MENU -----------")
            print(
                "1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit"
            )
            print("----------------------------\n")

            option = input("Enter option: ")

            try:
                option = int(option)
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.\n")
                continue

            if option == 1:
                print("\n--- Product List ---")
                self.__inventory.display_products()
                print()

            elif option == 2:
                print("\nAdd New Product")

                # Product ID validation
                while True:
                    product_id = input("Product ID: ").strip()
                    if not product_id:
                        print("Error: Product ID cannot be empty.")
                        continue
                    if self.__inventory.search_product(product_id) is not None:
                        print("Error: A product with this ID already exists.")
                        continue
                    break

                # Product Name validation
                while True:
                    input_product = input("Product Name: ").strip()
                    if not input_product:
                        print("Error: Product name cannot be empty.")
                        continue
                    break

                # Price validation
                while True:
                    try:
                        price = float(input("Price: "))
                        if price < 0:
                            print("Error: Price cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Error: Please enter a valid number for price.")

                # Stock validation
                while True:
                    try:
                        input_quantity = int(input("Stock Quantity: "))
                        if input_quantity < 0:
                            print("Error: Stock cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Error: Please enter a valid whole number for stock.")

                # Product Type
                while True:
                    product_type = (
                        input("Physical or Digital Product: ").strip().lower()
                    )
                    if not input_product:
                        print("Error: Product type cannot be empty.")
                        continue
                    elif product_type not in ["physical", "digital"]:
                        print("Error: Please enter either 'physical' or 'digital'.")
                        continue
                    break

                if product_type == "physical":
                    # Weight validation
                    while True:
                        try:
                            weight = float(input("Weight: "))
                            if weight < 0:
                                print("Error: Weight cannot be negative.")
                                continue
                            break
                        except ValueError:
                            print("Error: Please enter a valid number for Weight.")

                    item = PhysicalProduct(
                        product_id, input_product, price, input_quantity, weight
                    )

                elif product_type == "digital":
                    # Download size validation
                    while True:
                        try:
                            d_size = float(input("Download size: "))
                            if d_size < 0:
                                print("Error: Download size cannot be negative.")
                                continue
                            break
                        except ValueError:
                            print(
                                "Error: Please enter a valid number for Download size."
                            )

                    item = DigitalProduct(
                        product_id, input_product, price, input_quantity, d_size
                    )

                self.__inventory.add_product(item)
                print("\nProduct added successfully!\n")

            elif option == 3:
                print("\nUpdate Stock")
                id = input("Enter Product ID: ").strip()
                product = self.__inventory.search_product(id)

                if product is not None:
                    print("\nProduct Found:")
                    print(f"Name: {product.get_name()}")
                    print(f"Current Stock: {product.get_stock()}")

                    while True:
                        try:
                            new_stock = int(input("\nNew Stock Quantity: "))
                            if new_stock < 0:
                                print("Error: Stock cannot be negative.")
                                continue
                            break
                        except ValueError:
                            print("Error: Please enter a valid whole number.")

                    product.update_stock(new_stock)
                    print("Stock updated successfully.\n")
                else:
                    print("Product not found.\n")

            elif option == 4:
                print("\nSearch Product")
                id = input("Enter Product ID: ").strip()
                product = self.__inventory.search_product(id)

                if product is not None:
                    print("\nProduct Found")
                    print("------------------------------------------------")
                    print(f"ID: {product.get_product_id()} ")
                    print(f"Name: {product.get_name()} ")
                    print(f"Price: ${product.get_price():.2f} ")
                    print(f"Stock: {product.get_stock()} ")
                    print("------------------------------------------------\n")
                else:
                    print("Product not found.\n")

            elif option == 5:
                print("\nSaving inventory...")
                products = self.__inventory.get_inventory()
                self.__handle.save_inventory(products)
                print("Inventory saved successfully to inventory.json.\n")

            elif option == 6:
                print("\nSaving inventory before exit...")
                products = self.__inventory.get_inventory()
                self.__handle.save_inventory(products)
                print("Inventory saved successfully.\n")
                print(
                    "Thank you for using Inventory Management System.\nProgram terminated."
                )
                break
            else:
                print("Invalid option. Please choose between 1 and 6.\n")


if __name__ == "__main__":
    handler = file_handle()
    my_inventory = Inventory()
    app = menu(handler, my_inventory)
    # test = PhysicalProduct(1, "test", 2000, 10, 20)
    # print(test.display_information())
    # test.get_fufilment_info()
    # test = DigitalProduct(1, "test", 2000, 10, 20)
    # print(test.display_information())
    # test.get_fufilment_info()
