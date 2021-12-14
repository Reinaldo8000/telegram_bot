from datetime import datetime
from typing import List, Optional

from schemas.generic import GenericSchema


# Shared properties
class AgendaBase(GenericSchema):
    name: str
    description: Optional[str] = None
    date_time: datetime


# Properties to receive on Agenda creation
class AgendaCreate(AgendaBase):
    name: str
    date_time: datetime
    user_id: int


# Properties to receive on Agenda update
class AgendaUpdate(AgendaBase):
    pass


# Properties shared by models stored in DB
class AgendaInDBBase(AgendaBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Agenda(AgendaInDBBase):
    pass


# Properties properties stored in DB
class AgendaInDB(AgendaInDBBase):
    pass
