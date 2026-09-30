class FakeUserRepository:
    def __init__(self):
        self._users = {}

    def add(self, user):
        self._users[user.id] = user

    def exists_by_id(self, user_id):
        return user_id in self._users