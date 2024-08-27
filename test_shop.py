import pytest


class TestProducts:

    def test_product_check_quantity(self, product_book):
        assert product_book.check_quantity(product_book.quantity / 2) is True
        assert product_book.check_quantity(product_book.quantity) is True
        assert product_book.check_quantity(product_book.quantity + 1) is False

    def test_product_buy(self, product_book):
        product_book.buy(700)
        assert product_book.quantity == 300

    def test_product_buy_more_than_available(self, product_book):
        with pytest.raises(ValueError, match='Недостаточное количество товара на складе'):
            product_book.buy(1100)
            assert ValueError


class TestCartBasicCheck:

    def test_add_product_to_cart(self, product_book, cart):
        cart.add_product(product_book)
        assert cart.products[product_book] == 1

        cart.add_product(product_book, 2)
        assert cart.products[product_book] == 3

        with pytest.raises(ValueError, match='Количество товара не может быть равно или меньше 0'):
            cart.add_product(product_book, 0)
            assert ValueError

        with pytest.raises(ValueError, match='Количество товара не может быть равно или меньше 0'):
            cart.add_product(product_book, -10)
            assert ValueError

    def test_remove_product_from_cart_count_less(self, product_book, cart):
        cart.add_product(product_book, 10)
        cart.remove_product(product_book, 1)
        assert cart.products[product_book] == 9

    def test_remove_product_from_cart_count_none(self, product_book, cart):
        cart.add_product(product_book, 10)
        cart.remove_product(product_book, None)
        assert cart.products == {}

    def test_remove_product_from_cart_count_more(self, product_book, cart):
        cart.add_product(product_book, 10)
        cart.remove_product(product_book, 11)
        assert cart.products == {}

    def test_remove_product_from_cart_count_equals(self, product_book, cart):
        cart.add_product(product_book, 10)
        cart.remove_product(product_book, 10)
        assert cart.products == {}

    def test_clear_cart(self, product_book, cart):
        cart.add_product(product_book, 10)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price_of_cart(self, product_book, cart):
        cart.add_product(product_book, 10)
        assert cart.get_total_price() == 1000

    def test_buy_cart(self, product_book, cart):
        cart.add_product(product_book, 10)
        cart.buy()
        assert product_book.quantity == 990

    def test_buy_cart_more_than_available(self, product_book, cart):
        cart.add_product(product_book, 1100)
        with pytest.raises(ValueError, match='Не все товары в достаточном количестве'):
            cart.buy()
            assert ValueError


class TestCartWithSeveralProducts:

    def test_add_product_to_cart(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 10)
        cart.add_product(product_pencil, 100)
        assert cart.products[product_book] == 10 and cart.products[product_pencil] == 100

    def test_remove_product_from_cart_less(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 10)
        cart.add_product(product_pencil, 100)
        cart.remove_product(product_book, 1)
        cart.remove_product(product_pencil, 10)
        assert cart.products[product_book] == 9 and cart.products[product_pencil] == 90

    def test_remove_product_from_cart_count_none(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 10)
        cart.add_product(product_pencil, 100)
        cart.remove_product(product_book, None)
        assert cart.products == {product_pencil: 100}

    def test_remove_product_from_cart_count_more(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 10)
        cart.add_product(product_pencil, 100)
        cart.remove_product(product_book, 11)
        assert cart.products == {product_pencil: 100}

    def test_clear_cart(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 10)
        cart.add_product(product_pencil, 100)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price_of_cart(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 10)
        cart.add_product(product_pencil, 100)
        assert cart.get_total_price() == 2000

    def test_buy_cart(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 10)
        cart.add_product(product_pencil, 100)
        cart.buy()
        assert product_book.quantity == 990 and product_pencil.quantity == 1900

    def test_buy_cart_more_than_available(self, product_book, product_pencil, cart):
        cart.add_product(product_book, 1100)
        cart.add_product(product_pencil, 200)
        with pytest.raises(ValueError, match='Не все товары в достаточном количестве'):
            cart.buy()
            assert ValueError
