from models.typeofequipments import Type_Of_Equipments


class Equipment:
    def __init__(self, count: int = 0, eq_type: Type_Of_Equipments = None) -> None:
        self.count = count
        self.eq_type = eq_type

    def set_type(self, eq_type: Type_Of_Equipments) -> None:
        self.eq_type = eq_type

    def set_count(self, count: int) -> None:
        self.count = count

    def get_type(self) -> Type_Of_Equipments:
        return self.eq_type

    def get_count(self) -> int:
        return self.count

    def __str__(self) -> str:
        return f"Кол-во оборудования: {self.count} \nТип оборудования: {self.eq_type.get_type_of_equipment()}"

