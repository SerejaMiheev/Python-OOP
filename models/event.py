from datetime import datetime

from models.camera import Camera
from models.person import Person


class Event:
    FORMAT = "%Y-%m-%d-%H.%M.%S"

    def __init__(self, camera: Camera = None, person: Person = None) -> None:
        self.date = datetime.today()
        self.camera = camera
        self.person = person
        self.record = camera.get_locrecord()

    def set_record(self, record: str) -> None:
        self.record = record

    def set_camera(self, camera: Camera) -> None:
        self.camera = camera

    def set_person(self, person: Person) -> None:
        self.person = person

    def get_record(self) -> str:
        return self.record

    def get_camera(self) -> Camera:
        return self.camera

    def get_person(self) -> Person:
        return self.person

    def get_date(self) -> datetime:
        return self.date

    def __str__(self) -> str:
        return f"Дата и время наступления события: {self.date.strftime(Event.FORMAT)} \nЧеловек: {self.person} " \
               f"\nКамера: {self.camera} \nЗапись события: {self.record}"