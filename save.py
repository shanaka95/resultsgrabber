# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(532, 290)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 20))
        self.label.setStyleSheet(_fromUtf8("font: 11pt \"MS Reference Sans Serif\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 491, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 491, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 311, 20))
        self.label_2.setStyleSheet(_fromUtf8("font: 11pt \"MS Reference Sans Serif\";"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 80, 491, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 491, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 120, 491, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 160, 491, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Save Results", None))
        self.pushButton.setText(_translate("Form", "Save Advanced Level Results By stream order by Z-score", None))
        self.pushButton_2.setText(_translate("Form", "Save Ordinary Level Results By Rank", None))
        self.pushButton_3.setText(_translate("Form", "Save Advanced Level Results By Subjects", None))
        self.pushButton_4.setText(_translate("Form", "Save Ordinary Level Results By Subjects", None))
        self.pushButton_5.setText(_translate("Form", "Save Advanced Level Results order by Z-score", None))
        self.pushButton_6.setText(_translate("Form", "Save Advanced Level Results By stream order by Z-score with Grades obtained", None))

