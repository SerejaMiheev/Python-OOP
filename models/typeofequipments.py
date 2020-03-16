class Type_Of_Equipments:
    def __init__(self, type_of_equipment: str = "") -> None:
        self.type_of_equipment = type_of_equipment

    def set_type_of_equipment(self, type_of_equipment: str) -> None:
        self.type_of_equipment = type_of_equipment

    def get_type_of_equipment(self) -> str:
        return self.type_of_equipment

    def __str__(self):
        return f"Тип оборудования: {self.type_of_equipment}"
