import models.section as Section


class Camera:
    def __init__(self, numbercam: int = 0, locrecord: str = "", section: Section = None) -> None:
        self.numbercam = numbercam
        self.locrecord = locrecord
        self.section = section

    def set_numbercam(self, numbercam: int) -> None:
        self.numbercam = numbercam

    def set_locrecord(self, locrecord: str) -> None:
        self.locrecord = locrecord

    def set_section(self, section: Section) -> None:
        self.section = section

    def get_numbercam(self) -> int:
        return self.numbercam

    def get_locrecord(self) -> str:
        return self.locrecord

    def get_section(self) -> Section:
        return self.section

    def __str__(self) -> str:
        return f"Номер камеры: {self.numbercam} \nПуть записи: {self.locrecord} " \
               f"\nСекция в которой находится камера: {self.section.get_numsection()}"
