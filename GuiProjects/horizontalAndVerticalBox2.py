import sys
from PyQt5 import QtWidgets



def WindowFunction():

    app = QtWidgets.QApplication(sys.argv)

    okayButton = QtWidgets.QPushButton("Okay")
    cancelButton = QtWidgets.QPushButton("Cancel")
    addButton = QtWidgets.QPushButton("Add")
    deleteButton = QtWidgets.QPushButton("Delete")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addWidget(okayButton)
    h_box.addWidget(cancelButton)
    h_box.addStretch()
    h_box.addWidget(addButton)
    h_box.addWidget(deleteButton)
    #h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    window = QtWidgets.QWidget()
    window.setWindowTitle("Horizontal and Vertical Box 2")
    window.setLayout(v_box)
    window.setGeometry(100,100,500,500)
    window.show()


    sys.exit(app.exec_())



WindowFunction()
