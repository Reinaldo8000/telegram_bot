from db import db_connection
from models import Error
from schemas import ErrorCreate, ErrorUpdate
from crud.crud_base import CRUDBase


class CRUDError(CRUDBase[Error, ErrorCreate, ErrorUpdate]):
    def get_erro_by_error_tag(self, error_tag: str):
        return (
            db_connection.session.query(self.model)
            .filter(self.model.error_tag == error_tag)
            .first()
        )


crud_error = CRUDError(Error)
