#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#~ Copyright (C) 2014 Carlos Manuel Ferras Hernandez
#~ This file is part of LF02_package.

#~ LF02_package is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ LF02_package is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with LF02_package.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
from PyQt4 import QtCore  
from PyQt4 import QtGui 
from functools import partial
from UI.style import *
from UI import MainWindows
from config import config


from Dialogs.fontSelect import fontS 
from Dialogs.about import about
from GenSecLib import createXML,loadXML

def cursorAction():
	def decorador(fun):
		def interna(self,*arg):
			self.form1.setCursor(QtCore.Qt.WaitCursor)
			fun(self,*arg)
			self.form1.setCursor(QtCore.Qt.ArrowCursor)
		return interna
	return decorador
	
	
def seguro(msg):
	def decorador(fun):
		def interna(self,*arg):
			ret = QtGui.QMessageBox.warning(self.form1,QtGui.QApplication.translate('MainWindow','Attention!'),msg,QtGui.QMessageBox.No,QtGui.QMessageBox.Yes)
			if ret==QtGui.QMessageBox.Yes:
				fun(self)
		return interna
	return decorador

class UI_base(MainWindows.Ui_MainWindow): 
		def __init__(self,title,appIcon, parent=None):
			self.form1 =QtGui.QMainWindow()
			self.setupUi(self.form1,title,appIcon)		
			
			#self.form1.show()
				
			self.comandos=8
			self.grupos=0
			
			self.form1.closeEvent=self.onCloseEvent
			
			self.actionGurdar.triggered.connect(self.save)
			self.actionGurdar_como.triggered.connect(self.saveAs)
			self.actionAbrir.triggered.connect(self.open)
			self.actionNuevo.triggered.connect(self.new)
			self.actionDfgfh.triggered.connect(self.salir)			
			self.actionImprimir.triggered.connect(self.imprimir)
			self.actionFuente.triggered.connect(self.font)
			self.actionPegar.triggered.connect(self.paste)
			self.actionCopiar.triggered.connect(self.copy)
			self.actionCortar.triggered.connect(self.cut)
			self.actionAyuda.triggered.connect(self.help)
			self.actionDir_defecto.triggered.connect(self.defaultLocation)
			self.actionOpacity.triggered.connect(self.setOpacity)
			self.actionEjecutar_GenSec.triggered.connect(self.runGenSec)
			self.actionEjecutar_GenRep.triggered.connect(self.runGenRep)
			self.actionEjecutar_Comando.triggered.connect(self.runCommand)
			#self.actionAcerda_de.triggered.connect(partial(about,self.form1,'ejemplo',QtGui.QApplication.translate("MainWindow", 'es un ejemplo', None, QtGui.QApplication.UnicodeUTF8),QtGui.QApplication.translate("MainWindow", 'descripcion', None, QtGui.QApplication.UnicodeUTF8),'1.0.0',"pixmaps/gensec.png"))
			
			lang= QtGui.QAction(self.form1)
			lang.setObjectName("lang")
			self.menuLanguage.addAction(lang)
			lang.setText(QtGui.QApplication.translate("MainWindow", 'locale', None, QtGui.QApplication.UnicodeUTF8))
			lang.triggered.connect(partial(self.changeLang, 'locale'))
			lang.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change the language to default language on your PC", None, QtGui.QApplication.UnicodeUTF8))
			lang= QtGui.QAction(self.form1)
			lang.setObjectName("lang")
			self.menuLanguage.addAction(lang)
			lang.setText('en')
			lang.triggered.connect(partial(self.changeLang, 'en'))
			lang.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change the language to ", None, QtGui.QApplication.UnicodeUTF8)+'" en "')
			for filePath in os.listdir('Locale'):
			    fileName  = os.path.basename(filePath)
			    fileMatch = re.match("LF02_package_([a-z]{2,}).qm", fileName)
			    if fileMatch:
					lang= QtGui.QAction(self.form1)
					lang.setObjectName("lang")
					self.menuLanguage.addAction(lang)
					lang.setText(QtCore.QString.fromUtf8(fileMatch.group(1)))
					lang.triggered.connect(partial(self.changeLang, QtCore.QString.fromUtf8(fileMatch.group(1))))
					lang.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change the language to ", None, QtGui.QApplication.UnicodeUTF8)+ '" '+QtCore.QString.fromUtf8(fileMatch.group(1))+' "')
			
			self.thereAreCanges=False
			
			self.config=config()			
			self.general_config=self.config.loadGeneral()			
			self.gensec_config=self.config.loadGenSec()
			
			if self.general_config:
				self.fuente=self.general_config[0]
				self.size=self.general_config[1]
				self.fileLocation=self.general_config[2]
				if self.fileLocation=='None':
					self.fileLocation=''
				self.opacity=float(self.general_config[3])				
				self.lang=self.general_config[4]				
				
				font = QtGui.QFont()
				font.setFamily(self.fuente)
				font.setPointSize(self.size)
				
				self.form1.setWindowOpacity(self.opacity)
			else:
				self.fuente='Novason'
				self.size=12
				self.fileLocation=''
				self.opacity=1
				self.lang=''
				
			if self.gensec_config:
				self.col1=self.gensec_config[0]
				self.col2=self.gensec_config[1]
				self.col3=self.gensec_config[2]
			else:
				self.col1='#6695df'
				self.col2='#4e72aa'
				self.col3='#8665df'

			
			self.directorioArchivo=''
			self.clipboard=[]
			self.processClipboard=''
			
			self.assistant= QtCore.QProcess()
			self.process_order_by_sample={}
			
			#self.processGenVis=QtCore.QProcess()
			self.processGenSec=QtCore.QProcess()
			self.processGenRep=QtCore.QProcess()
			
			self.dirToOpen=''
		
		#App Run--------------------------------------------------------------------------------------------------------------------------------------
		def runCommand(self):
			pass			

		def runGenRep(self):
			"""Ejecuta GenRep"""
			self.closeAllDialogs()
			try:	
				if (self.processGenRep.state() != QtCore.QProcess.Running):
					self.beforeGenRep()
					print self.dirToOpen				
					self.processGenRep.start('python genrep.py '+self.dirToOpen)
					self.afterGenRep()
			except:
				self.error(QtGui.QApplication.translate('MainWindow','Unable to launch GenRep'))
		
		def beforeGenRep(self):
			pass
		def afterGenRep(self):
			pass
		
		def runGenSec(self):
			"""Ejecuta GenSec"""
			self.closeAllDialogs()
			try:
				if (self.processGenSec.state() != QtCore.QProcess.Running):
					self.beforeGenSec()
					self.processGenSec.start('python gensec.py '+self.dirToOpen)
					self.afterGenSec()
			except:
				self.error(QtGui.QApplication.translate('MainWindow','Unable to launch GenSec'))
		
		def beforeGenSec(self):
			pass
		def afterGenSec(self):
			pass
		
		#Options-----------------------------------------------------------------------------------------------------------------------------------------
		def changeLang(self,lang):
			"""cambia el idioma por defecto de la aplicacion"""
			self.lang=lang
			QtGui.QMessageBox.about(self.form1, "GenSec", QtGui.QApplication.translate('MainWindow','To save the changes you must restart'))
			
		
		def setOpacity(self):
			"""Abre una ventana para cambiar la opacidad de la ventana"""
			self.closeAllDialogs()
			dialog=QtGui.QDialog(self.form1)
			dialog.setGeometry(QtCore.QRect(0, 0, 170, 70));	
			
			horizontalSlider=QtGui.QSlider(dialog)
			horizontalSlider.setGeometry(QtCore.QRect(5,5, 160, 20));
			horizontalSlider.setOrientation(QtCore.Qt.Horizontal);
			horizontalSlider.setMinimum(80)
			horizontalSlider.setValue(self.opacity*100)
			
			def opacity():
				"""Cambia la opacidad de la ventana"""
				self.opacity=horizontalSlider.value()/100.0
				self.form1.setWindowOpacity(self.opacity)
				dialog.close()
				
			def cancel():
				"""Pone la opacidad como estaba anteriormente a la vista previa"""
				self.form1.setWindowOpacity(self.opacity)
				dialog.close()
				
			def preview():
				"""Vista previa de la opacidad que esta modificando el usuario"""
				o=horizontalSlider.value()/100.0
				self.form1.setWindowOpacity(o)
				
			def hide(event):
				"""Ajusta la opacidad de la ventana"""
				self.form1.setWindowOpacity(self.opacity)
			
			button=QtGui.QPushButton(QtGui.QApplication.translate('MainWindow','Aply'),dialog)
			button.setGeometry(QtCore.QRect(108,30, 60, 25));
			button.clicked.connect(opacity)
			
			button2=QtGui.QPushButton(QtGui.QApplication.translate('MainWindow','Cancel'),dialog)
			button2.setGeometry(QtCore.QRect(40,30, 60, 25));
			button2.clicked.connect(cancel)
			
			horizontalSlider.valueChanged.connect(preview)
			horizontalSlider.hideEvent =hide
			
			dialog.exec_()	
			
			
		def defaultLocation(self):
			"""Para escoger el directorio por defecto donde se van a guardar los archivos, y de donde seran cargados"""
			self.closeAllDialogs()
			self.fileLocation=QtGui.QFileDialog.getExistingDirectory (self.form1,'', self.fileLocation)
			if not self.fileLocation:
				self.fileLocation=''
		
		
		def font(self):
			"""Crea la ventana para escoger tipo y tamanno de fuente"""
			self.closeAllDialogs()
			try:
				self.fontS.form1.close()
			except:
				pass
			self.fontS=fontS(self.form1,self.fuente,self.size)
			self.fontS.pushButton.clicked.connect(self.change)
			
			
		def change(self):
			"""Cambia el tipo de letra y el tamanno de los elementos de la tabla"""
			pass
		
		#Edit-----------------------------------------------------------------------------------------------------------------------------------------		
		def new(self):
			"""Borra toda la informacion actual para comenzar desde cero"""
			pass			
		
		@cursorAction()
		def save(self,temp=False):
			"""Guarda la informacion en forma de xml"""
			pass		
		
		@cursorAction()
		def open(self,dir=False):
			"""Ventana para abrir un documento existente"""
			pass			
		
		@cursorAction()
		def saveAs(self,dir=False):
			"""Ventana para guardar un documanto"""
			pass		
		
		@cursorAction()
		def paste(self,temp=False):
			"""Pega en todas las casillas seleccionadas el texto k esta en el clipboard"""
			pass			
		
		@cursorAction()
		def copy(self,temp=False):
			"""Copia el texto de la casilla seleccionada en el clipboard"""
			pass			
		
		@cursorAction()
		def cut(self,temp=False):
			"""Corta el texto en la casilla seleccionada en el clipboard"""
			pass				
				
		@cursorAction()
		def imprimir(self,temp=False):
			"""Imprime toda la informacion de la aplicacion"""
			pass	
		
		
		#Others--------------------------------------------------------------------------------------------------------------------------
		def help(self):
			"""Corre la ayuda de la aplicacion"""
			self.closeAllDialogs()			
			if (self.assistant.state() != QtCore.QProcess.Running):
				self.assistant.start('python asistente.py')
		
		
		def error(self,text):
			"""Muestra una ventana de error"""
			self.closeAllDialogs()
			msgBox = QtGui.QMessageBox(self.form1)
			msgBox.setWindowTitle(QtGui.QApplication.translate('MainWindow','Error'))
			msgBox.setStyleSheet(ERROR_STYLE)
			msgBox.setText(text)
			msgBox.addButton(QtGui.QPushButton(QtGui.QApplication.translate('MainWindow','Accept')), QtGui.QMessageBox.YesRole)
			ret = msgBox.exec_()
			
		def salir(self):
			"""Cierra la ventana activa, si es La ventana principal, las cierra todas"""
			self.closeAllDialogs()
			self.form1.close()
			
		
		def onCloseEvent(self,event):
			"""Se ejecuta al cerrar la aplicacion, pregunta si desa guardar los cambios"""
			pass
		
		
		def question(self):
			"""Ventana para preguntar si se desean guardar los cambios"""
			if self.thereAreCanges==True:
				msgBox = QtGui.QMessageBox(self.form1)
				msgBox.setWindowTitle('GenSec')
				msgBox.setText(QtGui.QApplication.translate('MainWindow','Save changes?'))
				msgBox.addButton(QtGui.QPushButton(QtGui.QApplication.translate('MainWindow','Cancel')), QtGui.QMessageBox.DestructiveRole)
				msgBox.addButton(QtGui.QPushButton(QtGui.QApplication.translate('MainWindow','No')), QtGui.QMessageBox.NoRole)
				msgBox.addButton(QtGui.QPushButton(QtGui.QApplication.translate('MainWindow','Yes')), QtGui.QMessageBox.YesRole)
				ret = msgBox.exec_()
				return ret
			else:
				return 1
	
		
		def closeAllDialogs(self):
			"""Cuando se ejecuta se cierran todas las ventanas de Comandos"""
			try:
				self.fontS.form1.close()
			except:
				pass
			try:
				self.priview.form1.close()
			except:
				pass
			self.closeRestantDialogs()
				
		
		def closeRestantDialogs(self):
			pass
		