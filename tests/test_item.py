import src.item
import src.phone
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


def test_name(product):
    product.name = 'Фен'
    assert product.name == 'Фен'
    product.name = 'Холодильник'
    assert product.name == 'Холодильни'


def test_instantiate_from_csv():
    src.item.Item.instantiate_from_csv('tests/test_items.csv')
    assert len(src.item.Item.all) == 2


def test_string_to_number():
    assert src.item.Item.string_to_number('6.6') == 6


def test_repr(product):
    assert repr(product) == "Item('Соковарка', 15000, 2)"


def test_str(product):
    assert str(product) == 'Соковарка'


def test_add(product):
    assert product + product == 4
    with pytest.raises(ValueError):
        5 + product
