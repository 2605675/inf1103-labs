from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from supplier import Supplier


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
                "1. Display All Products\n2. Add Product\n3. Update Stock\n4. Remove Product\n5. Search Product\n6. Save Inventory\n7. Exit"
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

                    sup = self.get_supplier()

                    item = PhysicalProduct(
                        product_id, input_product, price, input_quantity, weight, sup
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

                    sup = self.get_supplier()

                    item = DigitalProduct(
                        product_id, input_product, price, input_quantity, d_size, sup
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
                print("\nRemove Product")
                id = input("Enter Product ID: ").strip()
                product = self.__inventory.search_product(id)
                if product is not None:
                    self.__inventory.remove_product(id)
                else:
                    print("Product not found.\n")

            elif option == 5:
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

            elif option == 6:
                print("\nSaving inventory...")
                products = self.__inventory.get_inventory()
                self.__handle.save_inventory(products)
                print("Inventory saved successfully to inventory.json.\n")

            elif option == 7:
                print("\nSaving inventory before exit...")
                products = self.__inventory.get_inventory()
                self.__handle.save_inventory(products)
                print("Inventory saved successfully.\n")
                print(
                    "Thank you for using Inventory Management System.\nProgram terminated."
                )
                break
            else:
                print("Invalid option. Please choose between 1 and 7.\n")

    def get_supplier(self):
        # Supplier ID validation
        while True:
            supplier_id = input("Supplier ID: ").strip()
            if not supplier_id:
                print("Error: Supplier ID cannot be empty.")
                continue
            break

        # Supplier Name validation
        while True:
            input_Supplier = input("Supplier Name: ").strip()
            if not input_Supplier:
                print("Error: Supplier name cannot be empty.")
                continue
            break

        # Supplier Email validation
        while True:
            input_email = input("Supplier Email: ").strip()
            if not input_email:
                print("Error: Supplier Email cannot be empty.")
                continue
            break

        sup = Supplier(supplier_id, input_Supplier, input_email)

        return sup
