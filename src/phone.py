from src.item import Item


class Phone(Item):
    """
    Класс-наследник от класса Item (для представления товара в магазине).
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :number_of_sim: Количество поддерживаемых сим-карт
        (Количество физических SIM-карт должно быть целым числом больше нуля)
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """Количество SIM-карт (number_of_sim)
        должно быть целым числом больше нуля"""
        if not isinstance(number_of_sim, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        if number_of_sim < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
