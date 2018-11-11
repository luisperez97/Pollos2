# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QAbstractAnimation, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox, QWidget, QLabel
import re

import sys
sys.path.append('..')

#import Cliente.SocketCliente
import SocketCliente

#-----------------------------------------------------------------------VENTANA LOGIN----------------------
def estiloventanalogin(ventanalogin):
	ventanalogin.setStyleSheet("""
		#Ventana_Login{
			background-image: url(Imagenes/pollos.jpg);
		}
		#Widget_Login2{
			background-color: rgba(0, 0, 0, 160);
			border-radius: 10px;
			padding: 10px;
		}

		#QPushButtonLogin{
			background-color: gray;
			border-radius: 4px;
			color: #fff;
			font-family: Ubuntu;
			font-size: 17px;
		}

		#QPushButtonRegistro{
			background-color: white;
			border-radius: 4px;
			border: 2px solid #ff7043;
			font-family: Ubuntu;
			font-size: 17px;
		}
		#QPushButtonRegistro:hover{
			background-color: #ff5722;
			border: 2px solid white;
			color: white;
		}
		#QPushButtonRegistro:pressed{
			background-color: #ff7043;
			border: 2px solid #ff5722;
			color: white;
		}

		QLineEdit{
			border-radius: 10px;
			border: 2px solid #DB7093;
			padding: 5px;
			font-family: Ubuntu;
		}

		QLabel{
			font-family: Ubuntu;
		}

		#label_usuario, #label_password{
			font-size: 17px;
			color: whitesmoke;
			font-weight: bold;
		}

		#label_login{
			font-size:30px;
			color: #fff;
			font-weight: bold;
		}

		#label_olvido{
			font-size: 12px;
			color: white;
			text-decoration: underline;

		}
		#label_olvido:hover{
			color: 	#7FFF00;
		}

		#label_error{
			color: magenta;
			background-color: transparent;
		}
	""")

def estiloventanaolvidoclave(ventanaolvido):
	ventanaolvido.setStyleSheet("""
		#Ventana_Olvido{
			background-image: url(Imagenes/pollos3.jpg);
		}
		#widgetolvido{
			background-color: rgba(0, 0, 0, 160);
			border-radius: 10px;
			padding: 10px;
		}

		#Label_Usuario, #label_preguntasecreta, #label_respuestasecreta{
			background-color: transparent;
			color: whitesmoke;
		}

		#label_preguntasecreta2{
			color: white;
			text-decoration: underline;
		}

		#label_error{
			color: magenta;
			background-color: transparent;
		}

		#lineEdit_usuario, #lineEdit_respuesta{
			border-radius: 10px;
			border: 2px solid #DB7093;
			padding: 5px;
			font-family: Ubuntu;
		}
	""")

def estiloVentanaClaveNueva(ventanaclavenueva):
	ventanaclavenueva.setStyleSheet("""
		#Ventana_Clave_Nueva{
			border-image: url(Imagenes/pollos4.jpg);
		}

		#widgetclavenueva{
			background-color: rgba(0, 0, 0, 160);
			border-radius: 10px;
			padding: 10px;
		}

		#Label_Clave, #Label_Clave2, #labelUsuario{
			background-color: transparent;
			color: whitesmoke;
		}
		#labelUsuario2{
			color: white;
			text-decoration: underline;
		}

		#label_error{
			color: magenta;
			background-color: transparent;
		}

		#lineEdit_clave, #lineEdit_clave2{
			border-radius: 10px;
			border: 2px solid #DB7093;
			padding: 5px;
			font-family: Ubuntu;
		}
	""")

def estiloVentanaRegistro(ventanaregistro):
	ventanaregistro.setStyleSheet("""
		#VentanaRegistro{
			border-image: url(Imagenes/pollosplaya.jpg);
		}
		#widgetregistro{
			background-color: rgba(0, 0, 0, 160);
			border-radius: 10px;
			padding: 10px;
		}
		#label{
			font-weight: bold;
 			font: 20pt "Segoe UI Light";
 			/*color: #ADFF2F;*/
			color: #00A5A5;
		}
		#label2{
			font: 13pt "Segoe UI Light";
 			color: white;
		}
		#labelNickname, #labelNombre, #labelPregunta, #labelSexo, #labelRespuesta, #labelClave, #labelClave2, #labelFechaNacimiento{
			background-color: transparent;
			color: whitesmoke;
		}
		#labelPregunta2{
			text-decoration: underline;
			color: white;
		}

		#radioButtonMasculino, #radioButtonFemenino{
			color: white;
		}
		#radioButtonMasculino:indicator:unchecked{
			background-color: white;
			border-radius: 6px;
			border: 2px solid white;
		}
		#radioButtonMasculino:indicator:checked{
			background-color: #FF4500;
			border-radius: 6px;
			border: 3px solid white;
		}
		#radioButtonFemenino:indicator:unchecked{
			background-color: white;
			border-radius: 6px;
			border: 2px solid white;
		}
		#radioButtonFemenino:indicator:checked{
			background-color: #FF4500;
			border-radius: 6px;
			border: 3px solid white;
		}

		#labelErrorNombre, #labelErrorNickname, #labelErrorRespuesta, #labelErrorClave, #labelErrorClave2{
			color: magenta;
			background-color: transparent;
		}

		#lineEditNickname, #lineEditNombre, #lineEditRespuesta, #lineEditClave, #lineEditClave2, #dateEditFechaNacimiento {
			border-radius: 10px;
			border: 2px solid #DB7093;
			padding: 5px;
			font-family: Ubuntu;
		}

		#dateEditFechaNacimiento::drop-down {
			subcontrol-origin: padding;
			subcontrol-position: top right;
			width: 15px;
			border-left-width: 1px;
			border-left-color: red;
			border-left-style: solid;
			border-top-right-radius: 3px;
			border-bottom-right-radius: 3px;
			}
		#dateEditFechaNacimiento::down-arrow {
			border-image: url(Imagenes/arrow.png);
		}
	""")

