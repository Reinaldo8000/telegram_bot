from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer

from db.base_class import Base


class GenericModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
