from db import db_connection
from models import Agenda
from schemas import AgendaCreate, AgendaUpdate
from crud.crud_base import CRUDBase


class CRUDAgenda(CRUDBase[Agenda, AgendaCreate, AgendaUpdate]):
    pass


crud_agenda = CRUDAgenda(Agenda)
