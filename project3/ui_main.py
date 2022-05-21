# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1loBodu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 959)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(210, 210, 650, 340))
        font = QFont()
        font.setFamily(u"\u5b8b\u4f53")
        self.groupBox_3.setFont(font)
        self.plotbu = QPushButton(self.groupBox_3)
        self.plotbu.setObjectName(u"plotbu")
        self.plotbu.setGeometry(QRect(555, 90, 75, 23))
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setBold(True)
        font1.setWeight(75)
        self.plotbu.setFont(font1)
        self.clearbu1 = QPushButton(self.groupBox_3)
        self.clearbu1.setObjectName(u"clearbu1")
        self.clearbu1.setGeometry(QRect(555, 190, 75, 23))
        self.clearbu1.setFont(font1)
        self.verticalLayoutWidget_10 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(140, 300, 351, 31))
        self.bar_1 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.bar_1.setObjectName(u"bar_1")
        self.bar_1.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget = QWidget(self.groupBox_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 20, 411, 271))
        self.plot_2 = QVBoxLayout(self.layoutWidget)
        self.plot_2.setObjectName(u"plot_2")
        self.plot_2.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.groupBox_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 70, 74, 141))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.plot_rho = QRadioButton(self.layoutWidget1)
        self.plot_rho.setObjectName(u"plot_rho")

        self.verticalLayout_8.addWidget(self.plot_rho)

        self.plot_p = QRadioButton(self.layoutWidget1)
        self.plot_p.setObjectName(u"plot_p")

        self.verticalLayout_8.addWidget(self.plot_p)

        self.plot_T = QRadioButton(self.layoutWidget1)
        self.plot_T.setObjectName(u"plot_T")

        self.verticalLayout_8.addWidget(self.plot_T)

        self.plot_Ma = QRadioButton(self.layoutWidget1)
        self.plot_Ma.setObjectName(u"plot_Ma")

        self.verticalLayout_8.addWidget(self.plot_Ma)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(210, 6, 650, 201))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(190, 50, 50, 111))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_3.addWidget(self.label_8)

        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(260, 50, 121, 119))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.alpha = QLineEdit(self.layoutWidget_2)
        self.alpha.setObjectName(u"alpha")

        self.verticalLayout_4.addWidget(self.alpha)

        self.gamma = QLineEdit(self.layoutWidget_2)
        self.gamma.setObjectName(u"gamma")

        self.verticalLayout_4.addWidget(self.gamma)

        self.dx = QLineEdit(self.layoutWidget_2)
        self.dx.setObjectName(u"dx")

        self.verticalLayout_4.addWidget(self.dx)

        self.eps = QLineEdit(self.layoutWidget_2)
        self.eps.setObjectName(u"eps")

        self.verticalLayout_4.addWidget(self.eps)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 80, 72, 15))
        self.Cx = QLineEdit(self.groupBox_2)
        self.Cx.setObjectName(u"Cx")
        self.Cx.setGeometry(QRect(490, 78, 113, 21))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 115, 72, 15))
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(450, 20, 101, 51))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.arti = QRadioButton(self.verticalLayoutWidget_5)
        self.arti.setObjectName(u"arti")

        self.verticalLayout_2.addWidget(self.arti)

        self.layoutWidget3 = QWidget(self.groupBox_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(50, 50, 127, 111))
        self.verticalLayout = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pro1 = QRadioButton(self.layoutWidget3)
        self.pro1.setObjectName(u"pro1")

        self.verticalLayout.addWidget(self.pro1)

        self.pro2 = QRadioButton(self.layoutWidget3)
        self.pro2.setObjectName(u"pro2")

        self.verticalLayout.addWidget(self.pro2)

        self.pro3 = QRadioButton(self.layoutWidget3)
        self.pro3.setObjectName(u"pro3")

        self.verticalLayout.addWidget(self.pro3)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(431, 141, 59, 21))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.rho = QRadioButton(self.verticalLayoutWidget_6)
        self.rho.setObjectName(u"rho")

        self.verticalLayout_5.addWidget(self.rho)

        self.verticalLayoutWidget_7 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(431, 168, 59, 21))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.T = QRadioButton(self.verticalLayoutWidget_7)
        self.T.setObjectName(u"T")

        self.verticalLayout_6.addWidget(self.T)

        self.verticalLayoutWidget_9 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(531, 168, 74, 21))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Ma = QRadioButton(self.verticalLayoutWidget_9)
        self.Ma.setObjectName(u"Ma")

        self.verticalLayout_10.addWidget(self.Ma)

        self.verticalLayoutWidget_8 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(531, 141, 59, 21))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.p = QRadioButton(self.verticalLayoutWidget_8)
        self.p.setObjectName(u"p")

        self.verticalLayout_7.addWidget(self.p)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(210, 550, 650, 340))
        font2 = QFont()
        font2.setFamily(u"\u5b8b\u4f53")
        font2.setBold(False)
        font2.setWeight(50)
        self.groupBox_4.setFont(font2)
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(110, 20, 411, 271))
        self.ani = QVBoxLayout(self.verticalLayoutWidget_3)
        self.ani.setObjectName(u"ani")
        self.ani.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(150, 300, 341, 31))
        self.bar2 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.bar2.setObjectName(u"bar2")
        self.bar2.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget_3 = QWidget(self.groupBox_4)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 90, 74, 141))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ani_rho = QRadioButton(self.layoutWidget_3)
        self.ani_rho.setObjectName(u"ani_rho")

        self.verticalLayout_9.addWidget(self.ani_rho)

        self.ani_p = QRadioButton(self.layoutWidget_3)
        self.ani_p.setObjectName(u"ani_p")

        self.verticalLayout_9.addWidget(self.ani_p)

        self.ani_T = QRadioButton(self.layoutWidget_3)
        self.ani_T.setObjectName(u"ani_T")

        self.verticalLayout_9.addWidget(self.ani_T)

        self.ani_Ma = QRadioButton(self.layoutWidget_3)
        self.ani_Ma.setObjectName(u"ani_Ma")

        self.verticalLayout_9.addWidget(self.ani_Ma)

        self.t_num = QLabel(self.groupBox_4)
        self.t_num.setObjectName(u"t_num")
        self.t_num.setGeometry(QRect(10, 35, 91, 16))
        self.widget = QWidget(self.groupBox_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(540, 70, 95, 171))
        self.verticalLayout_11 = QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.anibu = QPushButton(self.widget)
        self.anibu.setObjectName(u"anibu")
        self.anibu.setFont(font1)

        self.verticalLayout_11.addWidget(self.anibu)

        self.stop = QPushButton(self.widget)
        self.stop.setObjectName(u"stop")
        self.stop.setFont(font1)

        self.verticalLayout_11.addWidget(self.stop)

        self.continue_2 = QPushButton(self.widget)
        self.continue_2.setObjectName(u"continue_2")
        self.continue_2.setFont(font1)

        self.verticalLayout_11.addWidget(self.continue_2)

        self.clearbu2 = QPushButton(self.widget)
        self.clearbu2.setObjectName(u"clearbu2")
        self.clearbu2.setFont(font1)

        self.verticalLayout_11.addWidget(self.clearbu2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1088, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf", None))
        self.plotbu.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
        self.clearbu1.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
        self.plot_rho.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u5ea6", None))
        self.plot_p.setText(QCoreApplication.translate("MainWindow", u"\u538b\u5f3a", None))
        self.plot_T.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6", None))
        self.plot_Ma.setText(QCoreApplication.translate("MainWindow", u"\u9a6c\u8d6b\u6570", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u9009\u62e9", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u67ef\u6717\u6570", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u70ed\u6bd4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6b65 \u957f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u7cbe \u5ea6", None))
        self.alpha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.7", None))
        self.gamma.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.4", None))
        self.dx.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.eps.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1e-5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9ecf\u6027\u53c2\u6570", None))
        self.Cx.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4fdd\u5b58", None))
        self.arti.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u5de5\u9ecf\u6027", None))
        self.pro1.setText(QCoreApplication.translate("MainWindow", u"\u4e9a\u58f0\u901f-\u8d85\u58f0\u901f", None))
        self.pro2.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u5168\u4e9a\u58f0\u901f", None))
        self.pro3.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u6ce2\u6355\u6349", None))
        self.rho.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u5ea6", None))
        self.T.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6", None))
        self.Ma.setText(QCoreApplication.translate("MainWindow", u"\u9a6c\u8d6b\u6570", None))
        self.p.setText(QCoreApplication.translate("MainWindow", u"\u538b\u5f3a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6536\u655b\u52a8\u753b", None))
        self.ani_rho.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u5ea6", None))
        self.ani_p.setText(QCoreApplication.translate("MainWindow", u"\u538b\u5f3a", None))
        self.ani_T.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6", None))
        self.ani_Ma.setText(QCoreApplication.translate("MainWindow", u"\u9a6c\u8d6b\u6570", None))
        self.t_num.setText(QCoreApplication.translate("MainWindow", u"num", None))
        self.anibu.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u753b", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.continue_2.setText(QCoreApplication.translate("MainWindow", u"\u7ee7\u7eed", None))
        self.clearbu2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
    # retranslateUi

