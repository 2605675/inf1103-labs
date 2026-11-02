from Product import Product

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