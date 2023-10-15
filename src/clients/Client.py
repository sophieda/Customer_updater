import json
import logging
from dataclasses import dataclass
from typing import Dict, List

import requests


@dataclass
class Client:
    """Interact with an API pointed by the provided url."""

    base_url: str

    def put_customers(
        self, customers_data: List[Dict], simulate_api_working: bool = False
    ):
        """Send customers data to the API.

        Args:
            customers_data (list[dict]): The customer data.
            simulate_api_working (bool, optional): Boolean used only for the demo as the url doesn't work. Defaults to False.
        """
        # the argument simulate_api_working
        if not simulate_api_working:
            request = requests.put(self.base_url, data=json.dumps(customers_data))
            if request.status_code < 200 or request.status_code >= 300:
                raise Exception(
                    f"Request to API failed, status code {request.status_code}"
                )
        logging.info("API call done successfully")
