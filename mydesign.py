# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yolcuEkle.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 424)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 401, 233))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ad_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.ad_txt.setObjectName("ad_txt")
        self.verticalLayout.addWidget(self.ad_txt)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.soyad_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.soyad_txt.setObjectName("soyad_txt")
        self.verticalLayout.addWidget(self.soyad_txt)
        self.cinsiyet_cbBox = QtWidgets.QComboBox(self.layoutWidget)
        self.cinsiyet_cbBox.setObjectName("cinsiyet_cbBox")
        self.cinsiyet_cbBox.addItem("")
        self.cinsiyet_cbBox.addItem("")
        self.cinsiyet_cbBox.addItem("")
        self.verticalLayout.addWidget(self.cinsiyet_cbBox)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.binis_TEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.binis_TEdit.setObjectName("binis_TEdit")
        self.verticalLayout_2.addWidget(self.binis_TEdit)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.inis_TEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.inis_TEdit.setObjectName("inis_TEdit")
        self.verticalLayout_2.addWidget(self.inis_TEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iptal_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.iptal_btn.setObjectName("iptal_btn")
        self.horizontalLayout_2.addWidget(self.iptal_btn)
        self.kaydet_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.kaydet_btn.setObjectName("kaydet_btn")
        self.horizontalLayout_2.addWidget(self.kaydet_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 250, 437, 156))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.koltuk11_btn_13 = QtWidgets.QPushButton(self.widget)
        self.koltuk11_btn_13.setEnabled(True)
        self.koltuk11_btn_13.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk11_btn_13.setAutoFillBackground(False)
        self.koltuk11_btn_13.setStyleSheet("background-image: url(img/steering wheel.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk11_btn_13.setText("")
        self.koltuk11_btn_13.setObjectName("koltuk11_btn_13")
        self.horizontalLayout_4.addWidget(self.koltuk11_btn_13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.koltuk_1_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_1_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_1_btn.setAutoFillBackground(False)
        self.koltuk_1_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_1_btn.setText("")
        self.koltuk_1_btn.setObjectName("koltuk_1_btn")
        self.verticalLayout_8.addWidget(self.koltuk_1_btn)
        self.koltuk_2_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_2_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_2_btn.setAutoFillBackground(False)
        self.koltuk_2_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_2_btn.setText("")
        self.koltuk_2_btn.setObjectName("koltuk_2_btn")
        self.verticalLayout_8.addWidget(self.koltuk_2_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.koltuk_3_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_3_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_3_btn.setAutoFillBackground(False)
        self.koltuk_3_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_3_btn.setText("")
        self.koltuk_3_btn.setObjectName("koltuk_3_btn")
        self.verticalLayout_7.addWidget(self.koltuk_3_btn)
        self.koltuk_4_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_4_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_4_btn.setAutoFillBackground(False)
        self.koltuk_4_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_4_btn.setText("")
        self.koltuk_4_btn.setObjectName("koltuk_4_btn")
        self.verticalLayout_7.addWidget(self.koltuk_4_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.koltuk_5_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_5_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_5_btn.setAutoFillBackground(False)
        self.koltuk_5_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_5_btn.setText("")
        self.koltuk_5_btn.setObjectName("koltuk_5_btn")
        self.verticalLayout_6.addWidget(self.koltuk_5_btn)
        self.koltuk_6_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_6_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_6_btn.setAutoFillBackground(False)
        self.koltuk_6_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_6_btn.setText("")
        self.koltuk_6_btn.setObjectName("koltuk_6_btn")
        self.verticalLayout_6.addWidget(self.koltuk_6_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.koltuk_7_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_7_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_7_btn.setAutoFillBackground(False)
        self.koltuk_7_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_7_btn.setText("")
        self.koltuk_7_btn.setObjectName("koltuk_7_btn")
        self.verticalLayout_5.addWidget(self.koltuk_7_btn)
        self.koltuk_8_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_8_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_8_btn.setAutoFillBackground(False)
        self.koltuk_8_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_8_btn.setText("")
        self.koltuk_8_btn.setObjectName("koltuk_8_btn")
        self.verticalLayout_5.addWidget(self.koltuk_8_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.koltuk_9_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_9_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_9_btn.setAutoFillBackground(False)
        self.koltuk_9_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_9_btn.setText("")
        self.koltuk_9_btn.setObjectName("koltuk_9_btn")
        self.verticalLayout_4.addWidget(self.koltuk_9_btn)
        self.koltuk_10_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_10_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_10_btn.setAutoFillBackground(False)
        self.koltuk_10_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_10_btn.setText("")
        self.koltuk_10_btn.setObjectName("koltuk_10_btn")
        self.verticalLayout_4.addWidget(self.koltuk_10_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.koltuk_11_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_11_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_11_btn.setAutoFillBackground(False)
        self.koltuk_11_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_11_btn.setText("")
        self.koltuk_11_btn.setObjectName("koltuk_11_btn")
        self.verticalLayout_3.addWidget(self.koltuk_11_btn)
        self.koltuk_12_btn = QtWidgets.QPushButton(self.widget)
        self.koltuk_12_btn.setMinimumSize(QtCore.QSize(55, 72))
        self.koltuk_12_btn.setAutoFillBackground(False)
        self.koltuk_12_btn.setStyleSheet("background-image: url(img/free-seat.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.koltuk_12_btn.setText("")
        self.koltuk_12_btn.setObjectName("koltuk_12_btn")
        self.verticalLayout_3.addWidget(self.koltuk_12_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ad"))
        self.label_5.setText(_translate("Form", "Soyad"))
        self.cinsiyet_cbBox.setItemText(0, _translate("Form", "Cinsiyet"))
        self.cinsiyet_cbBox.setItemText(1, _translate("Form", "Erkek"))
        self.cinsiyet_cbBox.setItemText(2, _translate("Form", "Kadın"))
        self.label_9.setText(_translate("Form", "Tarih"))
        self.pushButton.setText(_translate("Form", "Bugün"))
        self.label_10.setText(_translate("Form", "Saat"))
        self.label_7.setText(_translate("Form", "Bineceği Yer"))
        self.label_8.setText(_translate("Form", "İneceği Yer"))
        self.iptal_btn.setText(_translate("Form", "İptal"))
        self.kaydet_btn.setText(_translate("Form", "Kaydet"))
