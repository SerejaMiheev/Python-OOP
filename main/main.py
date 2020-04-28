import sys

from PyQt5 import QtWidgets

from views.mainwin import MainWindow


def window():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
