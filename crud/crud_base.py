from typing import TypeVar, Type, Generic
from pydantic import BaseModel
from db.base_class import Base
from db import db_connection


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def create(self, obj_in: CreateSchemaType):
        db_connection.session.add(obj_in)
        db_connection.session.commit()
        db_connection.session.refresh(obj_in)
        return obj_in

    def get_all(self):
        return db_connection.session.query(self.model).all()

    def remove(self, id: int):
        db_connection.session.query(self.model).filter(self.model.id == id).delete()
        db_connection.session.commit()

    def search(self, parameter: str, collumn_name: str):
        db_connection.session.query(self.model).filter(
            f"{collumn_name}" == f"{parameter}"
        )
