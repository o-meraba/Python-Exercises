import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("File")
        menu_edit = menu_bar.addMenu("Edit")

        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")
        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")
        file_exit = QAction("Exit",self)
        file_exit.setShortcut("Ctrl+Q")

        menu_file.addAction(open_file)
        menu_file.addAction(save_file)
        menu_file.addAction(file_exit)

        find_and_change = menu_edit.addMenu("Find and Change")
        find = QAction("Find",self)
        find_and_change.addAction(find)
        find.setShortcut("Ctrl+F")
        change = QAction("Change",self)
        find_and_change.addAction(change)
        change.setShortcut("Ctrl+R")

        clear = QAction("Clear",self)
        menu_edit.addAction(clear)

        file_exit.triggered.connect(self.do_exit_func)
        menu_file.triggered.connect(self.response_func)
        self.setGeometry(200,200,300,200)
        self.setWindowTitle("The Menu")
        self.show()
    def do_exit_func(self):
        qApp.quit()

    def response_func(self,action):
        if action.text() == "Open File" :
            print("Clicked File Open")
        elif action.text() == "Save File" :
            print("Clicked Save File")
        elif action.text() == "Exit" :
            print("Clicked Exit")



app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())