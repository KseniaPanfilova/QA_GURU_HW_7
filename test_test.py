from models import Product, Cart

item = Product(name='item', price=100, description='123', quantity=3)
item1 = Product(name='item', price=100, description='123', quantity=20)


def test_test():
    # print(item.quantity)
    # print(item.check_quantity(15))
    # item.buy(15)
    # print(item.quantity)
    # print(item.quantity)
    cart = Cart()
    cart.add_product(item)
    # cart.add_product(item)
    # print(cart.get_total_price())
    # cart.buy()
    # print(item.quantity)
    cart1 = {}
    cart.add_product(item)
    # cart1 = {item: 1}
    print(cart1[item])

    # print(item.buy(10))
    # print(item.quantity)
