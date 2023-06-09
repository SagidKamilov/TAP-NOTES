# -*- coding: utf-8 -*-
from sqlite3 import Connection

# Form implementation generated from reading ui file '.\Test_v3_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
import sqlite3
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(934, 729)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.mainlayout = QtWidgets.QSplitter(Form)
        self.mainlayout.setOrientation(QtCore.Qt.Horizontal)
        self.mainlayout.setHandleWidth(0)
        self.mainlayout.setObjectName("mainlayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.mainlayout)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_records_read = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_records_read.setContentsMargins(0, 0, 0, 0)
        self.layout_records_read.setSpacing(0)
        self.layout_records_read.setObjectName("layout_records_read")
        self.r_add_record = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        self.r_add_record.setFont(font)
        self.r_add_record.setStyleSheet("background-color: chartreuse;\n"
                                        "padding: 20px;\n"
                                        "border-top: 0px;\n"
                                        "border-right: 2px solid black;")
        self.r_add_record.setFlat(False)
        self.r_add_record.setObjectName("r_add_record")
        self.layout_records_read.addWidget(self.r_add_record)
        self.r_table_racords = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.r_table_racords.setStyleSheet("border-right: 2px solid black;\n"
                                            "border-top: 0px;")
        self.r_table_racords.setObjectName("r_table_racords")
        self.r_table_racords.setColumnCount(1)
        self.r_table_racords.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        item.setFont(font)
        self.r_table_racords.setHorizontalHeaderItem(0, item)
        self.r_table_racords.horizontalHeader().setStretchLastSection(True)
        self.layout_records_read.addWidget(self.r_table_racords)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.mainlayout)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_records_write = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_records_write.setContentsMargins(0, 0, 0, 0)
        self.layout_records_write.setSpacing(0)
        self.layout_records_write.setObjectName("layout_records_write")
        self.w_head_data = QtWidgets.QHBoxLayout()
        self.w_head_data.setContentsMargins(0, 0, -1, -1)
        self.w_head_data.setSpacing(0)
        self.w_head_data.setObjectName("w_head_data")
        self.w_head = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.w_head.setFont(font)
        self.w_head.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.w_head.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w_head.setStyleSheet("background-color: #FFB47E;\n"
                                    "border: 0px;\n" "padding: 10px;")
        self.w_head.setFrameShadow(QtWidgets.QFrame.Plain)
        self.w_head.setIndent(0)
        self.w_head.setObjectName("w_head")
        self.w_head_data.addWidget(self.w_head)
        self.w_data = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.w_data.setFont(font)
        self.w_data.setStyleSheet("border: 0px;\n"
                                    "background-color: #FFB47E;\n"
                                    "padding: 10px;")
        self.w_data.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.w_data.setObjectName("w_data")
        self.w_head_data.addWidget(self.w_data)
        self.layout_records_write.addLayout(self.w_head_data)
        self.w_write_field = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.w_write_field.setFont(font)
        self.w_write_field.setStyleSheet("padding: 20px;\n"
                                            "background-color: #ECF4FF;\n"
                                            "border: 0px;\n"
                                            "border-left: 1px;")
        self.w_write_field.setObjectName("w_write_field")
        self.layout_records_write.addWidget(self.w_write_field)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget.setStyleSheet("background-color: #ECF4FF;\n"
                                    "padding:10px;\n"
                                    "margin-right:10px;\n"
                                    "margin-bottom: 10px;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: red;\n"
                                            "border-radius: 15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: chartreuse;\n"
                                        "border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.widget)
        self.layout_records_write.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.mainlayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.sql = sqlite3.connect('DB.db')
        self.cursor = self.sql.cursor()
        self.load_notes()
        self.r_table_racords.cellClicked.connect(self.open_note)
        self.r_add_record.clicked.connect(self.add_note)
        self.pushButton_2.clicked.connect(self.delete_note)
        self.pushButton.clicked.connect(self.save_note)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.r_add_record.setText(_translate("Form", "Добавить"))
        item = self.r_table_racords.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Записи"))
        self.pushButton_2.setText(_translate("Form", "Удалить"))
        self.pushButton.setText(_translate("Form", "Сохранить"))

    def load_notes(self):
        self.cursor.execute('SELECT name_note FROM notes')
        result = self.cursor.fetchall()
        for i in range(len(result)):
            self.r_table_racords.insertRow(i)
            item = QtWidgets.QTableWidgetItem(str(result[i][0]))
            item.setData(QtCore.Qt.BackgroundRole, QtGui.QColor(random.choice(["yellow", 'lightgreen', 'orange', 'lightblue'])))
            self.r_table_racords.setItem(i, 0, item)


    def open_note(self, row):
        self.r_table_racords.setEnabled(False)
        self.w_data.setStyleSheet("border: 0px;\n"
                                    f"background-color: {self.r_table_racords.item(row, 0).background().color().name()};\n"
                                    "padding: 10px;")
        self.w_head.setStyleSheet(f"background-color: {self.r_table_racords.item(row, 0).background().color().name()};\n"
                                  "border: 0px;\n" "padding: 10px;")
        name_note = self.r_table_racords.item(row, 0).text()
        self.cursor.execute(f'SELECT name_note, date_note, text_note FROM notes WHERE name_note="{name_note}"')
        result = self.cursor.fetchone()
        if result:
            self.w_head.setText(result[0])
            self.w_data.setText(result[1])
            self.w_write_field.setText(result[2])

    def delete_note(self):
        selected_row = self.r_table_racords.currentRow()
        if selected_row >= 0:
            name_note = self.r_table_racords.item(int(selected_row), 0).text()
            self.cursor.execute(f'DELETE FROM notes WHERE name_note="{name_note}"')
            self.sql.commit()
            self.r_table_racords.removeRow(selected_row)
            QMessageBox.information(Form, 'Запись удалена.', 'Запись была успешно удалена!')
            self.r_table_racords.setEnabled(True)
        else:
            QMessageBox.information(Form, 'Не удалось удалить!', 'Вы не выбрали запись для удаления.')

    def add_note(self):
        self.record_dialog = QtWidgets.QDialog()
        self.record_dialog.setWindowTitle('Добавить запись')
        self.record_dialog.setFixedSize(400, 200)
        layout = QtWidgets.QVBoxLayout(self.record_dialog)
        name_label = QtWidgets.QLabel('Имя записи:')
        layout.addWidget(name_label)
        self.name_line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.name_line_edit)

        button_box = QtWidgets.QDialogButtonBox()
        button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        button_box.accepted.connect(self.confirm_add_record)
        button_box.rejected.connect(self.record_dialog.reject)
        layout.addWidget(button_box)
        self.record_dialog.exec_()

    def confirm_add_record(self):
        name = self.name_line_edit.text()
        self.cursor.execute(f'INSERT INTO notes (name_note, date_note) VALUES ("{name}", "{datetime.now().date()}")')
        self.sql.commit()
        self.r_table_racords.insertRow(self.r_table_racords.rowCount())
        item = QtWidgets.QTableWidgetItem(name)
        item.setData(QtCore.Qt.BackgroundRole,
                     QtGui.QColor(random.choice(["yellow", 'lightgreen', 'orange', 'lightblue'])))
        self.r_table_racords.setItem(self.r_table_racords.rowCount() - 1, 0, item)
        self.record_dialog.accept()

    def save_note(self):
        selected_row = self.r_table_racords.currentRow()
        if selected_row >= 0:
            name_note = self.r_table_racords.item(selected_row, 0).text()
            new_text = self.w_write_field.toPlainText()
            self.cursor.execute(f'UPDATE notes SET text_note="{new_text}" WHERE name_note="{name_note}"')
            self.sql.commit()
            QMessageBox.information(Form, 'Запись сохранена.', 'Запись была успешно сохранена!')
            self.r_table_racords.setEnabled(True)
        else:
            QMessageBox.information(Form, 'Не удалось сохранить!', 'Вы не выбрали запись для сохранения.')


    def check_note(self, name_note):
        self.cursor.execute(f'SELECT name_note FROM notes WHERE name_note={name_note}')
        if self.cursor.fetchone():
            return True
        else:
            return False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
