"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    item = Item('apple', 10.0, 5)
    assert item.calculate_total_price() == 50.0


def test_apply_discount():
    item = Item('apple', 10.0, 5)
    item.apply_discount()
    assert item.price == 10.0 * item.pay_rate


@pytest.fixture
def sample_item():
    return Item("Sample Item", 10.0, 5)


def test_name_property(sample_item):
    assert sample_item.name == "Sample Item"


def test_name_setter(sample_item):
    sample_item.name = "New Item Name"
    assert sample_item.name == "New Item N"


def test_instantiate_from_csv():
    csv_file = "tests/test_data.csv"

    Item.instantiate_from_csv(csv_file)
    assert len(Item.all) == 2


def test_string_to_number():
    assert Item.string_to_number("10,5") == 10


def test_repr():
    item = Item("TestItem", 10.0, 5)
    assert repr(item) == "Item('TestItem', 10.0, 5)"


def test_str():
    item = Item("TestItem", 10.0, 5)
    assert str(item) == "TestItem"
