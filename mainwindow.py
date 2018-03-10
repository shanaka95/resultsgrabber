# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(612, 452)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 551, 51))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.s_details = QtGui.QPushButton(self.groupBox)
        self.s_details.setGeometry(QtCore.QRect(30, 10, 141, 31))
        self.s_details.setStyleSheet(_fromUtf8("border: none;\n"
"font: 75 10pt \"Arial\";\n"
" font-weight: bold;\n"
"text-align: left;\n"
""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("D:/ravindra_sir/l.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.s_details.setIcon(icon)
        self.s_details.setObjectName(_fromUtf8("s_details"))
        self.s_enq = QtGui.QPushButton(self.groupBox)
        self.s_enq.setGeometry(QtCore.QRect(200, 10, 151, 31))
        self.s_enq.setStyleSheet(_fromUtf8("border: none;\n"
"font: 75 10pt \"Arial\";\n"
" font-weight: bold;\n"
"text-align: left;"))
        self.s_enq.setIcon(icon)
        self.s_enq.setObjectName(_fromUtf8("s_enq"))
        self.s_enq_2 = QtGui.QPushButton(self.groupBox)
        self.s_enq_2.setGeometry(QtCore.QRect(380, 10, 151, 31))
        self.s_enq_2.setStyleSheet(_fromUtf8("border: none;\n"
"font: 75 10pt \"Arial\";\n"
" font-weight: bold;\n"
"text-align: left;"))
        self.s_enq_2.setIcon(icon)
        self.s_enq_2.setObjectName(_fromUtf8("s_enq_2"))
        self.g = QtGui.QGroupBox(self.centralWidget)
        self.g.setGeometry(QtCore.QRect(30, 90, 551, 311))
        self.g.setTitle(_fromUtf8(""))
        self.g.setObjectName(_fromUtf8("g"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 551, 311))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(120, 420, 441, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Result Grab ", None))
        self.s_details.setText(_translate("MainWindow", "Advanced Level", None))
        self.s_enq.setText(_translate("MainWindow", "Ordinary Level", None))
        self.s_enq_2.setText(_translate("MainWindow", "Save", None))
        self.label.setText(_translate("MainWindow", "Developed by Shanaka Anuradha | fb.com/shanaka1995 | 0715654548", None))

