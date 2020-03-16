import models.camera as Camera
from models.floor import Floor
from models.room import Room


class Section:
    def __init__(self, numsection: int = 0, floors: list = [], roomsnoonfloor: list = [],
                 cameras: list = []) -> None:
        self.numsection = numsection
        self.floors = floors
        self.roomsnoonfloor = roomsnoonfloor
        self.cameras = cameras

    def set_numsection(self, numsection: int) -> None:
        self.numsection = numsection

    def add_floor(self, floor: Floor) -> None:
        self.floors.append(floor)

    def set_floors(self, floors: list) -> None:
        self.floors = list(floors)

    def add_roomnoonfloor(self, room: Room) -> None:
        self.roomsnoonfloor.append(room)

    def set_roomsnoonfloor(self, rooms: list) -> None:
        self.roomsnoonfloor = list(rooms)

    def add_camera(self, camera: Camera) -> None:
        self.cameras.append(camera)

    def set_cameras(self, cameras: list) -> None:
        self.cameras = list(cameras)

    def get_numsection(self) -> int:
        return self.numsection

    def get_floors(self) -> list:
        return self.floors

    def get_floor(self, floor: Floor) -> Floor:
        try:
            return self.floors[self.floors.index(floor)]
        except ValueError:
            raise ValueError(f'{floor} is not in list')

    def get_roomsnoonfloor(self) -> list:
        return self.roomsnoonfloor

    def get_roomnoonfloor(self, room: Room) -> Room:
        try:
            return self.roomsnoonfloor[self.roomsnoonfloor.index(room)]
        except ValueError:
            raise ValueError(f'{room} is not in list')

    def get_cameras(self) -> list:
        return self.cameras

    def get_camera(self, camera: Camera) -> Camera:
        try:
            return self.cameras[self.cameras.index(camera)]
        except ValueError:
            raise ValueError(f'{camera} is not in list')

    def __str__(self) -> str:
        return f"Номер секции: {self.numsection} \nСписок этажей: {self.floors} \nСписок комнат не на этажах: {self.roomsnoonfloor} \nСписок камер: {self.cameras}"
