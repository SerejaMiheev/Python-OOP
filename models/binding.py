from datetime import datetime

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
    toe2 = Type_Of_Equipments(type_of_equipment="Стол")

    e1 = Equipment(count=20, eq_type=toe1)
    e2 = Equipment(count=10, eq_type=toe2)

    f1 = Floor(number=1)
    f2 = Floor(number=2)

    r1 = Room(number=101, equipments=e1, floor=f1)
    r2 = Room(number=102, equipments=e1, floor=f1)
    r3 = Room(number=103, equipments=e1, floor=f1)
    r4 = Room(number=201, equipments=e1, floor=f2)

    c1 = Camera(loc_record="C:\\Users\\Video\\1", section=f1)
    c2 = Camera(loc_record="C:\\Users\\Video\\2", section=f2)
    c3 = Camera(loc_record="C:\\Users\\Video\\3", section=r1)
    c4 = Camera(loc_record="C:\\Users\\Video\\4", section=r4)

    p1 = Person(fio="Иванов Иван Иванович")
    p2 = Person(fio="Исламов Виктор Григориевич")
    p3 = Person(fio="Негеса Злата Афанасиевна")
    p4 = Person(fio="Палванова Людмила Глебовна")
    p5 = Person(fio="Двуреченский Герман Мартьянович")

    ev1 = Event(date=datetime.today(),camera=c1,person=p1)
