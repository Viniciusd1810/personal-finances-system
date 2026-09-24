import uuid
from finances.domain.profile import Profile

class CreateProfile:
    def execute(self, name, currency, user_id):

        profile_id = uuid.uuid4()

        new_profile = Profile(name, currency, profile_id, user_id)
        return new_profile