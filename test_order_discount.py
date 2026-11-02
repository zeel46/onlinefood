import pytest


def calculate_order_total(items, discount_percent=0):
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    subtotal = sum(i["price"] * i["qty"] for i in items)
    return round(subtotal * (1 - discount_percent / 100), 2)


ITEMS = [
    {"name": "Burger", "price": 120, "qty": 2},   
    {"name": "Fries", "price": 80, "qty": 1},     
]  


def test_normal_discount():
    assert calculate_order_total(ITEMS, 10) == 288.0


def test_zero_discount():
    assert calculate_order_total(ITEMS, 0) == 320.0


def test_zero_value_order():
    assert calculate_order_total([], 10) == 0
    assert calculate_order_total([{"name": "Free", "price": 0, "qty": 3}], 20) == 0


def test_full_discount():
    assert calculate_order_total(ITEMS, 100) == 0


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_order_total(ITEMS, 150)
