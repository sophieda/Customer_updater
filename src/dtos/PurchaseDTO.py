from dataclasses import dataclass

from models.Currency import Currency
from models.Date import Date
from models.Price import Price
from models.Purchase import Purchase
from models.Quantity import Quantity


@dataclass
class PurchaseDTO:
    """Data to object Purchase instance.
    This class allows to translate purchase raw data to python object, and python object
    to API's json format. And by translation it also allows to translate raw data
    directly to API's json format.
    """

    dict_value: dict = None
    object_value: Purchase = None
    out_value: dict = None

    def get_purchase(self) -> Purchase:
        """From the dictionary data, create data object as a purchase type.

        Returns:
            Purchase: The object with all the purchase data.
        """
        if self.object_value is not None:
            return self.object_value
        # Raw parameters
        purchase_identifier_raw = self.dict_value["purchase_identifier"]
        customer_id_raw = int(self.dict_value["customer_id"])
        product_id_raw = int(self.dict_value["product_id"])
        quantity_raw = int(self.dict_value["quantity"])
        price_raw = int(self.dict_value["price"])
        currency_raw = self.dict_value["currency"]
        date_raw = self.dict_value["date"]

        # Objects
        quantity = Quantity(quantity_raw)
        currency = Currency(currency_raw)
        price = Price(price_raw, currency)
        date = Date(date_raw)
        self.object_value = Purchase(
            id=purchase_identifier_raw,
            customer_id=customer_id_raw,
            product_id=product_id_raw,
            quantity=quantity,
            price=price,
            date=date,
        )
        return self.object_value

    def get_purchase_out(self) -> dict:
        """From the purchase data, create the output data used for the API.

        Returns:
            dict: The output data formatted for the API.
        """
        if self.out_value is not None:
            return self.out_value
        if self.object_value is None:
            self.get_purchase()
        purchase = self.object_value
        result = {}
        result["product_id"] = purchase.product_id
        result["price"] = purchase.price.value
        result["currency"] = purchase.price.currency.full_name
        result["quantity"] = purchase.quantity.value
        result["purchased_at"] = purchase.date.str_value
        self.out_value = result
        return self.out_value
