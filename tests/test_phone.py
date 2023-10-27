# test_phone.py

from src.item import Item
from src.phone import Phone


def test_phone_initialization():
    phone = Phone("iPhone", 999.99, 5, 2)
    assert phone.name == "iPhone"
    assert phone.price == 999.99
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_phone_number_of_sim_setter():
    phone = Phone("Samsung", 799.99, 3, 1)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2


def test_phone_number_of_sim_setter_invalid_value():
    phone = Phone("Motorola", 599.99, 2, 1)
    try:
        phone.number_of_sim = -1
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля"
