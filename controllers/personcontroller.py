from pony.orm import db_session, commit

from models.binding import *


class PersonController:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_persons(self) -> list:
        return list(map(lambda item: item.to_dict(), Person.select()[:]))

    @db_session
    def del_person(self, person_d: dict) -> None:
        person = Person.select(lambda p: p.id == person_d['id'])
        person.delete()

    @db_session
    def new_person(self, person_d: dict) -> int:
        new_p = Person(fio=person_d['fio'])
        commit()
        return new_p.id

    @db_session
    def update_person(self, person_d: dict) -> None:
        person = Person[person_d['id']]
        person.fio = person_d['fio']

    @db_session
    def get_person(self, person_d: dict) -> dict:
        person = Person[person_d['id']]
        p_d = person.to_dict()
        return p_d
