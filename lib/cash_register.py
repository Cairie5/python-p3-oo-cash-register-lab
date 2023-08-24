#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.total = round(self.total, 2)
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.get_price_for_item(self.items[-1])
            self.total -= last_item_price
            self.items.pop()

    def get_price_for_item(self, item_title):
        item_prices = {
            "eggs": 0.98,
            "book": 5.00,
            "Lucky Charms": 4.5,
            "Ritz Crackers": 5.0,
            # ... add more items and prices as needed ...
        }
        return item_prices.get(item_title, 0.0)
    