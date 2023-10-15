from dataclasses import dataclass, field
from typing import List

from .CustomerTitle import CustomerTitle
from .Email import Email
from .PostalCode import PostalCode
from .Purchase import Purchase


@dataclass
class Customer:
    """Contains all the data describing a customer."""

    id: int
    title: CustomerTitle
    last_name: str
    first_name: str
    postal_code: PostalCode
    city: str
    email: Email
    purchases: List[Purchase] = field(default_factory=list)
