# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/krl1to5/Work/FULL/Sequence-ToolKit/2016/resources/ui/genrep/dialogs/association_by_criterion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_association(object):
    def setupUi(self, association):
        association.setObjectName("association")
        association.resize(566, 336)
        self.verticalLayout = QtWidgets.QVBoxLayout(association)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.form_area = QtWidgets.QFrame(association)
        self.form_area.setFrameShape(QtWidgets.QFrame.Box)
        self.form_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_area.setObjectName("form_area")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.form_area)
        self.verticalLayout_5.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.criterion_label = QtWidgets.QLabel(self.form_area)
        self.criterion_label.setObjectName("criterion_label")
        self.verticalLayout_2.addWidget(self.criterion_label)
        self.criterion_1 = QtWidgets.QComboBox(self.form_area)
        self.criterion_1.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_1.setObjectName("criterion_1")
        self.criterion_1.addItem("")
        self.criterion_1.addItem("")
        self.criterion_1.addItem("")
        self.criterion_1.addItem("")
        self.verticalLayout_2.addWidget(self.criterion_1)
        self.criterion_2 = QtWidgets.QComboBox(self.form_area)
        self.criterion_2.setEnabled(False)
        self.criterion_2.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_2.setObjectName("criterion_2")
        self.criterion_2.addItem("")
        self.criterion_2.addItem("")
        self.criterion_2.addItem("")
        self.criterion_2.addItem("")
        self.verticalLayout_2.addWidget(self.criterion_2)
        self.criterion_3 = QtWidgets.QComboBox(self.form_area)
        self.criterion_3.setEnabled(False)
        self.criterion_3.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_3.setObjectName("criterion_3")
        self.criterion_3.addItem("")
        self.criterion_3.addItem("")
        self.criterion_3.addItem("")
        self.criterion_3.addItem("")
        self.verticalLayout_2.addWidget(self.criterion_3)
        self.criterion_4 = QtWidgets.QComboBox(self.form_area)
        self.criterion_4.setEnabled(False)
        self.criterion_4.setMinimumSize(QtCore.QSize(160, 28))
        self.criterion_4.setObjectName("criterion_4")
        self.criterion_4.addItem("")
        self.criterion_4.addItem("")
        self.criterion_4.addItem("")
        self.criterion_4.addItem("")
        self.verticalLayout_2.addWidget(self.criterion_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.condition_label = QtWidgets.QLabel(self.form_area)
        self.condition_label.setObjectName("condition_label")
        self.verticalLayout_3.addWidget(self.condition_label)
        self.condition_1 = QtWidgets.QComboBox(self.form_area)
        self.condition_1.setEnabled(False)
        self.condition_1.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_1.setObjectName("condition_1")
        self.condition_1.addItem("")
        self.condition_1.addItem("")
        self.condition_1.addItem("")
        self.condition_1.addItem("")
        self.verticalLayout_3.addWidget(self.condition_1)
        self.condition_2 = QtWidgets.QComboBox(self.form_area)
        self.condition_2.setEnabled(False)
        self.condition_2.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_2.setObjectName("condition_2")
        self.condition_2.addItem("")
        self.condition_2.addItem("")
        self.condition_2.addItem("")
        self.condition_2.addItem("")
        self.verticalLayout_3.addWidget(self.condition_2)
        self.condition_3 = QtWidgets.QComboBox(self.form_area)
        self.condition_3.setEnabled(False)
        self.condition_3.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_3.setObjectName("condition_3")
        self.condition_3.addItem("")
        self.condition_3.addItem("")
        self.condition_3.addItem("")
        self.condition_3.addItem("")
        self.verticalLayout_3.addWidget(self.condition_3)
        self.condition_4 = QtWidgets.QComboBox(self.form_area)
        self.condition_4.setEnabled(False)
        self.condition_4.setMinimumSize(QtCore.QSize(160, 28))
        self.condition_4.setObjectName("condition_4")
        self.condition_4.addItem("")
        self.condition_4.addItem("")
        self.condition_4.addItem("")
        self.condition_4.addItem("")
        self.verticalLayout_3.addWidget(self.condition_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.value_label = QtWidgets.QLabel(self.form_area)
        self.value_label.setObjectName("value_label")
        self.verticalLayout_4.addWidget(self.value_label)
        self.value_1 = QtWidgets.QLineEdit(self.form_area)
        self.value_1.setEnabled(False)
        self.value_1.setMinimumSize(QtCore.QSize(160, 28))
        self.value_1.setObjectName("value_1")
        self.verticalLayout_4.addWidget(self.value_1)
        self.value_2 = QtWidgets.QLineEdit(self.form_area)
        self.value_2.setEnabled(False)
        self.value_2.setMinimumSize(QtCore.QSize(160, 28))
        self.value_2.setObjectName("value_2")
        self.verticalLayout_4.addWidget(self.value_2)
        self.value_3 = QtWidgets.QLineEdit(self.form_area)
        self.value_3.setEnabled(False)
        self.value_3.setMinimumSize(QtCore.QSize(160, 28))
        self.value_3.setObjectName("value_3")
        self.verticalLayout_4.addWidget(self.value_3)
        self.value_4 = QtWidgets.QLineEdit(self.form_area)
        self.value_4.setEnabled(False)
        self.value_4.setMinimumSize(QtCore.QSize(160, 28))
        self.value_4.setObjectName("value_4")
        self.verticalLayout_4.addWidget(self.value_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.form_area)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.consecutives = QtWidgets.QCheckBox(self.form_area)
        self.consecutives.setObjectName("consecutives")
        self.verticalLayout_5.addWidget(self.consecutives)
        self.verticalLayout.addWidget(self.form_area)
        self.line_2 = QtWidgets.QFrame(association)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.push_button_save = QtWidgets.QPushButton(association)
        self.push_button_save.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_save.setObjectName("push_button_save")
        self.horizontalLayout.addWidget(self.push_button_save)
        self.push_button_load = QtWidgets.QPushButton(association)
        self.push_button_load.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_load.setObjectName("push_button_load")
        self.horizontalLayout.addWidget(self.push_button_load)
        self.push_button_accept = QtWidgets.QPushButton(association)
        self.push_button_accept.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_accept.setObjectName("push_button_accept")
        self.horizontalLayout.addWidget(self.push_button_accept)
        self.push_button_cancel = QtWidgets.QPushButton(association)
        self.push_button_cancel.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_cancel.setObjectName("push_button_cancel")
        self.horizontalLayout.addWidget(self.push_button_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(association)
        QtCore.QMetaObject.connectSlotsByName(association)

    def retranslateUi(self, association):
        _translate = QtCore.QCoreApplication.translate
        association.setWindowTitle(_translate("association", "Association by Criterion"))
        self.criterion_label.setText(_translate("association", "Criterion"))
        self.criterion_1.setItemText(0, _translate("association", "<< select >>"))
        self.criterion_1.setItemText(1, _translate("association", "Sample ID"))
        self.criterion_1.setItemText(2, _translate("association", "Process Order"))
        self.criterion_1.setItemText(3, _translate("association", "Data Type"))
        self.criterion_2.setItemText(0, _translate("association", "<< select >>"))
        self.criterion_2.setItemText(1, _translate("association", "Sample ID"))
        self.criterion_2.setItemText(2, _translate("association", "Process Order"))
        self.criterion_2.setItemText(3, _translate("association", "Data Type"))
        self.criterion_3.setItemText(0, _translate("association", "<< select >>"))
        self.criterion_3.setItemText(1, _translate("association", "Sample ID"))
        self.criterion_3.setItemText(2, _translate("association", "Process Order"))
        self.criterion_3.setItemText(3, _translate("association", "Data Type"))
        self.criterion_4.setItemText(0, _translate("association", "<< select >>"))
        self.criterion_4.setItemText(1, _translate("association", "Sample ID"))
        self.criterion_4.setItemText(2, _translate("association", "Process Order"))
        self.criterion_4.setItemText(3, _translate("association", "Data Type"))
        self.condition_label.setText(_translate("association", "Condition"))
        self.condition_1.setItemText(0, _translate("association", "<< select >>"))
        self.condition_1.setItemText(1, _translate("association", "Same"))
        self.condition_1.setItemText(2, _translate("association", "Different"))
        self.condition_1.setItemText(3, _translate("association", "Value"))
        self.condition_2.setItemText(0, _translate("association", "<< select >>"))
        self.condition_2.setItemText(1, _translate("association", "Same"))
        self.condition_2.setItemText(2, _translate("association", "Different"))
        self.condition_2.setItemText(3, _translate("association", "Value"))
        self.condition_3.setItemText(0, _translate("association", "<< select >>"))
        self.condition_3.setItemText(1, _translate("association", "Same"))
        self.condition_3.setItemText(2, _translate("association", "Different"))
        self.condition_3.setItemText(3, _translate("association", "Value"))
        self.condition_4.setItemText(0, _translate("association", "<< select >>"))
        self.condition_4.setItemText(1, _translate("association", "Same"))
        self.condition_4.setItemText(2, _translate("association", "Different"))
        self.condition_4.setItemText(3, _translate("association", "Value"))
        self.value_label.setText(_translate("association", "Value"))
        self.consecutives.setText(_translate("association", "Group only consecutive commands."))
        self.push_button_save.setText(_translate("association", "Save"))
        self.push_button_load.setText(_translate("association", "Load"))
        self.push_button_accept.setText(_translate("association", "Accept"))
        self.push_button_cancel.setText(_translate("association", "Cancel"))

