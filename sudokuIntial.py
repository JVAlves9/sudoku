# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudokuInitial.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initialWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(QtWidgets.QMainWindow,str,str)
    def __init__(self, Dialog,MainWindow):
        self.MainWindow = MainWindow

        QtWidgets.QWidget.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QtCore.QSize(300, 200))
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 80, 201, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 271, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(70, 110, 150, 30))
        self.start.setObjectName("pushButton")
        #Dialog.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(Dialog)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        #self.menubar.setObjectName("menubar")
        #Dialog.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(Dialog)
        #self.statusbar.setObjectName("statusbar")
        #Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.start.clicked.connect(lambda:self.startPressed())


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Game"))
        self.comboBox.setCurrentText(_translate("Dialog", "Easy"))
        self.comboBox.setItemText(0, _translate("Dialog", "Easy"))
        self.comboBox.setItemText(1, _translate("Dialog", "Medium"))
        self.comboBox.setItemText(2, _translate("Dialog", "Hard"))
        self.start.setText(_translate("Dialog", "Start"))
    def startPressed(self):
        self.storeName(self.lineEdit.text())
        self.storeMode(self.comboBox.currentText())
        self.switch()
    def storeName(self,value):
        if value == '':
            self.name = 'Unknown'
        else:
            self.name = value
    def storeMode(self,value):
        self.mode = value
    def switch(self):
        self.switch_window.emit(self.MainWindow,self.name,self.mode)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    #ui = Ui_initialWindow(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
