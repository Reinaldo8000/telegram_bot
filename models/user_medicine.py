from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer

from db.base_class import Base

UserMedicine = Table(
    "user_medicine",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("medicine_id", Integer, ForeignKey("medicine.id")),
)
