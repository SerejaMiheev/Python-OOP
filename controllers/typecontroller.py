from pony.orm import db_session, commit

from models.binding import *


class TypeController:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.t_dict

    def set_dict(self, t_dict: dict) -> None:
        self.t_dict = t_dict

    @db_session
    def get_types(self) -> list:
        return list(map(lambda item: item.to_dict(), Type_Of_Equipments.select()[:]))

    @db_session
    def del_type(self, type_d: dict) -> None:
        type = Type_Of_Equipments.select(lambda t: t.type_of_equipment == type_d['type_of_equipment'])
        type.delete()

    @db_session
    def new_type(self, type_d: dict) -> int:
        new_t = Type_Of_Equipments(type_of_equipment=type_d['type_of_equipment'])
        commit()
        return new_t.id

    @db_session
    def update_type(self, type_d: dict) -> None:
        type = Type_Of_Equipments[type_d['id']]
        type.type_of_equipment = type_d['type_of_equipment']

    @db_session
    def get_type(self, type_d: dict) -> dict:
        type = Type_Of_Equipments.get(type_of_equipment=type_d['type_of_equipment'])
        toe_d = {'id': type.id, 'type_of_equipment': type.type_of_equipment}
        return toe_d

    @db_session
    def get_t(self, id: int) -> dict:
        type = Type_Of_Equipments[id]
        return {'id': type.id, 'type_of_equipment': type.type_of_equipment}