def verificacion(objeto, mensaje):
	if mensaje.split(' ')[0] == 'VL':
		if mensaje.split(' ')[1] == 'Aceptar':
			objeto.botonLogin.setEnabled(True)
			objeto.botonLogin.setStyleSheet("""
				#QPushButtonLogin{
					background-color: white;
					border-radius: 4px;
					border: 2px solid green;
					font-family: Ubuntu;
					font-size: 17px;
					color: black;
				}
				#QPushButtonLogin:hover{
					background-color: green;
					border: 2px solid white;
					color: white;
				}
				#QPushButtonLogin:pressed{
					background-color: #32CD32;
					border: 2px solid green;
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar':
			objeto.botonLogin.setEnabled(False)
			objeto.botonLogin.setStyleSheet("""
				#QPushButtonLogin{
					background-color: gray;
					border-radius: 4px;
					color: #fff;
					font-family: Ubuntu;
					font-size: 17px;
				}
			""")
	elif mensaje.split(' ')[0] == 'VL_VO':
		if mensaje.split(' ')[1] == 'Aceptar':
			objeto.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
			objeto.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
				#Boton_Aceptar{
					background-color: white;
					border-radius: 4px;
					border: 2px solid green;
					font-family: Ubuntu;
					font-size: 15px;
					color: black;
				}
				#Boton_Aceptar:hover{
					background-color: green;
					border: 2px solid white;
					color: white;
				}
				#Boton_Aceptar:pressed{
					background-color: #32CD32;
					border: 2px solid green;
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar':
			objeto.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
			objeto.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
				#Boton_Aceptar{
					background-color: gray;
					color: #fff;
					font-family: Ubuntu;
					font-size: 15px;
					border-radius: 4px;
				}
			""")
	elif mensaje.split(' ')[0] == 'VL_VN':
		if mensaje.split(' ')[1] == 'Aceptar':
			objeto.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
			objeto.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
				#Boton_Aceptar{
					background-color: white;
					border-radius: 4px;
					border: 2px solid green;
					font-family: Ubuntu;
					font-size: 15px;
					color: black;
				}
				#Boton_Aceptar:hover{
					background-color: green;
					border: 2px solid white;
					color: white;
				}
				#Boton_Aceptar:pressed{
					background-color: #32CD32;
					border: 2px solid green;
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar':
			objeto.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
			objeto.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
				#Boton_Aceptar{
					background-color: gray;
					color: #fff;
					font-family: Ubuntu;
					font-size: 15px;
					border-radius: 4px;
				}
			""")
	elif mensaje.split(' ')[0] == 'VL_VR':
		if mensaje.split(' ')[1] == 'Cancelar':
			objeto.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
			objeto.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
				#Boton_Aceptar{
					background-color: gray;
					color: #fff;
					font-family: Ubuntu;
					font-size: 15px;
					border-radius: 4px;
				}
			""")
		elif mensaje.split(' ')[1] == 'Aceptar':
			objeto.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(True)
			objeto.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
				#Boton_Aceptar{
					background-color: white;
					border-radius: 4px;
					border: 2px solid green;
					font-family: Ubuntu;
					font-size: 15px;
					color: black;
				}
				#Boton_Aceptar:hover{
					background-color: green;
					border: 2px solid white;
					color: white;
				}
				#Boton_Aceptar:pressed{
					background-color: #32CD32;
					border: 2px solid green;
					color: white;
				}
			""")

class Ventana_Login(QtWidgets.QMainWindow):
	#Ventana Login------------------------------------------------------------------------------------------------------------------------
	def __init__(self):
		super(Ventana_Login, self).__init__()
		self.setObjectName("Ventana_Login")
		self.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.setFixedSize(404, 385)
		self.setWindowTitle("Pollos")
		estiloventanalogin(self)
		self.closeEvent = self.eventosalir

		self.Widget_Login = QtWidgets.QWidget(self)
		self.Widget_Login.setObjectName("Widget_Login")

		self.Widget_Login2 = QtWidgets.QWidget(self.Widget_Login)
		self.Widget_Login2.setObjectName("Widget_Login2")
		self.Widget_Login2.setFixedSize(self.frameGeometry().width()-40, self.frameGeometry().height()-30)
		self.Widget_Login2.move(20,15)

		self.labelLogin = QtWidgets.QLabel(self.Widget_Login)
		self.labelLogin.setFixedWidth(self.frameGeometry().width())
		self.labelLogin.move(0, 25)
		self.labelLogin.setAlignment(Qt.AlignCenter)
		self.labelLogin.setObjectName("label_login")
		self.labelLogin.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelLogin.efectos.setBlurRadius(10)
		self.labelLogin.efectos.setColor(QtGui.QColor("#FFFF00"))
		self.labelLogin.efectos.setOffset(0,0)
		self.labelLogin.setGraphicsEffect(self.labelLogin.efectos)
		self.labelLogin.setText("Pollos\' ChatRoom")

		self.labelUsuario = QtWidgets.QLabel(self.Widget_Login)
		self.labelUsuario.setFixedWidth(self.frameGeometry().width())
		self.labelUsuario.move(0, 80)
		self.labelUsuario.setAlignment(Qt.AlignCenter)
		self.labelUsuario.setObjectName("label_usuario")
		self.labelUsuario.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelUsuario.efectos.setBlurRadius(10)
		self.labelUsuario.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.labelUsuario.efectos.setOffset(0,0)
		self.labelUsuario.setGraphicsEffect(self.labelUsuario.efectos)
		self.labelUsuario.setText("Nickname")

		self.lineEditUsuario = QtWidgets.QLineEdit(self.Widget_Login)
		self.lineEditUsuario.setFixedWidth(150)
		self.lineEditUsuario.move(127, 110)
		self.lineEditUsuario.setObjectName("lineEdit_Usuario")
		self.lineEditUsuario.textChanged.connect(self.lineEditVerificarUsuario)
		self.lineEditUsuario.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.lineEditUsuario.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.lineEditUsuario))
		self.lineEditUsuario.returnPressed.connect(lambda: self.botonLogin.click())
		self.lineEditUsuario.setPlaceholderText("Escribe tu nickname")

		self.labelPassword = QtWidgets.QLabel(self.Widget_Login)
		self.labelPassword.setFixedWidth(self.frameGeometry().width())
		self.labelPassword.move(0, 150)
		self.labelPassword.setAlignment(Qt.AlignCenter)
		self.labelPassword.setObjectName("label_password")
		self.labelPassword.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelPassword.efectos.setBlurRadius(10)
		self.labelPassword.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.labelPassword.efectos.setOffset(0,0)
		self.labelPassword.setGraphicsEffect(self.labelPassword.efectos)
		self.labelPassword.setText("Contraseña")

		self.lineEditPassword = QtWidgets.QLineEdit(self.Widget_Login)
		self.lineEditPassword.setFixedWidth(150)
		self.lineEditPassword.move(127, 180)
		self.lineEditPassword.setObjectName("lineEdit_Password")
		self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEditPassword.textChanged.connect(self.lineEditVerificarClave)
		self.lineEditPassword.keyPressEvent = self.pressKeyQLineEditPassword
		self.lineEditPassword.keyReleaseEvent = self.releaseKeyQLineEditPassword
		self.lineEditPassword.indicador = None
		self.lineEditPassword.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.lineEditPassword.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.lineEditPassword))
		self.lineEditPassword.returnPressed.connect(lambda: self.botonLogin.click())
		self.lineEditPassword.setEnabled(False)
		self.lineEditPassword.setStyleSheet('background-color: #B0C4DE;')
		self.lineEditPassword.setPlaceholderText("Escribe tu contraseña")

		self.labelOlvidoPassword = QtWidgets.QLabel(self.Widget_Login)
		self.labelOlvidoPassword.setFixedWidth(self.frameGeometry().width())
		self.labelOlvidoPassword.move(0, 215)
		self.labelOlvidoPassword.setAlignment(Qt.AlignCenter)
		self.labelOlvidoPassword.setObjectName("label_olvido")
		self.labelOlvidoPassword.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelOlvidoPassword.efectos.setBlurRadius(10)
		self.labelOlvidoPassword.efectos.setColor(QtGui.QColor("#FF4500"))
		self.labelOlvidoPassword.efectos.setOffset(0,0)
		self.labelOlvidoPassword.setGraphicsEffect(self.labelOlvidoPassword.efectos)
		self.labelOlvidoPassword.mouseReleaseEvent = self.eventolabelOlvido
		self.labelOlvidoPassword.setText("Olvidó su contraseña?")

		self.labelError = QtWidgets.QLabel(self.Widget_Login)
		self.labelError.setFixedWidth(self.frameGeometry().width())
		self.labelError.move(0, 235)
		self.labelError.setAlignment(Qt.AlignCenter)
		self.labelError.setObjectName("label_error")
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.labelError.setFont(font)
		self.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelError.efectos.setBlurRadius(5)
		self.labelError.efectos.setColor(QtGui.QColor("#000000"))
		self.labelError.efectos.setOffset(0,0)
		self.labelError.setText("\n")
		self.labelError.setGraphicsEffect(self.labelError.efectos)

		self.botonLogin = QtWidgets.QPushButton(self.Widget_Login)
		self.botonLogin.setFixedSize(120, 31)
		self.botonLogin.move(137, 280)
		self.botonLogin.setObjectName("QPushButtonLogin")
		self.botonLogin.setEnabled(False)
		self.botonLogin.clicked.connect(lambda: SocketCliente.controladorInicioSesion(self))
		self.botonLogin.setText("Iniciar Sesión")


		self.botonRegistro = QtWidgets.QPushButton(self.Widget_Login)
		self.botonRegistro.setFixedSize(120, 31)
		self.botonRegistro.move(137, 322)
		self.botonRegistro.setObjectName("QPushButtonRegistro")
		self.botonRegistro.clicked.connect(self.registro_ventana)
		self.botonRegistro.setText("Registrarse")

		self.NicknameVerificar = 0
		self.ClaveVerificar = 0

		self.setCentralWidget(self.Widget_Login)
		self.lineEditUsuario.setFocus()

	def eventosalir(self, event):
		print("Kuchiyose no Justsu")

	def eventolabelOlvido(self, event):
		if event.button() == 1:
			QtWidgets.QLabel.mouseReleaseEvent(self.labelOlvidoPassword, event)
			self.olvido_ventana()
		else:
			event.ignore()

	def menuContextualQLineEdit(self, objeto):
		menuContextual = QtWidgets.QMenu()
		poderPegar = QtWidgets.QApplication.clipboard().text()

		actionDeshacer = QtWidgets.QAction(QtGui.QIcon('Imagenes/acciondeshacer.png'), '&Deshacer\tCTRL+Z')
		actionDeshacer.setShortcut('CTRL+Z')
		actionDeshacer.triggered.connect(lambda: objeto.undo())
		if objeto.isUndoAvailable() == True:
			actionDeshacer.setEnabled(True)
		else:
			actionDeshacer.setEnabled(False)

		actionRehacer = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionrehacer.png'), '&Rehacer\tCTRL+Y')
		actionRehacer.setShortcut('CTRL+Y')
		actionRehacer.triggered.connect(lambda: objeto.redo())
		if objeto.isRedoAvailable() == True:
			actionRehacer.setEnabled(True)
		else:
			actionRehacer.setEnabled(False)

		actionCortar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accioncortar.png'), '&Cortar\tCTRL+X')
		actionCortar.setShortcut('CTRL+X')
		actionCortar.triggered.connect(lambda: objeto.cut())
		if objeto.hasSelectedText() == True:
			actionCortar.setEnabled(True)
		else:
			actionCortar.setEnabled(False)

		actionCopiar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accioncopiar.png'), '&Copiar\tCTRL+C')
		actionCopiar.setShortcut('CTRL+C')
		actionCopiar.triggered.connect(lambda: objeto.copy())
		if objeto.hasSelectedText() == True:
			actionCopiar.setEnabled(True)
		else:
			actionCopiar.setEnabled(False)

		actionPegar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionpegar.png'), '&Pegar\tCTRL+V')
		actionPegar.setShortcut('CTRL+V')
		actionPegar.triggered.connect(lambda: objeto.paste())
		if len(poderPegar):
			actionPegar.setEnabled(True)
		else:
			actionPegar.setEnabled(False)

		actionEliminar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionborrar.png'), '&Eliminar')
		actionEliminar.triggered.connect(lambda: objeto.backspace())
		if objeto.hasSelectedText() == True:
			actionEliminar.setEnabled(True)
		else:
			actionEliminar.setEnabled(False)

		actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A')
		actionSeleccionarTodo.setShortcut('CTRL+A')
		actionSeleccionarTodo.triggered.connect(lambda: objeto.selectAll())
		if len(objeto.text()):
			if len(objeto.selectedText()) != len(objeto.text()):
				actionSeleccionarTodo.setEnabled(True)
			else:
				actionSeleccionarTodo.setEnabled(False)
		else:
			actionSeleccionarTodo.setEnabled(False)

		menuContextual.addAction(actionDeshacer)
		menuContextual.addAction(actionRehacer)
		menuContextual.addSeparator()
		menuContextual.addAction(actionCortar)
		menuContextual.addAction(actionCopiar)
		menuContextual.addAction(actionPegar)
		menuContextual.addAction(actionEliminar)
		menuContextual.addSeparator()
		menuContextual.addAction(actionSeleccionarTodo)
		menuContextual.exec_(QtGui.QCursor.pos())

	def menuContextualQLineEditPassword(self, objeto):
		menuContextual = QtWidgets.QMenu()
		poderPegar = QtWidgets.QApplication.clipboard().text()

		actionDeshacer = QtWidgets.QAction(QtGui.QIcon('Imagenes/acciondeshacer.png'), '&Deshacer\tCTRL+Z')
		actionDeshacer.setShortcut('CTRL+Z')
		actionDeshacer.triggered.connect(lambda: objeto.undo())
		if objeto.isUndoAvailable() == True:
			actionDeshacer.setEnabled(True)
		else:
			actionDeshacer.setEnabled(False)

		actionRehacer = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionrehacer.png'), '&Rehacer\tCTRL+Y')
		actionRehacer.setShortcut('CTRL+Y')
		actionRehacer.triggered.connect(lambda: objeto.redo())
		if objeto.isRedoAvailable() == True:
			actionRehacer.setEnabled(True)
		else:
			actionRehacer.setEnabled(False)

		actionPegar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionpegar.png'), '&Pegar\tCTRL+V')
		actionPegar.setShortcut('CTRL+V')
		actionPegar.triggered.connect(lambda: objeto.paste())
		if len(poderPegar):
			actionPegar.setEnabled(True)
		else:
			actionPegar.setEnabled(False)

		actionEliminar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionborrar.png'), '&Eliminar')
		actionEliminar.triggered.connect(lambda: objeto.backspace())
		if objeto.hasSelectedText() == True:
			actionEliminar.setEnabled(True)
		else:
			actionEliminar.setEnabled(False)

		actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A')
		actionSeleccionarTodo.setShortcut('CTRL+A')
		actionSeleccionarTodo.triggered.connect(lambda: objeto.selectAll())
		if len(objeto.text()):
			if len(objeto.selectedText()) != len(objeto.text()):
				actionSeleccionarTodo.setEnabled(True)
			else:
				actionSeleccionarTodo.setEnabled(False)
		else:
			actionSeleccionarTodo.setEnabled(False)

		menuContextual.addAction(actionDeshacer)
		menuContextual.addAction(actionRehacer)
		menuContextual.addSeparator()
		menuContextual.addAction(actionPegar)
		menuContextual.addAction(actionEliminar)
		menuContextual.addSeparator()
		menuContextual.addAction(actionSeleccionarTodo)
		menuContextual.exec_(QtGui.QCursor.pos())
	####Evitar Cortar y copiar en un QLineEdit de Password
	def pressKeyQLineEditPassword(self, event):
		if event.key() == 16777249:
			self.lineEditPassword.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.lineEditPassword, event)
		elif event.key() == 88 or event.key() == 67:
			if self.lineEditPassword.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.lineEditPassword, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.lineEditPassword, event)

	def releaseKeyQLineEditPassword(self, event):
		if event.key() == 16777249:
			self.lineEditPassword.indicador = 0
	####--------------------------------------------------
	def lineEditVerificarUsuario(self):
		if len(self.lineEditUsuario.text()) == 0:
			self.NicknameVerificar = 0
			self.labelError.setText("\n")
			self.lineEditPassword.setEnabled(False)
			self.lineEditPassword.setStyleSheet('background-color: #B0C4DE;')
			self.lineEditPassword.blockSignals(True)
			self.lineEditPassword.clear()
			self.lineEditPassword.blockSignals(False)
			verificacion(self, 'VL Cancelar')
		else:
			if len(self.lineEditUsuario.text()) < 6:
				self.NicknameVerificar = 0
				self.labelError.setText("El nickname debe ser mínimo de 6 caracteres.")
				self.lineEditPassword.setEnabled(False)
				self.lineEditPassword.setStyleSheet('background-color: #B0C4DE;')
				verificacion(self, 'VL Cancelar')
			elif len(self.lineEditUsuario.text()) > 20:
				self.NicknameVerificar = 0
				self.labelError.setText("El nickname debe ser máximo de 20 caracteres.")
				self.lineEditPassword.setEnabled(False)
				self.lineEditPassword.setStyleSheet('background-color: #B0C4DE;')
				verificacion(self, 'VL Cancelar')
			elif re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', self.lineEditUsuario.text()) is None:
				self.NicknameVerificar = 0
				self.lineEditPassword.setEnabled(False)
				self.lineEditPassword.setStyleSheet('background-color: #B0C4DE;')
				self.labelError.setText("El nickname no puede comenzar con números, tener\nespacios o caracteres especiales.")
				self.labelError.setWordWrap(True)
				verificacion(self, 'VL Cancelar')
			else:
				self.NicknameVerificar = 1
				self.labelError.setText("\n")
				self.lineEditPassword.setEnabled(True)
				self.lineEditPassword.setStyleSheet('background-color: white;')
				if self.NicknameVerificar == 1 and self.ClaveVerificar == 1:
					verificacion(self, 'VL Aceptar')
				else:
					verificacion(self, 'VL Cancelar')

	def lineEditVerificarClave(self):
		if len(self.lineEditPassword.text()) == 0:
			self.ClaveVerificar = 0
			self.labelError.setText("\n")
			verificacion(self, 'VL Cancelar')
		else:
			if len(self.lineEditPassword.text()) < 6:
				self.ClaveVerificar = 0
				self.labelError.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.labelError.show()
				verificacion(self, 'VL Cancelar')
			elif re.match(r'^[^:]*$', self.lineEditPassword.text()) is None:
				self.ClaveVerificar = 0
				self.labelError.setText("Caracter dos puntos ':' no admitido en la contraseña.")
				self.labelError.show()
				verificacion(self, 'VL Cancelar')
			else:
				self.ClaveVerificar = 1
				self.labelError.setText("\n")
				if self.NicknameVerificar == 1 and self.ClaveVerificar == 1:
					verificacion(self, 'VL Aceptar')
				else:
					verificacion(self, 'VL Cancelar')

	def alerta(self, mensaje):
		self.ventanaAlerta = QtWidgets.QMessageBox(self)
		self.ventanaAlerta.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.ventanaAlerta.setIcon(QtWidgets.QMessageBox.Information)
		self.ventanaAlerta.setEnabled(True)
		self.ventanaAlerta.setMouseTracking(True)
		self.ventanaAlerta.setFocusPolicy(QtCore.Qt.NoFocus)
		self.ventanaAlerta.setWindowTitle("Pollos' ChatRoom Mensaje")
		self.ventanaAlerta.setText(mensaje)
		self.ventanaAlerta.setStandardButtons(QtWidgets.QMessageBox.Ok)
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Ok).setObjectName("Boton_Ok")
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Ok).setFixedSize(70,25)
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Ok).setText("Aceptar")
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Ok).setStyleSheet("""
			#Boton_Ok{
				background-color: white;
				border-radius: 4px;
				border: 2px solid green;
				font-family: Ubuntu;
				font-size: 15px;
				color: black;
			}
			#Boton_Ok:hover{
				background-color: green;
				border: 2px solid white;
				color: white;
			}
			#Boton_Ok:pressed{
				background-color: #32CD32;
				border: 2px solid green;
				color: white;
			}
		""")
		self.ventanaAlerta.exec_()
	#-----------------------------------------------------------------------------------------------------------------------------------------
	#Ventana Olvido Contraseña------------------------------------------------------------------------------------------------
	def olvido_ventana(self):
		self.olvidoVentana = QDialog(self, Qt.WindowCloseButtonHint)
		self.olvidoVentana.setFixedSize(351, 290)
		self.olvidoVentana.setMouseTracking(True)
		self.olvidoVentana.setObjectName("Ventana_Olvido")
		self.olvidoVentana.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.olvidoVentana.setWindowTitle("Recuperar Contraseña")
		estiloventanaolvidoclave(self.olvidoVentana)

		self.olvidoVentana.widget = QtWidgets.QWidget(self.olvidoVentana)
		self.olvidoVentana.widget.setObjectName("widgetolvido")
		self.olvidoVentana.widget.setFixedSize(self.olvidoVentana.frameGeometry().width()-20, self.olvidoVentana.frameGeometry().height()-20)
		self.olvidoVentana.widget.move(10,10)

		self.olvidoVentana.labelUsuario = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelUsuario.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelUsuario.move(0, 20)
		self.olvidoVentana.labelUsuario.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelUsuario.setObjectName("Label_Usuario")
		self.olvidoVentana.font = QtGui.QFont()
		self.olvidoVentana.font.setFamily("Ubuntu")
		self.olvidoVentana.font.setPointSize(11)
		self.olvidoVentana.font.setBold(True)
		self.olvidoVentana.font.setWeight(75)
		self.olvidoVentana.labelUsuario.setFont(self.olvidoVentana.font)
		self.olvidoVentana.labelUsuario.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelUsuario.efectos.setBlurRadius(10)
		self.olvidoVentana.labelUsuario.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.olvidoVentana.labelUsuario.efectos.setOffset(0,0)
		self.olvidoVentana.labelUsuario.setGraphicsEffect(self.olvidoVentana.labelUsuario.efectos)
		self.olvidoVentana.labelUsuario.setText("Nickname")

		self.olvidoVentana.lineEditUsuario = QtWidgets.QLineEdit(self.olvidoVentana)
		self.olvidoVentana.lineEditUsuario.setFixedWidth(150)
		self.olvidoVentana.lineEditUsuario.move(100.5, 45)
		self.olvidoVentana.lineEditUsuario.setObjectName("lineEdit_usuario")
		self.olvidoVentana.lineEditUsuario.textChanged.connect(self.lineEditVerificarUsuarioVentanaOlvido)
		self.olvidoVentana.lineEditUsuario.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.olvidoVentana.lineEditUsuario.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.olvidoVentana.lineEditUsuario))
		self.olvidoVentana.lineEditUsuario.setPlaceholderText("Escribe tu nickname")

		self.olvidoVentana.labelPreguntaSecreta = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelPreguntaSecreta.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelPreguntaSecreta.move(0, 90)
		self.olvidoVentana.labelPreguntaSecreta.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelPreguntaSecreta.setObjectName("label_preguntasecreta")
		self.olvidoVentana.labelPreguntaSecreta.setFont(self.olvidoVentana.font)
		self.olvidoVentana.labelPreguntaSecreta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelPreguntaSecreta.efectos.setBlurRadius(10)
		self.olvidoVentana.labelPreguntaSecreta.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.olvidoVentana.labelPreguntaSecreta.efectos.setOffset(0,0)
		self.olvidoVentana.labelPreguntaSecreta.setGraphicsEffect(self.olvidoVentana.labelPreguntaSecreta.efectos)
		self.olvidoVentana.labelPreguntaSecreta.setText("Pregunta Secreta:")

		self.olvidoVentana.labelPreguntaSecreta2 = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelPreguntaSecreta2.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelPreguntaSecreta2.move(0, 110)
		self.olvidoVentana.labelPreguntaSecreta2.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelPreguntaSecreta2.setObjectName("label_preguntasecreta2")
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(11)
		self.olvidoVentana.labelPreguntaSecreta2.setFont(font)
		self.olvidoVentana.labelPreguntaSecreta2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelPreguntaSecreta2.efectos.setBlurRadius(5)
		self.olvidoVentana.labelPreguntaSecreta2.efectos.setColor(QtGui.QColor("#FF4500"))
		self.olvidoVentana.labelPreguntaSecreta2.efectos.setOffset(0,0)
		self.olvidoVentana.labelPreguntaSecreta2.setGraphicsEffect(self.olvidoVentana.labelPreguntaSecreta2.efectos)
		self.olvidoVentana.labelPreguntaSecreta2.setText("¿Cuál es tu banda favorite?")

		self.olvidoVentana.labelRespuestaSecreta = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelRespuestaSecreta.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelRespuestaSecreta.move(0, 140)
		self.olvidoVentana.labelRespuestaSecreta.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelRespuestaSecreta.setObjectName("label_respuestasecreta")
		self.olvidoVentana.labelRespuestaSecreta.setFont(self.olvidoVentana.font)
		self.olvidoVentana.labelRespuestaSecreta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelRespuestaSecreta.efectos.setBlurRadius(10)
		self.olvidoVentana.labelRespuestaSecreta.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.olvidoVentana.labelRespuestaSecreta.efectos.setOffset(0,0)
		self.olvidoVentana.labelRespuestaSecreta.setGraphicsEffect(self.olvidoVentana.labelRespuestaSecreta.efectos)
		self.olvidoVentana.labelRespuestaSecreta.setText("Respuesta Secreta")

		self.olvidoVentana.lineEditRespuesta = QtWidgets.QLineEdit(self.olvidoVentana)
		self.olvidoVentana.lineEditRespuesta.setFixedWidth(150)
		self.olvidoVentana.lineEditRespuesta.move(100.5, 165)
		self.olvidoVentana.lineEditRespuesta.setObjectName("lineEdit_respuesta")
		self.olvidoVentana.lineEditRespuesta.textChanged.connect(self.lineEditVerificarRespuestaVentanaOlvido)
		self.olvidoVentana.lineEditRespuesta.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.olvidoVentana.lineEditRespuesta.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.olvidoVentana.lineEditRespuesta))
		self.olvidoVentana.lineEditRespuesta.setEnabled(False)
		self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #B0C4DE;')
		self.olvidoVentana.lineEditRespuesta.setPlaceholderText("Escribe tu respuesta")

		self.olvidoVentana.labelError = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelError.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelError.move(0, 200)
		self.olvidoVentana.labelError.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelError.setObjectName("label_error")
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.olvidoVentana.labelError.setFont(font)
		self.olvidoVentana.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelError.efectos.setBlurRadius(5)
		self.olvidoVentana.labelError.efectos.setColor(QtGui.QColor("#000000"))
		self.olvidoVentana.labelError.efectos.setOffset(0,0)
		self.olvidoVentana.labelError.setGraphicsEffect(self.olvidoVentana.labelError.efectos)
		self.olvidoVentana.labelError.setText("\n")

		self.olvidoVentana.botones = QtWidgets.QDialogButtonBox(self.olvidoVentana)
		self.olvidoVentana.botones.setFixedWidth(160)
		self.olvidoVentana.botones.move(95.5, 240)
		self.olvidoVentana.botones.setOrientation(QtCore.Qt.Horizontal)
		self.olvidoVentana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.olvidoVentana.botones.setCenterButtons(True)
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setObjectName("Boton_Aceptar")
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setFixedSize(70,25)
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setText("Aceptar")
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: SocketCliente.verificarDatosVentanaOlvidoClave(self))
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
			#Boton_Aceptar{
				background-color: gray;
				color: #fff;
				font-family: Ubuntu;
				font-size: 15px;
				border-radius: 4px;
			}
		""")

		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setObjectName("Boton_Cancelar")
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setFixedSize(70,25)
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setText("Cancelar")
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: self.olvidoVentana.hide())
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet("""
			#Boton_Cancelar{
				background-color: white;
				color: black;
				font-family: Ubuntu;
				font-size: 15px;
				border-radius: 4px;
				border: 2px solid red;

			}
			#Boton_Cancelar:hover{
				background-color: red;
				border: 2px solid white;
				color: white;
			}
			#Boton_Cancelar:pressed{
				background-color: #8B0000;
				border: 2px solid red;
				color: white;
			}
		""")

		self.olvidoVentana.NicknameVerificar = 0
		self.olvidoVentana.RespuestaVerificar = 0

		self.olvidoVentana.exec_()

	def lineEditVerificarUsuarioVentanaOlvido(self):
		if len(self.olvidoVentana.lineEditUsuario.text()) == 0:
			self.olvidoVentana.NicknameVerificar = 0
			self.olvidoVentana.labelError.setText("\n")
			self.olvidoVentana.lineEditRespuesta.setEnabled(False)
			self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #B0C4DE;')
			self.olvidoVentana.lineEditRespuesta.blockSignals(True)
			self.olvidoVentana.lineEditRespuesta.clear()
			self.olvidoVentana.lineEditRespuesta.blockSignals(False)
			verificacion(self, 'VL_VO Cancelar')
		else:
			if len(self.olvidoVentana.lineEditUsuario.text()) < 6:
				self.olvidoVentana.NicknameVerificar = 0
				self.olvidoVentana.labelError.setText("El nickname debe ser mínimo de 6 caracteres.")
				self.olvidoVentana.lineEditRespuesta.setEnabled(False)
				self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #B0C4DE;')
				verificacion(self, 'VL_VO Cancelar')
			elif len(self.olvidoVentana.lineEditUsuario.text()) > 20:
				self.olvidoVentana.NicknameVerificar = 0
				self.olvidoVentana.labelError.setText("El nickname debe ser máximo de 20 caracteres.")
				self.olvidoVentana.lineEditRespuesta.setEnabled(False)
				self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #B0C4DE;')
				verificacion(self, 'VL_VO Cancelar')
			elif re.match(r'^[a-zA-Z][a-zA-Z0-9]*$',self.olvidoVentana.lineEditUsuario.text()) is None:
				self.olvidoVentana.NicknameVerificar = 0
				self.olvidoVentana.lineEditRespuesta.setEnabled(False)
				self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #B0C4DE;')
				self.olvidoVentana.labelError.setText("El nickname no puede comenzar con números, tener\nespacios o caracteres especiales.")
				self.olvidoVentana.labelError.setWordWrap(True)
				verificacion(self, 'VL_VO Cancelar')
			else:
				self.olvidoVentana.NicknameVerificar = 1
				self.olvidoVentana.labelError.setText("\n")
				self.olvidoVentana.lineEditRespuesta.setEnabled(True)
				self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: white;')
				if self.olvidoVentana.NicknameVerificar == 1 and self.olvidoVentana.RespuestaVerificar == 1:
					verificacion(self, 'VL_VO Aceptar')
				else:
					verificacion(self, 'VL_VO Cancelar')

	def lineEditVerificarRespuestaVentanaOlvido(self):
		if len(self.olvidoVentana.lineEditRespuesta.text()) == 0:
			self.olvidoVentana.RespuestaVerificar = 0
			self.olvidoVentana.labelError.setText("Escribe una respuesta secreta.")
			verificacion(self, 'VL_VO Cancelar')
		else:
			if re.match(r'^[^:]*$', self.olvidoVentana.lineEditRespuesta.text()) is None:
				self.ClaveVerificar = 0
				self.olvidoVentana.labelError.setText("Caracter dos puntos ':' no admitido\nen la respuesta secreta.")
				self.olvidoVentana.labelError.setWordWrap(True)
				verificacion(self, 'VL_VO Cancelar')
			else:
				self.olvidoVentana.RespuestaVerificar = 1
				self.olvidoVentana.labelError.setText("\n")
				if self.olvidoVentana.NicknameVerificar == 1 and self.olvidoVentana.RespuestaVerificar == 1:
					verificacion(self, 'VL_VO Aceptar')
				else:
					verificacion(self, 'VL_VO Cancelar')

	#-------------------------------------------------------------------------------------------------------------------------
    #Ventana Nueva Contraseña
	def ventana_clave_nueva(self, usuario):
		self.claveNuevaVentana = QDialog(self, Qt.WindowCloseButtonHint)
		self.claveNuevaVentana.setFixedSize(351, 305)
		self.claveNuevaVentana.setObjectName("Ventana_Clave_Nueva")
		self.claveNuevaVentana.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.claveNuevaVentana.setMouseTracking(True)
		self.claveNuevaVentana.setWindowTitle("Nueva Contraseña")
		estiloVentanaClaveNueva(self.claveNuevaVentana)

		self.claveNuevaVentana.widget = QtWidgets.QWidget(self.claveNuevaVentana)
		self.claveNuevaVentana.widget.setObjectName("widgetclavenueva")
		self.claveNuevaVentana.widget.setFixedSize(self.claveNuevaVentana.frameGeometry().width()-20, self.claveNuevaVentana.frameGeometry().height()-20)
		self.claveNuevaVentana.widget.move(10,10)
		indicador = 30

		self.claveNuevaVentana.labelUsuario = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelUsuario.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelUsuario.move(0, indicador)
		self.claveNuevaVentana.labelUsuario.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelUsuario.setObjectName("labelUsuario")
		self.claveNuevaVentana.font = QtGui.QFont()
		self.claveNuevaVentana.font.setFamily("Ubuntu")
		self.claveNuevaVentana.font.setPointSize(11)
		self.claveNuevaVentana.font.setBold(True)
		self.claveNuevaVentana.font.setWeight(75)
		self.claveNuevaVentana.labelUsuario.setFont(self.claveNuevaVentana.font)
		self.claveNuevaVentana.labelUsuario.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelUsuario.efectos.setBlurRadius(5)
		self.claveNuevaVentana.labelUsuario.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.claveNuevaVentana.labelUsuario.efectos.setOffset(0,0)
		self.claveNuevaVentana.labelUsuario.setGraphicsEffect(self.claveNuevaVentana.labelUsuario.efectos)
		self.claveNuevaVentana.labelUsuario.setText("Usuario:")
		indicador = indicador + self.claveNuevaVentana.labelUsuario.frameGeometry().height()

		self.claveNuevaVentana.labelUsuario2 = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelUsuario2.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelUsuario2.move(0, indicador-10)
		self.claveNuevaVentana.labelUsuario2.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelUsuario2.setObjectName("labelUsuario2")
		self.claveNuevaVentana.font2 = QtGui.QFont()
		self.claveNuevaVentana.font2.setFamily("Ubuntu")
		self.claveNuevaVentana.font2.setPointSize(11)
		self.claveNuevaVentana.labelUsuario2.setFont(self.claveNuevaVentana.font2)
		self.claveNuevaVentana.labelUsuario2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelUsuario2.efectos.setBlurRadius(5)
		self.claveNuevaVentana.labelUsuario2.efectos.setColor(QtGui.QColor("#FF4500"))
		self.claveNuevaVentana.labelUsuario2.efectos.setOffset(0,0)
		self.claveNuevaVentana.labelUsuario2.setGraphicsEffect(self.claveNuevaVentana.labelUsuario2.efectos)
		self.claveNuevaVentana.labelUsuario2.setText(usuario)
		indicador = indicador + self.claveNuevaVentana.labelUsuario2.frameGeometry().height()-10

		self.claveNuevaVentana.labelClave = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelClave.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelClave.move(0, indicador)
		self.claveNuevaVentana.labelClave.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelClave.setObjectName("Label_Clave")
		self.claveNuevaVentana.labelClave.setFont(self.claveNuevaVentana.font)
		self.claveNuevaVentana.labelClave.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelClave.efectos.setBlurRadius(5)
		self.claveNuevaVentana.labelClave.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.claveNuevaVentana.labelClave.efectos.setOffset(0,0)
		self.claveNuevaVentana.labelClave.setGraphicsEffect(self.claveNuevaVentana.labelClave.efectos)
		self.claveNuevaVentana.labelClave.setText("Nueva Contraseña")
		indicador = indicador + self.claveNuevaVentana.labelClave.frameGeometry().height()

		self.claveNuevaVentana.lineEditClave = QtWidgets.QLineEdit(self.claveNuevaVentana)
		self.claveNuevaVentana.lineEditClave.setFixedWidth(150)
		self.claveNuevaVentana.lineEditClave.move(100.5, indicador-5)
		self.claveNuevaVentana.lineEditClave.setObjectName("lineEdit_clave")
		self.claveNuevaVentana.lineEditClave.textChanged.connect(self.lineEditVerificarNuevaClave)
		self.claveNuevaVentana.lineEditClave.setEchoMode(QtWidgets.QLineEdit.Password)
		self.claveNuevaVentana.lineEditClave.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.claveNuevaVentana.lineEditClave.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.claveNuevaVentana.lineEditClave))
		self.claveNuevaVentana.lineEditClave.indicador = None
		self.claveNuevaVentana.lineEditClave.keyPressEvent = self.pressKeyQLineEditPasswordVentanaNuevaClave
		self.claveNuevaVentana.lineEditClave.keyReleaseEvent = self.releaseKeyQLineEditPasswordVentanaNuevaClave
		self.claveNuevaVentana.lineEditClave.setPlaceholderText("Nueva contraseña")
		indicador = indicador + self.claveNuevaVentana.lineEditClave.frameGeometry().height()-5

		self.claveNuevaVentana.labelClave2 = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelClave2.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelClave2.move(0, indicador+13)
		self.claveNuevaVentana.labelClave2.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelClave2.setObjectName("Label_Clave2")
		self.claveNuevaVentana.labelClave2.setFont(self.claveNuevaVentana.font)
		self.claveNuevaVentana.labelClave2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelClave2.efectos.setBlurRadius(5)
		self.claveNuevaVentana.labelClave2.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.claveNuevaVentana.labelClave2.efectos.setOffset(0,0)
		self.claveNuevaVentana.labelClave2.setGraphicsEffect(self.claveNuevaVentana.labelClave2.efectos)
		self.claveNuevaVentana.labelClave2.setText("Confirme Nueva Contraseña")
		indicador = indicador + self.claveNuevaVentana.labelClave2.frameGeometry().height() + 13

		self.claveNuevaVentana.lineEditClave2 = QtWidgets.QLineEdit(self.claveNuevaVentana)
		self.claveNuevaVentana.lineEditClave2.setFixedWidth(150)
		self.claveNuevaVentana.lineEditClave2.move(100.5, indicador-5)
		self.claveNuevaVentana.lineEditClave2.setObjectName("lineEdit_clave2")
		self.claveNuevaVentana.lineEditClave2.textChanged.connect(self.lineEditVerificarNuevaClave2)
		self.claveNuevaVentana.lineEditClave2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.claveNuevaVentana.lineEditClave2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.claveNuevaVentana.lineEditClave2.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.claveNuevaVentana.lineEditClave2))
		self.claveNuevaVentana.lineEditClave2.indicador = None
		self.claveNuevaVentana.lineEditClave2.keyPressEvent = self.pressKeyQLineEditPassword2VentanaNuevaClave
		self.claveNuevaVentana.lineEditClave2.keyReleaseEvent = self.releaseKeyQLineEditPassword2VentanaNuevaClave
		self.claveNuevaVentana.lineEditClave2.setEnabled(False)
		self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
		self.claveNuevaVentana.lineEditClave2.setPlaceholderText("Confirma contraseña")
		indicador = indicador + self.claveNuevaVentana.lineEditClave2.frameGeometry().height()-5


		self.claveNuevaVentana.labelError = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelError.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelError.move(0, indicador+5)
		self.claveNuevaVentana.labelError.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelError.setObjectName("label_error")
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.claveNuevaVentana.labelError.setFont(font)
		self.claveNuevaVentana.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelError.efectos.setBlurRadius(5)
		self.claveNuevaVentana.labelError.efectos.setColor(QtGui.QColor("#000000"))
		self.claveNuevaVentana.labelError.efectos.setOffset(0,0)
		self.claveNuevaVentana.labelError.setGraphicsEffect(self.claveNuevaVentana.labelError.efectos)
		self.claveNuevaVentana.labelError.setText("\n")
		indicador = indicador + self.claveNuevaVentana.labelError.frameGeometry().height()+13

		self.claveNuevaVentana.botones = QtWidgets.QDialogButtonBox(self.claveNuevaVentana)
		self.claveNuevaVentana.botones.setFixedWidth(160)
		self.claveNuevaVentana.botones.move(95.5, self.claveNuevaVentana.widget.frameGeometry().height()-25-self.claveNuevaVentana.botones.frameGeometry().height()/2)
		self.claveNuevaVentana.botones.setOrientation(QtCore.Qt.Horizontal)
		self.claveNuevaVentana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.claveNuevaVentana.botones.setCenterButtons(True)
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setObjectName("Boton_Aceptar")
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setFixedSize(70,25)
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setText("Aceptar")
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: SocketCliente.controladorNuevaClave(self))
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
			#Boton_Aceptar{
				background-color: gray;
				color: #fff;
				font-family: Ubuntu;
				font-size: 15px;
				border-radius: 4px;
			}
		""")

		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setObjectName("Boton_Cancelar")
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setFixedSize(70,25)
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setText("Cancelar")
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: self.claveNuevaVentana.hide())
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet("""
			#Boton_Cancelar{
				background-color: white;
				color: black;
				font-family: Ubuntu;
				font-size: 15px;
				border-radius: 4px;
				border: 2px solid red;

			}
			#Boton_Cancelar:hover{
				background-color: red;
				border: 2px solid white;
				color: white;
			}
			#Boton_Cancelar:pressed{
				background-color: #8B0000;
				border: 2px solid red;
				color: white;
			}
		""")

		self.claveNuevaVentana.claveVerificar = 0
		self.claveNuevaVentana.claveVerificar2 = 0

		self.claveNuevaVentana.exec_()

	####Evitar Cortar y copiar en un QLineEdit de Password
	def pressKeyQLineEditPasswordVentanaNuevaClave(self, event):
		if event.key() == 16777249:
			self.claveNuevaVentana.lineEditClave.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.claveNuevaVentana.lineEditClave, event)
		elif event.key() == 88 or event.key() == 67:
			if self.claveNuevaVentana.lineEditClave.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.claveNuevaVentana.lineEditClave, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.claveNuevaVentana.lineEditClave, event)

	def releaseKeyQLineEditPasswordVentanaNuevaClave(self, event):
		if event.key() == 16777249:
			self.claveNuevaVentana.lineEditClave.indicador = 0

	def pressKeyQLineEditPassword2VentanaNuevaClave(self, event):
		if event.key() == 16777249:
			self.claveNuevaVentana.lineEditClave2.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.claveNuevaVentana.lineEditClave2, event)
		elif event.key() == 88 or event.key() == 67:
			if self.claveNuevaVentana.lineEditClave2.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.claveNuevaVentana.lineEditClave2, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.claveNuevaVentana.lineEditClave2, event)

	def releaseKeyQLineEditPassword2VentanaNuevaClave(self, event):
		if event.key() == 16777249:
			self.claveNuevaVentana.lineEditClave2.indicador = 0
	####--------------------------------------------------
	def lineEditVerificarNuevaClave(self):
		if len(self.claveNuevaVentana.lineEditClave.text()) == 0:
			self.claveNuevaVentana.claveVerificar = 0
			self.claveNuevaVentana.labelError.setText("\n")
			self.claveNuevaVentana.lineEditClave2.setEnabled(False)
			self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
			self.claveNuevaVentana.lineEditClave2.blockSignals(True)
			self.claveNuevaVentana.lineEditClave2.clear()
			self.claveNuevaVentana.lineEditClave2.blockSignals(False)
			verificacion(self, 'VL_VN Cancelar')
		else:
			self.claveNuevaVentana.lineEditClave2.blockSignals(True)
			self.claveNuevaVentana.lineEditClave2.clear()
			self.claveNuevaVentana.lineEditClave2.blockSignals(False)
			if len(self.claveNuevaVentana.lineEditClave.text()) < 6:
				self.claveNuevaVentana.claveVerificar = 0
				self.claveNuevaVentana.labelError.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.claveNuevaVentana.lineEditClave2.setEnabled(False)
				self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
				verificacion(self, 'VL_VN Cancelar')
			elif re.match(r'^[^:]*$', self.claveNuevaVentana.lineEditClave.text()) is None:
				self.claveNuevaVentana.claveVerificar = 0
				self.claveNuevaVentana.labelError.setText("Caracter dos puntos ':' no admitido\nen la contraseña.")
				self.claveNuevaVentana.labelError.setWordWrap(True)
				self.claveNuevaVentana.lineEditClave2.setEnabled(False)
				self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
				verificacion(self, 'VL_VN Cancelar')
			else:
				self.claveNuevaVentana.claveVerificar = 1
				self.claveNuevaVentana.labelError.setText("\n")
				self.claveNuevaVentana.lineEditClave2.setEnabled(True)
				self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: white;')
				if self.claveNuevaVentana.claveVerificar == 1 and self.claveNuevaVentana.claveVerificar2 == 1:
					verificacion(self, 'VL_VN Aceptar')
				else:
					verificacion(self, 'VL_VN Cancelar')

	def lineEditVerificarNuevaClave2(self):
		if len(self.claveNuevaVentana.lineEditClave2.text()) == 0:
			self.claveNuevaVentana.claveVerificar2 = 0
			self.claveNuevaVentana.labelError.setText("Confirma la contraseña.")
			verificacion(self, 'VL_VN Cancelar')
		else:
			if len(self.claveNuevaVentana.lineEditClave2.text()) < 6:
				self.claveNuevaVentana.claveVerificar2 = 0
				self.claveNuevaVentana.labelError.setText("La contraseña debe ser mínimo de 6 caracteres.")
				verificacion(self, 'VL_VN Cancelar')
			elif re.match(r'^[^:]*$', self.claveNuevaVentana.lineEditClave2.text()) is None:
				self.claveNuevaVentana.claveVerificar2 = 0
				self.claveNuevaVentana.labelError.setText("Caracter dos puntos ':' no admitido\nen la contraseña.")
				self.claveNuevaVentana.labelError.setWordWrap(True)
				verificacion(self, 'VL_VN Cancelar')
			else:
				if self.claveNuevaVentana.lineEditClave.text() != self.claveNuevaVentana.lineEditClave2.text():
					self.claveNuevaVentana.claveVerificar2 = 0
					self.claveNuevaVentana.labelError.setText("Las contraseñas no coinciden.")
					verificacion(self, 'VL_VN Cancelar')
				else:
					self.claveNuevaVentana.claveVerificar2 = 1
					self.claveNuevaVentana.labelError.setText("\n")
					if self.claveNuevaVentana.claveVerificar == 1 and self.claveNuevaVentana.claveVerificar2 == 1:
						verificacion(self, 'VL_VN Aceptar')
					else:
						verificacion(self, 'VL_VN Cancelar')

	#--------------------------------------------------------------------------------------------------------------------------
	#Ventana Registro
	def registro_ventana(self):
		self.ventanaRegistro = QtWidgets.QMainWindow(None, Qt.WindowCloseButtonHint)
		self.ventanaRegistro.setObjectName("VentanaRegistro")
		self.ventanaRegistro.setMouseTracking(True)
		self.ventanaRegistro.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.ventanaRegistro.setFixedSize(700, 580)
		self.ventanaRegistro.setWindowTitle("Registro")
		estiloVentanaRegistro(self.ventanaRegistro)

		self.ventanaRegistro.widget = QtWidgets.QWidget(self.ventanaRegistro)
		self.ventanaRegistro.widget.setObjectName("widgetregistro")
		self.ventanaRegistro.widget.setFixedSize(self.ventanaRegistro.frameGeometry().width()-60, self.ventanaRegistro.frameGeometry().height()-70)
		self.ventanaRegistro.widget.move(30,35)

		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)

		font2 = QtGui.QFont()
		font2.setFamily("Ubuntu")
		font2.setPointSize(10)

		self.ventanaRegistro.widget.label = QtWidgets.QLabel(self.ventanaRegistro.widget)
		self.ventanaRegistro.widget.label.setFixedWidth(self.ventanaRegistro.widget.frameGeometry().width())
		self.ventanaRegistro.widget.label.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaRegistro.widget.label.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.label.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.label.efectos.setColor(QtGui.QColor("#FFFF00"))
		self.ventanaRegistro.widget.label.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.label.setGraphicsEffect(self.ventanaRegistro.widget.label.efectos)
		self.ventanaRegistro.widget.label.setObjectName("label")
		self.ventanaRegistro.widget.label.move(10,20)
		self.ventanaRegistro.widget.label.setText("Registro")
		indicador = self.ventanaRegistro.widget.label.frameGeometry().height()+20

		self.ventanaRegistro.widget.label2 = QtWidgets.QLabel(self.ventanaRegistro.widget)
		self.ventanaRegistro.widget.label2.setFixedWidth(self.ventanaRegistro.widget.frameGeometry().width())
		self.ventanaRegistro.widget.label2.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaRegistro.widget.label2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.label2.efectos.setBlurRadius(10)
		self.ventanaRegistro.widget.label2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaRegistro.widget.label2.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.label2.setGraphicsEffect(self.ventanaRegistro.widget.label2.efectos)
		self.ventanaRegistro.widget.label2.setObjectName("label2")
		self.ventanaRegistro.widget.label2.move(0,indicador+20)
		self.ventanaRegistro.widget.label2.setText("Llene los datos del formulario y presione el botón aceptar para registrarse.")
		indicador = indicador + self.ventanaRegistro.widget.label2.frameGeometry().height()+20

		self.ventanaRegistro.widget.widget = QtWidgets.QWidget(self.ventanaRegistro.widget)
		self.ventanaRegistro.widget.widget.setFixedSize(self.ventanaRegistro.widget.frameGeometry().width()/2, self.ventanaRegistro.widget.frameGeometry().height() - self.ventanaRegistro.widget.label.frameGeometry().height() - self.ventanaRegistro.widget.label2.frameGeometry().height())
		self.ventanaRegistro.widget.widget.move(0, indicador)

		self.ventanaRegistro.widget.widget2 = QtWidgets.QWidget(self.ventanaRegistro.widget)
		self.ventanaRegistro.widget.widget2.setFixedSize(self.ventanaRegistro.widget.frameGeometry().width()/2, self.ventanaRegistro.widget.frameGeometry().height() - self.ventanaRegistro.widget.label.frameGeometry().height() - self.ventanaRegistro.widget.label2.frameGeometry().height())
		self.ventanaRegistro.widget.widget2.setStyleSheet("/*background-color: red;*/")
		self.ventanaRegistro.widget.widget2.move(self.ventanaRegistro.widget.frameGeometry().width()/2, indicador)

		indicador = 0

		self.ventanaRegistro.widget.widget.labelNickname = QtWidgets.QLabel(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.labelNickname.setFixedWidth(self.ventanaRegistro.widget.widget.frameGeometry().width())
		self.ventanaRegistro.widget.widget.labelNickname.move(0, indicador)
		self.ventanaRegistro.widget.widget.labelNickname.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget.labelNickname.setObjectName("labelNickname")
		self.ventanaRegistro.widget.widget.labelNickname.setFont(font)
		self.ventanaRegistro.widget.widget.labelNickname.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.labelNickname.efectos.setBlurRadius(10)
		self.ventanaRegistro.widget.widget.labelNickname.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.ventanaRegistro.widget.widget.labelNickname.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.labelNickname.setGraphicsEffect(self.ventanaRegistro.widget.widget.labelNickname.efectos)
		self.ventanaRegistro.widget.widget.labelNickname.setText("Nickname")
		indicador = indicador + self.ventanaRegistro.widget.widget.labelNickname.frameGeometry().height()

		self.ventanaRegistro.widget.widget.lineEditNickname = QtWidgets.QLineEdit(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.lineEditNickname.setFixedWidth(150)
		self.ventanaRegistro.widget.widget.lineEditNickname.move((self.ventanaRegistro.widget.widget.frameGeometry().width()/2)-75, indicador)
		self.ventanaRegistro.widget.widget.lineEditNickname.setObjectName("lineEditNickname")
		self.ventanaRegistro.widget.widget.lineEditNickname.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.widget.widget.lineEditNickname.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaRegistro.widget.widget.lineEditNickname))
		self.ventanaRegistro.widget.widget.lineEditNickname.textChanged.connect(self.verificarDatosRegistroNickname)
		self.ventanaRegistro.widget.widget.lineEditNickname.setPlaceholderText("Escribe un nickname")
		indicador = indicador + self.ventanaRegistro.widget.widget.labelNickname.frameGeometry().height()

		self.ventanaRegistro.widget.widget.labelErrorNickname = QtWidgets.QLabel(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.labelErrorNickname.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.labelErrorNickname.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget.labelErrorNickname.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.widget.widget.labelErrorNickname.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.labelErrorNickname.setGraphicsEffect(self.ventanaRegistro.widget.widget.labelErrorNickname.efectos)
		self.ventanaRegistro.widget.widget.labelErrorNickname.setObjectName("labelErrorNickname")
		self.ventanaRegistro.widget.widget.labelErrorNickname.setFixedWidth(self.ventanaRegistro.widget.widget.frameGeometry().width())
		self.ventanaRegistro.widget.widget.labelErrorNickname.move(0, indicador+5)
		self.ventanaRegistro.widget.widget.labelErrorNickname.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaRegistro.widget.widget.labelErrorNickname.setFont(font2)
		self.ventanaRegistro.widget.widget.labelErrorNickname.setText("\n")
		indicador = indicador + self.ventanaRegistro.widget.widget.labelErrorNickname.frameGeometry().height()+5

		self.ventanaRegistro.widget.widget.labelNombre = QtWidgets.QLabel(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.labelNombre.setFixedWidth(self.ventanaRegistro.widget.widget.frameGeometry().width())
		self.ventanaRegistro.widget.widget.labelNombre.move(0, indicador+15)
		self.ventanaRegistro.widget.widget.labelNombre.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget.labelNombre.setObjectName("labelNombre")
		self.ventanaRegistro.widget.widget.labelNombre.setFont(font)
		self.ventanaRegistro.widget.widget.labelNombre.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.labelNombre.efectos.setBlurRadius(10)
		self.ventanaRegistro.widget.widget.labelNombre.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.ventanaRegistro.widget.widget.labelNombre.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.labelNombre.setGraphicsEffect(self.ventanaRegistro.widget.widget.labelNombre.efectos)
		self.ventanaRegistro.widget.widget.labelNombre.setText("Nombre Completo")
		indicador = indicador + self.ventanaRegistro.widget.widget.labelNombre.frameGeometry().height()+15

		self.ventanaRegistro.widget.widget.lineEditNombre = QtWidgets.QLineEdit(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.lineEditNombre.setFixedWidth(150)
		self.ventanaRegistro.widget.widget.lineEditNombre.move((self.ventanaRegistro.widget.widget.frameGeometry().width()/2)-75, indicador)
		self.ventanaRegistro.widget.widget.lineEditNombre.setObjectName("lineEditNombre")
		self.ventanaRegistro.widget.widget.lineEditNombre.textChanged.connect(self.verificarDatosRegistroNombre)
		self.ventanaRegistro.widget.widget.lineEditNombre.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.widget.widget.lineEditNombre.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaRegistro.widget.widget.lineEditNombre))
		self.ventanaRegistro.widget.widget.lineEditNombre.setPlaceholderText("Escribe tu nombre")
		indicador = indicador + self.ventanaRegistro.widget.widget.lineEditNombre.frameGeometry().height()

		self.ventanaRegistro.widget.widget.labelErrorNombre = QtWidgets.QLabel(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.labelErrorNombre.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.labelErrorNombre.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget.labelErrorNombre.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.widget.widget.labelErrorNombre.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.labelErrorNombre.setGraphicsEffect(self.ventanaRegistro.widget.widget.labelErrorNombre.efectos)
		self.ventanaRegistro.widget.widget.labelErrorNombre.setObjectName("labelErrorNombre")
		self.ventanaRegistro.widget.widget.labelErrorNombre.setFixedWidth(self.ventanaRegistro.widget.widget.frameGeometry().width())
		self.ventanaRegistro.widget.widget.labelErrorNombre.move(0, indicador+5)
		self.ventanaRegistro.widget.widget.labelErrorNombre.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaRegistro.widget.widget.labelErrorNombre.setFont(font2)
		self.ventanaRegistro.widget.widget.labelErrorNombre.setText("\n")
		indicador = indicador + self.ventanaRegistro.widget.widget.labelErrorNombre.frameGeometry().height()+5

		self.ventanaRegistro.widget.widget.labelFechaNacimiento = QtWidgets.QLabel(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.setFixedWidth(self.ventanaRegistro.widget.widget.frameGeometry().width())
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.move(0, indicador+15)
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.setObjectName("labelFechaNacimiento")
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.setFont(font)
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.efectos.setBlurRadius(10)
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.setGraphicsEffect(self.ventanaRegistro.widget.widget.labelFechaNacimiento.efectos)
		self.ventanaRegistro.widget.widget.labelFechaNacimiento.setText("Fecha de Nacimiento")
		indicador = indicador + self.ventanaRegistro.widget.widget.labelFechaNacimiento.frameGeometry().height()+15

		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento = QtWidgets.QDateEdit(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setDateTime(QtCore.QDateTime.currentDateTime())
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setMinimumDate(QtCore.QDate(1930, 1, 1))
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setMaximumDate(QtCore.QDate.currentDate())
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setFixedWidth(150)
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.move((self.ventanaRegistro.widget.widget.frameGeometry().width()/2)-75, indicador)
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setObjectName("dateEditFechaNacimiento")
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setCalendarPopup(True)
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.keyPressEvent = self.pressKeyQDateEdit
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.keyReleaseEvent = self.releaseKeyQDateEdit
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.indicador = None
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.wheelEvent = self.eventoscalendario
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.customContextMenuRequested.connect(lambda: self.menuContextualCalendario(self.ventanaRegistro.widget.widget.dateEditFechaNacimiento))

		self.ventanaRegistro.widget.widget.calendario = QtWidgets.QCalendarWidget()
		self.ventanaRegistro.widget.widget.calendario.setFont(font2)
		self.ventanaRegistro.widget.widget.calendario.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.ventanaRegistro.widget.widget.calendario.setMinimumDate(QtCore.QDate(1930, 1, 1))
		self.ventanaRegistro.widget.widget.calendario.setMaximumDate(QtCore.QDate.currentDate())
		self.ventanaRegistro.widget.widget.calendario.setFirstDayOfWeek(QtCore.Qt.Monday)
		self.ventanaRegistro.widget.widget.calendario.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
		self.ventanaRegistro.widget.widget.calendario.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
		self.ventanaRegistro.widget.widget.calendario.setDateEditEnabled(False)
		self.ventanaRegistro.widget.widget.calendario.setObjectName("calendario")
		format= QtGui.QTextCharFormat()
		format.setForeground(QtGui.QColor(0,0,255))
		format.setBackground(QtGui.QColor(255,255,255))
		format.setFontWeight(QtGui.QFont.Bold)
		self.ventanaRegistro.widget.widget.calendario.setHeaderTextFormat(format)
		self.ventanaRegistro.widget.widget.calendario.setStyleSheet("""
		    QCalendarWidget QAbstractItemView{
		        background-color: white; /* цвет фона текущего месяца */
		        selection-background-color: pink; /* цвет фона выбранного дня */
		        selection-color: white; /* цвет текста выбранного дня */
		    }
		""")
		self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.setCalendarWidget(self.ventanaRegistro.widget.widget.calendario)
		indicador = indicador + self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.frameGeometry().height()+10


		self.ventanaRegistro.widget.widget.labelSexo = QtWidgets.QLabel(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.labelSexo.setFixedWidth(self.ventanaRegistro.widget.widget.frameGeometry().width())
		self.ventanaRegistro.widget.widget.labelSexo.move(0, indicador)
		self.ventanaRegistro.widget.widget.labelSexo.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget.labelSexo.setObjectName("labelSexo")
		self.ventanaRegistro.widget.widget.labelSexo.setFont(font)
		self.ventanaRegistro.widget.widget.labelSexo.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.labelSexo.efectos.setBlurRadius(10)
		self.ventanaRegistro.widget.widget.labelSexo.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.ventanaRegistro.widget.widget.labelSexo.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.labelSexo.setGraphicsEffect(self.ventanaRegistro.widget.widget.labelSexo.efectos)
		self.ventanaRegistro.widget.widget.labelSexo.setText("Sexo")
		indicador = indicador + self.ventanaRegistro.widget.widget.labelSexo.frameGeometry().height()

		self.ventanaRegistro.widget.widget.radioButtonMasculino = QtWidgets.QRadioButton(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.setFixedWidth(32)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.move((self.ventanaRegistro.widget.widget.frameGeometry().width()/2)-16-35, indicador)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.setChecked(True)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.setFont(font2)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.setObjectName("radioButtonMasculino")
		self.ventanaRegistro.widget.widget.radioButtonMasculino.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.radioButtonMasculino.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.efectos.setColor(QtGui.QColor("#FF4500"))
		self.ventanaRegistro.widget.widget.radioButtonMasculino.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.setGraphicsEffect(self.ventanaRegistro.widget.widget.radioButtonMasculino.efectos)
		self.ventanaRegistro.widget.widget.radioButtonMasculino.setText("M")

		self.ventanaRegistro.widget.widget.radioButtonFemenino = QtWidgets.QRadioButton(self.ventanaRegistro.widget.widget)
		self.ventanaRegistro.widget.widget.radioButtonFemenino.setFixedWidth(32)
		self.ventanaRegistro.widget.widget.radioButtonFemenino.move((self.ventanaRegistro.widget.widget.frameGeometry().width()/2)-16+35, indicador)
		self.ventanaRegistro.widget.widget.radioButtonFemenino.setFont(font2)
		self.ventanaRegistro.widget.widget.radioButtonFemenino.setObjectName("radioButtonFemenino")
		self.ventanaRegistro.widget.widget.radioButtonFemenino.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget.radioButtonFemenino.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget.radioButtonFemenino.efectos.setColor(QtGui.QColor("#FF4500"))
		self.ventanaRegistro.widget.widget.radioButtonFemenino.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget.radioButtonFemenino.setGraphicsEffect(self.ventanaRegistro.widget.widget.radioButtonFemenino.efectos)
		self.ventanaRegistro.widget.widget.radioButtonFemenino.setText("F")

		indicador = 0

		self.ventanaRegistro.widget.widget2.labelPregunta = QtWidgets.QLabel(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.labelPregunta.setFixedWidth(self.ventanaRegistro.widget.widget2.frameGeometry().width())
		self.ventanaRegistro.widget.widget2.labelPregunta.move(0, indicador)
		self.ventanaRegistro.widget.widget2.labelPregunta.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget2.labelPregunta.setObjectName("labelPregunta")
		self.ventanaRegistro.widget.widget2.labelPregunta.setFont(font)
		self.ventanaRegistro.widget.widget2.labelPregunta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget2.labelPregunta.efectos.setBlurRadius(10)
		self.ventanaRegistro.widget.widget2.labelPregunta.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.ventanaRegistro.widget.widget2.labelPregunta.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget2.labelPregunta.setGraphicsEffect(self.ventanaRegistro.widget.widget2.labelPregunta.efectos)
		self.ventanaRegistro.widget.widget2.labelPregunta.setText("Pregunta Secreta:")
		indicador = indicador + self.ventanaRegistro.widget.widget2.labelPregunta.frameGeometry().height()

		self.ventanaRegistro.widget.widget2.labelPregunta2 = QtWidgets.QLabel(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.labelPregunta2.setFixedWidth(self.ventanaRegistro.widget.widget2.frameGeometry().width())
		self.ventanaRegistro.widget.widget2.labelPregunta2.move(0, indicador)
		self.ventanaRegistro.widget.widget2.labelPregunta2.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget2.labelPregunta2.setObjectName("labelPregunta2")
		font3 = QtGui.QFont()
		font3.setFamily("Ubuntu")
		font3.setPointSize(11)
		self.ventanaRegistro.widget.widget2.labelPregunta2.setFont(font3)
		self.ventanaRegistro.widget.widget2.labelPregunta2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget2.labelPregunta2.efectos.setBlurRadius(10)
		self.ventanaRegistro.widget.widget2.labelPregunta2.efectos.setColor(QtGui.QColor("#FF4500"))
		self.ventanaRegistro.widget.widget2.labelPregunta2.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget2.labelPregunta2.setGraphicsEffect(self.ventanaRegistro.widget.widget2.labelPregunta2.efectos)
		self.ventanaRegistro.widget.widget2.labelPregunta2.setText("¿Cuál es tu banda favorite?")
		indicador = indicador + self.ventanaRegistro.widget.widget2.labelPregunta2.frameGeometry().height()

		self.ventanaRegistro.widget.widget2.labelRespuesta = QtWidgets.QLabel(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.labelRespuesta.setFixedWidth(self.ventanaRegistro.widget.widget2.frameGeometry().width())
		self.ventanaRegistro.widget.widget2.labelRespuesta.move(0, indicador)
		self.ventanaRegistro.widget.widget2.labelRespuesta.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget2.labelRespuesta.setObjectName("labelRespuesta")
		self.ventanaRegistro.widget.widget2.labelRespuesta.setFont(font)
		self.ventanaRegistro.widget.widget2.labelRespuesta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget2.labelRespuesta.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget2.labelRespuesta.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.ventanaRegistro.widget.widget2.labelRespuesta.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget2.labelRespuesta.setGraphicsEffect(self.ventanaRegistro.widget.widget2.labelRespuesta.efectos)
		self.ventanaRegistro.widget.widget2.labelRespuesta.setText("Respuesta Secreta")
		indicador = indicador + self.ventanaRegistro.widget.widget2.labelRespuesta.frameGeometry().height()

		self.ventanaRegistro.widget.widget2.lineEditRespuesta = QtWidgets.QLineEdit(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.lineEditRespuesta.setFixedWidth(150)
		self.ventanaRegistro.widget.widget2.lineEditRespuesta.move((self.ventanaRegistro.widget.widget2.frameGeometry().width()/2)-75, indicador)
		self.ventanaRegistro.widget.widget2.lineEditRespuesta.setObjectName("lineEditRespuesta")
		self.ventanaRegistro.widget.widget2.lineEditRespuesta.textChanged.connect(self.verificarDatosRegistroRespuesta)
		self.ventanaRegistro.widget.widget2.lineEditRespuesta.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.widget.widget2.lineEditRespuesta.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaRegistro.widget.widget2.lineEditRespuesta))
		self.ventanaRegistro.widget.widget2.lineEditRespuesta.setPlaceholderText("Escribe tu respuesta")
		indicador = indicador + self.ventanaRegistro.widget.widget2.lineEditRespuesta.frameGeometry().height()

		self.ventanaRegistro.widget.widget2.labelErrorRespuesta = QtWidgets.QLabel(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setGraphicsEffect(self.ventanaRegistro.widget.widget2.labelErrorRespuesta.efectos)
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setObjectName("labelErrorRespuesta")
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setFixedWidth(self.ventanaRegistro.widget.widget2.frameGeometry().width())
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.move(0, indicador+5)
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setFont(font2)
		self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setText("\n")
		indicador = indicador + self.ventanaRegistro.widget.widget2.labelErrorRespuesta.frameGeometry().height()

		self.ventanaRegistro.widget.widget2.labelClave = QtWidgets.QLabel(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.labelClave.setFixedWidth(self.ventanaRegistro.widget.widget2.frameGeometry().width())
		self.ventanaRegistro.widget.widget2.labelClave.move(0, indicador+15)
		self.ventanaRegistro.widget.widget2.labelClave.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.widget.widget2.labelClave.setObjectName("labelClave")
		self.ventanaRegistro.widget.widget2.labelClave.setFont(font)
		self.ventanaRegistro.widget.widget2.labelClave.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget2.labelClave.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget2.labelClave.efectos.setColor(QtGui.QColor("#00FA9A"))
		self.ventanaRegistro.widget.widget2.labelClave.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget2.labelClave.setGraphicsEffect(self.ventanaRegistro.widget.widget2.labelClave.efectos)
		self.ventanaRegistro.widget.widget2.labelClave.setText("Contraseña")
		indicador = indicador + self.ventanaRegistro.widget.widget2.labelClave.frameGeometry().height() + 15

		self.ventanaRegistro.widget.widget2.lineEditClave = QtWidgets.QLineEdit(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.lineEditClave.setFixedWidth(150)
		self.ventanaRegistro.widget.widget2.lineEditClave.move((self.ventanaRegistro.widget.widget2.frameGeometry().width()/2)-75, indicador)
		self.ventanaRegistro.widget.widget2.lineEditClave.setObjectName("lineEditClave")
		self.ventanaRegistro.widget.widget2.lineEditClave.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ventanaRegistro.widget.widget2.lineEditClave.textChanged.connect(self.verificarDatosRegistroClave)
		self.ventanaRegistro.widget.widget2.lineEditClave.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.widget.widget2.lineEditClave.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.ventanaRegistro.widget.widget2.lineEditClave))
		self.ventanaRegistro.widget.widget2.lineEditClave.indicador = None
		self.ventanaRegistro.widget.widget2.lineEditClave.keyPressEvent = self.pressKeyQLineEditPasswordVentanaRegistro
		self.ventanaRegistro.widget.widget2.lineEditClave.keyReleaseEvent = self.releaseKeyQLineEditPasswordVentanaRegistro
		self.ventanaRegistro.widget.widget2.lineEditClave.setPlaceholderText("Escribe una contraseña")
		indicador = indicador + self.ventanaRegistro.widget.widget2.lineEditClave.frameGeometry().height()

		self.ventanaRegistro.widget.widget2.labelErrorClave = QtWidgets.QLabel(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.labelErrorClave.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget2.labelErrorClave.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget2.labelErrorClave.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.widget.widget2.labelErrorClave.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget2.labelErrorClave.setGraphicsEffect(self.ventanaRegistro.widget.widget2.labelErrorClave.efectos)
		self.ventanaRegistro.widget.widget2.labelErrorClave.setObjectName("labelErrorClave")
		self.ventanaRegistro.widget.widget2.labelErrorClave.setFixedWidth(self.ventanaRegistro.widget.widget2.frameGeometry().width())
		self.ventanaRegistro.widget.widget2.labelErrorClave.move(0, indicador+5)
		self.ventanaRegistro.widget.widget2.labelErrorClave.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaRegistro.widget.widget2.labelErrorClave.setFont(font2)
		self.ventanaRegistro.widget.widget2.labelErrorClave.setText("\n")
		indicador = indicador + self.ventanaRegistro.widget.widget2.labelErrorClave.frameGeometry().height()+15

		self.ventanaRegistro.widget.widget2.lineEditClave2 = QtWidgets.QLineEdit(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.lineEditClave2.setFixedWidth(150)
		self.ventanaRegistro.widget.widget2.lineEditClave2.move((self.ventanaRegistro.widget.widget2.frameGeometry().width()/2)-75, indicador)
		self.ventanaRegistro.widget.widget2.lineEditClave2.setObjectName("lineEditClave2")
		self.ventanaRegistro.widget.widget2.lineEditClave2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ventanaRegistro.widget.widget2.lineEditClave2.textChanged.connect(self.verificarDatosRegistroClave2)
		self.ventanaRegistro.widget.widget2.lineEditClave2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.widget.widget2.lineEditClave2.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.ventanaRegistro.widget.widget2.lineEditClave2))
		self.ventanaRegistro.widget.widget2.lineEditClave2.indicador = None
		self.ventanaRegistro.widget.widget2.lineEditClave2.keyPressEvent = self.pressKeyQLineEditPassword2VentanaRegistro
		self.ventanaRegistro.widget.widget2.lineEditClave2.keyReleaseEvent = self.releaseKeyQLineEditPassword2VentanaRegistro
		self.ventanaRegistro.widget.widget2.lineEditClave2.setEnabled(False)
		self.ventanaRegistro.widget.widget2.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
		self.ventanaRegistro.widget.widget2.lineEditClave2.setPlaceholderText("Confirma la contraseña")
		indicador = indicador + self.ventanaRegistro.widget.widget2.lineEditClave2.frameGeometry().height()

		self.ventanaRegistro.widget.widget2.labelErrorClave2 = QtWidgets.QLabel(self.ventanaRegistro.widget.widget2)
		self.ventanaRegistro.widget.widget2.labelErrorClave2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.widget.widget2.labelErrorClave2.efectos.setBlurRadius(5)
		self.ventanaRegistro.widget.widget2.labelErrorClave2.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.widget.widget2.labelErrorClave2.efectos.setOffset(0,0)
		self.ventanaRegistro.widget.widget2.labelErrorClave2.setGraphicsEffect(self.ventanaRegistro.widget.widget2.labelErrorClave2.efectos)
		self.ventanaRegistro.widget.widget2.labelErrorClave2.setObjectName("labelErrorClave")
		self.ventanaRegistro.widget.widget2.labelErrorClave2.setFixedWidth(self.ventanaRegistro.widget.widget2.frameGeometry().width())
		self.ventanaRegistro.widget.widget2.labelErrorClave2.move(0, indicador+5)
		self.ventanaRegistro.widget.widget2.labelErrorClave2.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaRegistro.widget.widget2.labelErrorClave2.setFont(font2)
		self.ventanaRegistro.widget.widget2.labelErrorClave2.setText("\n")
		indicador = indicador + self.ventanaRegistro.widget.widget2.labelErrorClave2.frameGeometry().height()

		self.ventanaRegistro.botones = QtWidgets.QDialogButtonBox(self.ventanaRegistro.widget)
		self.ventanaRegistro.botones.setFixedWidth(160)
		self.ventanaRegistro.botones.move((self.ventanaRegistro.widget.frameGeometry().width()/2)-80, self.ventanaRegistro.widget.frameGeometry().height()-60)
		self.ventanaRegistro.botones.setOrientation(QtCore.Qt.Horizontal)
		self.ventanaRegistro.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.ventanaRegistro.botones.setCenterButtons(True)
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setObjectName("Boton_Aceptar")
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setFixedSize(70,25)
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setText("Aceptar")
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: SocketCliente.controladorRegistro(self))
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
			#Boton_Aceptar{
				background-color: gray;
				color: #fff;
				font-family: Ubuntu;
				font-size: 15px;
				border-radius: 4px;
			}
		""")

		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Cancel).setObjectName("Boton_Cancelar")
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Cancel).setFixedSize(70,25)
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Cancel).setText("Cancelar")
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: self.ventanaRegistro.hide())
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet("""
			#Boton_Cancelar{
				background-color: white;
				color: black;
				font-family: Ubuntu;
				font-size: 15px;
				border-radius: 4px;
				border: 2px solid red;

			}
			#Boton_Cancelar:hover{
				background-color: red;
				border: 2px solid white;
				color: white;
			}
			#Boton_Cancelar:pressed{
				background-color: #8B0000;
				border: 2px solid red;
				color: white;
			}
		""")

		self.ventanaRegistro.Nickname = 0
		self.ventanaRegistro.Nombre = 0
		self.ventanaRegistro.Respuesta = 0
		self.ventanaRegistro.Clave = 0
		self.ventanaRegistro.Clave2 = 0

		#self.ventanaRegistro.exec_()
		self.ventanaRegistro.show()
	def menuContextualCalendario(self, objeto):
		menuContextual = QtWidgets.QMenu()

		actionCopiar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accioncopiar.png'), '&Copiar\tCTRL+C')
		actionCopiar.setShortcut('CTRL+C')
		actionCopiar.triggered.connect(lambda: objeto.lineEdit().copy())
		if objeto.lineEdit().hasSelectedText() == True:
			actionCopiar.setEnabled(True)
		else:
			actionCopiar.setEnabled(False)

		actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A')
		actionSeleccionarTodo.setShortcut('CTRL+A')
		actionSeleccionarTodo.triggered.connect(lambda: objeto.selectAll())
		if len(objeto.text()):
			if len(objeto.lineEdit().selectedText()) != len(objeto.lineEdit().text()):
				actionSeleccionarTodo.setEnabled(True)
			else:
				actionSeleccionarTodo.setEnabled(False)
		else:
			actionSeleccionarTodo.setEnabled(False)

		menuContextual.addAction(actionCopiar)
		menuContextual.addSeparator()
		menuContextual.addAction(actionSeleccionarTodo)
		menuContextual.exec_(QtGui.QCursor.pos())
	####Evitar Cortar y copiar en un QLineEdit de Password
	def pressKeyQLineEditPasswordVentanaRegistro(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.widget.widget2.lineEditClave.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget2.lineEditClave, event)
		elif event.key() == 88 or event.key() == 67:
			if self.ventanaRegistro.widget.widget2.lineEditClave.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget2.lineEditClave, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget2.lineEditClave, event)

	def releaseKeyQLineEditPasswordVentanaRegistro(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.widget.widget2.lineEditClave.indicador = 0

	def pressKeyQLineEditPassword2VentanaRegistro(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.widget.widget2.lineEditClave2.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget2.lineEditClave2, event)
		elif event.key() == 88 or event.key() == 67:
			if self.ventanaRegistro.widget.widget2.lineEditClave2.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget2.lineEditClave2, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget2.lineEditClave2, event)

	def releaseKeyQLineEditPassword2VentanaRegistro(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.widget.widget2.lineEditClave2.indicador = 0
	##################################################
	def eventoscalendario(self, event):
		event.ignore()

	def pressKeyQDateEdit(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.lineEdit(), event)
		elif event.key() == 65 or event.key() == 67:
			if self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.indicador == 1:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.lineEdit(), event)
			else:
				event.ignore()
		else:
			event.ignore()

	def releaseKeyQDateEdit(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.widget.widget.dateEditFechaNacimiento.indicador = 0

	#Verificación sintáctica/semántica de datos
	def verificarDatosRegistroNickname(self):
		if len(self.ventanaRegistro.widget.widget.lineEditNickname.text()) == 0:
			self.ventanaRegistro.widget.widget.labelErrorNickname.setText("\n")
			self.ventanaRegistro.Nickname = 0
			verificacion(self, 'VL_VR Cancelar')
		else:
			if len(self.ventanaRegistro.widget.widget.lineEditNickname.text()) < 6:
				self.ventanaRegistro.Nickname = 0
				self.ventanaRegistro.widget.widget.labelErrorNickname.setText("El nickname debe ser mínimo de 6 caracteres.")
				verificacion(self, 'VL_VR Cancelar')
			elif len(self.ventanaRegistro.widget.widget.lineEditNickname.text()) > 20:
				self.ventanaRegistro.Nickname = 0
				self.ventanaRegistro.widget.widget.labelErrorNickname.setText("El nickname debe ser máximo de 20 caracteres.")
				verificacion(self, 'VL_VR Cancelar')
			elif re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', self.ventanaRegistro.widget.widget.lineEditNickname.text()) is None:
				self.ventanaRegistro.Nickname = 0
				self.ventanaRegistro.widget.widget.labelErrorNickname.setText("El nickname no puede comenzar con números,\ntener espacios o caracteres especiales.")
				self.ventanaRegistro.widget.widget.labelErrorNickname.setWordWrap(True)
				verificacion(self, 'VL_VR Cancelar')
			else:
				self.ventanaRegistro.Nickname = 1
				self.ventanaRegistro.widget.widget.labelErrorNickname.setText("\n")
				if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
					verificacion(self, 'VL_VR Aceptar')
				else:
					verificacion(self, 'VL_VR Cancelar')

	def verificarDatosRegistroNombre(self):
		if len(self.ventanaRegistro.widget.widget.lineEditNombre.text()) == 0:
			self.ventanaRegistro.widget.widget.labelErrorNombre.setText("\n")
			self.ventanaRegistro.Nombre = 0
			verificacion(self, 'VL_VR Cancelar')
		else:
			if len(self.ventanaRegistro.widget.widget.lineEditNombre.text()) < 5:
				self.ventanaRegistro.Nombre = 0
				self.ventanaRegistro.widget.widget.labelErrorNombre.setText("Escribe tu nombre completo.")
				verificacion(self, 'VL_VR Cancelar')
			elif re.match(r'^[a-zA-ZÀ-ÿ\u00f1\u00d1][a-zA-Z À-ÿ\u00f1\u00d1]*$', self.ventanaRegistro.widget.widget.lineEditNombre.text()) is None:
				self.ventanaRegistro.Nombre = 0
				self.ventanaRegistro.widget.widget.labelErrorNombre.setText("El nombre no puede contener números\no caracteres especiales.")
				self.ventanaRegistro.widget.widget.labelErrorNombre.setWordWrap(True)
				verificacion(self, 'VL_VR Cancelar')
			else:
				self.ventanaRegistro.Nombre = 1
				self.ventanaRegistro.widget.widget.labelErrorNombre.setText("\n")
				if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
					verificacion(self, 'VL_VR Aceptar')
				else:
					verificacion(self, 'VL_VR Cancelar')

	def verificarDatosRegistroRespuesta(self):
		if len(self.ventanaRegistro.widget.widget2.lineEditRespuesta.text()) == 0:
			self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setText("Escribe una respuesta secreta.")
			self.ventanaRegistro.Respuesta = 0
			verificacion(self, 'VL_VR Cancelar')
		else:
			if re.match(r'^[^:]*$', self.ventanaRegistro.widget.widget2.lineEditRespuesta.text()) is None:
				self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setText("Caracter dos puntos ':' no admitido\nen la respuesta secreta.")
				self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setWordWrap(True)
				self.ventanaRegistro.Respuesta = 0
				verificacion(self, 'VL_VR Cancelar')
			else:
				self.ventanaRegistro.Respuesta = 1
				self.ventanaRegistro.widget.widget2.labelErrorRespuesta.setText("\n")
				if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
					verificacion(self, 'VL_VR Aceptar')
				else:
					verificacion(self, 'VL_VR Cancelar')

	def verificarDatosRegistroClave(self):
		if len(self.ventanaRegistro.widget.widget2.lineEditClave.text()) == 0:
			self.ventanaRegistro.widget.widget2.labelErrorClave.setText("\n")
			self.ventanaRegistro.Clave = 0
			verificacion(self, 'VL_VR Cancelar')
			self.ventanaRegistro.widget.widget2.lineEditClave2.blockSignals(True)
			self.ventanaRegistro.widget.widget2.lineEditClave2.clear()
			self.ventanaRegistro.widget.widget2.labelErrorClave2.setText("\n")
			self.ventanaRegistro.widget.widget2.lineEditClave2.blockSignals(False)
			self.ventanaRegistro.widget.widget2.lineEditClave2.setEnabled(False)
			self.ventanaRegistro.widget.widget2.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
		else:
			self.ventanaRegistro.widget.widget2.lineEditClave2.blockSignals(True)
			self.ventanaRegistro.widget.widget2.lineEditClave2.clear()
			self.ventanaRegistro.widget.widget2.lineEditClave2.blockSignals(False)
			if len(self.ventanaRegistro.widget.widget2.lineEditClave.text()) < 6:
				self.ventanaRegistro.widget.widget2.lineEditClave2.setEnabled(False)
				self.ventanaRegistro.widget.widget2.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
				self.ventanaRegistro.Clave = 0
				self.ventanaRegistro.widget.widget2.labelErrorClave.setText("La contraseña debe ser de mínimo 6 caracteres.")
				verificacion(self, 'VL_VR Cancelar')
			elif re.match(r'^[^:]*$', self.ventanaRegistro.widget.widget2.lineEditClave.text()) is None:
				self.ventanaRegistro.widget.widget2.labelErrorClave.setText("Caracter dos puntos ':' no admitido\nen la contraseña.")
				self.ventanaRegistro.widget.widget2.labelErrorClave.setWordWrap(True)
				self.ventanaRegistro.widget.widget2.lineEditClave2.setEnabled(False)
				self.ventanaRegistro.widget.widget2.lineEditClave2.setStyleSheet('background-color: #B0C4DE;')
				self.ventanaRegistro.Clave = 0
				verificacion(self, 'VL_VR Cancelar')
			else:
				self.ventanaRegistro.Clave = 1
				self.ventanaRegistro.widget.widget2.lineEditClave2.setEnabled(True)
				self.ventanaRegistro.widget.widget2.lineEditClave2.setStyleSheet('background-color: white;')
				self.ventanaRegistro.widget.widget2.labelErrorClave.setText("\n")
				verificacion(self, 'VL_VR Cancelar')

	def verificarDatosRegistroClave2(self):
		if len(self.ventanaRegistro.widget.widget2.lineEditClave2.text()) == 0:
			self.ventanaRegistro.Clave2 = 0
			verificacion(self, 'VL_VR Cancelar')
			self.ventanaRegistro.widget.widget2.labelErrorClave2.setText("Confirma la contraseña.")
		else:
			if len(self.ventanaRegistro.widget.widget2.lineEditClave2.text()) < 6:
				self.ventanaRegistro.Clave2 = 0
				self.ventanaRegistro.widget.widget2.labelErrorClave2.setText("La contraseña debe ser de mínimo 6 caracteres.")
				verificacion(self, 'VL_VR Cancelar')
			elif re.match(r'^[^:]*$', self.ventanaRegistro.widget.widget2.lineEditClave2.text()) is None:
					self.ventanaRegistro.widget.widget2.labelErrorClave2.setText("Caracter dos puntos ':' no admitido\nen la contraseña.")
					self.ventanaRegistro.widget.widget2.labelErrorClave2.setWordWrap(True)
					self.ventanaRegistro.Clave = 0
					verificacion(self, 'VL_VR Cancelar')
			else:
				if self.ventanaRegistro.widget.widget2.lineEditClave.text() != self.ventanaRegistro.widget.widget2.lineEditClave2.text():
					self.ventanaRegistro.Clave2 = 0
					self.ventanaRegistro.widget.widget2.labelErrorClave2.setText("Las contraseñas no coinciden.")
					verificacion(self, 'VL_VR Cancelar')
				else:
					self.ventanaRegistro.widget.widget2.labelErrorClave2.setText("\n")
					self.ventanaRegistro.Clave2 = 1
					verificacion(self, 'VL_VR Habilitar Clave')
					if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
						verificacion(self, 'VL_VR Aceptar')
					else:
						verificacion(self, 'VL_VR Cancelar')

#-------------------------------------------------------------------------------------------------------------------------------------

def main():
	app = QtWidgets.QApplication(sys.argv)
	QtGui.QFontDatabase.addApplicationFont('Ubuntu.ttf')
	QtGui.QFontDatabase.addApplicationFont('segoeuil.ttf')
	VentanaLogin = Ventana_Login()
	VentanaLogin.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	import atexit
	atexit.register(SocketCliente.exit_handler)
	app = QtWidgets.QApplication(sys.argv)
	QtGui.QFontDatabase.addApplicationFont('Ubuntu.ttf')
	QtGui.QFontDatabase.addApplicationFont('segoeuil.ttf')
	VentanaLogin = Ventana_Login()
	#VentanaLogin.ventana_clave_nueva('reyda')
	VentanaLogin.show()
	sys.exit(app.exec_())
