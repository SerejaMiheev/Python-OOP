from models.room import Room


class Floor:
    def __init__(self, number: int, rooms_on_floor: list = []) -> None:
        self.number = number
        self.rooms_on_floor = rooms_on_floor

    def set_number(self, number: int) -> None:
        self.number = number

    def set_rooms_on_floor(self, rooms_on_floor) -> None:
        self.rooms_on_floor = rooms_on_floor

    def add_room_on_floor(self, room_on_floor) -> None:
        self.rooms_on_floor.append(room_on_floor)

    def get_number(self) -> int:
        return self.number

    def get_rooms_on_floor(self) -> list:
        return self.rooms_on_floor

    def get_room_on_floor(self, room: Room) -> Room:
        try:
            return self.rooms_on_floor[self.rooms_on_floor.index(room)]
        except ValueError:
            raise ValueError(f'{room} is not in list')

    def __str__(self) -> str:
        return f"Номер этажа: {self.number} \nКомнаты на этаже: {self.rooms_on_floor}"
