from db import db_connection
from models import Medicine
from schemas import MedicineCreate, MedicineUpdate
from crud.crud_base import CRUDBase


class CRUDMedicine(CRUDBase[Medicine, MedicineCreate, MedicineUpdate]):
    pass


crud_medicine = CRUDMedicine(Medicine)
