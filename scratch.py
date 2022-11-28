import sys

import requests

import Parser
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QGroupBox, QTextBrowser,
                             QPushButton, QProgressBar, QRadioButton, QButtonGroup)
from PyQt5 import QtGui, QtWebEngineWidgets

class Form(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.parser = Parser.Parser()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        font = QtGui.QFont()
        font.setPointSize(12)
        bold_font = QtGui.QFont()
        bold_font.setPointSize(12)
        bold_font.setBold(True)

        num_case_label = QLabel('Номер дела :')
        num_case_label.setFont(font)
        grid.addWidget(num_case_label, 0, 0, 1, 1)

        self.num_case_field = QLineEdit()
        self.num_case_field.setFont(font)
        grid.addWidget(self.num_case_field, 0, 1, 1, 2)

        year_label = QLabel('Год :')
        year_label.setFont(font)
        grid.addWidget(year_label, 0, 3, 1, 1)

        self.year_field = QLineEdit('2022')
        self.year_field.setFont(font)
        grid.addWidget(self.year_field, 0, 4, 1, 2)

        proceedings_groupbox = QGroupBox('Производство')
        proceedings_groupbox.setFont(font)
        grid.addWidget(proceedings_groupbox, 0, 6, 4, 1)

        self.adm_radio = QRadioButton('Административное')
        self.adm_radio.setChecked(True)
        self.civil_radio = QRadioButton('Гражданское')
        self.crime_radio = QRadioButton('Уголовное')

        proceedings_groupbox_layout = QGridLayout()
        proceedings_groupbox_layout.addWidget(self.adm_radio, 0, 0, 1, 1)
        proceedings_groupbox_layout.addWidget(self.civil_radio, 1, 0, 1, 1)
        proceedings_groupbox_layout.addWidget(self.crime_radio, 2, 0, 1, 1)
        proceedings_groupbox.setLayout(proceedings_groupbox_layout)

        search_area_groupbox = QGroupBox('Область поиска')
        search_area_groupbox.setFont(font)
        grid.addWidget(search_area_groupbox, 0, 7, 4, 1)

        self.our_area_radio = QRadioButton('Наши участки')
        self.our_area_radio.setChecked(True)
        self.all_radio = QRadioButton('Весь край')
        self.select_radio = QRadioButton('Выбрать')
        self.select_radio.toggled.connect(self.onChangeArea)

        search_layout = QGridLayout()
        search_layout.addWidget(self.our_area_radio, 0, 0, 1, 1)
        search_layout.addWidget(self.all_radio, 1, 0, 1, 1)
        search_layout.addWidget(self.select_radio, 2, 0, 1, 1)
        search_area_groupbox.setLayout(search_layout)

        person_label = QLabel('Лицо участвующее в деле :')
        person_label.setFont(font)
        grid.addWidget(person_label, 1, 0, 1, 2)

        self.person_field = QLineEdit()
        self.person_field.setFont(font)
        grid.addWidget(self.person_field, 2, 0, 1, 6)

        search_button = QPushButton('Найти')
        search_button.setFont(bold_font)
        grid.addWidget(search_button, 3, 0, 1, 3)
        search_button.clicked.connect(self.search)

        self.search_area_label = QLabel('Область поиска')
        self.search_area_label.setFont(font)
        self.search_area_label.setEnabled(False)
        grid.addWidget(self.search_area_label, 5, 7, 1, 1)

        self.search_area_field = QLineEdit('29-36, 72')
        self.search_area_field.setFont(font)
        self.search_area_field.setEnabled(False)
        grid.addWidget(self.search_area_field, 5, 8, 1, 1)

        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True)
        self.text_browser.setFont(font)
        grid.addWidget(self.text_browser, 6, 0, 1, 9)

        progress_bar = QProgressBar()
        grid.addWidget(progress_bar, 7, 0, 1, 9)

        self.setLayout(grid)

        self.setGeometry(300, 100, 500, 500)
        self.setWindowTitle('Review')
        self.show()

    def onChangeArea(self):
        if self.select_radio.isChecked():
            self.search_area_label.setEnabled(True)
            self.search_area_field.setEnabled(True)
        else:
            self.search_area_label.setEnabled(False)
            self.search_area_field.setEnabled(False)

    def search(self):
        self.text_browser.append('<td nowrap="" title="Для получения справки по делу, нажмите на номер дела"><a href="http://192.168.94.254:8029/cases.php?case_id=2111918&delo_id=1540005">2-1570/2022</a><br/> </td>')
        # self.text_browser.setText(requests.get('http://192.168.94.254:8029/cases.php?case_id=2111918&delo_id=1540005').text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())

