from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Product import Product
from supplier import Supplier


class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def store_all_products(self, product_list: list[dict]) -> None:
        if not product_list:
            return

        for item in product_list:
            product_type, details = next(iter(item.items()))

            supplier_detail = details["supplier"]
            supplier = Supplier(
                supplier_detail["supplier_id"],
                supplier_detail["name"],
                supplier_detail["contact_email"],
            )

            if product_type == "Physical":
                product = PhysicalProduct(
                    details["product_id"],
                    details["name"],
                    details["price"],
                    details["stock"],
                    details["weight"],
                    supplier,
                )
            elif product_type == "Digital":
                product = DigitalProduct(
                    details["product_id"],
                    details["name"],
                    details["price"],
                    details["stock"],
                    details["download_size"],
                    supplier,
                )
            else:
                continue

            self.add_product(product)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        for index, product in enumerate(self.__products):
            if product.product_id == product_id:
                del self.__products[index]
                return

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_products(self) -> None:
        if not self.__products:
            print("No products available in inventory.")
            return

        for product in self.__products:
            print(product.display_information())

    def get_inventory(self) -> list[dict]:
        return [product.to_dict() for product in self.__products]

    def show_product_details(self, product: Product) -> None:
        print(product.display_information())
        print(product.get_fulfilment_info())
