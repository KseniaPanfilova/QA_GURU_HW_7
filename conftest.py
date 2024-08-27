import pytest
from models import Product, Cart


@pytest.fixture
def product_book():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product_pencil():
    return Product("pencil", 10, "This is a pencil", 2000)


@pytest.fixture()
def cart():
    return Cart()
