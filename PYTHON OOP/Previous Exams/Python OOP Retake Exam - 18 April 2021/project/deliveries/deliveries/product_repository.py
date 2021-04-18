
class ProductRepository:
    def __init__(self):
        self.products = []  # NOTE will contain all products (objects)

    def add(self, product):
        product_name = product.name
        if product in self.products:
            raise ValueError(f"Product {product_name} already exists.")
        self.products.append(product)
        return f"Product {product_name} successfully added to inventory."

    def decrease(self, product, quantity: int):
        if product in self.products:
            product.quantity -= quantity
            return f"Left quantity of {product.name}: {product.quantity}"

    def find(self, product_name: str):
        product_exist = [prod for prod in self.products if prod.name == product_name]
        if not product_exist:
            return "None"
        product = product_exist[0]
        return product
