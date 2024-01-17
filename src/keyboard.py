from src.item import Item
from src.mixinlog import MixinLog


class Keyboard(Item, MixinLog):

    def __init__(self, name: str, price: float, quantity: int):
        """Товар отличается от `Item` тем, что у него есть атрибут `language`
        и метод для изменения языка (раскладки клавиатуры)"""
        super().__init__(name, price, quantity)
