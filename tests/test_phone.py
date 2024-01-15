import src.phone
import src.item
import pytest


@pytest.fixture
def product():
    test_phone = src.phone.Phone("OnePlus", 45500, 3, 6)
    return test_phone


def test__init__(product):
    assert product.name == "OnePlus"
    assert product.price == 45500
    assert product.number_of_sim == 6


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 136500.0


def test_apply_discount(product):
    src.item.Item.pay_rate = 1.5
    product.apply_discount()
    assert product.price == 68250.0


def test_name(product):
    product.name = 'Фон'
    assert product.name == 'Фон'
    product.name = 'СуперТелефон'
    assert product.name == 'СуперТелеф'


def test_number_of_sim(product):
    with pytest.raises(ValueError):
        product.number_of_sim = -1
    with pytest.raises(ValueError):
        product.number_of_sim = "-1"


def test_string_to_number():
    assert src.phone.Phone.string_to_number('6.6') == 6


def test_repr(product):
    assert repr(product) == "Phone('OnePlus', 45500, 3, 6)"


def test_str(product):
    assert str(product) == 'OnePlus'


def test_add(product):
    assert product + product == 6
    with pytest.raises(ValueError):
        product + 5


def test_radd(product):
    item11 = src.item.Item("НеТелефон", 10000, 7)
    assert item11 + product == 10
    ph11 = src.phone.Phone("НеТелефон", 10000, 6, 3)
    assert ph11 + product == 9
    with pytest.raises(ValueError):
        product + 5
    with pytest.raises(ValueError):
        5 + product
