from .Currency import Currency


class Price:
    """Check the price of purchase is positive."""

    def __init__(self, price_amount: int, currency: Currency) -> None:
        if price_amount < 0:
            raise Exception(
                f"Price amount cannot be lower than 0, invalid value: {price_amount}"
            )
        self.currency = currency
        self.value = price_amount
