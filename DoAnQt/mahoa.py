# Form implementation generated from reading ui file 'mahoa.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 603)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 0, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(-1)
        self.label_2.setLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btnCaesar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCaesar.setGeometry(QtCore.QRect(220, 140, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCaesar.setFont(font)
        self.btnCaesar.setObjectName("btnCaesar")
        self.btnVigenere = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnVigenere.setGeometry(QtCore.QRect(220, 200, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnVigenere.setFont(font)
        self.btnVigenere.setObjectName("pushButton_2")
        self.btnBelasco = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBelasco.setGeometry(QtCore.QRect(220, 320, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnBelasco.setFont(font)
        self.btnBelasco.setObjectName("pushButton_3")
        self.btnTrithemius = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTrithemius.setGeometry(QtCore.QRect(220, 380, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTrithemius.setFont(font)
        self.btnTrithemius.setObjectName("pushButton_4")
        self.btnChuyenViHaiDong = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnChuyenViHaiDong.setGeometry(QtCore.QRect(220, 500, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnChuyenViHaiDong.setFont(font)
        self.btnChuyenViHaiDong.setObjectName("pushButton_5")
        self.btnXor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnXor.setGeometry(QtCore.QRect(220, 260, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnXor.setFont(font)
        self.btnXor.setObjectName("pushButton_6")
        self.btnChuyenViNhieuDong = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnChuyenViNhieuDong.setGeometry(QtCore.QRect(220, 440, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnChuyenViNhieuDong.setFont(font)
        self.btnChuyenViNhieuDong.setObjectName("pushButton_7")
        self.btnback = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnback.setGeometry(QtCore.QRect(520, 510, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnback.setFont(font)
        self.btnback.setObjectName("btnback")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mã hóa văn bản"))
        self.label_2.setText(_translate("MainWindow", "Vui lòng chọn thuật toán muốn mã hóa"))
        self.btnCaesar.setText(_translate("MainWindow", "Caesar"))
        self.btnVigenere.setText(_translate("MainWindow", "Vigenere"))
        self.btnBelasco.setText(_translate("MainWindow", "Belasco"))
        self.btnTrithemius.setText(_translate("MainWindow", "Trithemius"))
        self.btnChuyenViHaiDong.setText(_translate("MainWindow", "Chuyển vị hai dòng"))
        self.btnXor.setText(_translate("MainWindow", "XOR"))
        self.btnChuyenViNhieuDong.setText(_translate("MainWindow", "Chuyển vị nhiều dòng"))
        self.btnback.setText(_translate("MainWindow", "Back"))
