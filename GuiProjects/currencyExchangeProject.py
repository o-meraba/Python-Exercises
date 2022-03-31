import requests
from bs4 import BeautifulSoup
import sys
from PyQt5 import QtWidgets

def request_exchange_datas():  # take exchange datas from doviz.com
    url = "https://www.doviz.com/"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    exchange_datas = soup.find_all("div", attrs={'class': 'item'})

    name_value = []
    for i in exchange_datas:
        name = str(i.find("span",attrs={'class':'name'}).text)
        value = str(i.find("span", attrs={'class': 'value'}).text)
        name_value.append((name,value))

    for i in name_value:
        print("Name:",i[0], "Value:", i[1])


request_exchange_datas()

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.dollar_name = QtWidgets.QLabel("Dollar")
        self.dollar_value = QtWidgets.QLabel("DollarValue")

        self.euro_name = QtWidgets.QLabel("Euro")
        self.euro_value = QtWidgets.QLabel("EuroValue")

        self.gold_name = QtWidgets.QLabel("Gold")
        self.gold_value = QtWidgets.QLabel("GoldValue")

        self.silver_name = QtWidgets.QLabel("Silver")
        self.silver_value = QtWidgets.QLabel("SilverValue")

        self.sterlin_name = QtWidgets.QLabel("Sterlin")
        self.sterlin_value = QtWidgets.QLabel("SterlinValue")

        self.bitcoin_name = QtWidgets.QLabel("Bitcoin")
        self.bitcoin_value = QtWidgets.QLabel("BitcoinValue")

        h_dollar_box = QtWidgets.QHBoxLayout()
        h_dollar_box.addWidget(self.dollar_name)
        h_dollar_box.addWidget(self.dollar_value)

        h_euro_box = QtWidgets.QHBoxLayout()
        h_euro_box.addWidget(self.euro_name)
        h_euro_box.addWidget(self.euro_value)

        h_sterlin_box = QtWidgets.QHBoxLayout()
        h_sterlin_box.addWidget(self.sterlin_name)
        h_sterlin_box.addWidget(self.sterlin_value)

        h_gold_box = QtWidgets.QHBoxLayout()
        h_gold_box.addWidget(self.gold_name)
        h_gold_box.addWidget(self.gold_value)

        h_silver_box = QtWidgets.QHBoxLayout()
        h_silver_box.addWidget(self.silver_name)
        h_silver_box.addWidget(self.silver_value)

        h_bitcoin_box = QtWidgets.QHBoxLayout()
        h_bitcoin_box.addWidget(self.bitcoin_name)
        h_bitcoin_box.addWidget(self.bitcoin_value)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_gold_box)
        v_box.addLayout(h_dollar_box)
        v_box.addLayout(h_euro_box)
        v_box.addLayout(h_sterlin_box)
        v_box.addLayout(h_bitcoin_box)
        v_box.addLayout(h_silver_box)

        v_box.addStretch()

        self.setWindowTitle("Exchange Currency Values")
        self.setGeometry(100,100,300,300)
        self.setLayout(v_box)
        self.show()

def windowShow():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowClass()
    sys.exit(app.exec_())

windowShow()