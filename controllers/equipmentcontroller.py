from pony.orm import db_session, commit

from models.binding import *


class EquipmentController:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.e_dict

    def set_dict(self, e_dict: dict) -> None:
        self.e_dict = e_dict

    @db_session
    def get_equipments(self) -> list:
        return list(map(lambda item: item.to_dict(), Equipment.select()[:]))

    @db_session
    def del_equipment(self, equipment_d: dict) -> None:
        equipment = Equipment.select(lambda e: e.id == equipment_d['id'])
        equipment.delete()

    @db_session
    def new_equipment(self, equipment_d: dict) -> int:
        new_e = Equipment(count=equipment_d['count'], eq_type=equipment_d['eq_type'])
        commit()
        return new_e.id

    @db_session
    def update_equipment(self, equipment_d: dict) -> None:
        equipment = Equipment[equipment_d['id']]
        equipment.count = equipment_d['count']
        equipment.eq_type = equipment_d['eq_type']

    @db_session
    def get_equipment(self, equipment_d: dict) -> dict:
        equipment = Equipment.get(count=equipment_d['count'], eq_type=equipment_d['eq_type'])
        eq_d = {'id': equipment.id, 'count': equipment.count, 'eq_type': equipment.eq_type}
        return eq_d
