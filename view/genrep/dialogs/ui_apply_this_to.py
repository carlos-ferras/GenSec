# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/krl1to5/Work/FULL/Sequence-ToolKit/2016/resources/ui/genrep/dialogs/apply_this_to.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_apply_to(object):
    def setupUi(self, apply_to):
        apply_to.setObjectName("apply_to")
        apply_to.resize(558, 285)
        self.verticalLayout = QtWidgets.QVBoxLayout(apply_to)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.form_area = QtWidgets.QFrame(apply_to)
        self.form_area.setFrameShape(QtWidgets.QFrame.Box)
        self.form_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_area.setObjectName("form_area")
        self.gridLayout = QtWidgets.QGridLayout(self.form_area)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.condition_label = QtWidgets.QLabel(self.form_area)
        self.condition_label.setObjectName("condition_label")
        self.gridLayout.addWidget(self.condition_label, 0, 1, 1, 1)
        self.condition_4 = QtWidgets.QComboBox(self.form_area)
        self.condition_4.setEnabled(False)
        self.condition_4.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_4.setObjectName("condition_4")
        self.condition_4.addItem("")
        self.condition_4.addItem("")
        self.condition_4.addItem("")
        self.condition_4.addItem("")
        self.gridLayout.addWidget(self.condition_4, 4, 1, 1, 1)
        self.condition_2 = QtWidgets.QComboBox(self.form_area)
        self.condition_2.setEnabled(False)
        self.condition_2.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_2.setObjectName("condition_2")
        self.condition_2.addItem("")
        self.condition_2.addItem("")
        self.condition_2.addItem("")
        self.condition_2.addItem("")
        self.gridLayout.addWidget(self.condition_2, 2, 1, 1, 1)
        self.criterion_2 = QtWidgets.QComboBox(self.form_area)
        self.criterion_2.setEnabled(False)
        self.criterion_2.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_2.setObjectName("criterion_2")
        self.criterion_2.addItem("")
        self.criterion_2.addItem("")
        self.criterion_2.addItem("")
        self.criterion_2.addItem("")
        self.gridLayout.addWidget(self.criterion_2, 2, 0, 1, 1)
        self.value_1 = QtWidgets.QLineEdit(self.form_area)
        self.value_1.setEnabled(False)
        self.value_1.setMinimumSize(QtCore.QSize(160, 28))
        self.value_1.setObjectName("value_1")
        self.gridLayout.addWidget(self.value_1, 1, 2, 1, 1)
        self.criterion_1 = QtWidgets.QComboBox(self.form_area)
        self.criterion_1.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_1.setObjectName("criterion_1")
        self.criterion_1.addItem("")
        self.criterion_1.addItem("")
        self.criterion_1.addItem("")
        self.criterion_1.addItem("")
        self.gridLayout.addWidget(self.criterion_1, 1, 0, 1, 1)
        self.value_2 = QtWidgets.QLineEdit(self.form_area)
        self.value_2.setEnabled(False)
        self.value_2.setMinimumSize(QtCore.QSize(160, 28))
        self.value_2.setObjectName("value_2")
        self.gridLayout.addWidget(self.value_2, 2, 2, 1, 1)
        self.condition_3 = QtWidgets.QComboBox(self.form_area)
        self.condition_3.setEnabled(False)
        self.condition_3.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_3.setObjectName("condition_3")
        self.condition_3.addItem("")
        self.condition_3.addItem("")
        self.condition_3.addItem("")
        self.condition_3.addItem("")
        self.gridLayout.addWidget(self.condition_3, 3, 1, 1, 1)
        self.value_4 = QtWidgets.QLineEdit(self.form_area)
        self.value_4.setEnabled(False)
        self.value_4.setMinimumSize(QtCore.QSize(160, 28))
        self.value_4.setObjectName("value_4")
        self.gridLayout.addWidget(self.value_4, 4, 2, 1, 1)
        self.criterion_4 = QtWidgets.QComboBox(self.form_area)
        self.criterion_4.setEnabled(False)
        self.criterion_4.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_4.setObjectName("criterion_4")
        self.criterion_4.addItem("")
        self.criterion_4.addItem("")
        self.criterion_4.addItem("")
        self.criterion_4.addItem("")
        self.gridLayout.addWidget(self.criterion_4, 4, 0, 1, 1)
        self.value_label = QtWidgets.QLabel(self.form_area)
        self.value_label.setObjectName("value_label")
        self.gridLayout.addWidget(self.value_label, 0, 2, 1, 1)
        self.criterion_label = QtWidgets.QLabel(self.form_area)
        self.criterion_label.setObjectName("criterion_label")
        self.gridLayout.addWidget(self.criterion_label, 0, 0, 1, 1)
        self.criterion_3 = QtWidgets.QComboBox(self.form_area)
        self.criterion_3.setEnabled(False)
        self.criterion_3.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_3.setObjectName("criterion_3")
        self.criterion_3.addItem("")
        self.criterion_3.addItem("")
        self.criterion_3.addItem("")
        self.criterion_3.addItem("")
        self.gridLayout.addWidget(self.criterion_3, 3, 0, 1, 1)
        self.value_3 = QtWidgets.QLineEdit(self.form_area)
        self.value_3.setEnabled(False)
        self.value_3.setMinimumSize(QtCore.QSize(160, 28))
        self.value_3.setObjectName("value_3")
        self.gridLayout.addWidget(self.value_3, 3, 2, 1, 1)
        self.condition_1 = QtWidgets.QComboBox(self.form_area)
        self.condition_1.setEnabled(False)
        self.condition_1.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_1.setObjectName("condition_1")
        self.condition_1.addItem("")
        self.condition_1.addItem("")
        self.condition_1.addItem("")
        self.condition_1.addItem("")
        self.gridLayout.addWidget(self.condition_1, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.form_area)
        self.line = QtWidgets.QFrame(apply_to)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.buttons_area = QtWidgets.QHBoxLayout()
        self.buttons_area.setSpacing(10)
        self.buttons_area.setObjectName("buttons_area")
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_area.addItem(spacerItem)
        self.push_button_apply_to_all = QtWidgets.QPushButton(apply_to)
        self.push_button_apply_to_all.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_apply_to_all.setObjectName("push_button_apply_to_all")
        self.buttons_area.addWidget(self.push_button_apply_to_all)
        self.push_button_accept = QtWidgets.QPushButton(apply_to)
        self.push_button_accept.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_accept.setObjectName("push_button_accept")
        self.buttons_area.addWidget(self.push_button_accept)
        self.push_button_cancel = QtWidgets.QPushButton(apply_to)
        self.push_button_cancel.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_cancel.setObjectName("push_button_cancel")
        self.buttons_area.addWidget(self.push_button_cancel)
        self.verticalLayout.addLayout(self.buttons_area)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(apply_to)
        QtCore.QMetaObject.connectSlotsByName(apply_to)

    def retranslateUi(self, apply_to):
        _translate = QtCore.QCoreApplication.translate
        apply_to.setWindowTitle(_translate("apply_to", "Apply this to"))
        self.condition_label.setText(_translate("apply_to", "Condition"))
        self.condition_4.setItemText(0, _translate("apply_to", "<< select >>"))
        self.condition_4.setItemText(1, _translate("apply_to", "Same"))
        self.condition_4.setItemText(2, _translate("apply_to", "Different"))
        self.condition_4.setItemText(3, _translate("apply_to", "Value"))
        self.condition_2.setItemText(0, _translate("apply_to", "<< select >>"))
        self.condition_2.setItemText(1, _translate("apply_to", "Same"))
        self.condition_2.setItemText(2, _translate("apply_to", "Different"))
        self.condition_2.setItemText(3, _translate("apply_to", "Value"))
        self.criterion_2.setItemText(0, _translate("apply_to", "<< select >>"))
        self.criterion_2.setItemText(1, _translate("apply_to", "Sample ID"))
        self.criterion_2.setItemText(2, _translate("apply_to", "Process Order"))
        self.criterion_2.setItemText(3, _translate("apply_to", "Data Type"))
        self.criterion_1.setItemText(0, _translate("apply_to", "<< select >>"))
        self.criterion_1.setItemText(1, _translate("apply_to", "Sample ID"))
        self.criterion_1.setItemText(2, _translate("apply_to", "Process Order"))
        self.criterion_1.setItemText(3, _translate("apply_to", "Data Type"))
        self.condition_3.setItemText(0, _translate("apply_to", "<< select >>"))
        self.condition_3.setItemText(1, _translate("apply_to", "Same"))
        self.condition_3.setItemText(2, _translate("apply_to", "Different"))
        self.condition_3.setItemText(3, _translate("apply_to", "Value"))
        self.criterion_4.setItemText(0, _translate("apply_to", "<< select >>"))
        self.criterion_4.setItemText(1, _translate("apply_to", "Sample ID"))
        self.criterion_4.setItemText(2, _translate("apply_to", "Process Order"))
        self.criterion_4.setItemText(3, _translate("apply_to", "Data Type"))
        self.value_label.setText(_translate("apply_to", "Value"))
        self.criterion_label.setText(_translate("apply_to", "Criterion"))
        self.criterion_3.setItemText(0, _translate("apply_to", "<< select >>"))
        self.criterion_3.setItemText(1, _translate("apply_to", "Sample ID"))
        self.criterion_3.setItemText(2, _translate("apply_to", "Process Order"))
        self.criterion_3.setItemText(3, _translate("apply_to", "Data Type"))
        self.condition_1.setItemText(0, _translate("apply_to", "<< select >>"))
        self.condition_1.setItemText(1, _translate("apply_to", "Same"))
        self.condition_1.setItemText(2, _translate("apply_to", "Different"))
        self.condition_1.setItemText(3, _translate("apply_to", "Value"))
        self.push_button_apply_to_all.setText(_translate("apply_to", "Apply to all"))
        self.push_button_accept.setText(_translate("apply_to", "Accept"))
        self.push_button_accept.setShortcut(_translate("apply_to", "Return"))
        self.push_button_cancel.setText(_translate("apply_to", "Cancel"))
        self.push_button_cancel.setShortcut(_translate("apply_to", "Esc"))
