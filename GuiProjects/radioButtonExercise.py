import sys
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):

        self.radio_text = QtWidgets.QLabel("Which Programming Language do you like?")
        self.radio_java = QtWidgets.QRadioButton("Java")
        self.radio_php = QtWidgets.QRadioButton("PHP")
        self.radio_python = QtWidgets.QRadioButton("Python")
        self.send_button = QtWidgets.QPushButton("Send")
        self.text_label = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.radio_text)
        v_box.addWidget(self.radio_java)
        v_box.addWidget(self.radio_php)
        v_box.addWidget(self.radio_python)
        v_box.addWidget(self.text_label)
        v_box.addWidget(self.send_button)


        self.setLayout(v_box)

        self.send_button.clicked.connect(lambda : self.click_func(self.radio_java.isChecked(),self.radio_php.isChecked(),self.radio_python.isChecked(),self.text_label))

        self.setWindowTitle("Radio Button Exercise")
        self.show()

    def click_func(self,radio_java,radio_php,radio_python,text_label):
        if radio_java:
            text_label.setText("JAVA")
        if radio_php:
            text_label.setText("PHP")
        if radio_python:
            text_label.setText("PYTHON")





app = QtWidgets.QApplication(sys.argv)

window = WindowClass()

sys.exit(app.exec_())