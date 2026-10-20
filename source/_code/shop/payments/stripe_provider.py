"""អ្នកផ្ដល់សេវាទូទាត់ប្រាក់តាម Stripe (ឧទាហរណ៍សាកល្បង)។"""

from ..models.order import Order
from . import config


def charge(order: Order, amount: float) -> str:
    """គិតប្រាក់សម្រាប់ការបញ្ជាទិញមួយ។"""
    return f"charged {amount} {config.CURRENCY} for order {order.order_id}"
