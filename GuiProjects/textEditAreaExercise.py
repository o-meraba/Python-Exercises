import sys
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def clear_func(self):
        self.text_area.clear()
    def ui_init(self):

        self.text_area = QtWidgets.QTextEdit()
        self.clear_button = QtWidgets.QPushButton("Clear")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.clear_button)

        self.clear_button.clicked.connect(self.clear_func)

        self.setLayout(v_box)
        self.setWindowTitle("Text Edit Area")
        self.show()




app = QtWidgets.QApplication(sys.argv)
window = WindowClass()
sys.exit(app.exec_())