from pony.orm import set_sql_debug

from models.database import db
from models.camera import Camera
from models.equipment import Equipment
from models.event import Event
from models.floor import Floor
from models.person import Person
from models.room import Room
from models.typeofequipments import Type_Of_Equipments

db.bind(provider='mysql', host='localhost', user='pony', passwd='Pony1234', db='oop')
set_sql_debug(True)
db.generate_mapping(create_tables=True)
