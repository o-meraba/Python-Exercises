import sys
from PyQt5 import QtWidgets

def MyFirstWindow():

    app = QtWidgets.QApplication(sys.argv)

    myWindow = QtWidgets.QWidget()
    myWindow.setWindowTitle("PyQt5 Lesson 1")

    myWindow.show()

    sys.exit(app.exec_())

MyFirstWindow()