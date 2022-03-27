import os
import sys
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.text_area = QtWidgets.QTextEdit()
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.open_button = QtWidgets.QPushButton("Open")
        self.save_button = QtWidgets.QPushButton("Save")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.clear_button)
        h_box.addWidget(self.open_button)
        h_box.addWidget(self.save_button)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)

        self.clear_button.clicked.connect(self.clear_func)
        self.open_button.clicked.connect(self.open_func)
        self.save_button.clicked.connect(self.save_func)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")
        self.show()

    def clear_func(self):
        self.text_area.clear()

    def open_func(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        with open(file_name[0],"r") as file:
            self.text_area.setText(file.read())

    def save_func(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
        with open(file_name[0],"w") as file:
            file.write(self.text_area.toPlainText())

app = QtWidgets.QApplication(sys.argv)
window = WindowClass()
sys.exit(app.exec_())