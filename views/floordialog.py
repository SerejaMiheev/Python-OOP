# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'floordialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Floor(object):
    def setupUi(self, Floor):
        Floor.setObjectName("Floor")
        Floor.resize(441, 429)
        Floor.setMinimumSize(QtCore.QSize(441, 429))
        Floor.setMaximumSize(QtCore.QSize(441, 429))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        Floor.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Floor)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Floor)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 10, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Floor)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 10, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(Floor)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 421, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_5 = QtWidgets.QPushButton(Floor)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 390, 81, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Floor)
        QtCore.QMetaObject.connectSlotsByName(Floor)
        Floor.setTabOrder(self.pushButton, self.pushButton_4)
        Floor.setTabOrder(self.pushButton_4, self.pushButton_2)

    def retranslateUi(self, Floor):
        _translate = QtCore.QCoreApplication.translate
        Floor.setWindowTitle(_translate("Floor", "Floors"))
        self.pushButton.setText(_translate("Floor", "Добавить"))
        self.pushButton_2.setText(_translate("Floor", "Удалить"))
        self.pushButton_4.setText(_translate("Floor", "Редактировать"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Floor", "Этаж"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Floor", "Кол-во комнат"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Floor", "Кол-во камер"))
        self.pushButton_5.setText(_translate("Floor", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Floor = QtWidgets.QDialog()
    ui = Ui_Floor()
    ui.setupUi(Floor)
    Floor.show()
    sys.exit(app.exec_())
