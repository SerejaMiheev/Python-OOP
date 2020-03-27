from models.database import *


class Person(db.Entity):
    fio = Required(str, unique=True)
    event = Optional('Event')
