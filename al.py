# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'al.ui'
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
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 40, 491, 171))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 13, 311, 20))
        self.label.setStyleSheet(_fromUtf8("font: 11pt \"MS Reference Sans Serif\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 491, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Please enter Student admission numbers", None))
        self.pushButton.setText(_translate("Form", "Grab", None))

