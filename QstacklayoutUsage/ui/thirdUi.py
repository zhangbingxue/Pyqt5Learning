# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thirdUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_thirdForm(object):
    def setupUi(self, thirdForm):
        thirdForm.setObjectName("thirdForm")
        thirdForm.resize(400, 300)
        self.lcdNumber = QtWidgets.QLCDNumber(thirdForm)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 110, 271, 101))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(thirdForm)
        QtCore.QMetaObject.connectSlotsByName(thirdForm)

    def retranslateUi(self, thirdForm):
        _translate = QtCore.QCoreApplication.translate
        thirdForm.setWindowTitle(_translate("thirdForm", "Form"))
