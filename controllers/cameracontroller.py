from pony.orm import db_session, commit

from models.binding import *


class CameraController:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.c_dict

    def set_dict(self, c_dict: dict) -> None:
        self.c_dict = c_dict

    @db_session
    def get_cameras(self) -> list:
        return list(map(lambda item: item.to_dict(), Camera.select()[:]))

    @db_session
    def del_camera(self, camera_d: dict) -> None:
        camera = Camera.select(lambda c: c.id == camera_d['id'])
        camera.delete()

    @db_session
    def new_camera(self, camera_d: dict) -> int:
        new_c = Camera(loc_record=camera_d['loc_record'])
        commit()
        return new_c.id

    @db_session
    def update_camera(self, camera_d: dict) -> None:
        camera = Camera[camera_d['id']]
        camera.loc_record = camera_d['loc_record']

    @db_session
    def get_camera(self, camera_d: dict) -> dict:
        camera = Camera.get(loc_record=camera_d['loc_record'])
        cm_d = {'id': camera.id, 'loc_record': camera.loc_record}
        return cm_d
