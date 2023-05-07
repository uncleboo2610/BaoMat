# Form implementation generated from reading ui file 'GiaiMaCeasar.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import Ceasar.ceasar as ceasar
import openfile, savefile


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 828)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGiaiMaCaesar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGiaiMaCaesar.setGeometry(QtCore.QRect(250, 470, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGiaiMaCaesar.setFont(font)
        self.btnGiaiMaCaesar.setObjectName("btnGiaiMaCaesar")
        self.btnSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSave.clicked.connect(self.btnSaveFile_Click)
        self.btnGiaiMaCaesar.clicked.connect(self.btnGiaiMa_clicked)
        self.btnSave.setGeometry(QtCore.QRect(250, 720, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnGiaiMa = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGiaiMa.setGeometry(QtCore.QRect(420, 720, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGiaiMa.setFont(font)
        self.btnGiaiMa.setObjectName("btnGiaiMa")
        self.btnBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(80, 720, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.EdtPath = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.EdtPath.setGeometry(QtCore.QRect(110, 100, 371, 22))
        self.EdtPath.setObjectName("EdtPath")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 490, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.result = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(30, 520, 561, 171))
        self.result.setObjectName("result")
        self.key = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.key.setGeometry(QtCore.QRect(30, 410, 561, 31))
        self.key.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.input = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.input.setGeometry(QtCore.QRect(30, 190, 561, 171))
        self.input.setObjectName("input")
        self.btnChonFile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnChonFile.setGeometry(QtCore.QRect(500, 100, 93, 28))
        self.btnChonFile.clicked.connect(self.btnChonFile_Click)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnChonFile.setFont(font)
        self.btnChonFile.setObjectName("btnChonFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# Chon file text
    def btnChonFile_Click(self):
        open_path_file = openfile.pathFile()
        self.EdtPath.setText(open_path_file)

        open_file = openfile.openFileDialog(open_path_file)
        self.input.setText(open_file)

# button Giai Ma
    def btnGiaiMa_clicked(self):
        input = self.input.toPlainText()
        key = int(self.key.text())
        GiaiMa = ceasar.GiaiMa(input,key)
        self.result.setText(GiaiMa)

    # Button Save
    def btnSaveFile_Click(self):
        res = self.result.toPlainText()
        savefile.saveFile(res)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGiaiMaCaesar.setText(_translate("MainWindow", "Giải mã"))
        self.btnSave.setText(_translate("MainWindow", "Lưu File"))
        self.label_2.setText(_translate("MainWindow", "File Path:"))
        self.btnGiaiMa.setText(_translate("MainWindow", "Mã hóa"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Giãi mã văn bản bằng Ceasar"))
        self.label_4.setText(_translate("MainWindow", "Kết quả:"))
        self.label_3.setText(_translate("MainWindow", "Nội dung giải mã:"))
        self.label_5.setText(_translate("MainWindow", "Key"))
        self.btnChonFile.setText(_translate("MainWindow", "Chọn File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
