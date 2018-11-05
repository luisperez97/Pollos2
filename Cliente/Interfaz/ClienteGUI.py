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


import sys 
sys.path.append('..')

#import Cliente.SocketCliente
import SocketCliente

def estiloventanaprincipal(ventanaprincipal):
	ventanaprincipal.setStyleSheet("""
		#Widget_Principal, VentanaPrincipal{
			background-image: url(pollos.jpg);
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
			color: white;
			font-weight: bold;
		}
		
		#label_login{
			font-size:30px;
			color: #fff;
			font-weight: bold;
		}

		#label_olvido{
			color: blue;
			text-decoration: underline;
			font-weight: bold;
		}
		#label_olvido:hover{
			color:red;
		}
		
		#label_error{
			color: magenta;
			background-color: transparent;
		}
	""")

def estiloventanaolvidoclave(ventanaolvido):
	ventanaolvido.setStyleSheet("""
		#Ventana_Olvido{
			background-image: url(pollos3.jpg);
		}
		
		#label_Usuario, label_preguntasecreta, label_respuestasecreta{
			background-color: transparent;
			color: black;
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
			background-image: url(pollos4.jpg);
		}
		
		#Label_Clave, Label_Clave2{
			background-color: transparent;
			color: black;
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
			border-image: url(pollos5.jpg);
		}
		
		#labelNickname, #labelNombre, #labelPregunta, #labelSexo, #labelRespuesta, #labelClave, #labelClave2, #labelFechaNacimiento{
			background-color: transparent;
			color: white;
		}
		#labelPregunta2{
			text-decoration: underline;
			color: white;
		}

		#radioButtonMasculino, #radioButtonFemenino{
			color: white;
		}
		#radioButtonMasculino:checked, #radioButtonFemenino:checked{
			color: black;
		}
		
		#labelError{
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
			border-image: url(arrow.png);
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
		elif mensaje.split(' ')[1] == 'Habilitar':
			if mensaje.split(' ')[2] == 'Nickname':
				objeto.ventanaRegistro.lineEditNombre.setEnabled(True)
				objeto.ventanaRegistro.lineEditNombre.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditRespuesta.setEnabled(True)
				objeto.ventanaRegistro.lineEditRespuesta.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditClave.setEnabled(True)
				objeto.ventanaRegistro.lineEditClave.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditClave2.setEnabled(True)
				objeto.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: white;')
			elif mensaje.split(' ')[2] == 'Nombre':
				objeto.ventanaRegistro.lineEditNickname.setEnabled(True)
				objeto.ventanaRegistro.lineEditNickname.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditRespuesta.setEnabled(True)
				objeto.ventanaRegistro.lineEditRespuesta.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditClave.setEnabled(True)
				objeto.ventanaRegistro.lineEditClave.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditClave2.setEnabled(True)
				objeto.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: white;')
			elif mensaje.split(' ')[2] == 'Respuesta':
				objeto.ventanaRegistro.lineEditNickname.setEnabled(True)
				objeto.ventanaRegistro.lineEditNickname.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditNombre.setEnabled(True)
				objeto.ventanaRegistro.lineEditNombre.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditClave.setEnabled(True)
				objeto.ventanaRegistro.lineEditClave.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditClave2.setEnabled(True)
				objeto.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: white;')
			elif mensaje.split(' ')[2] == 'Clave':
				objeto.ventanaRegistro.lineEditNickname.setEnabled(True)
				objeto.ventanaRegistro.lineEditNickname.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditNombre.setEnabled(True)
				objeto.ventanaRegistro.lineEditNombre.setStyleSheet('background-color: white;')
				objeto.ventanaRegistro.lineEditRespuesta.setEnabled(True)
				objeto.ventanaRegistro.lineEditRespuesta.setStyleSheet('background-color: white;')
		elif mensaje.split(' ')[1] == 'Deshabilitar':
			if mensaje.split(' ')[2] == 'Nickname':
				objeto.ventanaRegistro.lineEditNombre.setEnabled(False)
				objeto.ventanaRegistro.lineEditNombre.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditRespuesta.setEnabled(False)
				objeto.ventanaRegistro.lineEditRespuesta.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditClave.setEnabled(False)
				objeto.ventanaRegistro.lineEditClave.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditClave2.setEnabled(False)
				objeto.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
			elif mensaje.split(' ')[2] == 'Nombre':
				objeto.ventanaRegistro.lineEditNickname.setEnabled(False)
				objeto.ventanaRegistro.lineEditNickname.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditRespuesta.setEnabled(False)
				objeto.ventanaRegistro.lineEditRespuesta.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditClave.setEnabled(False)
				objeto.ventanaRegistro.lineEditClave.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditClave2.setEnabled(False)
				objeto.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
			elif mensaje.split(' ')[2] == 'Respuesta':
				objeto.ventanaRegistro.lineEditNickname.setEnabled(False)
				objeto.ventanaRegistro.lineEditNickname.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditNombre.setEnabled(False)
				objeto.ventanaRegistro.lineEditNombre.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditClave.setEnabled(False)
				objeto.ventanaRegistro.lineEditClave.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditClave2.setEnabled(False)
				objeto.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
			elif mensaje.split(' ')[2] == 'Clave':
				objeto.ventanaRegistro.lineEditNickname.setEnabled(False)
				objeto.ventanaRegistro.lineEditNickname.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditNombre.setEnabled(False)
				objeto.ventanaRegistro.lineEditNombre.setStyleSheet('background-color: #D3D3D3;')
				objeto.ventanaRegistro.lineEditRespuesta.setEnabled(False)
				objeto.ventanaRegistro.lineEditRespuesta.setStyleSheet('background-color: #D3D3D3;')
			
			
class Ventana_Principal(QtWidgets.QMainWindow):
	#Ventana Principal------------------------------------------------------------------------------------------------------------------------
	def __init__(self):
		super(Ventana_Principal, self).__init__()
		self.setObjectName("VentanaPrincipal")
		self.setWindowIcon(QtGui.QIcon('icono.png'))
		self.setFixedSize(394, 360)
		self.setWindowTitle("Pollos")
		estiloventanaprincipal(self)

		self.Widget_Principal = QtWidgets.QWidget()
		self.Widget_Principal.setObjectName("Widget_Principal")
		
		self.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.efectos.setBlurRadius(0)
		self.efectos.setColor(QtGui.QColor("#FFFF00"))
		self.efectos.setOffset(1,1)
		
		self.labelLogin = QtWidgets.QLabel(self.Widget_Principal)
		self.labelLogin.setFixedWidth(self.frameGeometry().width())
		self.labelLogin.move(0, 30)
		self.labelLogin.setAlignment(Qt.AlignCenter)
		self.labelLogin.setObjectName("label_login")
		self.labelLogin.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelLogin.efectos.setBlurRadius(0)
		self.labelLogin.efectos.setColor(QtGui.QColor("#FFFF00"))
		self.labelLogin.efectos.setOffset(1,1)
		self.labelLogin.setGraphicsEffect(self.labelLogin.efectos)
		self.labelLogin.setText("Pollos\' ChatRoom")
		
		self.labelUsuario = QtWidgets.QLabel(self.Widget_Principal)
		self.labelUsuario.setFixedWidth(self.frameGeometry().width())
		self.labelUsuario.move(0, 90)
		self.labelUsuario.setAlignment(Qt.AlignCenter)
		self.labelUsuario.setObjectName("label_usuario")
		self.labelUsuario.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelUsuario.efectos.setBlurRadius(0)
		self.labelUsuario.efectos.setColor(QtGui.QColor("#000000"))
		self.labelUsuario.efectos.setOffset(1,1)
		self.labelUsuario.setGraphicsEffect(self.labelUsuario.efectos)
		self.labelUsuario.setText("Nickname")
		
		self.lineEditUsuario = QtWidgets.QLineEdit(self.Widget_Principal)
		self.lineEditUsuario.setFixedWidth(131)
		self.lineEditUsuario.move(131.5, 120)
		self.lineEditUsuario.setObjectName("lineEdit_Usuario")
		self.lineEditUsuario.textChanged.connect(self.lineEditVerificarUsuario)
		self.lineEditUsuario.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.lineEditUsuario.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.lineEditUsuario))
		self.lineEditUsuario.returnPressed.connect(self.botonLoginPress)
		
		self.labelPassword = QtWidgets.QLabel(self.Widget_Principal)
		self.labelPassword.setFixedWidth(self.frameGeometry().width())
		self.labelPassword.move(0, 160)
		self.labelPassword.setAlignment(Qt.AlignCenter)
		self.labelPassword.setObjectName("label_password")
		self.labelPassword.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelPassword.efectos.setBlurRadius(0)
		self.labelPassword.efectos.setColor(QtGui.QColor("#000000"))
		self.labelPassword.efectos.setOffset(1,1)
		self.labelPassword.setGraphicsEffect(self.labelPassword.efectos)
		self.labelPassword.setText("Contraseña")
		
		self.lineEditPassword = QtWidgets.QLineEdit(self.Widget_Principal)
		self.lineEditPassword.setFixedWidth(131)
		self.lineEditPassword.move(131.5, 190)
		self.lineEditPassword.setObjectName("lineEdit_Password")
		self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEditPassword.textChanged.connect(self.lineEditVerificarClave)
		self.lineEditPassword.keyPressEvent = self.pressKeyQLineEditPassword
		self.lineEditPassword.keyReleaseEvent = self.releaseKeyQLineEditPassword
		self.lineEditPassword.indicador = None
		self.lineEditPassword.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.lineEditPassword.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.lineEditPassword))
		self.lineEditPassword.returnPressed.connect(self.botonLoginPress)
		self.lineEditPassword.setEnabled(False)
		self.lineEditPassword.setStyleSheet('background-color: #D3D3D3;')
		
		self.labelOlvidoPassword = QtWidgets.QLabel(self.Widget_Principal)
		self.labelOlvidoPassword.setFixedWidth(self.frameGeometry().width())
		self.labelOlvidoPassword.move(0, 225)
		self.labelOlvidoPassword.setAlignment(Qt.AlignCenter)
		self.labelOlvidoPassword.setObjectName("label_olvido")
		self.labelOlvidoPassword.mouseReleaseEvent = self.eventolabelOlvido
		self.labelOlvidoPassword.setText("Olvidó su contraseña?")
		
		self.labelError = QtWidgets.QLabel(self.Widget_Principal)
		self.labelError.setFixedWidth(self.frameGeometry().width())
		self.labelError.move(0, 245)
		self.labelError.setAlignment(Qt.AlignCenter)
		self.labelError.setObjectName("label_error")
		self.labelError.setWordWrap(True)
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.labelError.setFont(font)
		self.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.labelError.efectos.setBlurRadius(0)
		self.labelError.efectos.setColor(QtGui.QColor("#000000"))
		self.labelError.efectos.setOffset(1,1)
		self.labelError.setGraphicsEffect(self.labelError.efectos)
		
		self.botonLogin = QtWidgets.QPushButton(self.Widget_Principal)
		self.botonLogin.setFixedSize(120, 31)
		self.botonLogin.move(137, 270)
		self.botonLogin.setObjectName("QPushButtonLogin")
		self.botonLogin.setEnabled(False)
		self.botonLogin.clicked.connect(lambda: SocketCliente.controladorInicioSesion(self))
		self.botonLogin.setText("Iniciar Sesión")
		
		
		self.botonRegistro = QtWidgets.QPushButton(self.Widget_Principal)
		self.botonRegistro.setFixedSize(120, 31)
		self.botonRegistro.move(137, 312)
		self.botonRegistro.setObjectName("QPushButtonRegistro")
		self.botonRegistro.clicked.connect(self.registro_ventana)
		self.botonRegistro.setText("Registrarse")
		
		self.NicknameVerificar = 0
		self.ClaveVerificar = 0

		#-------------------------------------
		self.lineEditPassword.raise_()
		self.lineEditUsuario.raise_()
		self.botonRegistro.raise_()
		self.labelUsuario.raise_()
		self.labelLogin.raise_()
		self.labelPassword.raise_()
		self.labelOlvidoPassword.raise_()
		self.labelError.raise_()
		#------------------------------------
		self.setCentralWidget(self.Widget_Principal)
		
		self.lineEditUsuario.setFocus()
	
	def eventolabelOlvido(self, event):
		if event.button() == 1:
			QtWidgets.QLabel.mouseReleaseEvent(self.labelOlvidoPassword, event)
			self.olvido_ventana()
		else:
			event.ignore()

	def botonLoginPress(self):
		self.botonLogin.click()
	
	def menuContextualQLineEdit(self, objeto):
		menuContextual = QtWidgets.QMenu()
		poderPegar = QtWidgets.QApplication.clipboard().text()
		
		actionDeshacer = QtWidgets.QAction(QtGui.QIcon('acciondeshacer.png'), '&Deshacer\tCTRL+Z')
		actionDeshacer.setShortcut('CTRL+Z')
		actionDeshacer.triggered.connect(lambda: objeto.undo())
		if objeto.isUndoAvailable() == True:
			actionDeshacer.setEnabled(True)
		else:
			actionDeshacer.setEnabled(False)
		
		actionRehacer = QtWidgets.QAction(QtGui.QIcon('accionrehacer.png'), '&Rehacer\tCTRL+Y')
		actionRehacer.setShortcut('CTRL+Y')
		actionRehacer.triggered.connect(lambda: objeto.redo())
		if objeto.isRedoAvailable() == True:
			actionRehacer.setEnabled(True)
		else:
			actionRehacer.setEnabled(False)
		
		actionCortar = QtWidgets.QAction(QtGui.QIcon('accioncortar.png'), '&Cortar\tCTRL+X')
		actionCortar.setShortcut('CTRL+X')
		actionCortar.triggered.connect(lambda: objeto.cut())
		if objeto.hasSelectedText() == True:
			actionCortar.setEnabled(True)
		else:
			actionCortar.setEnabled(False)
			
		actionCopiar = QtWidgets.QAction(QtGui.QIcon('accioncopiar.png'), '&Copiar\tCTRL+C')
		actionCopiar.setShortcut('CTRL+C')
		actionCopiar.triggered.connect(lambda: objeto.copy())
		if objeto.hasSelectedText() == True:
			actionCopiar.setEnabled(True)
		else:
			actionCopiar.setEnabled(False)
			
		actionPegar = QtWidgets.QAction(QtGui.QIcon('accionpegar.png'), '&Pegar\tCTRL+V')
		actionPegar.setShortcut('CTRL+V')
		actionPegar.triggered.connect(lambda: objeto.paste())
		if len(poderPegar):
			actionPegar.setEnabled(True)
		else:
			actionPegar.setEnabled(False)
			
		actionEliminar = QtWidgets.QAction(QtGui.QIcon('accionborrar.png'), '&Eliminar')
		actionEliminar.triggered.connect(lambda: objeto.backspace())
		if objeto.hasSelectedText() == True:
			actionEliminar.setEnabled(True)
		else:
			actionEliminar.setEnabled(False)
			
		actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A')
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
		
		actionDeshacer = QtWidgets.QAction(QtGui.QIcon('acciondeshacer.png'), '&Deshacer\tCTRL+Z')
		actionDeshacer.setShortcut('CTRL+Z')
		actionDeshacer.triggered.connect(lambda: objeto.undo())
		if objeto.isUndoAvailable() == True:
			actionDeshacer.setEnabled(True)
		else:
			actionDeshacer.setEnabled(False)
		
		actionRehacer = QtWidgets.QAction(QtGui.QIcon('accionrehacer.png'), '&Rehacer\tCTRL+Y')
		actionRehacer.setShortcut('CTRL+Y')
		actionRehacer.triggered.connect(lambda: objeto.redo())
		if objeto.isRedoAvailable() == True:
			actionRehacer.setEnabled(True)
		else:
			actionRehacer.setEnabled(False)
			
		actionPegar = QtWidgets.QAction(QtGui.QIcon('accionpegar.png'), '&Pegar\tCTRL+V')
		actionPegar.setShortcut('CTRL+V')
		actionPegar.triggered.connect(lambda: objeto.paste())
		if len(poderPegar):
			actionPegar.setEnabled(True)
		else:
			actionPegar.setEnabled(False)
			
		actionEliminar = QtWidgets.QAction(QtGui.QIcon('accionborrar.png'), '&Eliminar')
		actionEliminar.triggered.connect(lambda: objeto.backspace())
		if objeto.hasSelectedText() == True:
			actionEliminar.setEnabled(True)
		else:
			actionEliminar.setEnabled(False)
			
		actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A')
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
			self.labelError.hide()
			self.lineEditPassword.setEnabled(False)
			self.lineEditPassword.setStyleSheet('background-color: #D3D3D3;')
			verificacion(self, 'VL Cancelar')
		else:
			if len(self.lineEditUsuario.text()) < 6:
				self.NicknameVerificar = 0
				self.labelError.setText("El nickname debe ser mínimo de 6 caracteres.")
				self.labelError.show()
				self.lineEditPassword.setEnabled(False)
				self.lineEditPassword.setStyleSheet('background-color: #D3D3D3;')
				verificacion(self, 'VL Cancelar')
			else:
				if ' ' in self.lineEditUsuario.text() or '@' in self.lineEditUsuario.text():
					self.NicknameVerificar = 0
					self.lineEditPassword.setEnabled(False)
					self.lineEditPassword.setStyleSheet('background-color: #D3D3D3;')
					self.labelError.setText("El nickname no debe contener @ o espacios.")
					self.labelError.show()
					verificacion(self, 'VL Cancelar')
				else:
					self.NicknameVerificar = 1
					self.labelError.hide()
					self.lineEditPassword.setEnabled(True)
					self.lineEditPassword.setStyleSheet('background-color: white;')
					if self.NicknameVerificar == 1 and self.ClaveVerificar == 1:
						verificacion(self, 'VL Aceptar')
					else:
						verificacion(self, 'VL Cancelar')

	def lineEditVerificarClave(self):
		if len(self.lineEditPassword.text()) == 0:
			self.ClaveVerificar = 0
			self.labelError.hide()
			verificacion(self, 'VL Cancelar')
		else:
			if len(self.lineEditPassword.text()) < 6:
				self.ClaveVerificar = 0
				self.labelError.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.labelError.show()
				verificacion(self, 'VL Cancelar')
			else:
				self.ClaveVerificar = 1
				self.labelError.hide()
				if self.NicknameVerificar == 1 and self.ClaveVerificar == 1:
					verificacion(self, 'VL Aceptar')
				else:
					verificacion(self, 'VL Cancelar')
					
	def alerta(self, mensaje):
		self.ventanaAlerta = QtWidgets.QMessageBox()
		self.ventanaAlerta.setObjectName("Alerta_Ventana")
		self.ventanaAlerta.setWindowIcon(QtGui.QIcon('icono.png'))
		self.ventanaAlerta.setIcon(QtWidgets.QMessageBox.Information)
		self.ventanaAlerta.setEnabled(True)
		self.ventanaAlerta.setMouseTracking(True)
		self.ventanaAlerta.setFocusPolicy(QtCore.Qt.NoFocus)
		self.ventanaAlerta.setWindowTitle("Información")
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

	def boton_cancelar(self, ventana):
		ventana.hide()
		ventana.deleteLater()
	#-----------------------------------------------------------------------------------------------------------------------------------------
	#Ventana Olvido Contraseña------------------------------------------------------------------------------------------------
	def olvido_ventana(self):
		self.olvidoVentana = QDialog(None, Qt.WindowCloseButtonHint)
		self.olvidoVentana.setFixedSize(321, 270)
		self.olvidoVentana.setMouseTracking(True)
		self.olvidoVentana.setObjectName("Ventana_Olvido")
		self.olvidoVentana.setWindowIcon(QtGui.QIcon('icono.png'))
		self.olvidoVentana.setWindowTitle("Recuperar Contraseña")
		estiloventanaolvidoclave(self.olvidoVentana)
		
		self.olvidoVentana.labelUsuario = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelUsuario.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelUsuario.move(0, 30)
		self.olvidoVentana.labelUsuario.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelUsuario.setObjectName("Label_Usuario")
		self.olvidoVentana.font = QtGui.QFont()
		self.olvidoVentana.font.setFamily("Ubuntu")
		self.olvidoVentana.font.setPointSize(11)
		self.olvidoVentana.font.setBold(True)
		self.olvidoVentana.font.setWeight(75)
		self.olvidoVentana.labelUsuario.setFont(self.olvidoVentana.font)
		self.olvidoVentana.labelUsuario.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelUsuario.efectos.setBlurRadius(0)
		self.olvidoVentana.labelUsuario.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.olvidoVentana.labelUsuario.efectos.setOffset(1,1)
		self.olvidoVentana.labelUsuario.setGraphicsEffect(self.olvidoVentana.labelUsuario.efectos)
		self.olvidoVentana.labelUsuario.setText("Nickname")

		self.olvidoVentana.lineEditUsuario = QtWidgets.QLineEdit(self.olvidoVentana)
		self.olvidoVentana.lineEditUsuario.setFixedWidth(131)
		self.olvidoVentana.lineEditUsuario.move(95, 50)
		self.olvidoVentana.lineEditUsuario.setObjectName("lineEdit_usuario")
		self.olvidoVentana.lineEditUsuario.textChanged.connect(self.lineEditVerificarUsuarioVentanaOlvido)
		self.olvidoVentana.lineEditUsuario.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.olvidoVentana.lineEditUsuario.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.olvidoVentana.lineEditUsuario))
		
		self.olvidoVentana.labelPreguntaSecreta = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelPreguntaSecreta.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelPreguntaSecreta.move(0, 90)
		self.olvidoVentana.labelPreguntaSecreta.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelPreguntaSecreta.setObjectName("label_preguntasecreta")
		self.olvidoVentana.labelPreguntaSecreta.setFont(self.olvidoVentana.font)
		self.olvidoVentana.labelPreguntaSecreta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelPreguntaSecreta.efectos.setBlurRadius(0)
		self.olvidoVentana.labelPreguntaSecreta.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.olvidoVentana.labelPreguntaSecreta.efectos.setOffset(1,1)
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
		self.olvidoVentana.labelPreguntaSecreta2.efectos.setBlurRadius(0)
		self.olvidoVentana.labelPreguntaSecreta2.efectos.setColor(QtGui.QColor("#000000"))
		self.olvidoVentana.labelPreguntaSecreta2.efectos.setOffset(1,1)
		self.olvidoVentana.labelPreguntaSecreta2.setGraphicsEffect(self.olvidoVentana.labelPreguntaSecreta2.efectos)
		self.olvidoVentana.labelPreguntaSecreta2.setText("¿Cuál es tu banda favorita?")

		self.olvidoVentana.labelRespuestaSecreta = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelRespuestaSecreta.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelRespuestaSecreta.move(0, 140)
		self.olvidoVentana.labelRespuestaSecreta.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelRespuestaSecreta.setObjectName("label_respuestasecreta")
		self.olvidoVentana.labelRespuestaSecreta.setFont(self.olvidoVentana.font)
		self.olvidoVentana.labelRespuestaSecreta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelRespuestaSecreta.efectos.setBlurRadius(0)
		self.olvidoVentana.labelRespuestaSecreta.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.olvidoVentana.labelRespuestaSecreta.efectos.setOffset(1,1)
		self.olvidoVentana.labelRespuestaSecreta.setGraphicsEffect(self.olvidoVentana.labelRespuestaSecreta.efectos)
		self.olvidoVentana.labelRespuestaSecreta.setText("Respuesta Secreta")

		self.olvidoVentana.lineEditRespuesta = QtWidgets.QLineEdit(self.olvidoVentana)
		self.olvidoVentana.lineEditRespuesta.setFixedWidth(131)
		self.olvidoVentana.lineEditRespuesta.move(95, 160)
		self.olvidoVentana.lineEditRespuesta.setObjectName("lineEdit_respuesta")
		self.olvidoVentana.lineEditRespuesta.textChanged.connect(self.lineEditVerificarRespuestaVentanaOlvido)
		self.olvidoVentana.lineEditRespuesta.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.olvidoVentana.lineEditRespuesta.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.olvidoVentana.lineEditRespuesta))
		self.olvidoVentana.lineEditRespuesta.setEnabled(False)
		self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #D3D3D3;')
		
		self.olvidoVentana.labelError = QtWidgets.QLabel(self.olvidoVentana)
		self.olvidoVentana.labelError.setFixedWidth(self.olvidoVentana.frameGeometry().width())
		self.olvidoVentana.labelError.move(0, 200)
		self.olvidoVentana.labelError.setAlignment(Qt.AlignCenter)
		self.olvidoVentana.labelError.setObjectName("label_error")
		self.olvidoVentana.labelError.setWordWrap(True)
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.olvidoVentana.labelError.setFont(font)
		self.olvidoVentana.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.olvidoVentana.labelError.efectos.setBlurRadius(0)
		self.olvidoVentana.labelError.efectos.setColor(QtGui.QColor("#000000"))
		self.olvidoVentana.labelError.efectos.setOffset(1,1)
		self.olvidoVentana.labelError.setGraphicsEffect(self.olvidoVentana.labelError.efectos)

		self.olvidoVentana.botones = QtWidgets.QDialogButtonBox(self.olvidoVentana)
		self.olvidoVentana.botones.setFixedWidth(160)
		self.olvidoVentana.botones.move(80.5, 230)
		self.olvidoVentana.botones.setOrientation(QtCore.Qt.Horizontal)
		self.olvidoVentana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.olvidoVentana.botones.setCenterButtons(True)
		self.olvidoVentana.botones.setObjectName("Botones_Olvido")
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
		self.olvidoVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: self.boton_cancelar(self.olvidoVentana))
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
			self.olvidoVentana.labelError.hide()
			self.olvidoVentana.lineEditRespuesta.setEnabled(False)
			self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #D3D3D3;')
			verificacion(self, 'VL_VO Cancelar')
		else:
			if len(self.olvidoVentana.lineEditUsuario.text()) < 6:
				self.olvidoVentana.NicknameVerificar = 0
				self.olvidoVentana.labelError.setText("El nickname debe ser mínimo de 6 caracteres.")
				self.olvidoVentana.labelError.show()
				self.olvidoVentana.lineEditRespuesta.setEnabled(False)
				self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #D3D3D3;')
				verificacion(self, 'VL_VO Cancelar')
			else:
				if ' ' in self.olvidoVentana.lineEditUsuario.text() or '@' in self.olvidoVentana.lineEditUsuario.text():
					self.olvidoVentana.NicknameVerificar = 0
					self.olvidoVentana.lineEditRespuesta.setEnabled(False)
					self.olvidoVentana.lineEditRespuesta.setStyleSheet('background-color: #D3D3D3;')
					self.olvidoVentana.labelError.setText("El nickname no debe contener @ o espacios.")
					self.olvidoVentana.labelError.show()
					verificacion(self, 'VL_VO Cancelar')
				else:
					self.olvidoVentana.NicknameVerificar = 1
					self.olvidoVentana.labelError.hide()
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
			self.olvidoVentana.labelError.show()
			verificacion(self, 'VL_VO Cancelar')
		else:
			self.olvidoVentana.RespuestaVerificar = 1
			self.olvidoVentana.labelError.hide()
			if self.olvidoVentana.NicknameVerificar == 1 and self.olvidoVentana.RespuestaVerificar == 1:
				verificacion(self, 'VL_VO Aceptar')
			else:
				verificacion(self, 'VL_VO Cancelar')
	
	#-------------------------------------------------------------------------------------------------------------------------	
    #Ventana Nueva Contraseña
	def ventana_clave_nueva(self):
		self.claveNuevaVentana = QDialog(None, Qt.WindowCloseButtonHint)
		self.claveNuevaVentana.setFixedSize(321, 270)
		self.claveNuevaVentana.setObjectName("Ventana_Clave_Nueva")
		self.claveNuevaVentana.setWindowIcon(QtGui.QIcon('icono.png'))
		self.claveNuevaVentana.setMouseTracking(True)
		self.claveNuevaVentana.setWindowTitle("Nueva Contraseña")
		estiloVentanaClaveNueva(self.claveNuevaVentana)
		
		self.claveNuevaVentana.labelClave = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelClave.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelClave.move(0, 30)
		self.claveNuevaVentana.labelClave.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelClave.setObjectName("Label_Clave")
		self.claveNuevaVentana.font = QtGui.QFont()
		self.claveNuevaVentana.font.setFamily("Ubuntu")
		self.claveNuevaVentana.font.setPointSize(11)
		self.claveNuevaVentana.font.setBold(True)
		self.claveNuevaVentana.font.setWeight(75)
		self.claveNuevaVentana.labelClave.setFont(self.claveNuevaVentana.font)
		self.claveNuevaVentana.labelClave.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelClave.efectos.setBlurRadius(0)
		self.claveNuevaVentana.labelClave.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.claveNuevaVentana.labelClave.efectos.setOffset(1,1)
		self.claveNuevaVentana.labelClave.setGraphicsEffect(self.claveNuevaVentana.labelClave.efectos)
		self.claveNuevaVentana.labelClave.setText("Nueva Contraseña")
		
		self.claveNuevaVentana.lineEditClave = QtWidgets.QLineEdit(self.claveNuevaVentana)
		self.claveNuevaVentana.lineEditClave.setFixedWidth(131)
		self.claveNuevaVentana.lineEditClave.move(95, 60)
		self.claveNuevaVentana.lineEditClave.setObjectName("lineEdit_clave")
		self.claveNuevaVentana.lineEditClave.textChanged.connect(self.lineEditVerificarNuevaClave)
		self.claveNuevaVentana.lineEditClave.setEchoMode(QtWidgets.QLineEdit.Password)
		self.claveNuevaVentana.lineEditClave.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.claveNuevaVentana.lineEditClave.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.claveNuevaVentana.lineEditClave))
		self.claveNuevaVentana.lineEditClave.indicador = None
		self.claveNuevaVentana.lineEditClave.keyPressEvent = self.pressKeyQLineEditPasswordVentanaNuevaClave
		self.claveNuevaVentana.lineEditClave.keyReleaseEvent = self.releaseKeyQLineEditPasswordVentanaNuevaClave
		
		self.claveNuevaVentana.labelClave2 = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelClave2.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelClave2.move(0, 100)
		self.claveNuevaVentana.labelClave2.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelClave2.setObjectName("Label_Clave2")
		self.claveNuevaVentana.labelClave2.setFont(self.claveNuevaVentana.font)
		self.claveNuevaVentana.labelClave2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelClave2.efectos.setBlurRadius(0)
		self.claveNuevaVentana.labelClave2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.claveNuevaVentana.labelClave2.efectos.setOffset(1,1)
		self.claveNuevaVentana.labelClave2.setGraphicsEffect(self.claveNuevaVentana.labelClave2.efectos)
		self.claveNuevaVentana.labelClave2.setText("Confirme Nueva Contraseña")
		
		self.claveNuevaVentana.lineEditClave2 = QtWidgets.QLineEdit(self.claveNuevaVentana)
		self.claveNuevaVentana.lineEditClave2.setFixedWidth(131)
		self.claveNuevaVentana.lineEditClave2.move(95, 130)
		self.claveNuevaVentana.lineEditClave2.setObjectName("lineEdit_clave2")
		self.claveNuevaVentana.lineEditClave2.textChanged.connect(self.lineEditVerificarNuevaClave2)
		self.claveNuevaVentana.lineEditClave2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.claveNuevaVentana.lineEditClave2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.claveNuevaVentana.lineEditClave2.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.claveNuevaVentana.lineEditClave2))
		self.claveNuevaVentana.lineEditClave2.indicador = None
		self.claveNuevaVentana.lineEditClave2.keyPressEvent = self.pressKeyQLineEditPassword2VentanaNuevaClave
		self.claveNuevaVentana.lineEditClave2.keyReleaseEvent = self.releaseKeyQLineEditPassword2VentanaNuevaClave
		self.claveNuevaVentana.lineEditClave2.setEnabled(False)
		self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
		
		self.claveNuevaVentana.labelError = QtWidgets.QLabel(self.claveNuevaVentana)
		self.claveNuevaVentana.labelError.setFixedWidth(self.claveNuevaVentana.frameGeometry().width())
		self.claveNuevaVentana.labelError.move(0, 200)
		self.claveNuevaVentana.labelError.setAlignment(Qt.AlignCenter)
		self.claveNuevaVentana.labelError.setObjectName("label_error")
		self.claveNuevaVentana.labelError.setWordWrap(True)
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.claveNuevaVentana.labelError.setFont(font)
		self.claveNuevaVentana.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.claveNuevaVentana.labelError.efectos.setBlurRadius(0)
		self.claveNuevaVentana.labelError.efectos.setColor(QtGui.QColor("#000000"))
		self.claveNuevaVentana.labelError.efectos.setOffset(1,1)
		self.claveNuevaVentana.labelError.setGraphicsEffect(self.claveNuevaVentana.labelError.efectos)
		
		self.claveNuevaVentana.botones = QtWidgets.QDialogButtonBox(self.claveNuevaVentana)
		self.claveNuevaVentana.botones.setFixedWidth(160)
		self.claveNuevaVentana.botones.move(80.5, 230)
		self.claveNuevaVentana.botones.setOrientation(QtCore.Qt.Horizontal)
		self.claveNuevaVentana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.claveNuevaVentana.botones.setCenterButtons(True)
		self.claveNuevaVentana.botones.setObjectName("Botones_Nueva_Clave")
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
		self.claveNuevaVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: self.boton_cancelar(self.claveNuevaVentana))
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
			self.claveNuevaVentana.labelError.hide()
			self.claveNuevaVentana.lineEditClave2.setEnabled(False)
			self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
			verificacion(self, 'VL_VN Cancelar')
		else:
			self.claveNuevaVentana.lineEditClave2.clear()
			if len(self.claveNuevaVentana.lineEditClave.text()) < 6:
				self.claveNuevaVentana.claveVerificar = 0
				self.claveNuevaVentana.labelError.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.claveNuevaVentana.labelError.show()
				self.claveNuevaVentana.lineEditClave2.setEnabled(False)
				self.claveNuevaVentana.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
				verificacion(self, 'VL_VN Cancelar')
			else:
				self.claveNuevaVentana.claveVerificar = 1
				self.claveNuevaVentana.labelError.hide()
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
			self.claveNuevaVentana.labelError.show()
			verificacion(self, 'VL_VN Cancelar')
		else:
			if len(self.claveNuevaVentana.lineEditClave2.text()) < 6:
				self.claveNuevaVentana.claveVerificar2 = 0
				self.claveNuevaVentana.labelError.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.claveNuevaVentana.labelError.show()
				verificacion(self, 'VL_VN Cancelar')
			else:
				if self.claveNuevaVentana.lineEditClave.text() != self.claveNuevaVentana.lineEditClave2.text():
					self.claveNuevaVentana.claveVerificar2 = 0
					self.claveNuevaVentana.labelError.setText("Las contraseñas no coinciden.")
					self.claveNuevaVentana.labelError.show()
					verificacion(self, 'VL_VN Cancelar')
				else:	
					self.claveNuevaVentana.claveVerificar2 = 1
					self.claveNuevaVentana.labelError.hide()
					if self.claveNuevaVentana.claveVerificar == 1 and self.claveNuevaVentana.claveVerificar2 == 1:
						verificacion(self, 'VL_VN Aceptar')
					else:
						verificacion(self, 'VL_VN Cancelar')

	#--------------------------------------------------------------------------------------------------------------------------
	#Ventana Registro
	def registro_ventana(self):
		self.ventanaRegistro = QDialog(None, Qt.WindowCloseButtonHint)
		self.ventanaRegistro.setObjectName("VentanaRegistro")
		self.ventanaRegistro.setMouseTracking(True)
		self.ventanaRegistro.setWindowIcon(QtGui.QIcon('icono.png'))
		self.ventanaRegistro.setFixedSize(394, 600)
		self.ventanaRegistro.setWindowTitle("Registro")
		estiloVentanaRegistro(self.ventanaRegistro)
		
		self.ventanaRegistro.labelNickname = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelNickname.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelNickname.move(0, 30)
		self.ventanaRegistro.labelNickname.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelNickname.setObjectName("labelNickname")
		self.ventanaRegistro.font = QtGui.QFont()
		self.ventanaRegistro.font.setFamily("Ubuntu")
		self.ventanaRegistro.font.setPointSize(11)
		self.ventanaRegistro.font.setBold(True)
		self.ventanaRegistro.font.setWeight(75)
		self.ventanaRegistro.labelNickname.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelNickname.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelNickname.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelNickname.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelNickname.efectos.setOffset(1,1)
		self.ventanaRegistro.labelNickname.setGraphicsEffect(self.ventanaRegistro.labelNickname.efectos)
		self.ventanaRegistro.labelNickname.setText("Nickname")
		
		self.ventanaRegistro.lineEditNickname = QtWidgets.QLineEdit(self.ventanaRegistro)
		self.ventanaRegistro.lineEditNickname.setFixedWidth(150)
		self.ventanaRegistro.lineEditNickname.move(122, 55)
		self.ventanaRegistro.lineEditNickname.setObjectName("lineEditNickname")
		self.ventanaRegistro.lineEditNickname.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.lineEditNickname.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaRegistro.lineEditNickname))
		self.ventanaRegistro.lineEditNickname.textChanged.connect(self.verificarDatosRegistroNickname)
		
		self.ventanaRegistro.labelNombre = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelNombre.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelNombre.move(0, 90)
		self.ventanaRegistro.labelNombre.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelNombre.setObjectName("labelNombre")
		self.ventanaRegistro.labelNombre.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelNombre.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelNombre.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelNombre.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelNombre.efectos.setOffset(1,1)
		self.ventanaRegistro.labelNombre.setGraphicsEffect(self.ventanaRegistro.labelNombre.efectos)
		self.ventanaRegistro.labelNombre.setText("Nombre Completo")
		
		self.ventanaRegistro.lineEditNombre = QtWidgets.QLineEdit(self.ventanaRegistro)
		self.ventanaRegistro.lineEditNombre.setFixedWidth(150)
		self.ventanaRegistro.lineEditNombre.move(122, 115)
		self.ventanaRegistro.lineEditNombre.setObjectName("lineEditNombre")
		self.ventanaRegistro.lineEditNombre.textChanged.connect(self.verificarDatosRegistroNombre)
		self.ventanaRegistro.lineEditNombre.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.lineEditNombre.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaRegistro.lineEditNombre))
		
		self.ventanaRegistro.labelFechaNacimiento = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelFechaNacimiento.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelFechaNacimiento.move(0, 150)
		self.ventanaRegistro.labelFechaNacimiento.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelFechaNacimiento.setObjectName("labelFechaNacimiento")
		self.ventanaRegistro.labelFechaNacimiento.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelFechaNacimiento.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelFechaNacimiento.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelFechaNacimiento.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelFechaNacimiento.efectos.setOffset(1,1)
		self.ventanaRegistro.labelFechaNacimiento.setGraphicsEffect(self.ventanaRegistro.labelFechaNacimiento.efectos)
		self.ventanaRegistro.labelFechaNacimiento.setText("Fecha Nacimiento")
		
		self.ventanaRegistro.dateEditFechaNacimiento = QtWidgets.QDateEdit(self.ventanaRegistro)
		self.ventanaRegistro.dateEditFechaNacimiento.setDateTime(QtCore.QDateTime.currentDateTime())
		self.ventanaRegistro.dateEditFechaNacimiento.setMinimumDate(QtCore.QDate(1930, 1, 1))
		self.ventanaRegistro.dateEditFechaNacimiento.setMaximumDate(QtCore.QDate.currentDate())
		self.ventanaRegistro.dateEditFechaNacimiento.setFixedWidth(150)
		self.ventanaRegistro.dateEditFechaNacimiento.move(122, 175)
		self.ventanaRegistro.dateEditFechaNacimiento.setObjectName("dateEditFechaNacimiento")
		self.ventanaRegistro.dateEditFechaNacimiento.setCalendarPopup(True)
		self.ventanaRegistro.dateEditFechaNacimiento.keyPressEvent = self.pressKeyQDateEdit
		self.ventanaRegistro.dateEditFechaNacimiento.keyReleaseEvent = self.releaseKeyQDateEdit
		self.ventanaRegistro.dateEditFechaNacimiento.indicador = None
		self.ventanaRegistro.dateEditFechaNacimiento.wheelEvent = self.eventoscalendario
		self.ventanaRegistro.dateEditFechaNacimiento.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.dateEditFechaNacimiento.customContextMenuRequested.connect(lambda: self.menuContextualCalendario(self.ventanaRegistro.dateEditFechaNacimiento))
		#Hacer menu contextual
		
		self.ventanaRegistro.calendario = QtWidgets.QCalendarWidget()
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.ventanaRegistro.calendario.setFont(font)
		self.ventanaRegistro.calendario.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.ventanaRegistro.calendario.setMinimumDate(QtCore.QDate(1930, 1, 1))
		self.ventanaRegistro.calendario.setMaximumDate(QtCore.QDate.currentDate())
		self.ventanaRegistro.calendario.setFirstDayOfWeek(QtCore.Qt.Monday)
		self.ventanaRegistro.calendario.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
		self.ventanaRegistro.calendario.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
		self.ventanaRegistro.calendario.setDateEditEnabled(False)
		self.ventanaRegistro.calendario.setObjectName("calendario")
		format= QtGui.QTextCharFormat()
		format.setForeground(QtGui.QColor(0,0,255))
		format.setBackground(QtGui.QColor(255,255,255))
		format.setFontWeight(QtGui.QFont.Bold)
		self.ventanaRegistro.calendario.setHeaderTextFormat(format)
		self.ventanaRegistro.calendario.setStyleSheet("""
			QCalendarWidget QAbstractItemView{
				background-color: white; /* цвет фона текущего месяца */
				selection-background-color: pink; /* цвет фона выбранного дня */
				selection-color: white; /* цвет текста выбранного дня */
			}
		""")
		self.ventanaRegistro.dateEditFechaNacimiento.setCalendarWidget(self.ventanaRegistro.calendario)
		
		
		self.ventanaRegistro.labelSexo = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelSexo.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelSexo.move(0, 210)
		self.ventanaRegistro.labelSexo.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelSexo.setObjectName("labelSexo")
		self.ventanaRegistro.labelSexo.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelSexo.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelSexo.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelSexo.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelSexo.efectos.setOffset(1,1)
		self.ventanaRegistro.labelSexo.setGraphicsEffect(self.ventanaRegistro.labelSexo.efectos)
		self.ventanaRegistro.labelSexo.setText("Sexo")
		
		self.ventanaRegistro.radioButtonMasculino = QtWidgets.QRadioButton(self.ventanaRegistro)
		self.ventanaRegistro.radioButtonMasculino.setFixedWidth(32)
		self.ventanaRegistro.radioButtonMasculino.move(145, 235)
		self.ventanaRegistro.radioButtonMasculino.setChecked(True)
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.ventanaRegistro.radioButtonMasculino.setFont(font)
		self.ventanaRegistro.radioButtonMasculino.setObjectName("radioButtonMasculino")
		self.ventanaRegistro.radioButtonMasculino.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.radioButtonMasculino.efectos.setBlurRadius(0)
		self.ventanaRegistro.radioButtonMasculino.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.radioButtonMasculino.efectos.setOffset(1,1)
		self.ventanaRegistro.radioButtonMasculino.setGraphicsEffect(self.ventanaRegistro.radioButtonMasculino.efectos)
		self.ventanaRegistro.radioButtonMasculino.setText("M")
		
		self.ventanaRegistro.radioButtonFemenino = QtWidgets.QRadioButton(self.ventanaRegistro)
		self.ventanaRegistro.radioButtonFemenino.setFixedWidth(32)
		self.ventanaRegistro.radioButtonFemenino.move(229, 235)
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.ventanaRegistro.radioButtonFemenino.setFont(font)
		self.ventanaRegistro.radioButtonFemenino.setObjectName("radioButtonFemenino")
		self.ventanaRegistro.radioButtonFemenino.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.radioButtonFemenino.efectos.setBlurRadius(0)
		self.ventanaRegistro.radioButtonFemenino.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.radioButtonFemenino.efectos.setOffset(1,1)
		self.ventanaRegistro.radioButtonFemenino.setGraphicsEffect(self.ventanaRegistro.radioButtonFemenino.efectos)
		self.ventanaRegistro.radioButtonFemenino.setText("F")
		
		self.ventanaRegistro.labelPregunta = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelPregunta.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelPregunta.move(0, 270)
		self.ventanaRegistro.labelPregunta.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelPregunta.setObjectName("labelPregunta")
		self.ventanaRegistro.labelPregunta.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelPregunta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelPregunta.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelPregunta.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelPregunta.efectos.setOffset(1,1)
		self.ventanaRegistro.labelPregunta.setGraphicsEffect(self.ventanaRegistro.labelPregunta.efectos)
		self.ventanaRegistro.labelPregunta.setText("Pregunta Secreta:")
		
		self.ventanaRegistro.labelPregunta2 = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelPregunta2.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelPregunta2.move(0, 295)
		self.ventanaRegistro.labelPregunta2.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelPregunta2.setObjectName("labelPregunta2")
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(11)
		self.ventanaRegistro.labelPregunta2.setFont(font)
		self.ventanaRegistro.labelPregunta2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelPregunta2.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelPregunta2.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelPregunta2.efectos.setOffset(1,1)
		self.ventanaRegistro.labelPregunta2.setGraphicsEffect(self.ventanaRegistro.labelPregunta2.efectos)
		self.ventanaRegistro.labelPregunta2.setText("¿Cuál es tu banda favorita?")
		
		self.ventanaRegistro.labelRespuesta = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelRespuesta.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelRespuesta.move(0, 330)
		self.ventanaRegistro.labelRespuesta.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelRespuesta.setObjectName("labelRespuesta")
		self.ventanaRegistro.labelRespuesta.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelRespuesta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelRespuesta.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelRespuesta.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelRespuesta.efectos.setOffset(1,1)
		self.ventanaRegistro.labelRespuesta.setGraphicsEffect(self.ventanaRegistro.labelRespuesta.efectos)
		self.ventanaRegistro.labelRespuesta.setText("Respuesta Secreta")
		
		self.ventanaRegistro.lineEditRespuesta = QtWidgets.QLineEdit(self.ventanaRegistro)
		self.ventanaRegistro.lineEditRespuesta.setFixedWidth(150)
		self.ventanaRegistro.lineEditRespuesta.move(122, 355)
		self.ventanaRegistro.lineEditRespuesta.setObjectName("lineEditRespuesta")
		self.ventanaRegistro.lineEditRespuesta.textChanged.connect(self.verificarDatosRegistroRespuesta)
		self.ventanaRegistro.lineEditRespuesta.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.lineEditRespuesta.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaRegistro.lineEditRespuesta))
		
		self.ventanaRegistro.labelClave = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelClave.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelClave.move(0, 390)
		self.ventanaRegistro.labelClave.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelClave.setObjectName("labelClave")
		self.ventanaRegistro.labelClave.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelClave.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelClave.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelClave.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelClave.efectos.setOffset(1,1)
		self.ventanaRegistro.labelClave.setGraphicsEffect(self.ventanaRegistro.labelClave.efectos)
		self.ventanaRegistro.labelClave.setText("Contraseña")
		
		self.ventanaRegistro.lineEditClave = QtWidgets.QLineEdit(self.ventanaRegistro)
		self.ventanaRegistro.lineEditClave.setFixedWidth(150)
		self.ventanaRegistro.lineEditClave.move(122, 415)
		self.ventanaRegistro.lineEditClave.setObjectName("lineEditClave")
		self.ventanaRegistro.lineEditClave.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ventanaRegistro.lineEditClave.textChanged.connect(self.verificarDatosRegistroClave)
		self.ventanaRegistro.lineEditClave.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.lineEditClave.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.ventanaRegistro.lineEditClave))
		self.ventanaRegistro.lineEditClave.indicador = None
		self.ventanaRegistro.lineEditClave.keyPressEvent = self.pressKeyQLineEditPasswordVentanaRegistro
		self.ventanaRegistro.lineEditClave.keyReleaseEvent = self.releaseKeyQLineEditPasswordVentanaRegistro
		
		self.ventanaRegistro.labelClave2 = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelClave2.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelClave2.move(0, 450)
		self.ventanaRegistro.labelClave2.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelClave2.setObjectName("labelClave2")
		self.ventanaRegistro.labelClave2.setFont(self.ventanaRegistro.font)
		self.ventanaRegistro.labelClave2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelClave2.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelClave2.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelClave2.efectos.setOffset(1,1)
		self.ventanaRegistro.labelClave2.setGraphicsEffect(self.ventanaRegistro.labelClave2.efectos)
		self.ventanaRegistro.labelClave2.setText("Confirme Contraseña")
		
		self.ventanaRegistro.lineEditClave2 = QtWidgets.QLineEdit(self.ventanaRegistro)
		self.ventanaRegistro.lineEditClave2.setFixedWidth(150)
		self.ventanaRegistro.lineEditClave2.move(122, 475)
		self.ventanaRegistro.lineEditClave2.setObjectName("lineEditClave2")
		self.ventanaRegistro.lineEditClave2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ventanaRegistro.lineEditClave2.textChanged.connect(self.verificarDatosRegistroClave2)
		self.ventanaRegistro.lineEditClave2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaRegistro.lineEditClave2.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.ventanaRegistro.lineEditClave2))
		self.ventanaRegistro.lineEditClave2.indicador = None
		self.ventanaRegistro.lineEditClave2.keyPressEvent = self.pressKeyQLineEditPassword2VentanaRegistro
		self.ventanaRegistro.lineEditClave2.keyReleaseEvent = self.releaseKeyQLineEditPassword2VentanaRegistro
		self.ventanaRegistro.lineEditClave2.setEnabled(False)
		self.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
		
		self.ventanaRegistro.labelError = QtWidgets.QLabel(self.ventanaRegistro)
		self.ventanaRegistro.labelError.setFixedWidth(self.ventanaRegistro.frameGeometry().width())
		self.ventanaRegistro.labelError.move(0, 515)
		self.ventanaRegistro.labelError.setAlignment(Qt.AlignCenter)
		self.ventanaRegistro.labelError.setObjectName("labelError")
		self.ventanaRegistro.labelError.setWordWrap(True)
		font = QtGui.QFont()
		font.setFamily("Ubuntu")
		font.setPointSize(10)
		self.ventanaRegistro.labelError.setFont(font)
		self.ventanaRegistro.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaRegistro.labelError.efectos.setBlurRadius(0)
		self.ventanaRegistro.labelError.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaRegistro.labelError.efectos.setOffset(1,1)
		self.ventanaRegistro.labelError.setGraphicsEffect(self.ventanaRegistro.labelError.efectos)
		
		self.ventanaRegistro.botones = QtWidgets.QDialogButtonBox(self.ventanaRegistro)
		self.ventanaRegistro.botones.setFixedWidth(160)
		self.ventanaRegistro.botones.move(117, 545)
		self.ventanaRegistro.botones.setOrientation(QtCore.Qt.Horizontal)
		self.ventanaRegistro.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.ventanaRegistro.botones.setCenterButtons(True)
		self.ventanaRegistro.botones.setObjectName("Botones_Nueva_Clave")
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
		self.ventanaRegistro.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: self.boton_cancelar(self.ventanaRegistro))
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
		
		self.ventanaRegistro.exec_()
	
	def menuContextualCalendario(self, objeto):
		menuContextual = QtWidgets.QMenu()
			
		actionCopiar = QtWidgets.QAction(QtGui.QIcon('accioncopiar.png'), '&Copiar\tCTRL+C')
		actionCopiar.setShortcut('CTRL+C')
		actionCopiar.triggered.connect(lambda: objeto.lineEdit().copy())
		if objeto.lineEdit().hasSelectedText() == True:
			actionCopiar.setEnabled(True)
		else:
			actionCopiar.setEnabled(False)
			
		actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A')
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
			self.ventanaRegistro.lineEditClave.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.lineEditClave, event)
		elif event.key() == 88 or event.key() == 67:
			if self.ventanaRegistro.lineEditClave.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.lineEditClave, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.lineEditClave, event)
		
	def releaseKeyQLineEditPasswordVentanaRegistro(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.lineEditClave.indicador = 0
	
	def pressKeyQLineEditPassword2VentanaRegistro(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.lineEditClave2.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.lineEditClave2, event)
		elif event.key() == 88 or event.key() == 67:
			if self.ventanaRegistro.lineEditClave2.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.lineEditClave2, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.lineEditClave2, event)
		
	def releaseKeyQLineEditPassword2VentanaRegistro(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.lineEditClave.indicador = 0
	##################################################
	def eventoscalendario(self, event):
		event.ignore()
	
	def pressKeyQDateEdit(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.dateEditFechaNacimiento.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.dateEditFechaNacimiento.lineEdit(), event)
		elif event.key() == 65 or event.key() == 67:
			if self.ventanaRegistro.dateEditFechaNacimiento.indicador == 1:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaRegistro.dateEditFechaNacimiento.lineEdit(), event)
			else:
				event.ignore()
		else:
			event.ignore()
	
	def releaseKeyQDateEdit(self, event):
		if event.key() == 16777249:
			self.ventanaRegistro.dateEditFechaNacimiento.indicador = 0
	
	#Verificación sintáctica/semántica de datos
	def verificarDatosRegistroNickname(self):
		if len(self.ventanaRegistro.lineEditNickname.text()) == 0:
			self.ventanaRegistro.labelError.hide()
			self.ventanaRegistro.Nickname = 0
			verificacion(self, 'VL_VR Cancelar')
			verificacion(self, 'VL_VR Habilitar Nickname')
		else:
			if len(self.ventanaRegistro.lineEditNickname.text()) < 6:
				verificacion(self, 'VL_VR Deshabilitar Nickname')
				self.ventanaRegistro.Nickname = 0 
				self.ventanaRegistro.labelError.setText("El nickname debe ser mínimo de 6 caracteres.")
				self.ventanaRegistro.labelError.show()
				verificacion(self, 'VL_VR Cancelar')
			else:
				if ' ' in self.ventanaRegistro.lineEditNickname.text() or '@' in self.ventanaRegistro.lineEditNickname.text():
					verificacion(self, 'VL_VR Deshabilitar Nickname')
					self.ventanaRegistro.Nickname = 0 
					self.ventanaRegistro.labelError.setText("El nickname no debe contener @ o espacios.")
					self.ventanaRegistro.labelError.show()
					verificacion(self, 'VL_VR Cancelar')
				else:
					verificacion(self, 'VL_VR Habilitar Nickname')
					self.ventanaRegistro.Nickname = 1
					self.ventanaRegistro.labelError.hide()
					if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
						verificacion(self, 'VL_VR Aceptar')
					else:
						verificacion(self, 'VL_VR Cancelar')
					
	def verificarDatosRegistroNombre(self):
		if len(self.ventanaRegistro.lineEditNombre.text()) == 0:
			self.ventanaRegistro.labelError.hide()
			self.ventanaRegistro.Nombre = 0
			verificacion(self, 'VL_VR Cancelar')
			verificacion(self, 'VL_VR Habilitar Nombre')
		else:
			if len(self.ventanaRegistro.lineEditNombre.text()) < 5:
				verificacion(self, 'VL_VR Deshabilitar Nombre')
				self.ventanaRegistro.Nombre = 0
				self.ventanaRegistro.labelError.setText("Escribe tu nombre completo.")
				self.ventanaRegistro.labelError.show()
				verificacion(self, 'VL_VR Cancelar')
			else:
				verificacion(self, 'VL_VR Habilitar Nombre')
				self.ventanaRegistro.Nombre = 1
				self.ventanaRegistro.labelError.hide()
				if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
					verificacion(self, 'VL_VR Aceptar')
				else:
					verificacion(self, 'VL_VR Cancelar')
	
	def verificarDatosRegistroRespuesta(self):
		if len(self.ventanaRegistro.lineEditRespuesta.text()) == 0:
			self.ventanaRegistro.labelError.setText("Escribe una respuesta secreta.")
			self.ventanaRegistro.labelError.show()
			self.ventanaRegistro.Respuesta = 0
			verificacion(self, 'VL_VR Cancelar')
			verificacion(self, 'VL_VR Deshabilitar Respuesta')
		else:
			verificacion(self, 'VL_VR Habilitar Respuesta')
			self.ventanaRegistro.Respuesta = 1
			self.ventanaRegistro.labelError.hide()
			if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
				verificacion(self, 'VL_VR Aceptar')
			else:
				verificacion(self, 'VL_VR Cancelar')
	
	def verificarDatosRegistroClave(self):
		if len(self.ventanaRegistro.lineEditClave.text()) == 0:
			self.ventanaRegistro.labelError.hide()
			self.ventanaRegistro.Clave = 0
			verificacion(self, 'VL_VR Cancelar')
			verificacion(self, 'VL_VR Habilitar Clave')
			self.ventanaRegistro.lineEditClave2.setEnabled(False)
			self.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
			
		else:
			self.ventanaRegistro.lineEditClave2.clear()
			if len(self.ventanaRegistro.lineEditClave.text()) < 6:
				verificacion(self, 'VL_VR Deshabilitar Clave')
				self.ventanaRegistro.lineEditClave2.setEnabled(False)
				self.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: #D3D3D3;')
				self.ventanaRegistro.Clave = 0
				self.ventanaRegistro.labelError.setText("La contraseña debe ser de mínimo 6 caracteres.")
				self.ventanaRegistro.labelError.show()
				verificacion(self, 'VL_VR Cancelar')
			else:
				self.ventanaRegistro.Clave = 1
				self.ventanaRegistro.lineEditClave2.setEnabled(True)
				self.ventanaRegistro.lineEditClave2.setStyleSheet('background-color: white;')
				self.ventanaRegistro.labelError.hide()
				verificacion(self, 'VL_VR Cancelar')
				verificacion(self, 'VL_VR Deshabilitar Clave')
						
	def verificarDatosRegistroClave2(self):
		if len(self.ventanaRegistro.lineEditClave2.text()) == 0:
			self.ventanaRegistro.Clave2 = 0
			verificacion(self, 'VL_VR Cancelar')
			verificacion(self, 'VL_VR Deshabilitar Clave')
			self.ventanaRegistro.labelError.setText("Confirma la contraseña.")
			self.ventanaRegistro.labelError.show()		
		else:
			if len(self.ventanaRegistro.lineEditClave2.text()) < 6:
				verificacion(self, 'VL_VR Deshabilitar Clave')
				self.ventanaRegistro.Clave2 = 0
				self.ventanaRegistro.labelError.setText("La contraseña debe ser de mínimo 6 caracteres.")
				self.ventanaRegistro.labelError.show()
				verificacion(self, 'VL_VR Cancelar')
			else:
				if self.ventanaRegistro.lineEditClave.text() != self.ventanaRegistro.lineEditClave2.text():
					self.ventanaRegistro.Clave2 = 0
					verificacion(self, 'VL_VR Deshabilitar Clave')
					self.ventanaRegistro.labelError.setText("Las contraseñas no coinciden.")
					self.ventanaRegistro.labelError.show()
					verificacion(self, 'VL_VR Cancelar')
				else:	
					self.ventanaRegistro.labelError.hide()
					self.ventanaRegistro.Clave2 = 1
					verificacion(self, 'VL_VR Habilitar Clave')
					if self.ventanaRegistro.Nickname == 1 and self.ventanaRegistro.Nombre == 1 and self.ventanaRegistro.Respuesta == 1 and self.ventanaRegistro.Clave == 1 and self.ventanaRegistro.Clave2 == 1:
						verificacion(self, 'VL_VR Aceptar')
					else:
						verificacion(self, 'VL_VR Cancelar')

class NewDialog(QtWidgets.QMainWindow):
	
	signal = QtCore.pyqtSignal()

	def __init__(self, parent=None):
		super(NewDialog, self).__init__(parent)
		self.setParent(None)
		self.setFixedSize(200,200)
		self.setObjectName("Principal")
		self.setFixedSize(521, 469)
		self.setWindowTitle("Pollos ChatRoom")
		
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(400, 360, 61, 21))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText("Enviar")
		self.pushButton.clicked.connect(lambda: ensaya2.si(self))
		self.signal.connect(self.reyda)
	
	def reyda(self):
		print("reyda")
	
def main():
	app = QtWidgets.QApplication(sys.argv)
	QtGui.QFontDatabase.addApplicationFont('Ubuntu.ttf')
	VentanaPrincipal = Ventana_Principal()
	VentanaPrincipal.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	import atexit
	atexit.register(SocketCliente.exit_handler)
	app = QtWidgets.QApplication(sys.argv)
	QtGui.QFontDatabase.addApplicationFont('Ubuntu.ttf')
	VentanaPrincipal = Ventana_Principal()
	VentanaPrincipal.show()
	sys.exit(app.exec_())
	

