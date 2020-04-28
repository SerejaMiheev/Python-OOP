from PyQt5.QtWidgets import QDialog

from controllers.cameracontroller import CameraController
from controllers.eventcontroller import EventController
from controllers.personcontroller import PersonController
from views.eventadd import Ui_EventAdd


class EventAddDialog(QDialog):
    def __init__(self, event_controller: EventController):
        super(EventAddDialog, self).__init__()
        self.event_controller = event_controller
        self.event_d = event_controller.get_dict()
        self.camera_controller = CameraController()
        self.person_controller = PersonController()
        self.initUI()

    def initUI(self):
        self.ui = Ui_EventAdd()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("Отсутствует")

        persons = self.person_controller.get_persons()
        for i in persons:
            self.ui.comboBox.addItem(i['fio'], i['id'])

        cameras = self.camera_controller.get_cameras()
        for i in cameras:
            self.ui.comboBox_2.addItem(str(i['id']))

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_add(self):
        if(self.ui.comboBox.currentText() == "Отсутствует"):
            self.event_d['camera'] = int(self.ui.comboBox_2.currentText())
            new_d = self.event_controller.new_event(self.event_d)
            self.event_d['id'] = new_d['id']
            self.event_d['date'] = new_d['date']
            self.event_controller.set_dict(self.event_d)
            self.accept()

        else:
            self.event_d['person'] = self.ui.comboBox.currentData()
            self.event_d['camera'] = int(self.ui.comboBox_2.currentText())
            new_d = self.event_controller.new_event(self.event_d)
            self.event_d['id'] = new_d['id']
            self.event_d['date'] = new_d['date']
            self.event_controller.set_dict(self.event_d)
            self.accept()

    def click_cancel(self):
        self.reject()
