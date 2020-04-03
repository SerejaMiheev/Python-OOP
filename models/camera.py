from models.database import *


class Camera(db.Entity):
    loc_record = Required(str, unique=True)
    section = Required('Section')
    event = Set('Event')
