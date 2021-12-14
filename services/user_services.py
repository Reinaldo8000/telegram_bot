from models import User
import schemas
from crud import crud_user


class UserService:
    def __init__(self) -> None:
        pass

    def get_user_by_id(self, id: int) -> schemas.User:
        val = crud_user.get_value(id)
        value = schemas.User(**val.__dict__)
        return value

    def get_user_medicines(self, id: int) -> str:
        value = self.get_user_by_id(id)
        return value.val_medicines()

    def get_user_agenda(self, id: int) -> str:
        value = self.get_user_by_id(id)
        return value.val_agenda()

    def check_user(self, user: User) -> User:
        pass

    def create_user(self, user: User):
        user_out = crud_user.create(user)
        return user_out

    def check_and_save_new_user(self, user: User):
        db_user = self.check_user(user)
        if db_user:
            self.create_user(user)
        return user
