from Product import Product 

class Inventory:
    def __init__(self):
        self.__products = []

    def store_all_products(self, product_list):
        if product_list:
            for item in product_list:
                product = Product(
                    item["product_id"], item["name"], item["price"], item["stock"]
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
            product.display_information()

    def get_inventory(self):
        return [product.to_dict() for product in self.__products]