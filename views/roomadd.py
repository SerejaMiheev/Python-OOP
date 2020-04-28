# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'roomadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RoomAdd(object):
    def setupUi(self, RoomAdd):
        RoomAdd.setObjectName("RoomAdd")
        RoomAdd.resize(210, 521)
        RoomAdd.setMinimumSize(QtCore.QSize(210, 521))
        RoomAdd.setMaximumSize(QtCore.QSize(210, 521))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        RoomAdd.setFont(font)
        self.label = QtWidgets.QLabel(RoomAdd)
        self.label.setGeometry(QtCore.QRect(10, 5, 71, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(RoomAdd)
        self.lineEdit.setGeometry(QtCore.QRect(80, 11, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(RoomAdd)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(RoomAdd)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 71, 31))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(RoomAdd)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 191, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(RoomAdd)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 290, 191, 181))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton = QtWidgets.QPushButton(RoomAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 480, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(RoomAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 480, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(RoomAdd)
        QtCore.QMetaObject.connectSlotsByName(RoomAdd)

    def retranslateUi(self, RoomAdd):
        _translate = QtCore.QCoreApplication.translate
        RoomAdd.setWindowTitle(_translate("RoomAdd", "Room"))
        self.label.setText(_translate("RoomAdd", "Комната:"))
        self.label_2.setText(_translate("RoomAdd", "Оборудование:"))
        self.label_3.setText(_translate("RoomAdd", "Камеры:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RoomAdd", "Название"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("RoomAdd", "Номер"))
        self.pushButton.setText(_translate("RoomAdd", "Добавить"))
        self.pushButton_2.setText(_translate("RoomAdd", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RoomAdd = QtWidgets.QDialog()
    ui = Ui_RoomAdd()
    ui.setupUi(RoomAdd)
    RoomAdd.show()
    sys.exit(app.exec_())
