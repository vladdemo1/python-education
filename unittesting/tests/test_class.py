"""Testing classes Product and Shop"""


import pytest
from unittesting.to_test import Product, Shop

# Product -> title, price, quantity


@pytest.fixture
def simple_product():
    """Create standard product"""
    return Product('Fanta', 15.0, quantity=10)


def test_main_init():
    """Check default property"""
    assert simple_product.price == 15.0
    assert simple_product.title == 'Fanta'
    assert simple_product.quantity == 10


def test_subtract_quantity():
    """Check subtract quantity"""
    simple_product.subtract_quantity(5)
    assert simple_product.quantity == 5


def test_add_quantity():
    """Normal test for change quantity"""
    simple_product.add_quantity(10)
    assert simple_product.quantity == 20


@pytest.mark.parametrize('price', (5, 7.5, 0, -11, -120.4))
def test_change_price(price):
    """Check something change price for product"""
    simple_product.change_price(price)
    # lol this price can be negative
    assert simple_product.price == price


@pytest.fixture
def main_shop():
    """Create standard shop like fixture"""
    return Shop(simple_product)


def test_money():
    """Check default money"""
    assert main_shop.money == 0


def test_add_same_product(simple_product):
    """Try to add same product"""
    shop = Shop(simple_product)
    assert shop.products == [simple_product]
    shop.add_product(simple_product)  # added same product
    assert shop.products == [simple_product]  # error, bcs in this 2 same products


def test_empty_products_index():
    """Check index empty product"""
    shop = Shop()
    assert shop._get_product_index('Fanta') is None


def test_first_index():
    """Check first index by 'Fanta' """
    assert main_shop._get_product_index('Fanta') == 0


@pytest.mark.parametrize('fanta', [('Fanta', 5),
                                   ('Fanta', 0),
                                   ('Fanta', -4),
                                   ('Fanta', -10.4)])
def test_sell_standard_product(fanta):
    """Normal test about sell product"""
    # This test all passed
    # But this func accepts incorrect values like 0, -4 or -10.4
    assert main_shop.sell_product(*fanta) == fanta[1]*15
