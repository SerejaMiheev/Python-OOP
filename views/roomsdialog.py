# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roomsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rooms(object):
    def setupUi(self, Rooms):
        Rooms.setObjectName("Rooms")
        Rooms.resize(331, 301)
        Rooms.setMinimumSize(QtCore.QSize(331, 301))
        Rooms.setMaximumSize(QtCore.QSize(331, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        Rooms.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Rooms)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Rooms)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Rooms)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 10, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(Rooms)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 311, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.pushButton_4 = QtWidgets.QPushButton(Rooms)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 260, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Rooms)
        QtCore.QMetaObject.connectSlotsByName(Rooms)

    def retranslateUi(self, Rooms):
        _translate = QtCore.QCoreApplication.translate
        Rooms.setWindowTitle(_translate("Rooms", "Rooms"))
        self.pushButton.setText(_translate("Rooms", "Добавить"))
        self.pushButton_2.setText(_translate("Rooms", "Редактировать"))
        self.pushButton_3.setText(_translate("Rooms", "Удалить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Rooms", "Комната"))
        self.pushButton_4.setText(_translate("Rooms", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rooms = QtWidgets.QDialog()
    ui = Ui_Rooms()
    ui.setupUi(Rooms)
    Rooms.show()
    sys.exit(app.exec_())
