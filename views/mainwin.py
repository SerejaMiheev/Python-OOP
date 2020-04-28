from PyQt5.QtWidgets import QMainWindow

from views.camerawin import CameraDialog
from views.equipmentswin import EquipmentsDialog
from views.eventwin import EventDialog
from views.floorwin import FloorDialog
from views.mainwindow import Ui_MainWindow
from views.personwin import PersonDialog
from views.roomwin import RoomsDialog
from views.typewin import TypeDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(231, 365)

        self.ui.pushButton.clicked.connect(self.click_event)
        self.ui.pushButton_2.clicked.connect(self.click_type)
        self.ui.pushButton_3.clicked.connect(self.click_equipment)
        self.ui.pushButton_4.clicked.connect(self.click_room)
        self.ui.pushButton_5.clicked.connect(self.click_floor)
        self.ui.pushButton_6.clicked.connect(self.click_camera)
        self.ui.pushButton_7.clicked.connect(self.click_person)

    def click_event(self):
        event_dialog = EventDialog()
        event_dialog.exec()

    def click_type(self):
        type_dialog = TypeDialog()
        type_dialog.exec()

    def click_equipment(self):
        equipments_dialog = EquipmentsDialog()
        equipments_dialog.exec()

    def click_room(self):
        room_dialog = RoomsDialog()
        room_dialog.exec()

    def click_floor(self):
        floor_dialog = FloorDialog()
        floor_dialog.exec()

    def click_camera(self):
        camera_dialog = CameraDialog()
        camera_dialog.exec()

    def click_person(self):
        person_dialog = PersonDialog()
        person_dialog.exec()