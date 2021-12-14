from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String


from models.generic import GenericModel


class Agenda(GenericModel):
    name = Column(String)
    description = Column(String)
    date_time = Column(DateTime)

    user_id = Column(Integer, ForeignKey("user.id"))
