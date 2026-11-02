def calculate_order_total(items, tax_rate=0.05, delivery_fee=40):
    subtotal = sum(i["price"] * i["qty"] for i in items)
    tax = subtotal * tax_rate
    total = subtotal + tax + delivery_fee
    return round(subtotal, 2), round(tax, 2), round(total, 2)
if __name__ == "__main__":
    order = [
        {"name": "Burger", "price": 120, "qty": 2},
        {"name": "Fries", "price": 80, "qty": 1},
        {"name": "Coke", "price": 50, "qty": 2},
    ]
    subtotal, tax, total = calculate_order_total(order)
    print(f"Subtotal: {subtotal}")
    print(f"Tax (5%): {tax}")
    print(f"Delivery: 40")
    print(f"Order Total: {total}")