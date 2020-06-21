import psycopg2
import creating
import inserting
import showing
import mainWindow
import insertDialog
import sys
import delDialog
import findDialog
import del_and_search
import infoDialog
from PyQt5 import QtWidgets


def getInfo(self):
    authorFullName = self.authorNameEdit.text()
    authorFullName = authorFullName.split(' ')
    if authorFullName.__len__() == 0:
        firstName = ''
        lastName = ''
    elif authorFullName.__len__() == 1:
        firstName = authorFullName[0]
        lastName = ''
    else:
        firstName = authorFullName[0]
        lastName = authorFullName[1]

    field_dict = {'Ссылка на видео': self.sourceEdit.text(),
                  'Название видео': self.nameEdit.text(),
                  'Псведоним создателя': self.nicknameEdit.text(),
                  'Жанр видео': self.genreEdit.text(),
                  'Страна создания': self.countryEdit.text(),
                  'Имя создателя': firstName,
                  'Фамилия создателя': lastName,
                  'День рождения создателя': self.birthdayEdit.text(),
                  'Пол создателя': self.sexEdit.text()}
    return field_dict


def getInfoNoA(self):
    field_dict = {'Ссылка на видео': self.sourceEdit.text(),
                  'Название видео': self.nameEdit.text(),
                  'Псведоним создателя': '',
                  'Жанр видео': self.genreEdit.text(),
                  'Страна создания': self.countryEdit.text(),
                  'Имя создателя': '',
                  'Фамилия создателя': '',
                  'День рождения создателя': '01.01.1753',
                  'Пол создателя': ''}
    return field_dict


class InfoForm(QtWidgets.QDialog, infoDialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class DelForm(QtWidgets.QDialog, delDialog.Ui_delDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.delFormButton.clicked.connect(self.doDel)

    def doDel(self):
        field_dict = getInfo(self)
        del_and_search.call_find(field_dict, cursor, 1)
        self.close()


class FindForm(QtWidgets.QDialog, findDialog.Ui_FindDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.findFormButton.clicked.connect(self.doFind)

    def doFind(self):
        field_dict = getInfo(self)
        k = del_and_search.call_find(field_dict, cursor, 2)
        window.ListWidget.clear()
        window.ListWidget.addItem("Результат поиска:")
        window.output(k)
        self.close()


class InsertForm(QtWidgets.QDialog, insertDialog.Ui_InsertDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.infoLabel.setText("Поля со звездочкой являются обязательными")
        self.insertFormButton.clicked.connect(self.doInsert)
        self.nameEdit.textChanged.connect(self.buttonActivate)
        self.sourceEdit.textChanged.connect(self.buttonActivate)
        self.checkBox.stateChanged.connect(self.activate)

    def buttonActivate(self):
        if self.nameEdit.text() != "" and self.sourceEdit.text() != "":
            self.insertFormButton.setEnabled(True)
        else:
            self.insertFormButton.setEnabled(False)

    def activate(self):
        if self.checkBox.isChecked():
            self.labelAuthorName.setEnabled(True)
            self.labelSex.setEnabled(True)
            self.labelNickname.setEnabled(True)
            self.labelbirthday.setEnabled(True)
            self.birthdayEdit.setEnabled(True)
            self.nicknameEdit.setEnabled(True)
            self.authorNameEdit.setEnabled(True)
            self.sexEdit.setEnabled(True)
        else:
            self.labelAuthorName.setEnabled(False)
            self.labelSex.setEnabled(False)
            self.labelNickname.setEnabled(False)
            self.labelbirthday.setEnabled(False)
            self.birthdayEdit.setEnabled(False)
            self.nicknameEdit.setEnabled(False)
            self.authorNameEdit.setEnabled(False)
            self.sexEdit.setEnabled(False)

    def doInsert(self):
        if self.checkBox.isChecked():
            field_dict = getInfo(self)
        else:
            field_dict = getInfoNoA(self)
        k = del_and_search.call_find(field_dict, cursor, 0)
        if k:
            inserting.call_insert(field_dict, cursor)
            self.infoLabel.setText("Поля со звездочкой являются обязательными")
            self.close()
        else:
            self.infoLabel.setText("Поля со звездочкой являются обязательными\n Такая запись уже существует!")


class MainForm(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.insertForm = InsertForm()
        self.delForm = DelForm()
        self.findForm = FindForm()
        self.infoForm = InfoForm()
        self.setupUi(self)
        self.AddButton.clicked.connect(self.showAdd)
        self.AllButton.clicked.connect(self.showAll)
        self.DelButton.clicked.connect(self.showDel)
        self.SearchButton.clicked.connect(self.showFind)
        self.ListWidget.itemClicked.connect(self.showItemInfo)

    def showItemInfo(self):
        a = (self.ListWidget.currentItem().text())
        if a == "Все записи:" or a == "Нет записей":
            return

        a = a[15:]
        b = a.split("\tСсылка на видео:")
        name = b[0][1:]
        b = b[1].split("\tАвтор:")
        source = b[0][1:]
        b = b[1].split("\tЖанр:")
        author = b[0][1:]
        b = b[1].split("\tСтрана:")
        genre = b[0][1:]
        country = b[1][1:]

        field_dict = del_and_search.findFullInfo(source, name, author, genre, country, cursor)
        self.infoForm.sourceEdit.setText(field_dict['Ссылка на видео'])
        self.infoForm.nameEdit.setText(field_dict['Название видео'])
        self.infoForm.genreEdit.setText(field_dict['Жанр видео'])
        self.infoForm.countryEdit.setText(field_dict['Страна создания'])
        self.infoForm.nicknameEdit.setText(field_dict['Псведоним создателя'])
        self.infoForm.firstNameEdit.setText(field_dict['Имя создателя'])
        self.infoForm.surnameEdit.setText(field_dict['Фамилия создателя'])
        self.infoForm.birthdayEdit.setText(field_dict['День рождения создателя'])
        self.infoForm.sexEdit.setText(field_dict['Пол создателя'])
        self.infoForm.show()

    def showFind(self):
        self.findForm.show()

    def showDel(self):
        self.delForm.show()

    def showAdd(self):
        self.insertForm.show()

    def showAll(self):
        k = showing.show_video(cursor)
        self.ListWidget.clear()
        self.ListWidget.addItem("Все записи:")
        self.output(k)

    def output(self, k):
        if k == "Нет записей":
            self.ListWidget.addItem(k)
        else:
            for i in k:
                self.ListWidget.addItem(i)


conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="qwer1234",
    host="localhost",
    port="5432")

cursor = conn.cursor()
creating.delete_db(cursor)
creating.create_db(cursor)

app = QtWidgets.QApplication(sys.argv)
window = MainForm()
window.show()
app.exec_()
conn.close()
print("Соединение завершено")
