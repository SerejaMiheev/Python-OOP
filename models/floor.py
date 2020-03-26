from models.database import *


class Floor(db.Entity):
    number_floor = Required(int)
    rooms_on_floor = Set('Room')
    section = Required('Section')
