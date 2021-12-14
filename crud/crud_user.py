from db import db_connection
from models import User
from crud.crud_base import CRUDBase
from schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_value(self, chat_id: int):
        return db_connection.session.query(User).filter(User.chat_id == chat_id).first()


crud_user = CRUDUser(User)
