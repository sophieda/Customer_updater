class Quantity:
    """Check the quantity of purchase is positive."""

    def __init__(self, quantity_amount: int) -> None:
        if quantity_amount < 0:
            raise Exception("Quantity cannot be < 0")
        self.value = quantity_amount

    def __eq__(self, other: object) -> bool:
        if other.__class__ is self.__class__:
            return self.value == other.value
        return False

    def __gt__(self, other: object) -> bool:
        if other.__class__ is self.__class__:
            return self.value > other.value
