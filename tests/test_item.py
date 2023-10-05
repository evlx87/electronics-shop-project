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
