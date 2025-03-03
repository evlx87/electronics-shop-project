import csv


class InstantiateCSVError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Item:
    """Класс для представления товара в магазине"""
    pay_rate = 1.0
    all = []

    @classmethod
    def set_discount_rate(cls, rate):
        """
        Устанавливает скидку для всех товаров.
        :param rate: Новое значение скидки.
        """
        cls.pay_rate = rate

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
        self.__class__.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара"""
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path='src/items.csv'):
        csv_file_path = "../" + str(path)

        try:
            cls.all = []
            with open(csv_file_path, 'r') as f:
                data = csv.DictReader(f)
                try:
                    for item in data:
                        cls(item['name'], float(item['price']), int(item['quantity']))
                except KeyError:
                    raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            print("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(string):
        cleaned_string = string.replace('.', ',')
        return int(cleaned_string.split(',')[0])

    def __add__(self, other: int) -> int or ValueError:
        """Магический метод для сложения количества товара"""
        return self.quantity + other.quantity
