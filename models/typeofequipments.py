from models.database import *


class Type_Of_Equipments(db.Entity):
    type_of_equipment = Required(str, unique=True)
    equipment = Set('Equipment')
