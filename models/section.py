from models.database import *


class Section(db.Entity):
    number = Required(int)
    cameras = Set('Camera')
