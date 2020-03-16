from models.equipment import Equipment


class Room:
    def __init__(self, number_room: int = 0, equipments: list = []) -> None:
        self.number_room = number_room
        self.equipments = equipments

    def set_number_room(self, number_room: int) -> None:
        self.number_room = number_room

    def set_equipments(self, equipments) -> None:
        self.equipments = equipments

    def add_equipment(self, equipment: Equipment) -> None:
        self.equipments.append(equipment)

    def get_number_room(self) -> int:
        return self.number_room

    def get_equipments(self) -> list:
        return self.equipments

    def get_equipment(self, equipment: Equipment) -> Equipment:
        try:
            return self.equipments[self.equipments.index(equipment)]
        except ValueError:
            raise ValueError(f'{equipment} is not in list')

    def __str__(self) -> str:
        return f"Номер комнаты: {self.number_room} \nСписок оборудования: {self.equipments}"

