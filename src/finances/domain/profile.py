class Profile:
    def __init__(self, name, currency):
        if not isinstance(name, str):
            raise TypeError("name cannot be this type")
        if name.strip() == "":
            raise ValueError("name cannot be blank")
        self._name = name

        self._currency = currency

    @property
    def name(self):
        return self._name
        