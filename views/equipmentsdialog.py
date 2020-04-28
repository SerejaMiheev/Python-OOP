# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equipmentsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Equipments(object):
    def setupUi(self, Equipments):
        Equipments.setObjectName("Equipments")
        Equipments.resize(331, 301)
        Equipments.setMinimumSize(QtCore.QSize(331, 301))
        Equipments.setMaximumSize(QtCore.QSize(331, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        Equipments.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Equipments)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Equipments)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Equipments)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 10, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(Equipments)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 311, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_4 = QtWidgets.QPushButton(Equipments)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 260, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Equipments)
        QtCore.QMetaObject.connectSlotsByName(Equipments)

    def retranslateUi(self, Equipments):
        _translate = QtCore.QCoreApplication.translate
        Equipments.setWindowTitle(_translate("Equipments", "Equipments"))
        self.pushButton.setText(_translate("Equipments", "Добавить"))
        self.pushButton_2.setText(_translate("Equipments", "Редактировать"))
        self.pushButton_3.setText(_translate("Equipments", "Удалить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Equipments", "Тип"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Equipments", "Кол-во"))
        self.pushButton_4.setText(_translate("Equipments", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Equipments = QtWidgets.QDialog()
    ui = Ui_Equipments()
    ui.setupUi(Equipments)
    Equipments.show()
    sys.exit(app.exec_())
