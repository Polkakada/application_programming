# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\delDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delDialog(object):
    def setupUi(self, delDialog):
        delDialog.setObjectName("delDialog")
        delDialog.resize(745, 686)
        self.horizontalLayout = QtWidgets.QHBoxLayout(delDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelName = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelName.setFont(font)
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.nameEdit = QtWidgets.QLineEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        spacerItem = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.labelSource = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSource.setFont(font)
        self.labelSource.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSource.setObjectName("labelSource")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelSource)
        self.sourceEdit = QtWidgets.QLineEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sourceEdit.setFont(font)
        self.sourceEdit.setObjectName("sourceEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sourceEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.labelGenre = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelGenre.setFont(font)
        self.labelGenre.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGenre.setObjectName("labelGenre")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelGenre)
        self.genreEdit = QtWidgets.QLineEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.genreEdit.setFont(font)
        self.genreEdit.setObjectName("genreEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.genreEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.labelCountry = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCountry.setFont(font)
        self.labelCountry.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCountry.setObjectName("labelCountry")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelCountry)
        self.countryEdit = QtWidgets.QLineEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countryEdit.setFont(font)
        self.countryEdit.setObjectName("countryEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.countryEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.labelNickname = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNickname.setFont(font)
        self.labelNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNickname.setObjectName("labelNickname")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelNickname)
        self.nicknameEdit = QtWidgets.QLineEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nicknameEdit.setFont(font)
        self.nicknameEdit.setObjectName("nicknameEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.nicknameEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.labelAuthorName = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAuthorName.setFont(font)
        self.labelAuthorName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAuthorName.setObjectName("labelAuthorName")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.labelAuthorName)
        self.authorNameEdit = QtWidgets.QLineEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authorNameEdit.setFont(font)
        self.authorNameEdit.setObjectName("authorNameEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.authorNameEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.labelbirthday = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelbirthday.setFont(font)
        self.labelbirthday.setAlignment(QtCore.Qt.AlignCenter)
        self.labelbirthday.setObjectName("labelbirthday")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.labelbirthday)
        self.birthdayEdit = QtWidgets.QDateEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birthdayEdit.setFont(font)
        self.birthdayEdit.setDate(QtCore.QDate(2200, 1, 1))
        self.birthdayEdit.setObjectName("birthdayEdit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.birthdayEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.LabelRole, spacerItem6)
        self.labelSex = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSex.setFont(font)
        self.labelSex.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSex.setObjectName("labelSex")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.labelSex)
        self.sexEdit = QtWidgets.QLineEdit(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sexEdit.setFont(font)
        self.sexEdit.setObjectName("sexEdit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.sexEdit)
        self.delFormButton = QtWidgets.QPushButton(delDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delFormButton.setFont(font)
        self.delFormButton.setObjectName("delFormButton")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.delFormButton)
        self.infoLabel = QtWidgets.QLabel(delDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.infoLabel.setFont(font)
        self.infoLabel.setText("")
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.SpanningRole, self.infoLabel)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(delDialog)
        QtCore.QMetaObject.connectSlotsByName(delDialog)

    def retranslateUi(self, delDialog):
        _translate = QtCore.QCoreApplication.translate
        delDialog.setWindowTitle(_translate("delDialog", "Удаление"))
        self.labelName.setText(_translate("delDialog", "Название видео"))
        self.labelSource.setText(_translate("delDialog", "Ссылка на видео"))
        self.labelGenre.setText(_translate("delDialog", "Жанр видео"))
        self.labelCountry.setText(_translate("delDialog", "Страна создания"))
        self.labelNickname.setText(_translate("delDialog", "Псведоним автора"))
        self.labelAuthorName.setText(_translate("delDialog", "Настоящее имя автора"))
        self.labelbirthday.setText(_translate("delDialog", "День рождения автора"))
        self.labelSex.setText(_translate("delDialog", "Пол автора"))
        self.delFormButton.setText(_translate("delDialog", "Удалить видео"))
