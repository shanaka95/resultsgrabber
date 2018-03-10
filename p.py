# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proccess.ui'
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
        self.label.setGeometry(QtCore.QRect(210, 40, 111, 20))
        self.label.setStyleSheet(_fromUtf8("font: 11pt \"MS Reference Sans Serif\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(70, 220, 411, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 371, 121))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 9pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 0, 127);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Please Wait...", None))

