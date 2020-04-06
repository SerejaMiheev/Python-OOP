from datetime import datetime, timedelta

from pony.orm import set_sql_debug, db_session, sum, select

from models.camera import Camera
from models.database import db
from models.equipment import Equipment
from models.event import Event
from models.person import Person
from models.room import Room
from models.floor import Floor
from models.typeofequipments import Type_Of_Equipments

db.bind(provider='mysql', host='localhost', user='pony', passwd='Pony1234', db='oop')
set_sql_debug(True)
db.generate_mapping(create_tables=True)

with db_session:
    # View:
    num = input("Type id: ")  # По данному типу отобразить кол-во всего оборудования данного типа
    s = sum(c.count for c in Equipment if c.eq_type == Type_Of_Equipments[num])

    num_f = input("Number floor: ")  # Показать все комнаты на этаже
    rooms = list(select(i for i in Room if i.floor.number == num_f))

    num_r = input("Number room: ")  # Показать все камеры в комнате
    cameras = list(select(i for i in Camera if i.section.number == num_r))

    # Delete:
    eve = select(i for i in Event if
                 i.date < (datetime.today() - timedelta(days=7)))  # Удаление событий дата которых, превысила 7 дней
    for it in eve:
        eve.delete()

    id_p = input("Person id: ")  # Удаление человека по id
    person = Person.select(lambda p: p.id == id_p)
    person.delete()

    # Update:
    id_c = input("Camera id: ")  # Изменение пути записи
    loc = input("New location record: ")
    camera = Camera[id_c]
    camera.loc_record = loc

    id_p_u = input("Person id:")  # Изменение фио
    fio = input("New fio: ")
    person = Person[id_p_u]
    person.fio = fio
