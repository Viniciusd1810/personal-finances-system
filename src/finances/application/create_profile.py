import uuid
from finances.domain.profile import Profile

class CreateProfile:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def execute(self, name, currency, user_id):
        user_in_repository = self._user_repository.exists_by_id(user_id)
        
        if user_in_repository is False:
            raise ValueError("User not exists")
        profile_id = uuid.uuid4()
        new_profile = Profile(name, currency, profile_id, user_id)
        return new_profile