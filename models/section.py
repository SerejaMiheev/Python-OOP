from models.database import *


class Section(db.Entity):
    number_section = Required(int)
    floors = Set('Floor')
    rooms_no_on_floor = Set('Room')
    cameras = Set('Camera')
