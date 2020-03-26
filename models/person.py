from models.database import *


class Person(db.Entity):
    fio = Required(str)
    event = Optional('Event')
