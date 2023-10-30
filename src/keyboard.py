class KeyboardLayoutMixin:
    def __init__(self, language="EN"):
        """Инициализирует объект KeyboardLayoutMixin"""
        self.__language = language

    @property
    def language(self):
        """Возвращает язык раскладки клавиатуры"""
        return self.__language

    @language.setter
    def language(self, language):
        """Устанавливает язык раскладки клавиатуры"""
        if language == "RU" or language == "EN":
            self.__language = language
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        """Изменяет язык раскладки клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
            return self.__language
        self.__language = "EN"
        return self


class Keyboard(KeyboardLayoutMixin):
    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        """Инициализирует объект Keyboard"""
        super().__init__(language)
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Возвращает строковое представление объекта Keyboard"""
        return self.name
