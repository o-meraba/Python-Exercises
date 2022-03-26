import sys
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.check_box = QtWidgets.QCheckBox("Do you like Python?")
        self.check_label = QtWidgets.QLabel("")
        self.check_button = QtWidgets.QPushButton("click me")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.check_box)
        v_box.addWidget(self.check_label)
        v_box.addWidget(self.check_button)
        self.check_button.clicked.connect(self.button_check_func)

        self.setLayout(v_box)

        self.show()
        self.setWindowTitle("Check Box")
    def button_check_func(self):
        if self.check_box.isChecked() == True:
            self.check_label.setText("Supeeeeer")
        else:
            self.check_label.setText("But Whyyy???")


app = QtWidgets.QApplication(sys.argv)
window = WindowClass()

sys.exit(app.exec_())

