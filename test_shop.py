"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity / 2) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(700)
        assert product.quantity == 300

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError, match='Недостаточное количество товара на складе'):
            product.buy(1100)
            assert ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart(self, product, cart):
        cart.add_product(product)
        print(cart.products.items())
        assert cart.products.values() == 1

    def test_remove_product_from_cart(self, product, cart):
        ...

    def test_clear_cart(self, product, cart):
        ...

    def test_get_total_price_of_cart(self, product, cart):
        ...

    def test_buy_cart(self, product, cart):
        ...
