# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'irradiation.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_process(object):
    def setupUi(self, process):
        process.setObjectName("process")
        process.resize(577, 222)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(process.sizePolicy().hasHeightForWidth())
        process.setSizePolicy(sizePolicy)
        process.setMinimumSize(QtCore.QSize(0, 0))
        process.setMaximumSize(QtCore.QSize(16777215, 222))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(process)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.form_area = QtWidgets.QFrame(process)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_area.sizePolicy().hasHeightForWidth())
        self.form_area.setSizePolicy(sizePolicy)
        self.form_area.setFrameShape(QtWidgets.QFrame.Box)
        self.form_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_area.setObjectName("form_area")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.form_area)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setObjectName("layout")
        self.irradiation_source_label = QtWidgets.QLabel(self.form_area)
        self.irradiation_source_label.setObjectName("irradiation_source_label")
        self.layout.addWidget(self.irradiation_source_label)
        self.irradiation_source = QtWidgets.QComboBox(self.form_area)
        self.irradiation_source.setMinimumSize(QtCore.QSize(90, 28))
        self.irradiation_source.setMaximumSize(QtCore.QSize(90, 16777215))
        self.irradiation_source.setObjectName("irradiation_source")
        self.irradiation_source.addItem("")
        self.irradiation_source.addItem("")
        self.layout.addWidget(self.irradiation_source)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.layout)
        self.line = QtWidgets.QFrame(self.form_area)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.layout_2 = QtWidgets.QHBoxLayout()
        self.layout_2.setSpacing(15)
        self.layout_2.setObjectName("layout_2")
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_3.setObjectName("layout_3")
        self.time_label = QtWidgets.QLabel(self.form_area)
        self.time_label.setObjectName("time_label")
        self.layout_3.addWidget(self.time_label)
        self.time = QtWidgets.QDoubleSpinBox(self.form_area)
        self.time.setMinimumSize(QtCore.QSize(80, 28))
        self.time.setMaximumSize(QtCore.QSize(80, 16777215))
        self.time.setMaximum(99999.0)
        self.time.setObjectName("time")
        self.layout_3.addWidget(self.time)
        self.layout_2.addLayout(self.layout_3)
        self.layout_4 = QtWidgets.QHBoxLayout()
        self.layout_4.setObjectName("layout_4")
        self.dose_label = QtWidgets.QLabel(self.form_area)
        self.dose_label.setObjectName("dose_label")
        self.layout_4.addWidget(self.dose_label)
        self.dose = QtWidgets.QLabel(self.form_area)
        self.dose.setObjectName("dose")
        self.layout_4.addWidget(self.dose)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_4.addItem(spacerItem1)
        self.layout_2.addLayout(self.layout_4)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.layout_2)
        self.line_2 = QtWidgets.QFrame(self.form_area)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.layout_5 = QtWidgets.QHBoxLayout()
        self.layout_5.setSpacing(15)
        self.layout_5.setObjectName("layout_5")
        self.layout_6 = QtWidgets.QHBoxLayout()
        self.layout_6.setObjectName("layout_6")
        self.stabilization_label = QtWidgets.QLabel(self.form_area)
        self.stabilization_label.setObjectName("stabilization_label")
        self.layout_6.addWidget(self.stabilization_label)
        self.stabilization = QtWidgets.QDoubleSpinBox(self.form_area)
        self.stabilization.setMinimumSize(QtCore.QSize(80, 28))
        self.stabilization.setMaximumSize(QtCore.QSize(80, 16777215))
        self.stabilization.setMaximum(99999.0)
        self.stabilization.setObjectName("stabilization")
        self.layout_6.addWidget(self.stabilization)
        self.layout_5.addLayout(self.layout_6)
        self.layout_7 = QtWidgets.QHBoxLayout()
        self.layout_7.setObjectName("layout_7")
        self.heating_rate_label = QtWidgets.QLabel(self.form_area)
        self.heating_rate_label.setObjectName("heating_rate_label")
        self.layout_7.addWidget(self.heating_rate_label)
        self.heating_rate = QtWidgets.QDoubleSpinBox(self.form_area)
        self.heating_rate.setMinimumSize(QtCore.QSize(80, 28))
        self.heating_rate.setMaximumSize(QtCore.QSize(80, 16777215))
        self.heating_rate.setMinimum(0.1)
        self.heating_rate.setMaximum(20.0)
        self.heating_rate.setObjectName("heating_rate")
        self.layout_7.addWidget(self.heating_rate)
        self.layout_5.addLayout(self.layout_7)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.layout_5)
        self.layout_8 = QtWidgets.QHBoxLayout()
        self.layout_8.setObjectName("layout_8")
        self.final_temperature_label = QtWidgets.QLabel(self.form_area)
        self.final_temperature_label.setObjectName("final_temperature_label")
        self.layout_8.addWidget(self.final_temperature_label)
        self.final_temperature = QtWidgets.QDoubleSpinBox(self.form_area)
        self.final_temperature.setMinimumSize(QtCore.QSize(80, 28))
        self.final_temperature.setMaximumSize(QtCore.QSize(80, 16777215))
        self.final_temperature.setMaximum(600.0)
        self.final_temperature.setObjectName("final_temperature")
        self.layout_8.addWidget(self.final_temperature)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.layout_8)
        self.horizontalLayout_7.addWidget(self.form_area)
        self.buttons_area = QtWidgets.QFrame(process)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_area.sizePolicy().hasHeightForWidth())
        self.buttons_area.setSizePolicy(sizePolicy)
        self.buttons_area.setMinimumSize(QtCore.QSize(0, 0))
        self.buttons_area.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttons_area.setFrameShape(QtWidgets.QFrame.Box)
        self.buttons_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_area.setObjectName("buttons_area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.buttons_area)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.push_button_accept = QtWidgets.QPushButton(self.buttons_area)
        self.push_button_accept.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_accept.setShortcut("Return")
        self.push_button_accept.setObjectName("push_button_accept")
        self.verticalLayout_2.addWidget(self.push_button_accept)
        self.push_button_cancel = QtWidgets.QPushButton(self.buttons_area)
        self.push_button_cancel.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_cancel.setShortcut("Esc")
        self.push_button_cancel.setObjectName("push_button_cancel")
        self.verticalLayout_2.addWidget(self.push_button_cancel)
        self.push_button_information = QtWidgets.QPushButton(self.buttons_area)
        self.push_button_information.setMinimumSize(QtCore.QSize(100, 32))
        self.push_button_information.setObjectName("push_button_information")
        self.verticalLayout_2.addWidget(self.push_button_information)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_7.addWidget(self.buttons_area)

        self.retranslateUi(process)
        QtCore.QMetaObject.connectSlotsByName(process)

    def retranslateUi(self, process):
        _translate = QtCore.QCoreApplication.translate
        process.setWindowTitle(_translate("process", "Irradiation"))
        self.irradiation_source_label.setText(_translate("process", "Irradiation Source"))
        self.irradiation_source.setItemText(0, _translate("process", "Beta"))
        self.irradiation_source.setItemText(1, _translate("process", "External"))
        self.time_label.setText(_translate("process", "Time (s)"))
        self.dose_label.setText(_translate("process", "Dose (Gy):"))
        self.dose.setText(_translate("process", "0.0"))
        self.stabilization_label.setText(_translate("process", "Stabilization (s)"))
        self.heating_rate_label.setText(_translate("process", "Heating Rate (°C/s)"))
        self.final_temperature_label.setText(_translate("process", "Final Temperature (°C)"))
        self.push_button_accept.setText(_translate("process", "Accept"))
        self.push_button_cancel.setText(_translate("process", "Cancel"))
        self.push_button_information.setText(_translate("process", "Information"))

