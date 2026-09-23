from finances.domain.currency import Currency

class Profile:
    def __init__(self, name, currency):
        if not isinstance(name, str):
            raise TypeError("name cannot be this type")

        normalized_name = name.strip()
        if normalized_name == "":
            raise ValueError("name cannot be blank")

        if not isinstance(currency, Currency):
            raise TypeError("Currency has to be a enum")
        
        self._name = normalized_name
        self._currency = currency

    @property
    def name(self):
        return self._name

    @property
    def currency(self):
        return self._currency