# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/view_list.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewList(object):
    def setupUi(self, ViewList):
        ViewList.setObjectName("ViewList")
        ViewList.resize(559, 535)
        self.centralWidget = QtWidgets.QWidget(ViewList)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_name_input = QtWidgets.QLabel(self.frame)
        self.lbl_name_input.setObjectName("lbl_name_input")
        self.gridLayout.addWidget(self.lbl_name_input, 0, 0, 1, 1)
        self.tb_name_input = QtWidgets.QLineEdit(self.frame)
        self.tb_name_input.setObjectName("tb_name_input")
        self.gridLayout.addWidget(self.tb_name_input, 0, 1, 1, 1)
        self.btn_search = QtWidgets.QPushButton(self.frame)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout.addWidget(self.btn_search, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.tv_list = QtWidgets.QTableView(self.centralWidget)
        self.tv_list.setObjectName("tv_list")
        self.verticalLayout.addWidget(self.tv_list)
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_edit = QtWidgets.QPushButton(self.frame_2)
        self.btn_edit.setObjectName("btn_edit")
        self.gridLayout_2.addWidget(self.btn_edit, 0, 3, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.frame_2)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout_2.addWidget(self.btn_delete, 0, 2, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.frame_2)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 0, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        ViewList.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(ViewList)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 559, 22))
        self.menuBar.setDefaultUp(True)
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        ViewList.setMenuBar(self.menuBar)
        self.actionfiles = QtWidgets.QAction(ViewList)
        self.actionfiles.setObjectName("actionfiles")
        self.actionnew = QtWidgets.QAction(ViewList)
        self.actionnew.setObjectName("actionnew")
        self.actionedit = QtWidgets.QAction(ViewList)
        self.actionedit.setObjectName("actionedit")
        self.menuMenu.addAction(self.actionfiles)
        self.menuMenu.addAction(self.actionnew)
        self.menuMenu.addAction(self.actionedit)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(ViewList)
        QtCore.QMetaObject.connectSlotsByName(ViewList)

    def retranslateUi(self, ViewList):
        _translate = QtCore.QCoreApplication.translate
        ViewList.setWindowTitle(_translate("ViewList", "Add New Member"))
        self.lbl_name_input.setText(_translate("ViewList", "Enter name:"))
        self.btn_search.setText(_translate("ViewList", "Search"))
        self.btn_edit.setText(_translate("ViewList", "Edit"))
        self.btn_delete.setText(_translate("ViewList", "Delete"))
        self.btn_add.setText(_translate("ViewList", "Add"))
        self.btn_cancel.setText(_translate("ViewList", "Cancel"))
        self.menuMenu.setTitle(_translate("ViewList", "Menu"))
        self.actionfiles.setText(_translate("ViewList", "files"))
        self.actionnew.setText(_translate("ViewList", "new"))
        self.actionedit.setText(_translate("ViewList", "edit"))

