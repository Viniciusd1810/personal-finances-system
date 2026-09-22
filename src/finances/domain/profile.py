class Profile:
    def __init__(self, profile_name, currency):
        if not isinstance(profile_name, str):
            raise TypeError("profile_name cannot be this type")
        if profile_name.strip() == "":
            raise ValueError("profile_name cannot be blank")
        self._profile_name = profile_name
        
        self._currency = currency