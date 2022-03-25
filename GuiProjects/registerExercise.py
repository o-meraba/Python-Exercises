import sys
import sqlite3
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):

        self.setWindowTitle("Register Page")
        v_box = QtWidgets.QVBoxLayout()
        self.user_name = QtWidgets.QLineEdit("")
        self.user_password = QtWidgets.QLineEdit("")
        self.register_button = QtWidgets.QPushButton("Register")
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.user_name_label = QtWidgets.QLabel("User Name")
        self.user_password_label = QtWidgets.QLabel("User Password")

        h_userBox = QtWidgets.QHBoxLayout()
        h_passwordBox = QtWidgets.QHBoxLayout()
        h_registerCleanBox = QtWidgets.QHBoxLayout()

        h_userBox.addWidget(self.user_name_label)
        h_userBox.addWidget(self.user_name)

        h_passwordBox.addWidget(self.user_password_label)
        h_passwordBox.addWidget(self.user_password)

        h_registerCleanBox.addWidget(self.register_button)
        h_registerCleanBox.addWidget(self.clear_button)

        v_box.addLayout(h_userBox)
        v_box.addLayout(h_passwordBox)
        v_box.addLayout(h_registerCleanBox)
        self.setLayout(v_box)

        self.show()


app = QtWidgets.QApplication(sys.argv)
window = WindowClass()

sys.exit(app.exec_())