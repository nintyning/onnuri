# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 662)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_mid_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_mid_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_mid_name.setObjectName("lbl_mid_name")
        self.gridLayout.addWidget(self.lbl_mid_name, 4, 0, 1, 1)
        self.lbl_last_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_last_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_last_name.setObjectName("lbl_last_name")
        self.gridLayout.addWidget(self.lbl_last_name, 4, 3, 1, 1)
        self.lbl_first_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_first_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_first_name.setObjectName("lbl_first_name")
        self.gridLayout.addWidget(self.lbl_first_name, 3, 0, 1, 1)
        self.lbl_email = QtWidgets.QLabel(self.groupBox)
        self.lbl_email.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_email.setObjectName("lbl_email")
        self.gridLayout.addWidget(self.lbl_email, 7, 3, 1, 1)
        self.lbl_phone = QtWidgets.QLabel(self.groupBox)
        self.lbl_phone.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_phone.setObjectName("lbl_phone")
        self.gridLayout.addWidget(self.lbl_phone, 7, 0, 1, 1)
        self.lbl_birthday = QtWidgets.QLabel(self.groupBox)
        self.lbl_birthday.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_birthday.setObjectName("lbl_birthday")
        self.gridLayout.addWidget(self.lbl_birthday, 3, 3, 1, 1)
        self.lbl_kor_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_kor_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_kor_name.setObjectName("lbl_kor_name")
        self.gridLayout.addWidget(self.lbl_kor_name, 0, 0, 1, 1)
        self.de_dob = QtWidgets.QDateEdit(self.groupBox)
        self.de_dob.setCalendarPopup(True)
        self.de_dob.setObjectName("de_dob")
        self.gridLayout.addWidget(self.de_dob, 3, 4, 1, 1)
        self.tb_kor_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_kor_name.setObjectName("tb_kor_name")
        self.gridLayout.addWidget(self.tb_kor_name, 0, 1, 1, 1)
        self.tb_first_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_first_name.setObjectName("tb_first_name")
        self.gridLayout.addWidget(self.tb_first_name, 3, 1, 1, 1)
        self.tb_mid_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_mid_name.setObjectName("tb_mid_name")
        self.gridLayout.addWidget(self.tb_mid_name, 4, 1, 1, 1)
        self.tb_phone = QtWidgets.QLineEdit(self.groupBox)
        self.tb_phone.setObjectName("tb_phone")
        self.gridLayout.addWidget(self.tb_phone, 7, 1, 1, 1)
        self.tb_last_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_last_name.setObjectName("tb_last_name")
        self.gridLayout.addWidget(self.tb_last_name, 4, 4, 1, 1)
        self.tb_email = QtWidgets.QLineEdit(self.groupBox)
        self.tb_email.setObjectName("tb_email")
        self.gridLayout.addWidget(self.tb_email, 7, 4, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb_gender_male = QtWidgets.QRadioButton(self.frame_3)
        self.rb_gender_male.setObjectName("rb_gender_male")
        self.horizontalLayout.addWidget(self.rb_gender_male)
        self.rb_gender_female = QtWidgets.QRadioButton(self.frame_3)
        self.rb_gender_female.setObjectName("rb_gender_female")
        self.horizontalLayout.addWidget(self.rb_gender_female)
        self.gridLayout.addWidget(self.frame_3, 0, 4, 1, 1)
        self.lbl_gender = QtWidgets.QLabel(self.groupBox)
        self.lbl_gender.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_gender.setObjectName("lbl_gender")
        self.gridLayout.addWidget(self.lbl_gender, 0, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_baptism_date = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_baptism_date.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_baptism_date.setObjectName("lbl_baptism_date")
        self.gridLayout_2.addWidget(self.lbl_baptism_date, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)
        self.lbl_register_date = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_register_date.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_register_date.setObjectName("lbl_register_date")
        self.gridLayout_2.addWidget(self.lbl_register_date, 0, 0, 1, 1)
        self.de_reg = QtWidgets.QDateEdit(self.groupBox_2)
        self.de_reg.setCalendarPopup(True)
        self.de_reg.setObjectName("de_reg")
        self.gridLayout_2.addWidget(self.de_reg, 0, 1, 1, 1)
        self.lbl_baptism_place = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_baptism_place.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_baptism_place.setObjectName("lbl_baptism_place")
        self.gridLayout_2.addWidget(self.lbl_baptism_place, 2, 0, 1, 1)
        self.lbl_new_family_study = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_new_family_study.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_new_family_study.setObjectName("lbl_new_family_study")
        self.gridLayout_2.addWidget(self.lbl_new_family_study, 6, 0, 1, 1)
        self.chk_new_family_study = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_new_family_study.setObjectName("chk_new_family_study")
        self.gridLayout_2.addWidget(self.chk_new_family_study, 6, 1, 1, 1)
        self.chk_new_comer_study = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_new_comer_study.setObjectName("chk_new_comer_study")
        self.gridLayout_2.addWidget(self.chk_new_comer_study, 5, 1, 1, 1)
        self.lbl_new_comer_study = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_new_comer_study.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_new_comer_study.setObjectName("lbl_new_comer_study")
        self.gridLayout_2.addWidget(self.lbl_new_comer_study, 5, 0, 1, 1)
        self.lbl_duty = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_duty.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_duty.setObjectName("lbl_duty")
        self.gridLayout_2.addWidget(self.lbl_duty, 4, 0, 1, 1)
        self.cb_duty = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_duty.setObjectName("cb_duty")
        self.gridLayout_2.addWidget(self.cb_duty, 4, 1, 1, 1)
        self.lbl_baptism_by = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_baptism_by.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_baptism_by.setObjectName("lbl_baptism_by")
        self.gridLayout_2.addWidget(self.lbl_baptism_by, 3, 0, 1, 1)
        self.de_bap = QtWidgets.QDateEdit(self.groupBox_2)
        self.de_bap.setCalendarPopup(True)
        self.de_bap.setObjectName("de_bap")
        self.gridLayout_2.addWidget(self.de_bap, 1, 1, 1, 1)
        self.tb_baptism_place = QtWidgets.QLineEdit(self.groupBox_2)
        self.tb_baptism_place.setObjectName("tb_baptism_place")
        self.gridLayout_2.addWidget(self.tb_baptism_place, 2, 1, 1, 1)
        self.tb_baptism_by = QtWidgets.QLineEdit(self.groupBox_2)
        self.tb_baptism_by.setObjectName("tb_baptism_by")
        self.gridLayout_2.addWidget(self.tb_baptism_by, 3, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chk_john = QtWidgets.QCheckBox(self.frame_4)
        self.chk_john.setObjectName("chk_john")
        self.horizontalLayout_3.addWidget(self.chk_john)
        self.chk_romans = QtWidgets.QCheckBox(self.frame_4)
        self.chk_romans.setObjectName("chk_romans")
        self.horizontalLayout_3.addWidget(self.chk_romans)
        self.chk_timothy = QtWidgets.QCheckBox(self.frame_4)
        self.chk_timothy.setObjectName("chk_timothy")
        self.horizontalLayout_3.addWidget(self.chk_timothy)
        self.gridLayout_2.addWidget(self.frame_4, 7, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_show = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_show.setObjectName("btn_show")
        self.verticalLayout_3.addWidget(self.btn_show)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.btn_save = QtWidgets.QPushButton(self.frame_2)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add New Member"))
        self.groupBox.setTitle(_translate("MainWindow", "Personal Information"))
        self.lbl_mid_name.setText(_translate("MainWindow", "Middle Name"))
        self.lbl_last_name.setText(_translate("MainWindow", "Last Name"))
        self.lbl_first_name.setText(_translate("MainWindow", "First Name"))
        self.lbl_email.setText(_translate("MainWindow", "E-Mail"))
        self.lbl_phone.setText(_translate("MainWindow", " Phone"))
        self.lbl_birthday.setText(_translate("MainWindow", "Date of Birth"))
        self.lbl_kor_name.setText(_translate("MainWindow", "Korean Name"))
        self.de_dob.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.rb_gender_male.setText(_translate("MainWindow", "Male"))
        self.rb_gender_female.setText(_translate("MainWindow", "Female"))
        self.lbl_gender.setText(_translate("MainWindow", "Gender"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Believer Information"))
        self.lbl_baptism_date.setText(_translate("MainWindow", "Baptism Date"))
        self.label_12.setText(_translate("MainWindow", "Bible Study"))
        self.lbl_register_date.setText(_translate("MainWindow", "Registration Date"))
        self.de_reg.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.lbl_baptism_place.setText(_translate("MainWindow", "Baptism Site"))
        self.lbl_new_family_study.setText(_translate("MainWindow", "New Family Study"))
        self.chk_new_family_study.setText(_translate("MainWindow", "complete"))
        self.chk_new_comer_study.setText(_translate("MainWindow", "complete"))
        self.lbl_new_comer_study.setText(_translate("MainWindow", "Newcomer Study"))
        self.lbl_duty.setText(_translate("MainWindow", "Duty"))
        self.lbl_baptism_by.setText(_translate("MainWindow", "Baptism"))
        self.de_bap.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.chk_john.setText(_translate("MainWindow", "John"))
        self.chk_romans.setText(_translate("MainWindow", "Romans"))
        self.chk_timothy.setText(_translate("MainWindow", "Timothy"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Family Infomation"))
        self.btn_show.setText(_translate("MainWindow", "Show"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))