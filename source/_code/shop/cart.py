"""រទេះទំនិញ។"""


class Cart:
    """រទេះទំនិញសាមញ្ញ។"""

    def __init__(self):
        self.items = []

    def add(self, product, quantity=1):
        """បន្ថែមទំនិញ។"""
        self.items.append((product, quantity))
        return len(self.items)

    def total(self):
        """ផលបូកតម្លៃទាំងអស់។"""
        return sum(p.price * q for p, q in self.items)
