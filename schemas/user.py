from typing import List, Optional
from schemas.agenda import Agenda

from schemas.generic import GenericSchema
from schemas.medicine import Medicine


# Shared properties
class UserBase(GenericSchema):
    name: str
    chat_id: int


# Properties to receive on User creation
class UserCreate(UserBase):
    name: str
    chat_id: str


# Properties to receive on User update
class UserUpdate(UserBase):
    pass


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class User(UserInDBBase):
    medicine: Optional[List[Medicine]]
    agenda: Optional[List[Agenda]]

    def __str__(self):
        return f"User: {self.name}, Chat ID: {self.chat_id}"

    def val_medicines(self):
        s = ""
        for med in self.medicine:
            s = s + f"Medicine: {med.name} - Times a day: {med.frequency_a_day}\n"
            for t in med.dosage:
                s = s + f"Dosage at: {t.time.hour}h\n"
        return s

    def val_agenda(self):
        s = ""
        for ag in self.agenda:
            s = (
                s
                + f"Agenda: {ag.name} - Date: {ag.date_time.day}/{ag.date_time.month}/{ag.date_time.year} - Hour: {ag.date_time.time()} \n"
            )
        return s


# Properties properties stored in DB
class UserInDB(UserInDBBase):
    pass
