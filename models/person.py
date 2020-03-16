class Person:
    def __init__(self, fio: str = "", id: int = -1) -> None:
        self.fio = fio
        self.id = id

    def set_fio(self, fio: str) -> None:
        self.fio = fio

    def set_id(self, id: int) -> None:
        self.id = id

    def get_fio(self) -> str:
        return self.fio

    def get_id(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f"ФИО: {self.fio} \nID: {self.id}"
