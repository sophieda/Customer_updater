from datetime import datetime


class Date:
    """Check the format of the date."""

    def __init__(self, date: str) -> None:
        date_format = "%Y-%m-%d"
        correct_date_format = True
        try:
            correct_date_format = bool(datetime.strptime(date, date_format))
        except ValueError:
            correct_date_format = False
        if not correct_date_format:
            raise Exception("Date format invalid, correct format is yyyy-mm-dd: {date}")
        self.str_value = date
        self.date_time = datetime.strptime(date, date_format)
