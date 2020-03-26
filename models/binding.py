from pony.orm import set_sql_debug, db_session

from models.camera import Camera
from models.equipment import Equipment
from models.event import Event
from models.floor import Floor
from models.person import Person
from models.room import Room, db
from models.section import Section
from models.typeofequipments import Type_Of_Equipments

db.bind(provider='mysql', host='localhost', user='pony', passwd='Pony1234', db='oop')
set_sql_debug(True)
db.generate_mapping(create_tables=True)

with db_session:
    toe1 = Type_Of_Equipments(type_of_equipment="Стул")
    e1 = Equipment(count=20, eq_type=toe1)
    r1 = Room(number_room=354, equipments=e1)
    s1 = Section(number_section=1, rooms_no_on_floor=r1)
    f1 = Floor(number_floor=1, section=s1)
    c1 = Camera(loc_record="C:\\Users\\Video", section=s1)
    p1 = Person(fio="Иванов Иван Иванович")
