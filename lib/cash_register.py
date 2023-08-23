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
            self.total *= (1 - self.discount / 100)
            self.total = round(self.total, 2)
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_item_price = self._get_last_item_price()
            self.total -= last_item_price
            self.items.pop()

    def _get_last_item_price(self):
        last_item = self.items[-1]
        # You should have a way to look up the price of an item based on its title.
        # For simplicity, let's assume there's a function named `get_price_for_item`
        # that takes an item title and returns its price.
        return get_price_for_item(last_item)

    def _get_last_item_price(self):
        last_item = self.items[-1]
        # This is a placeholder method for demonstration purposes.
        # You need to replace it with a proper method to get item prices.
        return self.get_price_for_item(last_item)

    def get_price_for_item(self, item_title):
        # You should implement a logic here to fetch the price for the given item title.
        # This could involve looking up the price in a database or a predefined dictionary.
        # For this example, let's assume there's a dictionary named `item_prices`:
        item_prices = {
            "eggs": 0.98,
            "book": 5.00,
            "Lucky Charms": 4.5,
            "Ritz Crackers": 5.0,
            # ... add more items and prices as needed ...
        }

        # Return the price for the item_title if it exists in the dictionary.
        # You should handle cases where the item is not found and provide an appropriate default behavior.
        return item_prices.get(item_title, 0.0)
