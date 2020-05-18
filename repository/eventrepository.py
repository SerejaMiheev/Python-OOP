from datetime import datetime

from pony.orm import db_session, commit

from models.binding import *


class EventRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.e_dict

    def set_dict(self, e_dict: dict) -> None:
        self.e_dict = e_dict

    @db_session
    def get_events(self) -> list:
        return list(map(lambda item: item.to_dict(), Event.select()[:]))

    @db_session
    def del_event(self, event_d: dict) -> None:
        event = Event.select(lambda e: e.id == event_d['id'])
        event.delete()

    @db_session
    def new_event(self, event_d: dict) -> dict:
        if (event_d['person'] == -1):
            new_e = Event(date=datetime.today(), camera=event_d['camera'])
            commit()
            new_d = {'id': new_e.id, 'date': new_e.date}
            return new_d
        else:
            new_e = Event(date=datetime.today(), camera=event_d['camera'], person=event_d['person'])
            commit()
            new_d = {'id': new_e.id, 'date': new_e.date}
            return new_d

    @db_session
    def del_old_event(self) -> None:
        eve = select(i for i in Event if
                     i.date < (datetime.today() - timedelta(days=7)))
        for it in eve:
            eve.delete()

    @db_session
    def get_event(self, event_d: dict) -> dict:
        event = Event[event_d['id']]
        e_d = event.to_dict()
        return e_d
