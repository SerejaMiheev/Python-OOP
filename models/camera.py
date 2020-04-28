from models.database import *


class Camera(db.Entity):
    loc_record = Required(str, unique=True)
    section = Optional('Section')
    event = Set('Event')
