from models.database import *
from models.section import Section


class Room(Section):
    equipments = Set('Equipment')
    floor = Optional('Floor')
