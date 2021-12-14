from typing import List, Optional
from datetime import time

from schemas.generic import GenericSchema


class Frequency(GenericSchema):
    time: time


# Shared properties
class MedicineBase(GenericSchema):
    name: str
    frequency_a_day: Optional[int] = None
    dosage: Optional[List[Frequency]] = None


# Properties to receive on Medicine creation
class MedicineCreate(MedicineBase):
    name: str
    dosage: str


# Properties to receive on Medicine update
class MedicineUpdate(MedicineBase):
    pass


# Properties shared by models stored in DB
class MedicineInDBBase(MedicineBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Medicine(MedicineInDBBase):
    pass


# Properties properties stored in DB
class MedicineInDB(MedicineInDBBase):
    pass
