from collections import deque

class Order:
    def __init__(self, order_id, date, price, quantity):
        self.order_id = order_id
        self.date = date
        self.price = price
        self.quantity = quantity

o1 = Order(1, "2026-01-01", 100, 4)
o2 = Order(2, "2026-04-22", 200, 1)
o3 = Order(3, "2026-11-13", 150, 3)
o4 = Order(4, "2026-06-04", 250, 2)
o5 = Order(5, "2026-10-15", 300, 7)

orders = deque([o1, o2, o3, o4, o5])


o6 = Order(6, "2026-12-01", 175, 5)
orders.append(o6)

while orders:
    cur = orders.popleft()
    print(f"Order ID: {cur.order_id}, Date: {cur.date}, Price: {cur.price}, Quantity: {cur.quantity}")