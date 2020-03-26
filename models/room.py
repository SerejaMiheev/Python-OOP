from models.database import *


class Room(db.Entity):
    number_room = Required(int)
    equipments = Set('Equipment')
    floor = Optional('Floor')
    section = Optional('Section')
