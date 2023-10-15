import re


class Email:
    """Check the format of the email."""

    def __init__(self, email: str) -> None:
        # Regex for email address
        self.value = ""
        if email:
            regex = re.compile(
                r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
            )
            if not re.fullmatch(regex, email):
                raise Exception(f"Email not valid: {email}")
            self.value = email

    def __eq__(self, other: object) -> bool:
        if other.__class__ is self.__class__:
            return self.value == other.value
        return False
