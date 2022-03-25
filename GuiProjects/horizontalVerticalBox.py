import sys

from PyQt5 import QtWidgets


def WindowFunction():

    app = QtWidgets.QApplication(sys.argv)

    okayButton = QtWidgets.QPushButton("Okay")
    cancelButton = QtWidgets.QPushButton("Cancel")

    h_box = QtWidgets.QHBoxLayout()
    #h_box.addStretch() # leaving space for left
    h_box.addWidget(okayButton)
    #h_box.addStretch() # leaving space for between buttons
    h_box.addWidget(cancelButton)
    h_box.addStretch() # leaving space for right

    window = QtWidgets.QWidget()
    window.setWindowTitle("Horizontal And Vertical Box")

    window.setLayout(h_box)

    window.setGeometry(100,100,500,500)
    window.show()
    sys.exit(app.exec_())



WindowFunction()