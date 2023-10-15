import csv
import logging
from dataclasses import dataclass


@dataclass
class CsvParser:
    file_path: str

    def parse(self) -> list:
        try:
            with open(self.file_path, "r") as csv_read:
                reader = csv.DictReader(f=csv_read, delimiter=";")
                result = list(reader)
        except Exception as exception:
            logging.debug(f"Could not read csv file {self.file_path}:{exception}")
            return []
        logging.info(f"Csv file {self.file_path} read:\n{result}")
        return result

    def set_file(self, new_file_path) -> None:
        self.file_path = new_file_path
