from datetime import datetime

from models.database import *


class Event(db.Entity):
    date = Required(datetime)
    camera = Set('Camera')
    person = Optional('Person')
