import sys
import os
from PyQt5 import QtWidgets

class WindowClass(QtWidgets.QWidget): # Created a class for Window
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self): # created a initial func for user interface

        self.clear_button = QtWidgets.QPushButton("Clear")
        self.save_button = QtWidgets.QPushButton("Save")
        self.open_button = QtWidgets.QPushButton("Open")
        self.exit_button = QtWidgets.QPushButton("Exit")
        self.text_edit_area = QtWidgets.QTextEdit()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.clear_button)
        h_box.addWidget(self.open_button)
        h_box.addWidget(self.save_button)
        h_box.addWidget(self.exit_button)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_edit_area)
        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.clear_button.clicked.connect(self.clear_textArea_func)
        self.exit_button.clicked.connect(self.exit_func)
        self.open_button.clicked.connect(self.open_file_func)
        self.save_button.clicked.connect(self.save_file_func)

    def open_file_func(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        with open(file_name[0],"r") as file:
            self.text_edit_area.setText(file.read())

    def clear_textArea_func(self):
        self.text_edit_area.clear()

    def save_file_func(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
        with open(file_name[0],"w") as file:
            file.write(self.text_edit_area.toPlainText())

    def exit_func(self):
        QtWidgets.qApp.quit()

class MenuClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = WindowClass()
        self.setCentralWidget(self.window)
        self.setWindowTitle("My NotePad")
        self.setGeometry(100, 100, 300, 200)
        self.show()

        self.create_menus()

    def create_menus(self):
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("File")
        menu_edit = menu_bar.addMenu("Edit")

        open_file = QtWidgets.QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QtWidgets.QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clear_textArea = QtWidgets.QAction("Clear",self)
        clear_textArea.setShortcut("Ctrl+D")

        exit_app = QtWidgets.QAction("Exit",self)
        exit_app.setShortcut("Ctrl+Q")

        menu_file.addAction(open_file)
        menu_file.addAction(save_file)
        menu_file.addAction(clear_textArea)
        menu_file.addAction(exit_app)


        menu_file.triggered.connect(self.response)

    def response(self,action):
        if action.text() == "Open File" :
            self.window.open_file_func()
        elif action.text() == "Save File":
            self.window.save_file_func()
        elif action.text() == "Exit":
            self.window.exit_func()
        elif action.text() == "Clear":
            self.window.clear_textArea_func()




app = QtWidgets.QApplication(sys.argv)
menu = MenuClass()
sys.exit(app.exec_())
