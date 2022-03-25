import sys
import sqlite3
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db_connecting()
        self.ui_init()

    def ui_init(self):

        self.setWindowTitle("Register Page")
        v_box = QtWidgets.QVBoxLayout()
        self.user_name = QtWidgets.QLineEdit("")
        self.user_password = QtWidgets.QLineEdit("")
        self.user_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_button = QtWidgets.QPushButton("Register")
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.user_name_label = QtWidgets.QLabel("User Name")
        self.user_password_label = QtWidgets.QLabel("User Password")
        self.exit_button = QtWidgets.QPushButton("Exit")


        self.setGeometry(500,500,500,250)


        h_userBox = QtWidgets.QHBoxLayout()
        h_passwordBox = QtWidgets.QHBoxLayout()
        h_registerCleanBox = QtWidgets.QHBoxLayout()

        h_userBox.addWidget(self.user_name_label)
        h_userBox.addStretch()
        h_userBox.addWidget(self.user_name)

        h_passwordBox.addWidget(self.user_password_label)
        h_passwordBox.addStretch()
        h_passwordBox.addWidget(self.user_password)

        h_registerCleanBox.addWidget(self.register_button)
        h_registerCleanBox.addWidget(self.clear_button)
        h_registerCleanBox.addWidget(self.exit_button)

        v_box.addLayout(h_userBox)
        v_box.addLayout(h_passwordBox)
        v_box.addStretch()
        v_box.addLayout(h_registerCleanBox)
        self.setLayout(v_box)

        self.register_button.clicked.connect(self.register_func)
        self.clear_button.clicked.connect(self.clear_func)
        self.exit_button.clicked.connect(self.exit_func)
        self.show()

    def exit_func(self):
        self.con.close()
        sys.exit(app.exec_())
    def db_connecting(self):
        self.con = sqlite3.connect("members_db.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS members(username TEXT, password TEXT)")
        self.con.commit()


    def register_func(self):
        user_name_data = self.user_name.text()
        user_password_data = self.user_password.text()
        self.cursor.execute("INSERT INTO members(username, password) VALUES(?,?)",(user_name_data,user_password_data))
        self.con.commit()
        data = self.cursor.fetchall()
        for i in data:
            print(data)


    def clear_func(self):
        self.user_name.clear()
        self.user_password.clear()
app = QtWidgets.QApplication(sys.argv)
window = WindowClass()

sys.exit(app.exec_())
