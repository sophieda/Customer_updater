class CustomerTitle:
    """Identify the gender of a customer. 
    NOTE : Normally we would specify this relation in a database, but for this 
    exercise we use a class instead.
    """

    def __init__(self, title_id: int) -> None:
        self.id = title_id
    
        self.value = ""
        if title_id == 1:
            self.value = "Ms."
        elif title_id == 2:
            self.value = "Mr."
        else:
            raise Exception(f"Title id not recognized: {title_id}")

    def __eq__(self, other: object) -> bool:
        if other.__class__ is self.__class__:
            return self.title_id == other.title_id
        return False
