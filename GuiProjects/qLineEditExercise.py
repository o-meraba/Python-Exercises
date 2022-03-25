import sys
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazı_alani = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdir")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yazı_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addStretch()

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.clickFunc)
        self.yazdir.clicked.connect(self.clickFunc)



        self.show()

    def clickFunc(self):
        sender = self.sender()
        if sender.text() == "Temizle":
            self.yazı_alani.clear()
        else:
            print(self.yazı_alani.text())

app = QtWidgets.QApplication(sys.argv)
window = WindowClass()
sys.exit(app.exec_())
