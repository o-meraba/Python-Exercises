import sys
from PyQt5 import QtWidgets

def windowFunction():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("My District")

    button = QtWidgets.QPushButton(window)
    button.setText("This is a button")
    label = QtWidgets.QLabel(window)
    label.setText("Hello World")
    label.move(160,120)
    button.move(150,150)




    window.setGeometry(100,100,500,500)
    window.show()
    sys.exit(app.exec_())



windowFunction()