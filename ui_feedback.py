# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.feedbackText = QtWidgets.QPlainTextEdit(Dialog)
        self.feedbackText.setGeometry(QtCore.QRect(20, 20, 361, 211))
        self.feedbackText.setObjectName("feedbackText")
        self.send = QtWidgets.QPushButton(Dialog)
        self.send.setGeometry(QtCore.QRect(20, 240, 361, 41))
        self.send.setObjectName("send")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "反馈"))
        self.feedbackText.setPlaceholderText(_translate("Dialog", "你想对作者说的话，可以加上联系方式欧"))
        self.send.setText(_translate("Dialog", "发送"))


