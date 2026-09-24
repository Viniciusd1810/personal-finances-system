import uuid
from finances.domain.currency import Currency

class Profile:
    def __init__(self, name, currency, profile_id, user_id):
        if not isinstance(name, str):
            raise TypeError("name cannot be this type")

        normalized_name = name.strip()
        if normalized_name == "":
            raise ValueError("name cannot be blank")

        if not isinstance(currency, Currency):
            raise TypeError("currency must be a Currency enum")
        
        self._name = normalized_name
        self._currency = currency

        if not isinstance(profile_id,uuid.UUID):
            raise TypeError("id have to be uuid")
        self._id = profile_id

        if not isinstance(user_id, uuid.UUID):
            raise TypeError("user id have to be uuid")
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @property
    def currency(self):
        return self._currency

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id