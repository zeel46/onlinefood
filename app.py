from flask import Flask, jsonify
from order_total import calculate_order_total

app = Flask(__name__)

MENU = [
    {"id": 1, "name": "Burger", "price": 120},
    {"id": 2, "name": "Fries", "price": 80},
    {"id": 3, "name": "Coke", "price": 50},
]


@app.route("/")
def home():
    return jsonify(message="Welcome to the Online Food Ordering App")


@app.route("/menu")
def menu():
    return jsonify(MENU)


@app.route("/total")
def total():
    order = [
        {"name": "Burger", "price": 120, "qty": 2},
        {"name": "Fries", "price": 80, "qty": 1},
        {"name": "Coke", "price": 50, "qty": 2},
    ]
    subtotal, tax, grand_total = calculate_order_total(order)
    return jsonify(subtotal=subtotal, tax=tax, delivery_fee=40, order_total=grand_total)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
