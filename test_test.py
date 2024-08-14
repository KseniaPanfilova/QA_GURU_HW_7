from models import Product
item = Product(name='item', price=100, description='123', quantity=20)

def test_test():
    print(item.check_quantity(25))