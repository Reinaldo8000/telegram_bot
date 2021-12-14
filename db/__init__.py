from .base_class import Base
from models.user import User
from models.medicine import Medicine
from models.user_medicine import UserMedicine
from models.agenda import Agenda
from .db import Database
from core.config import settings

# from .db import db_connection

db_connection = Database(
    "postgresql://postgres:reimg8000@localhost:5432/lightningassist"
)
