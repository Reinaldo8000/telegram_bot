from typing import Optional

from schemas.generic import GenericSchema


# Shared properties
class ErrorBase(GenericSchema):
    error_tag: str
    message: Optional[int] = None


# Properties to receive on Error creation
class ErrorCreate(ErrorBase):
    error_tag: str
    message: str


# Properties to receive on Error update
class ErrorUpdate(ErrorBase):
    pass


# Properties shared by models stored in DB
class ErrorInDBBase(ErrorBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Error(ErrorInDBBase):
    pass


# Properties properties stored in DB
class ErrorInDB(ErrorInDBBase):
    pass
