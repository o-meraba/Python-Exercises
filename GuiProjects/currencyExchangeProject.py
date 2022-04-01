import time

import requests
from bs4 import BeautifulSoup
import sys
from PyQt5 import QtWidgets
import os

class WindowClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.request_exchange_datas()
        self.ui_init()

    def ui_init(self):
        self.dollar_name = QtWidgets.QLabel("Dollar")
        self.dollar_value = QtWidgets.QLabel(self.name_value_dict['DOLAR'])

        self.euro_name = QtWidgets.QLabel("Euro")
        self.euro_value = QtWidgets.QLabel(self.name_value_dict['EURO'])

        self.gold_name = QtWidgets.QLabel("Gold")
        self.gold_value = QtWidgets.QLabel(self.name_value_dict['GRAM ALTIN'])

        self.silver_name = QtWidgets.QLabel("Silver")
        self.silver_value = QtWidgets.QLabel(self.name_value_dict['GÜMÜŞ'])

        self.sterlin_name = QtWidgets.QLabel("Sterlin")
        self.sterlin_value = QtWidgets.QLabel(self.name_value_dict['STERLİN'])

        self.bitcoin_name = QtWidgets.QLabel("Bitcoin")
        self.bitcoin_value = QtWidgets.QLabel(self.name_value_dict['BITCOIN'])

        self.amount_label = QtWidgets.QLabel("Amount")
        self.amount_textLine = QtWidgets.QLineEdit()

        self.from_currency = QtWidgets.QLabel("From Currency")
        self.from_currency_options = QtWidgets.QComboBox()
        self.from_currency_options.addItems(["Dollar","Euro","Sterlin","Gold","Silver","Bitcoin","Turkish Lira"])


        self.to_currency = QtWidgets.QLabel("To Currency")
        self.to_currency_options = QtWidgets.QComboBox()
        self.to_currency_options.addItems(["Turkish Lira","Dollar","Euro","Sterlin","Gold","Silver","Bitcoin"])

        self.convert_button = QtWidgets.QPushButton("Convert")
        self.result_label = QtWidgets.QLabel("Result")
        self.result_conv = QtWidgets.QLabel()

        h_result_box = QtWidgets.QHBoxLayout()
        h_result_box.addWidget(self.result_label)
        h_result_box.addWidget(self.result_conv)

        h_amount_box = QtWidgets.QHBoxLayout()
        h_amount_box.addWidget(self.amount_label)
        h_amount_box.addWidget(self.amount_textLine)

        h_from_currency_opt = QtWidgets.QHBoxLayout()
        h_from_currency_opt.addWidget(self.from_currency)
        h_from_currency_opt.addWidget(self.from_currency_options)

        h_to_currency_opt = QtWidgets.QHBoxLayout()
        h_to_currency_opt.addWidget(self.to_currency)
        h_to_currency_opt.addWidget(self.to_currency_options)

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

        self.refresh_button = QtWidgets.QPushButton("Refresh")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_gold_box)
        v_box.addLayout(h_dollar_box)
        v_box.addLayout(h_euro_box)
        v_box.addLayout(h_sterlin_box)
        v_box.addLayout(h_bitcoin_box)
        v_box.addLayout(h_silver_box)
        v_box.addStretch()
        v_box.addLayout(h_amount_box)
        v_box.addLayout(h_from_currency_opt)
        v_box.addLayout(h_to_currency_opt)
        v_box.addLayout(h_result_box)
        v_box.addWidget(self.convert_button)
        v_box.addWidget(self.refresh_button)

        self.refresh_button.clicked.connect(self.refresh_func)
        self.convert_button.clicked.connect(self.convert_func)
        self.setWindowTitle("Exchange Currency Values")
        self.setGeometry(100,100,300,300)
        self.setLayout(v_box)
        self.show()

    def refresh_func(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
    def convert_func(self):
        if self.from_currency_options.currentText() == "Dollar" and self.to_currency_options.currentText() == "Turkish Lira" :
            self.result = int(self.amount_textLine.text()) * float(self.dollar_value.text().replace(',','.'))
            self.result_conv.setText(str(round(self.result,3)))
        else:
            pass


    def request_exchange_datas(self):  # take exchange datas from doviz.com
        self.url = "https://www.doviz.com/"
        self.response = requests.get(self.url)
        self.html_content = self.response.content
        self.soup = BeautifulSoup(self.html_content, "html.parser")
        self.exchange_datas = self.soup.find_all("div", attrs={'class': 'item'})

        self.name_value_dict = {}
        for i in self.exchange_datas:
            self.name = str(i.find("span", attrs={'class': 'name'}).text)
            self.value = str(i.find("span", attrs={'class': 'value'}).text)
            self.name_value_dict[self.name] = self.value


def windowShow():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowClass()
    sys.exit(app.exec_())



windowShow()