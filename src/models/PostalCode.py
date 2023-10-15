class PostalCode:
    """Check the format of the postal."""

    def __init__(self, postal_code: str) -> None:
        # Postal code is not a mandatory information in client's profile
        self.value = ""
        if postal_code:
            # The test here is not relevant (it is only for France's case) because there are many
            # format of postal_code. In a bigger project this is where we could check on the
            # postal_code format based on country/city if provided
            if len(postal_code) != 5:
                raise Exception(f"Postal code invalid: {postal_code}")
            self.value = postal_code

    def __eq__(self, other: object) -> bool:
        if other.__class__ is self.__class__:
            return self.value == other.value
        return False
