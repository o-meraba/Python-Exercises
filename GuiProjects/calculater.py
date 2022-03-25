import sys

from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        button1 = QtWidgets.QPushButton()
        button1.setText("1")

        button2 = QtWidgets.QPushButton()
        button2.setText("2")

        button3 = QtWidgets.QPushButton()
        button3.setText("3")

        button4 = QtWidgets.QPushButton()
        button4.setText("4")

        button5 = QtWidgets.QPushButton()
        button5.setText("5")

        button6 = QtWidgets.QPushButton()
        button6.setText("6")

        button7 = QtWidgets.QPushButton()
        button7.setText("7")

        button8 = QtWidgets.QPushButton()
        button8.setText("8")

        button9 = QtWidgets.QPushButton()
        button9.setText("9")

        button0 = QtWidgets.QPushButton()
        button0.setText("0")

        buttonSum = QtWidgets.QPushButton()
        buttonSum.setText("+")

        buttonMinus = QtWidgets.QPushButton()
        buttonMinus.setText("-")

        buttonDivide = QtWidgets.QPushButton()
        buttonDivide.setText("/")

        buttonMultiple = QtWidgets.QPushButton()
        buttonMultiple.setText("*")

        buttonEqual = QtWidgets.QPushButton()
        buttonEqual.setText("=")

        textArea = QtWidgets.QTextEdit()
        buttonEnter = QtWidgets.QPushButton()
        buttonDelete = QtWidgets.QPushButton()


        #h0_box = QtWidgets.QHBoxLayout(self.window())
        #h1_box = QtWidgets.QHBoxLayout(self.window())
        h2_box = QtWidgets.QHBoxLayout(self.window())
        h3_box = QtWidgets.QHBoxLayout(self.window())
        h4_box = QtWidgets.QHBoxLayout(self.window())
        #h5_box = QtWidgets.QHBoxLayout(self.window())
        v_box = QtWidgets.QVBoxLayout(self.window())

        #h5_box.addWidget(textArea)
        #h5_box.addWidget(buttonEnter)
        #h5_box.addWidget(buttonDelete)
        # h0_box.addWidget(buttonSum)
        # h0_box.addWidget(buttonMinus)
        # h0_box.addWidget(buttonMultiple)
        # h0_box.addWidget(buttonDivide)
        # h1_box.addWidget(button1)
        # h1_box.addWidget(button2)
        # h1_box.addWidget(button3)
        # h2_box.addWidget(button4)
        # h2_box.addWidget(button5)
        h2_box.addWidget(button6)
        h3_box.addWidget(button7)
        h3_box.addWidget(button8)
        h3_box.addWidget(button9)
        #h4_box.addStretch()
        h4_box.addWidget(button0)
        #h4_box.addStretch()


        #v_box.addStretch()
        #v_box.addLayout(h5_box)
        # v_box.addLayout(h0_box)
        # v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        #v_box.addLayout(h4_box)
        self.setLayout(v_box)

        self.show()


def windowFunction():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowClass()
    window.setWindowTitle("Calculater")
    window.setGeometry(100,100,500,500)
    sys.exit(app.exec_())

windowFunction()