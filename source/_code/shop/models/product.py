"""ម៉ូដែលទំនិញ។"""


class Product:
    """ទំនិញមួយមុខ។"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"


def _internal_helper():
    """អនុគមន៍ផ្ទៃក្នុង — មិនមែនជាផ្នែកនៃ API សាធារណៈទេ។"""
    return "internal"
