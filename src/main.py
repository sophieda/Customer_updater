import logging
import sys

from clients.Client import Client
from clients.config import API_URL
from dtos.CustomerDTO import CustomerDTO
from dtos.PurchaseDTO import PurchaseDTO
from ui.Cli import Cli
from ui.Gui import Gui
from utils.CsvParser import CsvParser


def main():
    if len(sys.argv) != 2 and (sys.argv[1] in ["cli", "gui"]):
        logging.info(
            'main.py should be called with one argument, either "cli" or "gui".'
        )
    if sys.argv[1] == "cli":
        main_cli = Cli(
            lambda customer_file_path, purchase_file_path: algorithm(
                customer_file_path, purchase_file_path
            )
        )
        main_cli.run()
    elif sys.argv[1] == "gui":
        main_gui = Gui(
            lambda customer_file_path, purchase_file_path: algorithm(
                customer_file_path, purchase_file_path
            )
        )
        main_gui.run()


def algorithm(customer_file_path, purchase_file_path):
    try:
        # Get data from csv as "raw" data (python dictionaries)

        # Customers
        csv_parser = CsvParser(customer_file_path)
        customers_raw = csv_parser.parse()

        # Purchases
        csv_parser.set_file(purchase_file_path)
        purchases_raw = csv_parser.parse()

        # Transform raw data to python object for better control and input checks
        customers = [
            CustomerDTO(dict_value=customer).get_customer()
            for customer in customers_raw
        ]
        purchases = [
            PurchaseDTO(dict_value=purchase).get_purchase()
            for purchase in purchases_raw
        ]

        # Naive algorithm, could be optimized for better performance (withdraw purchases from selection
        # when mapped to a customer)
        for customer in customers:
            for purchase in purchases:
                if customer.id == purchase.customer_id:
                    customer.purchases.append(purchase)

        # Get data as json format to be sent to the API (as a list of python dictionaries)
        customers_out = [
            CustomerDTO(object_value=customer).get_customer_out()
            for customer in customers
        ]
        logging.info(f"Information to be send to API :\n{customers_out}")

        # Send the data to the API
        client = Client(API_URL)
        client.put_customers(customers_out, simulate_api_working=True)
        logging.info("Process finished successfully")

    except Exception as exception:
        logging.debug(exception)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.DEBUG)
    main()
