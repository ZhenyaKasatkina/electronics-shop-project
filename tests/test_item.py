import src.item
import pytest


@pytest.fixture
def product():
    test_item = src.item.Item("Соковарка", 15000, 2)
    return test_item


def test__init__(product):
    assert product.name == "Соковарка"
    assert product.price == 15000


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 30000


def test_apply_discount(product):
    src.item.Item.pay_rate = 1.2
    product.apply_discount()
    assert product.price == 18000.0
