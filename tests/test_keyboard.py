import src.keyboard
# import src.item
import pytest


@pytest.fixture
def product():
    test_keyboard = src.keyboard.Keyboard("Logitech", 1500, 3)
    return test_keyboard


def test__init__(product):
    assert product.name == "Logitech"
    assert product.price == 1500
    assert product.language == "EN"


def test_str(product):
    assert str(product) == "Logitech"
    assert str(product.language) == "EN"


def test_change_lang(product):
    product.change_lang()
    assert str(product.language) == "RU"
    product.change_lang()
    assert str(product.language) == "EN"
    product.change_lang()
    assert str(product.language) == "RU"
