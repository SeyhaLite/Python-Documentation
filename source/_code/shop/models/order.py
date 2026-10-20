"""ម៉ូដែលការបញ្ជាទិញ។"""


class Order:
    """ការបញ្ជាទិញមួយ។"""

    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.lines = []

    def __repr__(self):
        return f"Order({self.order_id!r}, {self.customer!r})"
