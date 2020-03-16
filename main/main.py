from models.camera import Camera
from models.equipment import Equipment
from models.event import Event
from models.floor import Floor
from models.person import Person
from models.room import Room
from models.section import Section
from models.typeofequipments import Type_Of_Equipments

type1 = Type_Of_Equipments("Tables")
print(type1)
print("\n")

q1 = Equipment(34, type1)
print(q1)
print("\n")

f1 = Floor(1)

p1 = Person("Иванов Иван Иванович", 1234)
print(p1)
print("\n")

r1 = Room(101)
r1.add_equipment(q1)

f1.add_room_on_floor(r1)
print(f1)
print("\n")

s1 = Section(11)

c1 = Camera(12, "C:\\Users")

s1.add_camera(c1)
s1.add_floor(f1)

r2 = Room(201)

s1.add_roomnoonfloor(r2)
print(s1)
print("\n")

c1.set_section(s1)
print(c1)
print("\n")

event1 = Event(c1, p1)
print(event1)
