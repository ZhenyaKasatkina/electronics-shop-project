

class MixinLog:
    """Реализуйте дополнительный функционал по хранению и изменению
    раскладки клавиатуры в отдельном классе-миксине, который “подмешивается”
    в цепочку наследования класса `Keyboard`."""

    def __init__(self):

        self.__language = "EN"

    def change_lang(self):
        """Метод для изменения языка (раскладки клавиатуры)"""
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        else:
            raise AttributeError

    @property
    def language(self):
        return self.__language

    def __str__(self):
        return f"{self.language}"
