from models.database import *


class Equipment(db.Entity):
    count = Required(int)
    eq_type = Required('Type_Of_Equipments')
    room = Set('Room')
