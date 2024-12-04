#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.items = []
    self.total = 0
    self.last = 0
    self.last_q = 1

  def add_item(self, name, amount, quantity = 1):
    self.total += amount * quantity
    self.last = amount
    self.last_q = quantity
    [self.items.append(name) for n in range(quantity)]
  def apply_discount(self):
    self.total -= (self.total*20)/100
    print(f"After the discount, the total comes to ${int(self.total)}." if self.discount != 0 else "There is no discount to apply.")
  def void_last_transaction(self):
    self.total -= self.last * self.last_q

