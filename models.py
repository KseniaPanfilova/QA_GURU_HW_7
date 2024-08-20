class Product:
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if self.quantity >= quantity:
            return True
        return False

    def buy(self, quantity):
        if self.check_quantity(quantity) is False:
            raise ValueError('Недостаточное количество товара на складе')
        else:
            self.quantity -= quantity

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None or remove_count > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for key, value in self.products.items():
            total_price += key.price * value
        return total_price

    def buy(self):
        for key, value in self.products.items():
            key.buy(value)
