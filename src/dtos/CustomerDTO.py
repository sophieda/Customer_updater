from dataclasses import dataclass

from models.Customer import Customer
from models.CustomerTitle import CustomerTitle
from models.Email import Email
from models.PostalCode import PostalCode

from .PurchaseDTO import PurchaseDTO


@dataclass
class CustomerDTO:
    """Data to object Customer instance.
    This class allows to translate customer raw data to python object, and python object
    to API's json format. And by translation it also allows to translate raw data
    directly to API's json format."""

    dict_value: dict = None
    object_value: Customer = None
    out_value: dict = None

    def get_customer(self) -> Customer:
        """From the dictionary data, create data object as a Customer type.

        Returns:
            Customer: The object with all the customer data.
        """
        if self.object_value is not None:
            return self.object_value
        # Raw parameters
        customer_id_raw = int(self.dict_value["customer_id"])
        title_raw = int(self.dict_value["title"])
        last_name_raw = self.dict_value["lastname"]
        first_name_raw = self.dict_value["firstname"]
        postal_code_raw = self.dict_value["postal_code"]
        city_raw = self.dict_value["city"]
        email_raw = self.dict_value["email"]

        # Objects
        customer_title = CustomerTitle(title_raw)
        postal_code = PostalCode(postal_code_raw)
        email = Email(email_raw)
        self.object_value = Customer(
            id=customer_id_raw,
            title=customer_title,
            last_name=last_name_raw,
            first_name=first_name_raw,
            postal_code=postal_code,
            city=city_raw,
            email=email,
        )
        return self.object_value

    def get_customer_out(self) -> dict:
        """From the customer data, create the output data used for the API.

        Returns:
            dict: The output data formatted for the API.
        """
        if self.out_value is not None:
            return self.out_value
        if self.object_value is None:
            self.get_customer()
        result = {}
        customer = self.object_value
        result["salutation"] = customer.title.value if customer.title.value else ""
        result["last_name"] = customer.last_name if customer.last_name else ""
        result["first_name"] = customer.first_name if customer.first_name else ""
        result["email"] = customer.email.value if customer.email.value else ""
        purchases = [
            PurchaseDTO(object_value=purchase).get_purchase_out()
            for purchase in customer.purchases
        ]
        result["purchases"] = purchases
        self.out_value = result
        return self.out_value
