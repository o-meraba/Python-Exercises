import sys

from PyQt5 import QtWidgets,QtGui

def MyWindowFunction():

    app = QtWidgets.QApplication(sys.argv)

    myWindow = QtWidgets.QWidget()
    myWindow.setWindowTitle("Add Text and Picture")

    firstLabel = QtWidgets.QLabel(myWindow)
    secondLabel = QtWidgets.QLabel(myWindow)
    secondLabel.setPixmap(QtGui.QPixmap("pythonPngImage"))

    secondLabel.move(90,50)

    firstLabel.setText("This is a text")
    firstLabel.move(200,30)

    myWindow.setGeometry(100,100,500,500)
    myWindow.show()



    sys.exit(app.exec_())

MyWindowFunction()