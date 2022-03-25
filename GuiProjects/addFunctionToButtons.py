import sys
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_area = QtWidgets.QLabel("Bana henüz tıklanmadı")
        self.button = QtWidgets.QPushButton("Bana Tıkla")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.button)
        v_box.addWidget(self.text_area)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click) 

        self.show()
    def click(self):
        self.say += 1
        self.text_area.setText("Bana " + str(self.say) + " defa tıklandı.")


app = QtWidgets.QApplication(sys.argv)
window = WindowClass()

sys.exit(app.exec_())

