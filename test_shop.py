import pytest


class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(product.quantity / 2) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False

    def test_product_buy(self, product):
        product.buy(700)
        assert product.quantity == 300

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError, match='Недостаточное количество товара на складе'):
            product.buy(1100)
            assert ValueError


class TestCart:

    def test_add_product_to_cart(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1

        cart.add_product(product, 2)
        assert cart.products[product] == 3

    def test_remove_product_from_cart_count_less(self, product, cart):
        cart.add_product(product, 10)
        cart.remove_product(product, 1)
        assert cart.products[product] == 9

    def test_remove_product_from_cart_count_none(self, product, cart):
        cart.add_product(product, 10)
        cart.remove_product(product, None)
        assert cart.products == {}

    def test_remove_product_from_cart_count_more(self, product, cart):
        cart.add_product(product, 10)
        cart.remove_product(product, 11)
        assert cart.products == {}

    def test_clear_cart(self, product, cart):
        cart.add_product(product, 10)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price_of_cart(self, product, cart):
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

    def test_buy_cart(self, product, cart):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

    def test_buy_cart_more_than_available(self, product, cart):
        cart.add_product(product, 1100)
        with pytest.raises(ValueError, match='Недостаточное количество товара на складе'):
            cart.buy()
            assert ValueError
