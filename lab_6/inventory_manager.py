class Product:
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
        print(
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }


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
