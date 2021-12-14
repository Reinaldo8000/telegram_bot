from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship

from models.generic import GenericModel
from models.user_medicine import UserMedicine


class User(GenericModel):
    name = Column(String)
    chat_id = Column(Integer, unique=True)

    medicine = relationship("Medicine", secondary=UserMedicine, lazy="joined")
    agenda = relationship("Agenda", lazy="joined")
