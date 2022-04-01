
from PyQt5 import QtWidgets
import sys
from sendMailProject import *

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
    def ui_init(self):
        self.mail_receiver_label = QtWidgets.QLabel("Receiver Address")
        self.mail_receiver_textLine = QtWidgets.QLineEdit()

        self.mail_subject_label = QtWidgets.QLabel("Subject")
        self.mail_subject_textLine = QtWidgets.QLineEdit()

        self.mail_text_label = QtWidgets.QLabel("Text")
        self.mail_text_textLine = QtWidgets.QTextEdit()

        self.send_button = QtWidgets.QPushButton("Send")
        self.clear_button = QtWidgets.QPushButton("Clear")

        h_box_receiver_addr = QtWidgets.QHBoxLayout()
        h_box_receiver_addr.addWidget(self.mail_receiver_label)
        h_box_receiver_addr.addWidget(self.mail_receiver_textLine)

        h_box_subject = QtWidgets.QHBoxLayout()
        h_box_subject.addWidget(self.mail_subject_label)
        h_box_subject.addWidget(self.mail_subject_textLine)

        h_box_bodyText = QtWidgets.QHBoxLayout()
        h_box_bodyText.addWidget(self.mail_text_label)
        h_box_bodyText.addWidget(self.mail_text_textLine)

        h_box_tasks = QtWidgets.QHBoxLayout()
        h_box_tasks.addWidget(self.send_button)
        h_box_tasks.addWidget(self.clear_button)


        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box_receiver_addr)
        v_box.addLayout(h_box_subject)
        v_box.addLayout(h_box_bodyText)
        v_box.addLayout(h_box_tasks)

        self.clear_button.clicked.connect(self.clear_func)
        self.send_button.clicked.connect(self.mail_send_func)

        self.setLayout(v_box)
        self.setWindowTitle("Mail Send Program")
        self.show()


    def clear_func(self):
        self.mail_receiver_textLine.clear()
        self.mail_subject_textLine.clear()
        self.mail_text_textLine.clear()

    def mail_send_func(self):
        sending_mail(self.mail_receiver_textLine.text(), self.mail_subject_textLine.text(), self.mail_text_textLine.toPlainText())
        sys.exit(app.exec_())


app = QtWidgets.QApplication(sys.argv)
window = WindowClass()
sys.exit(app.exec_())