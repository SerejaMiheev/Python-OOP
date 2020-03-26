from models.database import *


class Type_Of_Equipments(db.Entity):
    type_of_equipment = Required(str)
    equipment = Set('Equipment')
