from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from models.generic import GenericModel


class Error(GenericModel):
    error_tag = Column(String)
    message = Column(String)
