from pony.orm import db_session, commit

from models.binding import *


class FloorRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.f_dict

    def set_dict(self, f_dict: dict) -> None:
        self.f_dict = f_dict

    @db_session
    def get_floors(self) -> list:
        return list(map(lambda item: item.to_dict(with_collections=True), Floor.select()[:]))

    @db_session
    def del_floor(self, floor_d: dict) -> None:
        floor = Floor.select(lambda f: f.id == floor_d['id'])
        floor.delete()

    @db_session
    def new_floor(self, floor_d: dict) -> dict:
        if ((floor_d['cameras'] != -1) and (floor_d['rooms'] != -1)):
            new_f = Floor(number=floor_d['number'], rooms=self.get_rooms_by_id(floor_d['rooms']),
                          cameras=self.get_cameras_by_id(floor_d['cameras']))
            commit()
            new_d = {'id': new_f.id, 'number': new_f.number, 'rooms': floor_d['rooms'], 'cameras': floor_d['cameras']}
            return new_d
        else:
            if ((floor_d['cameras'] == -1) and (floor_d['rooms'] == -1)):
                new_f = Floor(number=floor_d['number'])
                commit()
                new_d = {'id': new_f.id, 'number': new_f.number, 'rooms': -1, 'cameras': -1}
                return new_d
            else:
                if (floor_d['cameras'] != -1):
                    new_f = Floor(number=floor_d['number'], cameras=self.get_cameras_by_id(floor_d['cameras']))
                    commit()
                    new_d = {'id': new_f.id, 'number': new_f.number, 'rooms': -1, 'cameras': floor_d['cameras']}
                    return new_d
                else:
                    new_f = Floor(number=floor_d['number'], rooms=self.get_rooms_by_id(floor_d['rooms']))
                    commit()
                    new_d = {'id': new_f.id, 'number': new_f.number, 'rooms': floor_d['rooms'], 'cameras': -1}
                    return new_d

    @db_session
    def update_floor(self, floor_d: dict) -> None:
        floor = Floor[floor_d['id']]
        if ((floor_d['cameras'] != -1) and (floor_d['rooms'] != -1)):
            floor.number = floor_d['number']
            floor.rooms = self.get_rooms_by_id(floor_d['rooms'])
            floor.cameras = self.get_cameras_by_id(floor_d['cameras'])
        else:
            if ((floor_d['cameras'] == -1) and (floor_d['rooms'] == -1)):
                floor.number = floor_d['number']
                floor.rooms = []
                floor.cameras = []
            else:
                if (floor_d['cameras'] != -1):
                    floor.number = floor_d['number']
                    floor.rooms = []
                    floor.cameras = self.get_cameras_by_id(floor_d['cameras'])
                else:
                    floor.number = floor_d['number']
                    floor.rooms = self.get_rooms_by_id(floor_d['rooms'])
                    floor.cameras = []

    @db_session
    def get_floor(self, floor_d: dict) -> dict:
        floor = Floor[floor_d['id']]
        f_d = floor.to_dict(with_collections=True)
        return f_d

    @db_session
    def get_rooms_by_id(self, roomsids):
        return set([Room.get(id=id) for id in roomsids])

    @db_session
    def get_cameras_by_id(self, camerasids):
        return set([Camera.get(id=id) for id in camerasids])
