class Currency:
    """
    Identify the currency of the purchase used by the customer. 
    NOTE : Normally we would specify this relation in a database, but for this 
    exercise we use a class instead.
    """
    def __init__(self, currency) -> None:
        self.full_name, self.short_name, self.symbol = "", "", ""
        if currency == "EUR":
            self.full_name = "euros"
            self.short_name = "EUR"
            self.symbol = "€"
        elif currency == "USD":
            self.full_name = "dollars"
            self.short_name = "USD"
            self.symbol = "$"
        else:
            raise Exception(f"Currency unknown: {currency}")

    def __eq__(self, other: "Currency") -> bool:
        if other.__class__ is self.__class__:
            return self.full_name == other.full_name
        return False
