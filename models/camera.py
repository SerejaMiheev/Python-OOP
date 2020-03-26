from models.database import *


class Camera(db.Entity):
    loc_record = Required(str)
    section = Required('Section')
    event = Set('Event')
