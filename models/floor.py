from models.database import *
from models.section import Section


class Floor(Section):
    rooms = Set('Room')
