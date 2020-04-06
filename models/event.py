from datetime import datetime

from models.database import *


class Event(db.Entity):
    date = Required(datetime)
    camera = Required('Camera')
    person = Optional('Person')
