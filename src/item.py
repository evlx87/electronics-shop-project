class Item:
    """
    Класс для представления товара в магазине.
    """
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
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
