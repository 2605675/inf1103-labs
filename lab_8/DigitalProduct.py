from Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self):
        info, supplier = super().display_information()
        print(f"{info} | Download size: {self.__download_size}" f"\n{supplier}")

    def get_fufilment_info(self):
        print("Product is delivered digitally")
        return

    def to_dict(self):
        data = super().to_dict()
        data["download_size"] = self.__download_size
        
        return {"Digital": data}