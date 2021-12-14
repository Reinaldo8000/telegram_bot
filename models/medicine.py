from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import JSON, Integer, String
from models.generic import GenericModel


class Medicine(GenericModel):
    name = Column(String)
    frequency_a_day = Column(Integer)
    dosage = Column(JSON)
