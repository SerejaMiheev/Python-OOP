# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flooradd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FloorAdd(object):
    def setupUi(self, FloorAdd):
        FloorAdd.setObjectName("FloorAdd")
        FloorAdd.resize(210, 521)
        FloorAdd.setMinimumSize(QtCore.QSize(210, 521))
        FloorAdd.setMaximumSize(QtCore.QSize(210, 521))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        FloorAdd.setFont(font)
        self.label = QtWidgets.QLabel(FloorAdd)
        self.label.setGeometry(QtCore.QRect(10, 5, 61, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(FloorAdd)
        self.lineEdit.setGeometry(QtCore.QRect(60, 12, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(FloorAdd)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FloorAdd)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 71, 31))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(FloorAdd)
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
        self.tableWidget_2 = QtWidgets.QTableWidget(FloorAdd)
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
        self.pushButton = QtWidgets.QPushButton(FloorAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 480, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(FloorAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 480, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(FloorAdd)
        QtCore.QMetaObject.connectSlotsByName(FloorAdd)

    def retranslateUi(self, FloorAdd):
        _translate = QtCore.QCoreApplication.translate
        FloorAdd.setWindowTitle(_translate("FloorAdd", "Floor"))
        self.label.setText(_translate("FloorAdd", "Этаж:"))
        self.label_2.setText(_translate("FloorAdd", "Комнаты:"))
        self.label_3.setText(_translate("FloorAdd", "Камеры:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FloorAdd", "Номер"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("FloorAdd", "Номер"))
        self.pushButton.setText(_translate("FloorAdd", "Добавить"))
        self.pushButton_2.setText(_translate("FloorAdd", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FloorAdd = QtWidgets.QDialog()
    ui = Ui_FloorAdd()
    ui.setupUi(FloorAdd)
    FloorAdd.show()
    sys.exit(app.exec_())
