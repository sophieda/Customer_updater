from dataclasses import dataclass

from .Date import Date
from .Price import Price
from .Quantity import Quantity


@dataclass
class Purchase:
    """Contains all the data describing a purchase."""

    id: str
    customer_id: int
    product_id: int
    quantity: Quantity
    price: Price
    date: Date
