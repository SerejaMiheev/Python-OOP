from pony.orm import db_session, commit

from models.binding import *


class RoomController:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.r_dict

    def set_dict(self, r_dict: dict) -> None:
        self.r_dict = r_dict

    @db_session
    def get_rooms(self) -> list:
        return list(map(lambda item: item.to_dict(), Room.select()[:]))

    @db_session
    def del_room(self, room_d: dict) -> None:
        room = Room.select(lambda r: r.id == room_d['id'])
        room.delete()

    @db_session
    def new_room(self, room_d: dict) -> dict:
        if ((room_d['cameras'] != -1) and (room_d['equipments'] != -1)):
            new_r = Room(number=room_d['number'], equipments=self.get_equipments_by_id(room_d['equipments']),
                         cameras=self.get_cameras_by_id(room_d['cameras']))
            commit()
            new_d = {'id': new_r.id, 'number': new_r.number, 'equipments': room_d['equipments'],
                     'cameras': room_d['cameras']}
            return new_d
        else:
            if ((room_d['cameras'] == -1) and (room_d['equipments'] == -1)):
                new_r = Room(number=room_d['number'])
                commit()
                new_d = {'id': new_r.id, 'number': new_r.number, 'equipments': -1, 'cameras': -1}
                return new_d
            else:
                if (room_d['cameras'] != -1):
                    new_r = Room(number=room_d['number'], cameras=self.get_cameras_by_id(room_d['cameras']))
                    commit()
                    new_d = {'id': new_r.id, 'number': new_r.number, 'equipments': -1, 'cameras': room_d['cameras']}
                    return new_d
                else:
                    new_r = Room(number=room_d['number'], equipments=self.get_equipments_by_id(room_d['equipments']))
                    commit()
                    new_d = {'id': new_r.id, 'number': new_r.number, 'equipments': room_d['equipments'], 'cameras': -1}
                    return new_d

    @db_session
    def update_room(self, room_d: dict) -> None:
        room = Room[room_d['id']]
        if ((room_d['cameras'] != -1) and (room_d['equipments'] != -1)):
            room.number = room_d['number']
            room.equipments = self.get_equipments_by_id(room_d['equipments'])
            room.cameras = self.get_cameras_by_id(room_d['cameras'])
        else:
            if ((room_d['cameras'] == -1) and (room_d['equipments'] == -1)):
                room.number = room_d['number']
                room.equipments = []
                room.cameras = []
            else:
                if (room_d['cameras'] != -1):
                    room.number = room_d['number']
                    room.equipments = []
                    room.cameras = self.get_cameras_by_id(room_d['cameras'])
                else:
                    room.number = room_d['number']
                    room.equipments = self.get_equipments_by_id(room_d['equipments'])
                    room.cameras = []

    @db_session
    def get_room(self, room_d: dict) -> dict:
        room = Room[room_d['id']]
        r_d = room.to_dict(with_collections=True)
        return r_d

    @db_session
    def get_equipments_by_id(self, equipmentsids):
        return set([Equipment.get(id=id) for id in equipmentsids])

    @db_session
    def get_cameras_by_id(self, camerasids):
        return set([Camera.get(id=id) for id in camerasids])
