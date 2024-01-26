import csv
import os
from config import ROOT_DIR
from src.instantiatecsverror import InstantiateCSVError

FILENAME = 'src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity
        return total_cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_item):
        """Проверяет, что длина наименования товара не больше 10 символов.
        В противном случае, обрезать строку (оставив первые 10 символов)"""

        if len(name_item) <= 10:
            self.__name = name_item
        else:
            self.__name = "".join(list(name_item)[:10])

    @classmethod
    def instantiate_from_csv(cls, file_csv=FILENAME):
        """Класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv_"""
        cls.all.clear()
        try:
            with (open(os.path.join(ROOT_DIR, file_csv),
                       encoding="cp1251", newline='') as csvfile):
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # print(row)

                    # обработка повреждения данных файла
                    for key, value in row.items():
                        if key not in ['name', 'price', 'quantity'] or not value:
                            raise InstantiateCSVError(f"Файл item.csv поврежден")

                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    cls.all.append(cls(name, price, quantity))
                return cls(name, price, quantity)

        except FileNotFoundError:
            print("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(item_str):
        """Статический метод, возвращающий число из числа-строки"""
        return int(item_str.split(".")[0])

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"
