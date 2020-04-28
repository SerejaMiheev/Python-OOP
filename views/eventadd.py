# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventAdd(object):
    def setupUi(self, EventAdd):
        EventAdd.setObjectName("EventAdd")
        EventAdd.resize(372, 121)
        EventAdd.setMinimumSize(QtCore.QSize(372, 121))
        EventAdd.setMaximumSize(QtCore.QSize(372, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        EventAdd.setFont(font)
        self.label = QtWidgets.QLabel(EventAdd)
        self.label.setGeometry(QtCore.QRect(10, 5, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EventAdd)
        self.label_2.setGeometry(QtCore.QRect(12, 45, 71, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(EventAdd)
        self.comboBox.setGeometry(QtCore.QRect(80, 12, 281, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(EventAdd)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 50, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(EventAdd)
        self.pushButton.setGeometry(QtCore.QRect(190, 80, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(EventAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 80, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(EventAdd)
        QtCore.QMetaObject.connectSlotsByName(EventAdd)

    def retranslateUi(self, EventAdd):
        _translate = QtCore.QCoreApplication.translate
        EventAdd.setWindowTitle(_translate("EventAdd", "Event"))
        self.label.setText(_translate("EventAdd", "Человек:"))
        self.label_2.setText(_translate("EventAdd", "Камера:"))
        self.pushButton.setText(_translate("EventAdd", "Создать"))
        self.pushButton_2.setText(_translate("EventAdd", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EventAdd = QtWidgets.QDialog()
    ui = Ui_EventAdd()
    ui.setupUi(EventAdd)
    EventAdd.show()
    sys.exit(app.exec_())
