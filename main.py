#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem

answers = ['', '', '']


class Form1(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form1, self).__init__()
        uic.loadUi('uis/form1.ui', self)
        self.button_exit.clicked.connect(self.close)
        self.button_start.clicked.connect(self.next)

    def next(self):
        self.switch_window.emit('1>2')


class Form2(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form2, self).__init__()
        uic.loadUi('uis/form2.ui', self)

        if answers[0] is not None:
            self.label_selected.setText('Выбрано: ' + answers[0])

        self.listWidget.itemClicked.connect(self.item_click)
        self.button_back.clicked.connect(self.back)
        self.button_next.clicked.connect(self.next)

    def item_click(self, item):
        answers[0] = item.text()
        self.label_selected.setText('Выбрано: ' + answers[0])

    def back(self):
        self.switch_window.emit('1<2')

    def next(self):
        self.switch_window.emit('2>3')


class Form3(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form3, self).__init__()
        uic.loadUi('uis/form3.ui', self)

        if answers[1] is not None:
            self.label_selected.setText('Выбрано: ' + answers[1])

        self.comboBox.activated.connect(self.handleActivated)
        self.button_back.clicked.connect(self.back)
        self.button_next.clicked.connect(self.next)

    def handleActivated(self, index):
        answers[1] = self.comboBox.itemText(index)
        self.label_selected.setText('Выбрано: ' + answers[1])

    def back(self):
        self.switch_window.emit('2<3')

    def next(self):
        self.switch_window.emit('3>4')


class Form4(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form4, self).__init__()
        uic.loadUi('uis/form4.ui', self)

        self.radioButton_1.toggled.connect(
            lambda: self.onToggled(self.radioButton_1))
        self.radioButton_2.toggled.connect(
            lambda: self.onToggled(self.radioButton_2))
        self.radioButton_3.toggled.connect(
            lambda: self.onToggled(self.radioButton_3))
        self.radioButton_4.toggled.connect(
            lambda: self.onToggled(self.radioButton_4))

        self.button_back.clicked.connect(self.back)
        self.button_next.clicked.connect(self.next)

    def onToggled(self, radiobutton):
        if radiobutton.isChecked():
            answers[2] = radiobutton.text()
            self.label_selected.setText('Выбрано: ' + answers[2])

    def back(self):
        self.switch_window.emit('3<4')

    def next(self):
        self.switch_window.emit('4>5')


class Form5(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form5, self).__init__()
        uic.loadUi('uis/form5.ui', self)
        self.tableWidget.setItem(0, 1, QTableWidgetItem(answers[0]))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(answers[1]))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(answers[2]))

        self.button_back.clicked.connect(self.back)
        self.button_exit.clicked.connect(self.close)

    def back(self):
        self.switch_window.emit("4<5")


class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()

        if text == '1>2':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = Form5()
            self.form5.switch_window.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '4<5':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '3<4':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '2<3':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form3.close()

        if text == '1<2':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec())
