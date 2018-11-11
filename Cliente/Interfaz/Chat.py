# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cuerpa.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import re
sys.path.append('..')
#import SocketCliente

def estiloventanaprincipal(ventanaprincipal):
	ventanaprincipal.setStyleSheet("""
		#Ventana_Principal{
			border-image: url(Imagenes/pollos_principal.jpg);
		}

		#label_usuario{
			font-weight: bold;
 			font: 20pt "Segoe UI Light";
 			color: #00A5A5;
		}

		#OpcionesCuenta{
    		border-radius: 6px;
			border-color: navy;
    		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #B0C4DE);
		}
		#OpcionesCuenta::menu-indicator {
			width: 0px;
		}
		#OpcionesCuenta::hover{
			background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
		}
		#OpcionesCuenta::pressed{
			 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
		}
	""")

def estilotabwidget(tabwidget):
	tabwidget.setStyleSheet("""
		QTabWidget::pane { /* The tab widget frame */
			border-radius: 2px;
		}
		/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */
		QTabBar::tab {
			font: 11pt "Segoe UI Light";
			font-weight: bold;
			color: gray;
			background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #B0C4DE);
			border: 2px solid whitesmoke;
			border-bottom-color: #C2C7CB; /* same as the pane color */
			border-top-left-radius: 4px;
			border-top-right-radius: 4px;
			min-width: 50ex;
			max-width: 100ex;
			padding: 2px;
		}
		QTabBar::tab:selected, QTabBar::tab:hover {
			background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);

		}
		QTabBar::tab::selected {
			border-color: rgba(9, 73, 119, 70);
		}

		QTabBar::tab:!selected {
			margin-top: 2px; /* make non-selected tabs look smaller */
		}
		QTabBar::tab:selected{
			font: bold; color: #311089;
		}

		QTabWidget::tab-bar {
			alignment: center;
		}
		QTabWidget::pane {
			position: absolute; top: -0.5em;
		}
	""")

def estilolista(ventana):
	ventana.setStyleSheet("""
	QListWidget {
    show-decoration-selected: 1; /* make the selection span the entire width of the view */
	background-color: rgba(0, 0, 0, 200);
	border-radius:10px;
	}

	QListWidget::item:alternate {
		background: #EEEEEE;
		border-radius: 10px;
	}

	QListWidget::item:selected {
		border: 1px solid #6a6ea9;
		border-radius: 10px;
	}

	QListWidget::item:selected:!active {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
									stop: 0 #ABAFE5, stop: 1 #8588B2);
		border-radius: 10px;
	}

	QListWidget::item:selected:active {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
									stop: 0 #6a6ea9, stop: 1 #888dd9);
		border-radius: 10px;
	}

	QListWidget::item:hover {
		background: rgba(76,240,50,90);
		border-radius: 10px;
	}

	QScrollBar:vertical {
		background: white;
		border-radius: 10px;;
		width:10px;
		margin: 0px 0px 0px 0px;
	}
	QScrollBar::handle:vertical {
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
		stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));
		min-height: 0px;
	}
	QScrollBar::add-line:vertical {
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
		stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
		height: 0px;
		subcontrol-position: bottom;
		subcontrol-origin: margin;
	}
	QScrollBar::sub-line:vertical {
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
		stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
		height: 0 px;
		subcontrol-position: top;
		subcontrol-origin: margin;
	}

	""")

def estiloventanainformacionusuario(ventana):
	ventana.setStyleSheet("""
		#informacionusuarioventana{
			border-image: url(Imagenes/polloinformacion.jpg);
		}
		#informacionusuarioventanawidget{
			background-color: rgba(0, 0, 0, 200);
			border-radius: 10px;
			padding: 10px;
		}
		#labelNickname, #labelNombre, #labelSexo, #labelFechaNacimiento, #labelEdad{
			color: 	white;
			font: 14pt "Segoe UI Light";

		}
		#labelNickname2, #labelNombre2, #labelSexo2, #labelFechaNacimiento2, #labelEdad2{
			color: white;
			font: 13pt "Segoe UI Light";
		}
	""")

def estiloventanaeditardatos(ventana):
	ventana.setStyleSheet("""
		#editardatosventana{
			border-image: url(Imagenes/polloscambio.jpg);
		}
		#ventanaeditardatoswidget{
			background-color: rgba(0, 0, 0, 200);
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
		#labelNombre, #labelSexo, #labelFechaNacimiento, #labelClave, #labelPregunta{
			font: 14pt "Segoe UI Light";
			color: white;
		}
		#labelNombre2{
			font: 11pt  "Segoe UI Light";
			color: white;
		}
	 	#labelSexo2, #labelFechaNacimiento2, #labelPregunta2{
			font: 13pt  "Segoe UI Light";
			color: white;
		}
		#lineEditNombre, #dateEditFechaNacimiento, #lineEditClave, #lineEditClaveNueva, #lineEditClaveNueva2, #lineEditRespuesta{
			border-radius: 10px;
			border: 2px solid #DB7093;
			padding: 4px;
			font-family: Ubuntu;
		}
		#labelNombreError, #labelClaveError, #labelClaveError2, #labelRespuestaError{
			color: magenta;
		}
		#botonAceptarNombre, #botonCancelarNombre, #botonAceptarSexo, #botonCancelarSexo, #botonAceptarCalendario, #botonCancelarCalendario, #botonCancelarClaveNueva, #botonAceptarClaveNueva, #botonAceptarRespuesta, #botonCancelarRespuesta{
			background-color: rgba(0, 0, 0, 200);
			border-radius: 4px;
			font-family: Ubuntu;
			font-size: 12px;
			border: 2px solid gray;
			color: gray;
		}
		#radioButtonMasculino{
			color: white;
			font: 13pt  "Segoe UI Light";
		}
		#radioButtonMasculino:indicator:unchecked{
			background-color: white;
			border-radius: 6px;
			border: 2px solid white;
		}
		#radioButtonMasculino:indicator:checked{
			background-color: green;
			border-radius: 6px;
			border: 3px solid white;
		}
		#radioButtonFemenino{
			color: white;
			font: 13pt  "Segoe UI Light";
		}
		#radioButtonFemenino:indicator:unchecked{
			background-color: white;
			border-radius: 6px;
			border: 2px solid white;
		}
		#radioButtonFemenino:indicator:checked{
			background-color: green;
			border-radius: 6px;
			border: 3px solid white;
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
			#botonVolverEditarDatos{
			background-color: rgba(0, 0, 0, 200);
			border-radius: 4px;
			font-family: Ubuntu;
			font-size: 15px;
			border: 2px solid green;
			color: white;
		}
		#botonVolverEditarDatos:hover{
			background-color: rgba(0, 0, 0, 200);
			border: 2px solid GreenYellow;
			color: white;
		}
		#botonVolverEditarDatos:pressed{
			background-color: rgba(0, 0, 0, 200);
			border: 2px solid rgb(102,255,0);
			color: white;
			}
	""")

def estiloventanamenuopciones2(ventana,indicador):
	if indicador == 0:
		ventana.setStyleSheet("""
			#crearsalaventana{
				border-image: url(Imagenes/pollosplaya.jpg);
			}
			#ventanacrearsalawidget{
				background-color: rgba(0, 0, 0, 200);
				border-radius: 10px;
				padding: 10px;
			}
			#label{
				font: 14pt "Segoe UI Light";
				color: white;
			}
			#lineEdit{
				border-radius: 10px;
				border: 2px solid #DB7093;
				padding: 4px;
				font-family: Ubuntu;
			}
			#label2{
				font: 11pt "Segoe UI Light";
	 			color: white;
			}
			#labelError{
				color: magenta;
			}
			#botonAceptar{
				background-color: rgba(0, 0, 0, 200);
				border-radius: 4px;
				font-family: Ubuntu;
				font-size: 12px;
				border: 2px solid gray;
				color: gray;
			}
			#botonCancelar{
				background-color: rgba(0, 0, 0, 200);
				border-radius: 4px;
				font-family: Ubuntu;
				font-size: 12px;
				border: 2px solid red;
				color: white;
			}
			#botonCancelar:hover{
				background-color: rgba(0, 0, 0, 200);
				border: 2px solid rgb(255, 102, 51);
				color: white;
			}
			#botonCancelar:pressed{
				background-color: rgba(0, 0, 0, 200);
				border: 2px solid rgb(255, 173, 51);
				color: white;
			}
		""")

def verificacion1(ventana, mensaje):
	if mensaje.split(' ')[0] == 'EditarNombre':
		if mensaje.split(' ')[1] == 'Aceptar1':
			ventana.botonAceptarNombre.setStyleSheet("""
				#botonAceptarNombre{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid green;
					color: white;
				}
				#botonAceptarNombre:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid GreenYellow;
					color: white;
				}
				#botonAceptarNombre:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Aceptar0':
			ventana.botonAceptarNombre.setStyleSheet("""
				#botonAceptarNombre{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar1':
			ventana.botonCancelarNombre.setStyleSheet("""
				#botonCancelarNombre{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid red;
					color: white;
				}
				#botonCancelarNombre:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 102, 51);
					color: white;
				}
				#botonCancelarNombre:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 173, 51);
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar0':
			ventana.botonCancelarNombre.setStyleSheet("""
				#botonCancelarNombre{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
		elif mensaje.split(' ')[1] == 'Nofocus':
			ventana.lineEditNombre.clear()
			QtWidgets.QApplication.focusWidget().clearFocus()
	if mensaje.split(' ')[0] == 'EditarSexo':
		if mensaje.split(' ')[1] == 'Aceptar':
			ventana.botonAceptarSexo.setEnabled(True)
			ventana.botonCancelarSexo.setEnabled(True)
			ventana.botonAceptarSexo.setStyleSheet("""
				#botonAceptarSexo{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid green;
					color: white;
				}
				#botonAceptarSexo:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid GreenYellow;
					color: white;
				}
				#botonAceptarSexo:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")
			ventana.botonCancelarSexo.setStyleSheet("""
				#botonCancelarSexo{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid red;
					color: white;
				}
				#botonCancelarSexo:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 102, 51);
					color: white;
				}
				#botonCancelarSexo:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 173, 51);
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar':
			ventana.botonAceptarSexo.setEnabled(False)
			ventana.botonCancelarSexo.setEnabled(False)
			if ventana.radioButtonFemenino.isChecked() == True:
				ventana.radioButtonFemenino.setAutoExclusive(False)
				ventana.radioButtonFemenino.setChecked(False)
				ventana.radioButtonFemenino.setAutoExclusive(True)
			elif ventana.radioButtonMasculino.isChecked() == True:
				ventana.radioButtonMasculino.setAutoExclusive(False)
				ventana.radioButtonMasculino.setChecked(False)
				ventana.radioButtonMasculino.setAutoExclusive(True)
			QtWidgets.QApplication.focusWidget().clearFocus()
			ventana.botonAceptarSexo.setStyleSheet("""
				#botonAceptarSexo{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.botonCancelarSexo.setStyleSheet("""
				#botonCancelarSexo{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
	if mensaje.split(' ')[0] == 'EditarFecha':
		if mensaje.split(' ')[1] == 'Aceptar':
			ventana.botonAceptarCalendario.setEnabled(True)
			ventana.botonCancelarCalendario.setEnabled(True)
			ventana.botonAceptarCalendario.setStyleSheet("""
				#botonAceptarCalendario{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid green;
					color: white;
				}
				#botonAceptarCalendario:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid GreenYellow;
					color: white;
				}
				#botonAceptarCalendario:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")
			ventana.botonCancelarCalendario.setStyleSheet("""
				#botonCancelarCalendario{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid red;
					color: white;
				}
				#botonCancelarCalendario:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 102, 51);
					color: white;
				}
				#botonCancelarCalendario:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 173, 51);
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar':
			ventana.botonAceptarCalendario.setEnabled(False)
			ventana.botonCancelarCalendario.setEnabled(False)
			ventana.dateEditFechaNacimiento.setDate(QtCore.QDate.fromString(usuario["fechaNacimiento"],'dd/MM/yyyy'))
			QtWidgets.QApplication.focusWidget().clearFocus()
			ventana.botonAceptarCalendario.setStyleSheet("""
				#botonAceptarCalendario{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.botonCancelarCalendario.setStyleSheet("""
				#botonCancelarCalendario{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
	if mensaje.split(' ')[0] == 'EditarClave':
		if mensaje.split(' ')[1] == 'Cancelar':
			ventana.botonAceptarClaveNueva.setStyleSheet("""
				#botonAceptarClaveNueva{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.botonCancelarClaveNueva.setStyleSheet("""
				#botonCancelarClaveNueva{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar1':
			ventana.botonCancelarClaveNueva.setStyleSheet("""
				#botonCancelarClaveNueva{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid red;
					color: white;
				}
				#botonCancelarClaveNueva:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 102, 51);
					color: white;
				}
				#botonCancelarClaveNueva:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 173, 51);
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Aceptar0':
			ventana.botonAceptarClaveNueva.setStyleSheet("""
				#botonAceptarClaveNueva{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
		elif mensaje.split(' ')[1] == 'Aceptar1':
			ventana.botonAceptarClaveNueva.setStyleSheet("""
				#botonAceptarClaveNueva{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid green;
					color: white;
				}
				#botonAceptarClaveNueva:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid GreenYellow;
					color: white;
				}
				#botonAceptarClaveNueva:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Nofocus':
			ventana.botonCancelarClaveNueva.setStyleSheet("""
				#botonCancelarClaveNueva{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.botonAceptarClaveNueva.setStyleSheet("""
				#botonAceptarClaveNueva{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.lineEditClave.clear()
			ventana.lineEditClaveNueva.clear()
			ventana.lineEditClaveNueva2.blockSignals(True)
			ventana.lineEditClaveNueva2.clear()
			ventana.lineEditClaveNueva2.blockSignals(False)
			ventana.botonAceptarClaveNueva.setEnabled(False)
			ventana.botonCancelarClaveNueva.setEnabled(False)
			QtWidgets.QApplication.focusWidget().clearFocus()
	if mensaje.split(' ')[0] == 'EditarRespuesta':
		if mensaje.split(' ')[1] == 'Aceptar':
			ventana.botonAceptarRespuesta.setStyleSheet("""
				#botonAceptarRespuesta{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid green;
					color: white;
				}
				#botonAceptarRespuesta:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid GreenYellow;
					color: white;
				}
				#botonAceptarRespuesta:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")
			ventana.botonCancelarRespuesta.setStyleSheet("""
				#botonCancelarRespuesta{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid red;
					color: white;
				}
				#botonCancelarRespuesta:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 102, 51);
					color: white;
				}
				#botonCancelarRespuesta:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 173, 51);
					color: white;
				}
			""")
		elif mensaje.split(' ')[1] == 'Cancelar':
			ventana.botonAceptarRespuesta.setStyleSheet("""
				#botonAceptarRespuesta{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.botonCancelarRespuesta.setStyleSheet("""
				#botonCancelarRespuesta{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
		elif mensaje.split(' ')[1] == 'Nofocus':
			ventana.botonAceptarRespuesta.setStyleSheet("""
				#botonAceptarRespuesta{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.botonCancelarRespuesta.setStyleSheet("""
				#botonCancelarRespuesta{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
			ventana.botonAceptarRespuesta.setEnabled(False)
			ventana.botonCancelarRespuesta.setEnabled(False)
			ventana.lineEditRespuesta.clear()
			QtWidgets.QApplication.focusWidget().clearFocus()

class QCustomWidgetList (QtWidgets.QWidget):
	def __init__ (self, parent = None):
		super(QCustomWidgetList, self).__init__(parent)
		self.textQVBoxLayout = QtWidgets.QVBoxLayout()
		self.textUpQLabel    = QtWidgets.QLabel()
		self.textDownQLabel  = QtWidgets.QLabel()
		self.textQVBoxLayout.addWidget(self.textUpQLabel)
		self.textQVBoxLayout.addWidget(self.textDownQLabel)
		self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
		self.iconQLabel      = QtWidgets.QLabel()
		self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
		self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
		self.setLayout(self.allQHBoxLayout)
		# setStyleSheet
		self.textUpQLabel.setStyleSheet('''
		color: rgb(255, 0, 0);
		''')
		self.textDownQLabel.setStyleSheet('''
		color: rgb(255, 255, 255);
		''')

	def setTextUp (self, text):
		self.textUpQLabel.setText(text)

	def setTextDown (self, text):
		self.textDownQLabel.setText(text)

	def setIcon (self, imagePath):
		icon = QtGui.QPixmap()
		icon.load(imagePath)
		self.iconQLabel.setPixmap(icon)

class Ventana_Principal(QtWidgets.QMainWindow):
	entro = QtCore.pyqtSignal(str)
	salio = QtCore.pyqtSignal(str)

	def __init__(self):
		super(Ventana_Principal, self).__init__()
		self.setParent(None)
		self.setObjectName("Ventana_Principal")
		self.setFixedSize(800, 600)
		self.setWindowTitle("Pollos' ChatRoom")
		self.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		estiloventanaprincipal(self)
		self.closeEvent = self.eventoCerrado
		#------Opciones/Botón------------------------------------------------------
		menuOpciones = QtWidgets.QMenu()
		menuOpciones.setObjectName("menuOpciones")
		menuOpciones.setStyleSheet("""
			#menuOpciones{
				font-family: Ubuntu;
			}
		""")
		infoAccion = QtWidgets.QAction(QtGui.QIcon('Imagenes/accioninformacion.png'), '&Información de cuenta\tCTRL + I', self)
		infoAccion.setShortcut('CTRL+I')
		infoAccion.triggered.connect(lambda: self.informacionusuarioventana(self.usuario))
		editarAccion = QtWidgets.QAction(QtGui.QIcon('Imagenes/editar.png'), '&Editar Cuenta', self)
		editarAccion.triggered.connect(lambda: self.ventanaeditardatos(self.usuario))
		eliminarAccion = QtWidgets.QAction(QtGui.QIcon('Imagenes/eliminar.png'), '&Eliminar Cuenta', self)
		eliminarAccion.triggered.connect(lambda: self.alerta('Segure que deseas eliminar tu cuenta?', 'question', 'eliminarCuenta'))
		cerrarSesionAccion = QtWidgets.QAction(QtGui.QIcon('Imagenes/cerrar.png'), '&Cerrar Sesión\tCTRL + Q', self)
		cerrarSesionAccion.setShortcut('CTRL+Q')
		cerrarSesionAccion.triggered.connect(self.nada)
		salirAccion = QtWidgets.QAction(QtGui.QIcon('Imagenes/salir.png'), '&Salir\tALT + F4', self)
		salirAccion.setShortcut('ALT+F4')
		salirAccion.triggered.connect(lambda: self.alerta('Segure que deseas salir?','warning','salirPrograma'))

		menuOpciones.addAction(infoAccion)
		menuOpciones.addAction(editarAccion)
		menuOpciones.addAction(eliminarAccion)
		menuOpciones.addAction(cerrarSesionAccion)
		menuOpciones.addAction(salirAccion)

		self.botonOpcionesCuenta = QtWidgets.QPushButton(self)
		self.botonOpcionesCuenta.setGeometry(QtCore.QRect(self.frameGeometry().width()-60, 20, 33, 33))
		self.botonOpcionesCuenta.setObjectName("OpcionesCuenta")
		self.botonOpcionesCuenta.setIcon(QtGui.QIcon('Imagenes/opciones.png'))
		self.botonOpcionesCuenta.setIconSize(QtCore.QSize(29, 29))
		self.botonOpcionesCuenta.setMenu(menuOpciones)
		#-------------------------------------------------------------------------------------------------------------
	def eventoCerrado(self, event):
		self.alerta('Segure que deseas salir?','warning','salirPrograma')
		#event.ignore()

	def alerta(self, mensaje, tipo, accion):
		self.ventanaAlerta = QtWidgets.QMessageBox(self)
		self.ventanaAlerta.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		if tipo == 'question':
			self.ventanaAlerta.setIcon(QtWidgets.QMessageBox.Question)
		elif tipo == 'warning':
			self.ventanaAlerta.setIcon(QtWidgets.QMessageBox.Warning)
		elif tipo == 'critical':
			self.ventanaAlerta.setIcon(QtWidgets.QMessageBox.Critical)
		elif tipo == 'information':
			self.ventanaAlerta.setIcon(QtWidgets.QMessageBox.Critical)
		self.ventanaAlerta.setWindowTitle("Pollos' ChatRoom Mensaje")
		self.ventanaAlerta.setEnabled(True)
		self.ventanaAlerta.setMouseTracking(True)
		self.ventanaAlerta.setFocusPolicy(QtCore.Qt.NoFocus)
		self.ventanaAlerta.setText(mensaje)
		self.ventanaAlerta.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
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
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Cancel).setObjectName("Boton_Cancelar")
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Cancel).setFixedSize(70,25)
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Cancel).setText("Cancelar")
		self.ventanaAlerta.button(QtWidgets.QMessageBox.Cancel).setStyleSheet("""
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
		if accion == 'salirPrograma':
			self.ventanaAlerta.button(QtWidgets.QMessageBox.Ok).clicked.connect(lambda: self.nada)
		elif accion == 'eliminarSala':
			self.ventanaAlerta.button(QtWidgets.QMessageBox.Ok).clicked.connect(lambda: self.nada)
		elif accion == 'eliminarCuenta':
			self.ventanaAlerta.button(QtWidgets.QMessageBox.Ok).clicked.connect(lambda: self.nada)

		self.ventanaAlerta.exec_()

	def constructor(self, usuario, sala, usuariosSala, usuariosMensajesPrivados, mensajesPrivados):
		self.usuario= usuario #Usuario Actual Información : Diccionario
		self.sala= sala #Sala  Default
		self.usuariosSala = usuariosSala #Usuarios de la Sala Default
		self.usuariosMensajesPrivados = usuariosMensajesPrivados #Usuarios con los que el usuario ha tenido mensajes privados.
		self.mensajesPrivados = mensajesPrivados #Mensajes Privados del usuario.

		labelUsuario = QtWidgets.QLabel(self)
		labelUsuario.setFixedSize(self.frameGeometry().width()/2,50)
		labelUsuario.move(200, 10)
		labelUsuario.setAlignment(QtCore.Qt.AlignCenter)
		labelUsuario.setObjectName("label_usuario")
		labelUsuario.efectos = QtWidgets.QGraphicsDropShadowEffect()
		labelUsuario.efectos.setBlurRadius(10)
		labelUsuario.efectos.setColor(QtGui.QColor("#000000"))
		labelUsuario.efectos.setOffset(1,1)
		labelUsuario.setGraphicsEffect(labelUsuario.efectos)
		labelUsuario.setText("Bienvenide "+usuario['nickname'])
		#Pestañas------------------------------------------------------------------------------------------------------
		self.tabWidget = QtWidgets.QTabWidget(self)
		self.tabWidget.setFixedSize((self.frameGeometry().width()*95)/100, ((self.frameGeometry().height()*90)/100)-20)
		self.tabWidget.move((self.frameGeometry().width()-self.tabWidget.frameGeometry().width())/2,((self.frameGeometry().height()-self.tabWidget.frameGeometry().height())/2)+28)
		self.tabWidget.setObjectName("tabWidget")
		self.tabWidget.setAttribute(Qt.Qt.WA_TranslucentBackground, True )
		self.tabWidget.setAttribute(Qt.Qt.WA_NoSystemBackground, False)
		self.construirTabSala(sala)
		self.construirTabMensaje()
		estilotabwidget(self.tabWidget)
	#-----------------------------------------------------------------------------------------------------------------
	#Tab Sala
	def construirTabSala(self, sala):
		self.tabWidget.removeTab(0)
		self.tabSala = QtWidgets.QWidget()
		self.tabSala.setObjectName("tabSala")
		self.tabSala.setStyleSheet("""
			#tabSala {
				margin-top: 6px;
				background-color:  rgba(20, 164, 137, 90);
				border-radius: 20px;
			}
		""")
		self.tabSala.textEdit = QtWidgets.QTextEdit(self.tabSala)
		self.tabSala.textEdit.setAcceptRichText(True)
		#self.tabSala.textEdit.setTextColor(QtGui.QColor(102,255,0))
		self.tabSala.textEdit.setFixedSize((3*(self.tabSala.frameGeometry().width()/3)-125),((3*((self.tabSala.frameGeometry().height())/3))-90))
		self.tabSala.textEdit.move(30,30)
		self.tabSala.textEdit.setWordWrapMode(True)
		self.tabSala.textEdit.setObjectName("textEdit")
		self.tabSala.textEdit.setStyleSheet("""
			#textEdit{
				background-color: rgba(0, 0, 0, 200);
				border-radius: 10px;
				padding: 10px;
				border: 2px solid #DB7093;
			}
		""")
		self.tabSala.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.tabSala.textEdit.customContextMenuRequested.connect(lambda: self.menuContextualQTextEdit(self.tabSala.textEdit))
		format= QtGui.QTextCharFormat()
		format.setForeground(QtGui.QColor(254, 103, 47))
		#format.setBackground(QtGui.QColor(255,255,255))
		format.setFontWeight(QtGui.QFont.Normal)
		format.setFont(QtGui.QFont("Ubuntu", 10))
		format2 = QtGui.QTextCharFormat()
		format2.setForeground(QtGui.QColor(61,254,47))
		format2.setFont(QtGui.QFont("Ubuntu", 10))
		self.tabSala.textEdit.setReadOnly(True)
		self.tabSala.textEdit.cursor = self.tabSala.textEdit.textCursor()
		self.tabSala.textEdit.cursor.mergeCharFormat(format)
		self.tabSala.textEdit.cursor.insertText("Sistema: ")
		self.tabSala.textEdit.cursor.mergeCharFormat(format2)
		self.tabSala.textEdit.cursor.insertText("ABC")
		#self.tabSala.textEdit.update()
		#self.tabSala.paintEvent = self.eventoTextEdit

		labelUsuariosSala = QtWidgets.QLabel(self.tabSala)
		labelUsuariosSala.move(self.tabSala.frameGeometry().width()-83, 25)
		labelUsuariosSala.setAlignment(QtCore.Qt.AlignCenter)
		labelUsuariosSala.setObjectName("labelUsuariosSala")
		labelUsuariosSala.efectos = QtWidgets.QGraphicsDropShadowEffect()
		labelUsuariosSala.efectos.setBlurRadius(10)
		labelUsuariosSala.efectos.setColor(QtGui.QColor("#FF00FF"))
		labelUsuariosSala.efectos.setOffset(1,1)
		labelUsuariosSala.setGraphicsEffect(labelUsuariosSala.efectos)
		labelUsuariosSala.setText("Usuaries conectades:")
		labelUsuariosSala.setStyleSheet("""
			#labelUsuariosSala{
				font-weight: bold;
				font: 16pt "Segoe UI Light";
				color: white;
			}
		""")
		self.tabSala.myQListWidget = QtWidgets.QListWidget(self.tabSala)
		for usuario, atributos in usuariosSala.items():
			print(atributos['nickname'], atributos['nombre'], atributos['sexo'])
			myQCustomWidgetList = QCustomWidgetList()
			myQCustomWidgetList.setTextUp(atributos['nickname'])
			myQCustomWidgetList.setTextDown(atributos['nombre'])
			if atributos['sexo'] == 'Masculino':
				myQCustomWidgetList.setIcon('Imagenes/man.png')
			else:
				myQCustomWidgetList.setIcon('Imagenes/woman.png')
			myQListWidgetItem = QtWidgets.QListWidgetItem(self.tabSala.myQListWidget)
			myQListWidgetItem.nickname = atributos['nickname']
			myQListWidgetItem.setSizeHint(myQCustomWidgetList.sizeHint())
			self.tabSala.myQListWidget.addItem(myQListWidgetItem)
			self.tabSala.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomWidgetList)
		self.tabSala.myQListWidget.resize(170, 300)
		self.tabSala.myQListWidget.move((self.tabSala.frameGeometry().width())-78,60)
		self.tabSala.myQListWidget.mousePressEvent = self.eventolistaMouse
		self.tabSala.myQListWidget.mouseReleaseEvent = self.eventolistaMouse2
		self.tabSala.myQListWidget.keyPressEvent = self.eventoPressKeyLista
		self.tabSala.myQListWidget.itemDoubleClicked.connect(self.nada)
		self.tabSala.myQListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.tabSala.myQListWidget.customContextMenuRequested.connect(lambda: self.menuContextualQList(self.tabSala.myQListWidget.currentItem().nickname))
		estilolista(self.tabSala.myQListWidget)
		self.tabSala.myQListWidget.show()
		#------------------------------------------------------------------------------------------------
		self.tabSala.toolButton2 = QtWidgets.QPushButton(self.tabSala)
		self.tabSala.toolButton2.setFixedSize(36, 36)
		self.tabSala.toolButton2.move((2*(self.tabWidget.frameGeometry().width()/3))+130, (2*(self.tabWidget.frameGeometry().height()/3))+30)
		self.tabSala.toolButton2.setObjectName("Opciones2")
		self.tabSala.toolButton2.setIcon(QtGui.QIcon('Imagenes/herramientahover.png'))
		self.tabSala.toolButton2.enterEvent = self.eventoherramientamouse
		self.tabSala.toolButton2.leaveEvent = self.eventoherramientamouse
		self.tabSala.toolButton2.setIconSize(QtCore.QSize(35, 35))
		self.tabSala.toolButton2.setStyleSheet("""
			#Opciones2{
				background-color: transparent;
			}
			#Opciones2::menu-indicator {
				width: 0px;
			}
		""")
		menuOpciones2 = QtWidgets.QMenu()
		menuOpciones2.setObjectName("menuOpciones2")
		menuOpciones2.setStyleSheet("""
			#menuOpciones2{
				font-family: Ubuntu;
			}
		""")
		crearAccion = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionCrearSala.png'), '&Crear sala', self.tabSala)
		crearAccion.triggered.connect(self.ventanacrearsala)

		accionIngresar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionIngresar.png'), '&Ingresar a sala', self.tabSala)
		accionIngresar.triggered.connect(self.nada)

		accionSalirSalar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionSalirSala.png'), '&Salir de la sala', self.tabSala)
		accionSalirSalar.triggered.connect(self.nada)

		#Verificar que sea el dueño
		accionEliminar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionEliminar.png'), '&Eliminar sala', self.tabSala)
		accionEliminar.triggered.connect(lambda: self.alerta('Segure que deseas eliminar ésta sala?', 'critical', 'eliminarSala'))

		accionSalasDisponibles = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionSalasDisponibles.png'), '&Ver salas disponibles', self.tabSala)
		accionSalasDisponibles.triggered.connect(self.nada)

		accionUsuariosDisponibles = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionVerUsuarios.png'), '&Ver usuarios del sistema', self.tabSala)
		accionUsuariosDisponibles.triggered.connect(self.nada)

		menuOpciones2.addAction(crearAccion)
		menuOpciones2.addAction(accionIngresar)
		menuOpciones2.addAction(accionSalirSalar)
		menuOpciones2.addAction(accionEliminar)
		menuOpciones2.addSeparator()
		menuOpciones2.addAction(accionSalasDisponibles)
		menuOpciones2.addAction(accionUsuariosDisponibles)

		self.tabSala.toolButton2.setMenu(menuOpciones2)
		#--------------------------------------------------------------------------------------------------------------
		self.tabSala.lineEditChat = QtWidgets.QLineEdit(self.tabSala)
		self.tabSala.lineEditChat.setFixedWidth((3*(self.tabSala.frameGeometry().width()/3)-125))
		self.tabSala.lineEditChat.move(30,self.tabSala.textEdit.frameGeometry().height()+50)
		self.tabSala.lineEditChat.returnPressed.connect(lambda: self.tabSala.botonEnviar.click())
		self.tabSala.lineEditChat.textChanged.connect(self.verificacionLineEditChat)
		self.tabSala.lineEditChat.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.tabSala.lineEditChat.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.tabSala.lineEditChat))
		self.tabSala.lineEditChat.setPlaceholderText("Escribe un mensaje")
		self.tabSala.lineEditChat.setObjectName("lineEditChat")
		self.tabSala.lineEditChat.setStyleSheet("""
			#lineEditChat{
				background-color: rgba(0, 0, 0, 200);
				color: white;
				font-family: Ubuntu;
				font-size: 14px;
				border-radius: 10px;
				border: 2px solid #DB7093;
				padding: 10px;
				font-family: Ubuntu;
			}
		""")

		self.tabSala.botonAdjunto = QtWidgets.QPushButton(self.tabSala)
		self.tabSala.botonAdjunto.setFixedSize(28, 28)
		self.tabSala.botonAdjunto.move(self.tabSala.lineEditChat.frameGeometry().width()+40,self.tabSala.textEdit.frameGeometry().height()+57)
		self.tabSala.botonAdjunto.setObjectName("botonAdjunto")
		self.tabSala.botonAdjunto.setIcon(QtGui.QIcon('Imagenes/adjunto.png'))
		self.tabSala.botonAdjunto.setIconSize(QtCore.QSize(25,25))
		self.tabSala.botonAdjunto.setStyleSheet('QPushButton{border: 0px solid;}')
		self.tabSala.botonAdjunto.clicked.connect(self.adjuntarArchivo)

		self.tabSala.botonAdjuntoCancelar = QtWidgets.QPushButton(self.tabSala)
		self.tabSala.botonAdjuntoCancelar.setFixedSize(28, 28)
		self.tabSala.botonAdjuntoCancelar.move(self.tabSala.lineEditChat.frameGeometry().width()+42,self.tabSala.textEdit.frameGeometry().height()+85)
		self.tabSala.botonAdjuntoCancelar.setObjectName("botonAdjuntoCancelar")
		self.tabSala.botonAdjuntoCancelar.setIcon(QtGui.QIcon('Imagenes/adjuntocancelar.png'))
		self.tabSala.botonAdjuntoCancelar.setIconSize(QtCore.QSize(25,25))
		self.tabSala.botonAdjuntoCancelar.setStyleSheet('QPushButton{border: 0px solid;}')
		self.tabSala.botonAdjuntoCancelar.hide()
		self.tabSala.botonAdjuntoCancelar.clicked.connect(self.nada)
		self.tabSala.botonAdjuntoCancelar.enterEvent = self.botonAdjuntoCancelarEvento
		self.tabSala.botonAdjuntoCancelar.leaveEvent = self.botonAdjuntoCancelarEvento

		self.tabSala.botonEnviar = QtWidgets.QPushButton(self.tabSala)
		self.tabSala.botonEnviar.setFixedSize(61,31)
		self.tabSala.botonEnviar.move(self.tabSala.lineEditChat.frameGeometry().width()+80,self.tabSala.textEdit.frameGeometry().height()+56)
		self.tabSala.botonEnviar.setObjectName("botonEnviar")
		self.tabSala.botonEnviar.setText("Enviar")
		self.tabSala.botonEnviar.setEnabled(False)
		self.tabSala.botonEnviar.setStyleSheet("""
			#botonEnviar{
				background-color: rgba(0, 0, 0, 200);
				border-radius: 4px;
				font-family: Ubuntu;
				font-size: 14px;
				border: 2px solid gray;
				color: gray;
			}
		""")
		#self.tabSala.botonEnviar.clicked.connect(lambda: self.informacionusuarioventana({'Nombre':'Reyda'}))
		self.fileName = None

		self.tabWidget.insertTab(0, self.tabSala, 'Sala: '+sala['nombre'])
		self.tabWidget.setCurrentIndex(0)
		#--------------------------------------------------------------------------------------------------------------------------------

	def ventanacrearsala(self):
		self.tabSala.crearSalaVentana = QtWidgets.QDialog(self.tabSala, QtCore.Qt.WindowCloseButtonHint)
		self.tabSala.crearSalaVentana.setFixedSize(321, 230)
		self.tabSala.crearSalaVentana.setMouseTracking(True)
		self.tabSala.crearSalaVentana.setObjectName("crearsalaventana")
		self.tabSala.crearSalaVentana.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.tabSala.crearSalaVentana.setWindowTitle("Crear sala")

		font2 = QtGui.QFont()
		font2.setFamily("Ubuntu")
		font2.setPointSize(10)

		self.tabSala.crearSalaVentana.widget = QtWidgets.QWidget(self.tabSala.crearSalaVentana)
		self.tabSala.crearSalaVentana.widget.setFixedSize(self.tabSala.crearSalaVentana.frameGeometry().width()-30, self.tabSala.crearSalaVentana.frameGeometry().height()-30)
		self.tabSala.crearSalaVentana.widget.move(15,15)
		self.tabSala.crearSalaVentana.widget.setObjectName("ventanacrearsalawidget")
		indicador = 10

		self.tabSala.crearSalaVentana.widget.label = QtWidgets.QLabel(self.tabSala.crearSalaVentana.widget)
		self.tabSala.crearSalaVentana.widget.label.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.crearSalaVentana.widget.label.efectos.setBlurRadius(5)
		self.tabSala.crearSalaVentana.widget.label.efectos.setColor(QtGui.QColor("#FF00FF"))
		self.tabSala.crearSalaVentana.widget.label.efectos.setOffset(0,0)
		self.tabSala.crearSalaVentana.widget.label.setGraphicsEffect(self.tabSala.crearSalaVentana.widget.label.efectos)
		self.tabSala.crearSalaVentana.widget.label.setObjectName("label")
		self.tabSala.crearSalaVentana.widget.label.setFixedWidth(self.tabSala.crearSalaVentana.widget.frameGeometry().width())
		self.tabSala.crearSalaVentana.widget.label.setAlignment(QtCore.Qt.AlignCenter)
		self.tabSala.crearSalaVentana.widget.label.move(0,10)
		self.tabSala.crearSalaVentana.widget.label.setText("Crear una sala")
		indicador = indicador + self.tabSala.crearSalaVentana.widget.label.frameGeometry().height()

		self.tabSala.crearSalaVentana.widget.label2 = QtWidgets.QLabel(self.tabSala.crearSalaVentana.widget)
		self.tabSala.crearSalaVentana.widget.label2.setFixedWidth(self.tabSala.crearSalaVentana.widget.frameGeometry().width()-10)
		self.tabSala.crearSalaVentana.widget.label2.move(10, indicador)
		self.tabSala.crearSalaVentana.widget.label2.setAlignment(QtCore.Qt.AlignLeft)
		self.tabSala.crearSalaVentana.widget.label2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.crearSalaVentana.widget.label2.efectos.setBlurRadius(1)
		self.tabSala.crearSalaVentana.widget.label2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.tabSala.crearSalaVentana.widget.label2.efectos.setOffset(0,0)
		self.tabSala.crearSalaVentana.widget.label2.setGraphicsEffect(self.tabSala.crearSalaVentana.widget.label2.efectos)
		self.tabSala.crearSalaVentana.widget.label2.setObjectName("label2")
		self.tabSala.crearSalaVentana.widget.label2.setText("Escribe el nombre de la sala que quieres crear y presiona el botón Crear.")
		self.tabSala.crearSalaVentana.widget.label2.setWordWrap(True)
		indicador = indicador + self.tabSala.crearSalaVentana.widget.label2.frameGeometry().height()

		self.tabSala.crearSalaVentana.widget.lineEdit = QtWidgets.QLineEdit(self.tabSala.crearSalaVentana.widget)
		self.tabSala.crearSalaVentana.widget.lineEdit.setFixedWidth(190)
		self.tabSala.crearSalaVentana.widget.lineEdit.move((self.tabSala.crearSalaVentana.widget.frameGeometry().width()-190)/2, indicador+15)
		self.tabSala.crearSalaVentana.widget.lineEdit.setObjectName("lineEdit")
		self.tabSala.crearSalaVentana.widget.lineEdit.textChanged.connect(self.ventanaCrearSalaVerificar)
		self.tabSala.crearSalaVentana.widget.lineEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.tabSala.crearSalaVentana.widget.lineEdit.setPlaceholderText("Escribe el nombre de la sala")
		self.tabSala.crearSalaVentana.widget.lineEdit.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.tabSala.crearSalaVentana.widget.lineEdit))
		self.tabSala.crearSalaVentana.widget.lineEdit.keyPressEvent = self.ventanaCrearSalaEventoLineEdit
		indicador = indicador + self.tabSala.crearSalaVentana.widget.lineEdit.frameGeometry().height()+15

		self.tabSala.crearSalaVentana.widget.labelError = QtWidgets.QLabel(self.tabSala.crearSalaVentana.widget)
		self.tabSala.crearSalaVentana.widget.labelError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.crearSalaVentana.widget.labelError.efectos.setBlurRadius(1)
		self.tabSala.crearSalaVentana.widget.labelError.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.tabSala.crearSalaVentana.widget.labelError.efectos.setOffset(0,0)
		self.tabSala.crearSalaVentana.widget.labelError.setGraphicsEffect(self.tabSala.crearSalaVentana.widget.labelError.efectos)
		self.tabSala.crearSalaVentana.widget.labelError.setObjectName("labelError")
		self.tabSala.crearSalaVentana.widget.labelError.setFixedWidth(self.tabSala.crearSalaVentana.widget.frameGeometry().width()-10)
		self.tabSala.crearSalaVentana.widget.labelError.move(10, indicador+5)
		self.tabSala.crearSalaVentana.widget.labelError.setAlignment(QtCore.Qt.AlignCenter)
		self.tabSala.crearSalaVentana.widget.labelError.setFont(font2)
		self.tabSala.crearSalaVentana.widget.labelError.hide()
		indicador = indicador + self.tabSala.crearSalaVentana.widget.labelError.frameGeometry().height()+5

		self.tabSala.crearSalaVentana.widget.botonAceptar = QtWidgets.QPushButton(self.tabSala.crearSalaVentana.widget)
		self.tabSala.crearSalaVentana.widget.botonAceptar.setFixedSize(60,25)
		self.tabSala.crearSalaVentana.widget.botonAceptar.move((self.tabSala.crearSalaVentana.widget.frameGeometry().width()/2)-30-35, self.tabSala.crearSalaVentana.widget.frameGeometry().height()-25-15)
		self.tabSala.crearSalaVentana.widget.botonAceptar.setObjectName("botonAceptar")
		self.tabSala.crearSalaVentana.widget.botonAceptar.clicked.connect(lambda:print("si"))
		self.tabSala.crearSalaVentana.widget.botonAceptar.setText("Crear")
		self.tabSala.crearSalaVentana.widget.botonAceptar.setEnabled(False)

		self.tabSala.crearSalaVentana.widget.botonCancelar = QtWidgets.QPushButton(self.tabSala.crearSalaVentana.widget)
		self.tabSala.crearSalaVentana.widget.botonCancelar.setFixedSize(60,25)
		self.tabSala.crearSalaVentana.widget.botonCancelar.move((self.tabSala.crearSalaVentana.widget.frameGeometry().width()/2)-30+35, self.tabSala.crearSalaVentana.widget.frameGeometry().height()-25-15)
		self.tabSala.crearSalaVentana.widget.botonCancelar.setObjectName("botonCancelar")
		self.tabSala.crearSalaVentana.widget.botonCancelar.setText("Cancelar")
		self.tabSala.crearSalaVentana.widget.botonCancelar.clicked.connect(lambda: self.tabSala.crearSalaVentana.hide())
		estiloventanamenuopciones2(self.tabSala.crearSalaVentana, 0)

		self.tabSala.crearSalaVentana.exec_()

	def ventanaCrearSalaVerificar(self):
		if len(self.tabSala.crearSalaVentana.widget.lineEdit.text()) == 0:
			self.tabSala.crearSalaVentana.widget.labelError.hide()
			self.tabSala.crearSalaVentana.widget.botonAceptar.setEnabled(False)
			self.tabSala.crearSalaVentana.widget.botonAceptar.setStyleSheet("""
				#botonAceptar{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 12px;
					border: 2px solid gray;
					color: gray;
				}
			""")
		else:
			if len(self.tabSala.crearSalaVentana.widget.lineEdit.text()) < 4:
				self.tabSala.crearSalaVentana.widget.labelError.setText("El nombre de la sala debe ser mínimo de 4 caracteres.")
				self.tabSala.crearSalaVentana.widget.labelError.setWordWrap(True)
				self.tabSala.crearSalaVentana.widget.labelError.show()
				self.tabSala.crearSalaVentana.widget.botonAceptar.setEnabled(False)
				self.tabSala.crearSalaVentana.widget.botonAceptar.setStyleSheet("""
					#botonAceptar{
						background-color: rgba(0, 0, 0, 200);
						border-radius: 4px;
						font-family: Ubuntu;
						font-size: 12px;
						border: 2px solid gray;
						color: gray;
					}
				""")
			elif len(self.tabSala.crearSalaVentana.widget.lineEdit.text()) > 25:
				self.tabSala.crearSalaVentana.widget.labelError.setText("El nombre de la sala debe ser máximo de 25 caracteres.")
				self.tabSala.crearSalaVentana.widget.labelError.setWordWrap(True)
				self.tabSala.crearSalaVentana.widget.labelError.show()
				self.tabSala.crearSalaVentana.widget.botonAceptar.setEnabled(False)
				self.tabSala.crearSalaVentana.widget.botonAceptar.setStyleSheet("""
					#botonAceptar{
						background-color: rgba(0, 0, 0, 200);
						border-radius: 4px;
						font-family: Ubuntu;
						font-size: 12px;
						border: 2px solid gray;
						color: gray;
					}
				""")
			else:
				self.tabSala.crearSalaVentana.widget.labelError.hide()
				self.tabSala.crearSalaVentana.widget.botonAceptar.setEnabled(True)
				self.tabSala.crearSalaVentana.widget.botonAceptar.setStyleSheet("""
					#botonAceptar{
						background-color: rgba(0, 0, 0, 200);
						border-radius: 4px;
						font-family: Ubuntu;
						font-size: 12px;
						border: 2px solid green;
						color: white;
					}
					#botonAceptar:hover{
						background-color: rgba(0, 0, 0, 200);
						border: 2px solid GreenYellow;
						color: white;
					}
					#botonAceptar:pressed{
						background-color: rgba(0, 0, 0, 200);
						border: 2px solid rgb(102,255,0);
						color: white;
					}
				""")

	def ventanaCrearSalaEventoLineEdit(self, event):
		if event.key() == 16777220:
			self.tabSala.crearSalaVentana.widget.botonAceptar.click()
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.tabSala.crearSalaVentana.widget.lineEdit, event)

	def verificacionLineEditChat(self):
		if len(self.tabSala.lineEditChat.text()) == 0:
			if self.fileName != None:
				self.tabSala.botonEnviar.setEnabled(True)
				self.tabSala.botonEnviar.setStyleSheet("""
					#botonEnviar{
						background-color: rgba(0, 0, 0, 200);
						border-radius: 4px;
						font-family: Ubuntu;
						font-size: 14px;
						border: 2px solid green;
						color: white;
					}
					#botonEnviar:hover{
						background-color: rgba(0, 0, 0, 200);
						border: 2px solid white;
						color: green;
					}
					#botonEnviar:pressed{
						background-color: rgba(0, 0, 0, 200);
						border: 2px solid rgb(102,255,0);
						color: white;
					}
				""")
			else:
				self.tabSala.botonEnviar.setEnabled(False)
				self.tabSala.botonEnviar.setStyleSheet("""
					#botonEnviar{
						background-color: rgba(0, 0, 0, 200);
						border-radius: 4px;
						font-family: Ubuntu;
						font-size: 14px;
						border: 2px solid gray;
						color: gray;
					}
				""")
		else:
			self.tabSala.botonEnviar.setEnabled(True)
			self.tabSala.botonEnviar.setStyleSheet("""
				#botonEnviar{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 14px;
					border: 2px solid green;
					color: white;
				}
				#botonEnviar:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid white;
					color: green;
				}
				#botonEnviar:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")

	def botonAdjuntoCancelarEvento(self, event):
		if event.type() == 10:
			self.tabSala.botonAdjuntoCancelar.setIcon(QtGui.QIcon('Imagenes/adjuntocancelarhover.png'))
			self.tabSala.botonAdjuntoCancelar.setIconSize(QtCore.QSize(25,25))
		else:
			self.tabSala.botonAdjuntoCancelar.setIcon(QtGui.QIcon('Imagenes/adjuntocancelar.png'))
			self.tabSala.botonAdjuntoCancelar.setIconSize(QtCore.QSize(25,25))

	def eventoherramientamouse(self, event):
		if event.type() == 10:
			self.tabSala.toolButton2.setIcon(QtGui.QIcon('Imagenes/herramienta.png'))
			self.tabSala.toolButton2.setIconSize(QtCore.QSize(35,35))
		else:
			self.tabSala.toolButton2.setIcon(QtGui.QIcon('Imagenes/herramientahover.png'))
			self.tabSala.toolButton2.setIconSize(QtCore.QSize(35,35))

	def setIndexTab(self, index):
		self.tabWidget.setCurrentIndex(index)

	def eventolistaMouse(self, event):
		if event.button() == 2 or event.button() == 1:
			QtWidgets.QListWidget.mousePressEvent(self.tabSala.myQListWidget, event)
		else:
			event.ignore()

	def eventolistaMouse2(self, event):
		if event.button() == 2 or event.button() == 1:
			QtWidgets.QListWidget.mouseReleaseEvent(self.tabSala.myQListWidget, event)
		else:
			event.ignore()

	def eventoPressKeyLista(self, event):
		event.ignore()

	def adjuntarArchivo(self):
		options = QtWidgets.QFileDialog.Options()
		#self.label2.hide() -- Label de cancelar
		self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.tabSala,"Selecciona un archivo adjunto", "","Todos los archivos (*)", options=options)
		if self.fileName:
			self.tabSala.botonAdjuntoCancelar.show()
			self.tabSala.botonAdjunto.setEnabled(False)
			#self.tabSala.lineEditChat.setText("")
			#self.tabSala.lineEditChat.setEnabled(False)
			'''self.tabSala.lineEditChat.setStyleSheet("""
				#lineEditChat{
					background-color: rgba(112, 128, 144, 200);
					color: white;
					font-family: Ubuntu;
					font-size: 14px;
					border-radius: 10px;
					border: 2px solid #DB7093;
					padding: 10px;
					font-family: Ubuntu;
				}
			""")'''
			self.tabSala.botonEnviar.setEnabled(True)
			self.tabSala.botonEnviar.setStyleSheet("""
				#botonEnviar{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 14px;
					border: 2px solid green;
					color: white;
				}
				#botonEnviar:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid white;
					color: green;
				}
				#botonEnviar:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")
			#self.label2.show()
			print(self.fileName)

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

	def menuContextualQTextEdit(self, objeto):
		menuContextual = QtWidgets.QMenu()

		actionCopiar = QtWidgets.QAction(QtGui.QIcon('Imagenes/accioncopiar.png'), '&Copiar\tCTRL+C')
		actionCopiar.setShortcut('CTRL+C')
		actionCopiar.triggered.connect(lambda: objeto.copy())
		cursor = self.tabSala.textEdit.textCursor()
		text = self.tabSala.textEdit.toPlainText()
		if cursor.selectionEnd() - cursor.selectionStart() != 0:
			actionCopiar.setEnabled(True)
		else:
			actionCopiar.setEnabled(False)

		actionSeleccionarTodo = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionseleccionar.png'), '&Seleccionar Todo\tCTRL+A')
		actionSeleccionarTodo.setShortcut('CTRL+A')
		actionSeleccionarTodo.triggered.connect(lambda: objeto.selectAll())
		cursor = self.tabSala.textEdit.textCursor()
		text = self.tabSala.textEdit.toPlainText()
		if len(text):
			actionSeleccionarTodo.setEnabled(True)
		else:
			actionSeleccionarTodo.setEnabled(False)
		if cursor.selectionEnd() - cursor.selectionStart() == len(text):
			actionSeleccionarTodo.setEnabled(False)
		else:
			actionSeleccionarTodo.setEnabled(True)

		menuContextual.addAction(actionCopiar)
		menuContextual.addSeparator()
		menuContextual.addAction(actionSeleccionarTodo)
		menuContextual.exec_(QtGui.QCursor.pos())

	def menuContextualQList(self, usuarioseleccionado):
		menuContextual = QtWidgets.QMenu()
		print(usuarioseleccionado)
		actionInformacion = QtWidgets.QAction(QtGui.QIcon('Imagenes/accioninformacion.png'), 'Ver información del usuario')
		actionInformacion.triggered.connect(self.nada)
		actionEnviarMensaje = QtWidgets.QAction(QtGui.QIcon('Imagenes/accionenviarmensaje.png'), 'Enviar Mensaje Privado')
		actionEnviarMensaje.triggered.connect(self.nada)

		menuContextual.addAction(actionInformacion)
		menuContextual.addAction(actionEnviarMensaje)
		menuContextual.exec_(QtGui.QCursor.pos())

	def informacionusuarioventana(self, usuario):
		self.tabSala.informacionUsuarioVentana = QtWidgets.QDialog(self.tabSala, QtCore.Qt.WindowCloseButtonHint)
		self.tabSala.informacionUsuarioVentana.setFixedSize(321, 270)
		self.tabSala.informacionUsuarioVentana.setMouseTracking(True)
		self.tabSala.informacionUsuarioVentana.setObjectName("informacionusuarioventana")
		self.tabSala.informacionUsuarioVentana.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.tabSala.informacionUsuarioVentana.setWindowTitle("Información de Usuario")

		self.tabSala.informacionUsuarioVentana.widget = QtWidgets.QWidget(self.tabSala.informacionUsuarioVentana)
		self.tabSala.informacionUsuarioVentana.widget.setFixedSize(self.tabSala.informacionUsuarioVentana.frameGeometry().width()-30, self.tabSala.informacionUsuarioVentana.frameGeometry().height()-50)
		self.tabSala.informacionUsuarioVentana.widget.move(15,5)
		self.tabSala.informacionUsuarioVentana.widget.setObjectName("informacionusuarioventanawidget")

		self.tabSala.informacionUsuarioVentana.widget.labelNickname = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.efectos.setBlurRadius(5)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.efectos.setColor(QtGui.QColor("#ADFF2F"))
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelNickname.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.setObjectName("labelNickname")
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.move(10,15)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname.setText("Nickname:")

		self.tabSala.informacionUsuarioVentana.widget.labelNickname2 = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.efectos.setBlurRadius(1)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelNickname2.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.setObjectName("labelNickname2")
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.setMinimumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-self.tabSala.informacionUsuarioVentana.widget.labelNickname.frameGeometry().width()-20)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.setMaximumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-self.tabSala.informacionUsuarioVentana.widget.labelNickname.frameGeometry().width()-20)
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.move(self.tabSala.informacionUsuarioVentana.widget.labelNickname.frameGeometry().width()+10,17)
		#Nickname del usuario
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.setText(usuario['nickname'])
		self.tabSala.informacionUsuarioVentana.widget.labelNickname2.setWordWrap(True)

		self.tabSala.informacionUsuarioVentana.widget.labelNombre = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.efectos.setBlurRadius(5)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.efectos.setColor(QtGui.QColor("#ADFF2F"))
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelNombre.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.setObjectName("labelNombre")
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.move(10,50)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre.setText("Nombre:")

		self.tabSala.informacionUsuarioVentana.widget.labelNombre2 = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.efectos.setBlurRadius(1)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelNombre2.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.setObjectName("labelNombre2")
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.setMaximumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelNombre.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.setMinimumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelNombre.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.move(self.tabSala.informacionUsuarioVentana.widget.labelNombre.frameGeometry().width()+10,52)
		#Nombre del usuario
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.setText(usuario['nombre'])
		self.tabSala.informacionUsuarioVentana.widget.labelNombre2.setWordWrap(True)

		self.tabSala.informacionUsuarioVentana.widget.labelSexo = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.efectos.setBlurRadius(5)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.efectos.setColor(QtGui.QColor("#ADFF2F"))
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelSexo.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.setObjectName("labelSexo")
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.move(10,110)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo.setText("Sexo:")

		self.tabSala.informacionUsuarioVentana.widget.labelSexo2 = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.efectos.setBlurRadius(1)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelSexo2.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.setObjectName("labelSexo2")
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.setMaximumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelSexo.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.setMinimumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelSexo.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.move(self.tabSala.informacionUsuarioVentana.widget.labelSexo.frameGeometry().width()+10,112.5)
		#Sexo del usuario
		self.tabSala.informacionUsuarioVentana.widget.labelSexo2.setText(usuario['sexo'])

		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.efectos.setBlurRadius(5)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.efectos.setColor(QtGui.QColor("#ADFF2F"))
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.setObjectName("labelFechaNacimiento")
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.move(10,145)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.setText("F. Nacimiento:")

		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2 = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.efectos.setBlurRadius(1)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.setObjectName("labelFechaNacimiento2")
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.setMaximumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.setMinimumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.move(self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento.frameGeometry().width()+43,147)
		#Fecha Nacimiento usuario
		self.tabSala.informacionUsuarioVentana.widget.labelFechaNacimiento2.setText(usuario['fechaNacimiento'])

		self.tabSala.informacionUsuarioVentana.widget.labelEdad = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.efectos.setBlurRadius(5)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.efectos.setColor(QtGui.QColor("#ADFF2F"))
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelEdad.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.setObjectName("labelEdad")
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.move(10,180)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad.setText("Edad:")

		self.tabSala.informacionUsuarioVentana.widget.labelEdad2 = QtWidgets.QLabel(self.tabSala.informacionUsuarioVentana.widget)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.efectos.setBlurRadius(1)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.efectos.setOffset(0,0)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.setGraphicsEffect(self.tabSala.informacionUsuarioVentana.widget.labelEdad2.efectos)
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.setObjectName("labelEdad2")
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.setMaximumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelEdad.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.setMinimumWidth(self.tabSala.informacionUsuarioVentana.widget.frameGeometry().width()-10-self.tabSala.informacionUsuarioVentana.widget.labelEdad.frameGeometry().width())
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.move(self.tabSala.informacionUsuarioVentana.widget.labelEdad.frameGeometry().width()+10,182)
		#Fecha Nacimiento usuario
		self.tabSala.informacionUsuarioVentana.widget.labelEdad2.setText(str(usuario['edad']))

		estiloventanainformacionusuario(self.tabSala.informacionUsuarioVentana)

		self.tabSala.informacionUsuarioVentana.botones = QtWidgets.QDialogButtonBox(self.tabSala.informacionUsuarioVentana)
		if usuario['nickname'] != self.usuario['nickname']:
			self.tabSala.informacionUsuarioVentana.botones.move(8,self.tabSala.informacionUsuarioVentana.frameGeometry().height()-33)
			self.tabSala.informacionUsuarioVentana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Cancel)
			self.tabSala.informacionUsuarioVentana.botones.setCenterButtons(True)
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setObjectName("Boton_Aceptar")
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setFixedSize(150,25)
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setText("Enviar Mensaje")
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("""
				#Boton_Aceptar{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 14px;
					border: 2px solid green;
					color: white;
				}
				#Boton_Aceptar:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid GreenYellow;
					color: white;
				}
				#Boton_Aceptar:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setObjectName("Boton_Volver")
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setFixedSize(150,25)
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setText("Volver")
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.tabSala.informacionUsuarioVentana.hide())
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet("""
				#Boton_Volver{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 14px;
					border: 2px solid red;
					color: white;
				}
				#Boton_Volver:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 102, 51);
					color: white;
				}
				#Boton_Volver:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(255, 173, 51);
					color: white;
				}
			""")
		else:
			self.tabSala.informacionUsuarioVentana.botones.move((self.tabSala.informacionUsuarioVentana.frameGeometry().width()/2)-75,self.tabSala.informacionUsuarioVentana.frameGeometry().height()-33)
			self.tabSala.informacionUsuarioVentana.botones.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setObjectName("Boton_Volver")
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setFixedSize(150,25)
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setText("Volver")
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.tabSala.informacionUsuarioVentana.hide())
			self.tabSala.informacionUsuarioVentana.botones.button(QtWidgets.QDialogButtonBox.Cancel).setStyleSheet("""
				#Boton_Volver{
					background-color: rgba(0, 0, 0, 200);
					border-radius: 4px;
					font-family: Ubuntu;
					font-size: 14px;
					border: 2px solid green;
					color: white;
				}
				#Boton_Volver:hover{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid GreenYellow;
					color: white;
				}
				#Boton_Volver:pressed{
					background-color: rgba(0, 0, 0, 200);
					border: 2px solid rgb(102,255,0);
					color: white;
				}
			""")

		self.tabSala.informacionUsuarioVentana.exec_()

	def ventanaeditardatos(self,usuario):
		self.ventanaEditarDatos = QtWidgets.QMainWindow(None, QtCore.Qt.WindowCloseButtonHint)
		self.ventanaEditarDatos.setFixedSize(700, 580)
		self.ventanaEditarDatos.setMouseTracking(True)
		self.ventanaEditarDatos.setObjectName("editardatosventana")
		self.ventanaEditarDatos.setWindowIcon(QtGui.QIcon('Imagenes/icono.png'))
		self.ventanaEditarDatos.setWindowTitle("Editar Cuenta")

		self.ventanaEditarDatos.widget = QtWidgets.QWidget(self.ventanaEditarDatos)
		self.ventanaEditarDatos.widget.setFixedSize(self.ventanaEditarDatos.frameGeometry().width()-30, self.ventanaEditarDatos.frameGeometry().height()-60)
		self.ventanaEditarDatos.widget.move(15,15)
		self.ventanaEditarDatos.widget.setObjectName("ventanaeditardatoswidget")

		font2 = QtGui.QFont()
		font2.setFamily("Ubuntu")
		font2.setPointSize(10)

		self.ventanaEditarDatos.widget.label = QtWidgets.QLabel(self.ventanaEditarDatos.widget)
		self.ventanaEditarDatos.widget.label.setFixedWidth(self.ventanaEditarDatos.widget.frameGeometry().width())
		self.ventanaEditarDatos.widget.label.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.label.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.label.efectos.setBlurRadius(5)
		self.ventanaEditarDatos.widget.label.efectos.setColor(QtGui.QColor("#000000"))
		self.ventanaEditarDatos.widget.label.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.label.setGraphicsEffect(self.ventanaEditarDatos.widget.label.efectos)
		self.ventanaEditarDatos.widget.label.setObjectName("label")
		self.ventanaEditarDatos.widget.label.move(10,10)
		self.ventanaEditarDatos.widget.label.setText("Edita los datos de tu cuenta")

		self.ventanaEditarDatos.widget.label2 = QtWidgets.QLabel(self.ventanaEditarDatos.widget)
		self.ventanaEditarDatos.widget.label2.setFixedWidth(self.ventanaEditarDatos.widget.frameGeometry().width())
		self.ventanaEditarDatos.widget.label2.move(10, self.ventanaEditarDatos.widget.label.frameGeometry().height()+25)
		self.ventanaEditarDatos.widget.label2.setAlignment(QtCore.Qt.AlignLeft)
		self.ventanaEditarDatos.widget.label2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.label2.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.label2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.label2.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.label2.setGraphicsEffect(self.ventanaEditarDatos.widget.label2.efectos)
		self.ventanaEditarDatos.widget.label2.setObjectName("label2")
		self.ventanaEditarDatos.widget.label2.setText("Selecciona algún campo, llénalo y dale guardar para cambiar tus datos.")

		self.ventanaEditarDatos.widget.widget =  QtWidgets.QWidget(self.ventanaEditarDatos.widget)
		self.ventanaEditarDatos.widget.widget.setFixedSize(self.ventanaEditarDatos.widget.frameGeometry().width()/2, self.ventanaEditarDatos.widget.frameGeometry().height()-self.ventanaEditarDatos.widget.label2.frameGeometry().height()-self.ventanaEditarDatos.widget.label.frameGeometry().height())
		self.ventanaEditarDatos.widget.widget.move(0,self.ventanaEditarDatos.widget.label2.frameGeometry().height()+self.ventanaEditarDatos.widget.label.frameGeometry().height()+25)
		indicador = 20
		#-------NOMBRE--------------------------------------------------------------------------------------------------------------
		self.ventanaEditarDatos.widget.widget.labelNombre = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.labelNombre.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget.labelNombre.efectos.setBlurRadius(5)
		self.ventanaEditarDatos.widget.widget.labelNombre.efectos.setColor(QtGui.QColor("#FF00FF"))
		self.ventanaEditarDatos.widget.widget.labelNombre.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget.labelNombre.setGraphicsEffect(self.ventanaEditarDatos.widget.widget.labelNombre.efectos)
		self.ventanaEditarDatos.widget.widget.labelNombre.setObjectName("labelNombre")
		self.ventanaEditarDatos.widget.widget.labelNombre.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget.labelNombre.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget.labelNombre.move(0,20)
		self.ventanaEditarDatos.widget.widget.labelNombre.setText("Nombre:")
		indicador = indicador + self.ventanaEditarDatos.widget.widget.labelNombre.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.labelNombre2 = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.labelNombre2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget.labelNombre2.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget.labelNombre2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget.labelNombre2.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget.labelNombre2.setGraphicsEffect(self.ventanaEditarDatos.widget.widget.labelNombre2.efectos)
		self.ventanaEditarDatos.widget.widget.labelNombre2.setObjectName("labelNombre2")
		self.ventanaEditarDatos.widget.widget.labelNombre2.setMinimumWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width()-20)
		self.ventanaEditarDatos.widget.widget.labelNombre2.setMaximumWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width()-20)
		self.ventanaEditarDatos.widget.widget.labelNombre2.move(0, indicador-5)
		self.ventanaEditarDatos.widget.widget.labelNombre2.setAlignment(QtCore.Qt.AlignCenter)
		#Nickname del usuario
		self.ventanaEditarDatos.widget.widget.labelNombre2.setText(usuario['nombre'])
		self.ventanaEditarDatos.widget.widget.labelNombre2.setWordWrap(True)
		indicador = indicador + self.ventanaEditarDatos.widget.widget.labelNombre2.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.lineEditNombre = QtWidgets.QLineEdit(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.lineEditNombre.setFixedWidth(190)
		self.ventanaEditarDatos.widget.widget.lineEditNombre.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()-190)/2, indicador-5)
		self.ventanaEditarDatos.widget.widget.lineEditNombre.setObjectName("lineEditNombre")
		self.ventanaEditarDatos.widget.widget.lineEditNombre.textChanged.connect(self.ventanaEditarDatosVerificacionNombre)
		self.ventanaEditarDatos.widget.widget.lineEditNombre.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaEditarDatos.widget.widget.lineEditNombre.setPlaceholderText("Escribe tu nombre")
		self.ventanaEditarDatos.widget.widget.lineEditNombre.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaEditarDatos.widget.widget.lineEditNombre))
		self.ventanaEditarDatos.widget.widget.lineEditNombre.keyPressEvent = self.ventanaEditarDatosVerificacionNombreEvento
		indicador = indicador + self.ventanaEditarDatos.widget.widget.lineEditNombre.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.labelNombreError = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.labelNombreError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget.labelNombreError.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget.labelNombreError.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget.labelNombreError.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget.labelNombreError.setGraphicsEffect(self.ventanaEditarDatos.widget.widget.labelNombreError.efectos)
		self.ventanaEditarDatos.widget.widget.labelNombreError.setObjectName("labelNombreError")
		self.ventanaEditarDatos.widget.widget.labelNombreError.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width()-10)
		self.ventanaEditarDatos.widget.widget.labelNombreError.move(0, indicador-5)
		self.ventanaEditarDatos.widget.widget.labelNombreError.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget.labelNombreError.setFont(font2)
		self.ventanaEditarDatos.widget.widget.labelNombreError.setText("\n")
		indicador = indicador + self.ventanaEditarDatos.widget.widget.labelNombreError.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.botonAceptarNombre = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget.botonAceptarNombre.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30-35, indicador)
		self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setObjectName("botonAceptarNombre")
		self.ventanaEditarDatos.widget.widget.botonAceptarNombre.clicked.connect(lambda:print("si"))
		self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setText("Guardar")
		self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setEnabled(False)

		self.ventanaEditarDatos.widget.widget.botonCancelarNombre = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.botonCancelarNombre.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget.botonCancelarNombre.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30+35, indicador)
		self.ventanaEditarDatos.widget.widget.botonCancelarNombre.setObjectName("botonCancelarNombre")
		self.ventanaEditarDatos.widget.widget.botonCancelarNombre.setText("Cancelar")
		self.ventanaEditarDatos.widget.widget.botonCancelarNombre.setEnabled(False)
		self.ventanaEditarDatos.widget.widget.botonCancelarNombre.clicked.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget,'EditarNombre Nofocus'))
		indicador = indicador + self.ventanaEditarDatos.widget.widget.botonCancelarNombre.frameGeometry().height()
		#---------------------------------------------------------------------------------------------------------------
		self.ventanaEditarDatos.widget.widget.labelSexo = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.labelSexo.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget.labelSexo.efectos.setBlurRadius(5)
		self.ventanaEditarDatos.widget.widget.labelSexo.efectos.setColor(QtGui.QColor("#FF00FF"))
		self.ventanaEditarDatos.widget.widget.labelSexo.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget.labelSexo.setGraphicsEffect(self.ventanaEditarDatos.widget.widget.labelSexo.efectos)
		self.ventanaEditarDatos.widget.widget.labelSexo.setObjectName("labelSexo")
		self.ventanaEditarDatos.widget.widget.labelSexo.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget.labelSexo.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget.labelSexo.move(0, indicador+5)
		self.ventanaEditarDatos.widget.widget.labelSexo.setText("Sexo:")
		indicador = indicador + self.ventanaEditarDatos.widget.widget.labelSexo.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.labelSexo2 = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.labelSexo2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget.labelSexo2.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget.labelSexo2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget.labelSexo2.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget.labelSexo2.setGraphicsEffect(self.ventanaEditarDatos.widget.widget.labelSexo2.efectos)
		self.ventanaEditarDatos.widget.widget.labelSexo2.setObjectName("labelSexo2")
		self.ventanaEditarDatos.widget.widget.labelSexo2.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget.labelSexo2.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget.labelSexo2.move(0, indicador)
		self.ventanaEditarDatos.widget.widget.labelSexo2.setText(usuario["sexo"])
		indicador = indicador + self.ventanaEditarDatos.widget.widget.labelSexo2.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.radioButtonMasculino = QtWidgets.QRadioButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.radioButtonMasculino.setFixedWidth(32)
		self.ventanaEditarDatos.widget.widget.radioButtonMasculino.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-16-40, indicador)
		self.ventanaEditarDatos.widget.widget.radioButtonMasculino.setObjectName("radioButtonMasculino")
		self.ventanaEditarDatos.widget.widget.radioButtonMasculino.setText("M")
		self.ventanaEditarDatos.widget.widget.radioButtonMasculino.clicked.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget,'EditarSexo Aceptar'))

		self.ventanaEditarDatos.widget.widget.radioButtonFemenino = QtWidgets.QRadioButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.radioButtonFemenino.setFixedWidth(32)
		self.ventanaEditarDatos.widget.widget.radioButtonFemenino.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-16+40, indicador)
		self.ventanaEditarDatos.widget.widget.radioButtonFemenino.setObjectName("radioButtonFemenino")
		self.ventanaEditarDatos.widget.widget.radioButtonFemenino.setText("F")
		self.ventanaEditarDatos.widget.widget.radioButtonFemenino.clicked.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget,'EditarSexo Aceptar'))
		indicador = indicador + self.ventanaEditarDatos.widget.widget.radioButtonFemenino.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.botonAceptarSexo = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.botonAceptarSexo.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget.botonAceptarSexo.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30-35,indicador)
		self.ventanaEditarDatos.widget.widget.botonAceptarSexo.setObjectName("botonAceptarSexo")
		self.ventanaEditarDatos.widget.widget.botonAceptarSexo.clicked.connect(lambda:print("si"))
		self.ventanaEditarDatos.widget.widget.botonAceptarSexo.setText("Guardar")
		self.ventanaEditarDatos.widget.widget.botonAceptarSexo.setEnabled(False)

		self.ventanaEditarDatos.widget.widget.botonCancelarSexo = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.botonCancelarSexo.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget.botonCancelarSexo.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30+35,indicador)
		self.ventanaEditarDatos.widget.widget.botonCancelarSexo.setObjectName("botonCancelarSexo")
		self.ventanaEditarDatos.widget.widget.botonCancelarSexo.setText("Cancelar")
		self.ventanaEditarDatos.widget.widget.botonCancelarSexo.setEnabled(False)
		self.ventanaEditarDatos.widget.widget.botonCancelarSexo.clicked.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget,'EditarSexo Cancelar'))
		indicador = indicador + self.ventanaEditarDatos.widget.widget.botonCancelarSexo.frameGeometry().height()
		#----------------------------------------------------------------------------------------------------------------------------------

		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento= QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.efectos.setBlurRadius(5)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.efectos.setColor(QtGui.QColor("#FF00FF"))
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.setGraphicsEffect(self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.efectos)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.setObjectName("labelFechaNacimiento")
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.move(0, indicador+10)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.setText("F. Nacimiento:")
		indicador = indicador + self.ventanaEditarDatos.widget.widget.labelFechaNacimiento.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2= QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.setGraphicsEffect(self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.efectos)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.setObjectName("labelFechaNacimiento2")
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.move(0, indicador+10)
		self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.setText(usuario['fechaNacimiento'])
		indicador= indicador + self.ventanaEditarDatos.widget.widget.labelFechaNacimiento2.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento = QtWidgets.QDateEdit(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setButtonSymbols(2)
		#Poner Fecha del Usuario
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setDate(QtCore.QDate.fromString(usuario["fechaNacimiento"],'dd/MM/yyyy'))
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setMinimumDate(QtCore.QDate(1930, 1, 1))
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setMaximumDate(QtCore.QDate.currentDate())
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setFixedWidth(190)
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()-190)/2, indicador+10)
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setObjectName("dateEditFechaNacimiento")
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setCalendarPopup(True)
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.keyPressEvent = self.pressKeyQDateEdit
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.keyReleaseEvent = self.releaseKeyQDateEdit
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.indicador = None
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.wheelEvent = self.eventoscalendario
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.dateChanged.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget,'EditarFecha Aceptar'))
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.customContextMenuRequested.connect(lambda: self.menuContextualCalendario(self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento))
		indicador= indicador + self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget.calendario = QtWidgets.QCalendarWidget()
		self.ventanaEditarDatos.widget.widget.calendario.setFont(font2)
		self.ventanaEditarDatos.widget.widget.calendario.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		self.ventanaEditarDatos.widget.widget.calendario.setMinimumDate(QtCore.QDate(1930, 1, 1))
		self.ventanaEditarDatos.widget.widget.calendario.setMaximumDate(QtCore.QDate.currentDate())
		self.ventanaEditarDatos.widget.widget.calendario.setFirstDayOfWeek(QtCore.Qt.Monday)
		self.ventanaEditarDatos.widget.widget.calendario.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
		self.ventanaEditarDatos.widget.widget.calendario.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
		self.ventanaEditarDatos.widget.widget.calendario.setDateEditEnabled(False)
		self.ventanaEditarDatos.widget.widget.calendario.setObjectName("calendario")
		format= QtGui.QTextCharFormat()
		format.setForeground(QtGui.QColor(0,0,255))
		format.setBackground(QtGui.QColor(255,255,255))
		format.setFontWeight(QtGui.QFont.Bold)
		self.ventanaEditarDatos.widget.widget.calendario.setHeaderTextFormat(format)
		self.ventanaEditarDatos.widget.widget.calendario.setStyleSheet("""
			QCalendarWidget QAbstractItemView{
				background-color: white; /* цвет фона текущего месяца */
				selection-background-color: pink; /* цвет фона выбранного дня */
				selection-color: white; /* цвет текста выбранного дня */
			}
		""")
		self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.setCalendarWidget(self.ventanaEditarDatos.widget.widget.calendario)

		self.ventanaEditarDatos.widget.widget.botonAceptarCalendario = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.botonAceptarCalendario.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget.botonAceptarCalendario.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30-35,indicador+22)
		self.ventanaEditarDatos.widget.widget.botonAceptarCalendario.setObjectName("botonAceptarCalendario")
		self.ventanaEditarDatos.widget.widget.botonAceptarCalendario.clicked.connect(lambda:print("si"))
		self.ventanaEditarDatos.widget.widget.botonAceptarCalendario.setText("Guardar")
		self.ventanaEditarDatos.widget.widget.botonAceptarCalendario.setEnabled(False)

		self.ventanaEditarDatos.widget.widget.botonCancelarCalendario = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget)
		self.ventanaEditarDatos.widget.widget.botonCancelarCalendario.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget.botonCancelarCalendario.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30+35,indicador+22)
		self.ventanaEditarDatos.widget.widget.botonCancelarCalendario.setObjectName("botonCancelarCalendario")
		self.ventanaEditarDatos.widget.widget.botonCancelarCalendario.setText("Cancelar")
		self.ventanaEditarDatos.widget.widget.botonCancelarCalendario.setEnabled(False)
		self.ventanaEditarDatos.widget.widget.botonCancelarCalendario.clicked.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget,'EditarFecha Cancelar'))
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
		self.ventanaEditarDatos.widget.widget2 = QtWidgets.QWidget(self.ventanaEditarDatos.widget)
		self.ventanaEditarDatos.widget.widget2.setFixedSize(self.ventanaEditarDatos.widget.frameGeometry().width()/2, self.ventanaEditarDatos.widget.frameGeometry().height()-self.ventanaEditarDatos.widget.label2.frameGeometry().height()-self.ventanaEditarDatos.widget.label.frameGeometry().height())
		self.ventanaEditarDatos.widget.widget2.move(self.ventanaEditarDatos.widget.frameGeometry().width()/2,self.ventanaEditarDatos.widget.label2.frameGeometry().height()+self.ventanaEditarDatos.widget.label.frameGeometry().height()+25)
		self.ventanaEditarDatos.widget.widget2.setStyleSheet("/*background-color:blue;*/")
		indicador = 20

		self.ventanaEditarDatos.widget.widget2.labelClave = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.labelClave.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget2.labelClave.efectos.setBlurRadius(5)
		self.ventanaEditarDatos.widget.widget2.labelClave.efectos.setColor(QtGui.QColor("#FF00FF"))
		self.ventanaEditarDatos.widget.widget2.labelClave.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget2.labelClave.setGraphicsEffect(self.ventanaEditarDatos.widget.widget2.labelClave.efectos)
		self.ventanaEditarDatos.widget.widget2.labelClave.setObjectName("labelClave")
		self.ventanaEditarDatos.widget.widget2.labelClave.setFixedWidth(self.ventanaEditarDatos.widget.widget2.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget2.labelClave.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget2.labelClave.move(0,20)
		self.ventanaEditarDatos.widget.widget2.labelClave.setText("Contraseña:")
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.labelClave.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.lineEditClave = QtWidgets.QLineEdit(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.lineEditClave.setFixedWidth(190)
		self.ventanaEditarDatos.widget.widget2.lineEditClave.move((self.ventanaEditarDatos.widget.widget2.frameGeometry().width()-190)/2, indicador)
		self.ventanaEditarDatos.widget.widget2.lineEditClave.setObjectName("lineEditClave")
		self.ventanaEditarDatos.widget.widget2.lineEditClave.textChanged.connect(self.ventanaEditarDatosVerificacionClaveActual)
		self.ventanaEditarDatos.widget.widget2.lineEditClave.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaEditarDatos.widget.widget2.lineEditClave.setPlaceholderText("Contraseña actual")
		self.ventanaEditarDatos.widget.widget2.lineEditClave.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ventanaEditarDatos.widget.widget2.lineEditClave.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.ventanaEditarDatos.widget.widget2.lineEditClave))
		self.ventanaEditarDatos.widget.widget2.lineEditClave.indicador = None
		self.ventanaEditarDatos.widget.widget2.claveActual = 0
		self.ventanaEditarDatos.widget.widget2.lineEditClave.keyPressEvent = self.keyPressEventLineEditClave
		self.ventanaEditarDatos.widget.widget2.lineEditClave.keyReleaseEvent = self.keyReleaseEventLineEditClave
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.lineEditClave.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.labelClaveError = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget2.labelClaveError.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget2.labelClaveError.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.setGraphicsEffect(self.ventanaEditarDatos.widget.widget2.labelClaveError.efectos)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.setObjectName("labelClaveError")
		self.ventanaEditarDatos.widget.widget2.labelClaveError.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width()-10)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.move(0, indicador)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.setFont(font2)
		self.ventanaEditarDatos.widget.widget2.labelClaveError.setText("\n")
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.labelClaveError.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva = QtWidgets.QLineEdit(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setFixedWidth(190)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.move((self.ventanaEditarDatos.widget.widget2.frameGeometry().width()-190)/2, indicador+10)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setObjectName("lineEditClaveNueva")
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.textChanged.connect(self.ventanaEditarDatosVerificacionClaveNueva)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setPlaceholderText("Nueva contraseña")
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva))
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setEnabled(False)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setStyleSheet('background-color: #B0C4DE;')
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.indicador = None
		self.ventanaEditarDatos.widget.widget2.claveNueva = 0
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.keyPressEvent = self.keyPressEventLineEditClaveNueva
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.keyReleaseEvent = self.keyReleaseEventLineEditClaveNueva
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2 = QtWidgets.QLineEdit(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setFixedWidth(190)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.move((self.ventanaEditarDatos.widget.widget2.frameGeometry().width()-190)/2, indicador+20)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setObjectName("lineEditClaveNueva2")
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.textChanged.connect(self.ventanaEditarDatosVerificacionClaveNueva2)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setPlaceholderText("Confirma nueva contraseña")
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.customContextMenuRequested.connect(lambda: self.menuContextualQLineEditPassword(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2))
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.indicador = None
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.keyPressEvent = self.keyPressEventLineEditClaveNueva2
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.keyReleaseEvent = self.keyReleaseEventLineEditClaveNueva2
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setEnabled(False)
		self.ventanaEditarDatos.widget.widget2.claveNueva2 = 0
		self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setStyleSheet('background-color: #B0C4DE;')
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.frameGeometry().height()+20

		self.ventanaEditarDatos.widget.widget2.labelClaveError2 = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.setGraphicsEffect(self.ventanaEditarDatos.widget.widget2.labelClaveError2.efectos)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.setObjectName("labelClaveError2")
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width()-10)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.move(0, indicador)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.setFont(font2)
		self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("\n")
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.labelClaveError2.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30-35,indicador+5)
		self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setObjectName("botonAceptarClaveNueva")
		self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.clicked.connect(lambda:print("si"))
		self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setText("Guardar")
		self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)

		self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30+35,indicador+5)
		self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.setObjectName("botonCancelarClaveNueva")
		self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.setText("Cancelar")
		self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.setEnabled(False)
		self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.clicked.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarClave Nofocus'))
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.frameGeometry().height()+10

		self.ventanaEditarDatos.widget.widget2.labelPregunta = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.labelPregunta.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget2.labelPregunta.efectos.setBlurRadius(5)
		self.ventanaEditarDatos.widget.widget2.labelPregunta.efectos.setColor(QtGui.QColor("#FF00FF"))
		self.ventanaEditarDatos.widget.widget2.labelPregunta.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget2.labelPregunta.setGraphicsEffect(self.ventanaEditarDatos.widget.widget2.labelPregunta.efectos)
		self.ventanaEditarDatos.widget.widget2.labelPregunta.setObjectName("labelPregunta")
		self.ventanaEditarDatos.widget.widget2.labelPregunta.setFixedWidth(self.ventanaEditarDatos.widget.widget2.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget2.labelPregunta.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget2.labelPregunta.move(0,indicador+10)
		self.ventanaEditarDatos.widget.widget2.labelPregunta.setText("Pregunta Secreta:")
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.labelPregunta.frameGeometry().height() +10

		self.ventanaEditarDatos.widget.widget2.labelPregunta2 = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.setGraphicsEffect(self.ventanaEditarDatos.widget.widget2.labelPregunta2.efectos)
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.setObjectName("labelPregunta2")
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.setFixedWidth(self.ventanaEditarDatos.widget.widget2.frameGeometry().width())
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.move(0,indicador)
		self.ventanaEditarDatos.widget.widget2.labelPregunta2.setText("¿Cuál es tu banda favorite?")
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.labelPregunta2.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta = QtWidgets.QLineEdit(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.setFixedWidth(190)
		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.move((self.ventanaEditarDatos.widget.widget2.frameGeometry().width()-190)/2, indicador)
		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.setObjectName("lineEditRespuesta")
		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.textChanged.connect(self.ventanaEditarDatosVerificacionRespuesta)
		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.setPlaceholderText("Escribe la respuesta secreta")
		self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.customContextMenuRequested.connect(lambda: self.menuContextualQLineEdit(self.ventanaEditarDatos.widget.widget2.lineEditRespuesta))
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.labelRespuestaError = QtWidgets.QLabel(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.efectos = QtWidgets.QGraphicsDropShadowEffect()
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.efectos.setBlurRadius(1)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.efectos.setColor(QtGui.QColor("#FFFFFF"))
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.efectos.setOffset(0,0)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setGraphicsEffect(self.ventanaEditarDatos.widget.widget2.labelRespuestaError.efectos)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setObjectName("labelRespuestaError")
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setFixedWidth(self.ventanaEditarDatos.widget.widget.frameGeometry().width()-10)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.move(0, indicador)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setAlignment(QtCore.Qt.AlignCenter)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setFont(font2)
		self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setText("\n")
		indicador = indicador + self.ventanaEditarDatos.widget.widget2.labelRespuestaError.frameGeometry().height()

		self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30-35,indicador+7)
		self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.setObjectName("botonAceptarRespuesta")
		self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.clicked.connect(lambda:print("si"))
		self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.setText("Guardar")
		self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.setEnabled(False)

		self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta = QtWidgets.QPushButton(self.ventanaEditarDatos.widget.widget2)
		self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.setFixedSize(60,25)
		self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.move((self.ventanaEditarDatos.widget.widget.frameGeometry().width()/2)-30+35,indicador+7)
		self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.setObjectName("botonCancelarRespuesta")
		self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.clicked.connect(lambda: verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarRespuesta Nofocus'))
		self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.setText("Cancelar")
		self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.setEnabled(False)

		self.ventanaEditarDatos.botonVolver = QtWidgets.QPushButton(self.ventanaEditarDatos)
		self.ventanaEditarDatos.botonVolver.setFixedSize(90,25)
		self.ventanaEditarDatos.botonVolver.move((self.ventanaEditarDatos.frameGeometry().width()/2)-30,self.ventanaEditarDatos.widget.frameGeometry().height()+25)
		self.ventanaEditarDatos.botonVolver.setObjectName("botonVolverEditarDatos")
		self.ventanaEditarDatos.botonVolver.clicked.connect(lambda: self.ventanaEditarDatos.hide())
		self.ventanaEditarDatos.botonVolver.setText("Volver")

		estiloventanaeditardatos(self.ventanaEditarDatos)

		#self.ventanaEditarDatos.exec_()
		self.ventanaEditarDatos.show()

	def ventanaEditarDatosVerificacionRespuesta(self):
		if len(self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.text()) == 0:
			self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setText("\n")
			self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.setEnabled(False)
			self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.setEnabled(False)
			verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarRespuesta Cancelar')
		else:
			if re.match(r'^[^:]*$', self.ventanaEditarDatos.widget.widget2.lineEditRespuesta.text()) is None:
				self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setText("Caracter dos puntos ':' no admitido\nen la respuesta secreta.")
				self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setWordWrap(True)
				self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.setEnabled(False)
				verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarRespuesta Cancelar')
			else:
				self.ventanaEditarDatos.widget.widget2.labelRespuestaError.setText("\n")
				self.ventanaEditarDatos.widget.widget2.botonAceptarRespuesta.setEnabled(True)
				self.ventanaEditarDatos.widget.widget2.botonCancelarRespuesta.setEnabled(True)
				verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarRespuesta Aceptar')

	def ventanaEditarDatosVerificacionClaveActual(self):
		if len(self.ventanaEditarDatos.widget.widget2.lineEditClave.text()) == 0:
			self.ventanaEditarDatos.widget.widget2.claveActual = 0
			self.ventanaEditarDatos.widget.widget2.labelClaveError.setText("\n")
			self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
			self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.setEnabled(False)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setEnabled(False)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.clear()
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setStyleSheet('background-color: #B0C4DE;')
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setEnabled(False)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setStyleSheet('background-color: #B0C4DE;')
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.blockSignals(True)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.clear()
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.blockSignals(False)
			verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarClave Cancelar')
		else:
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.clear()
			self.ventanaEditarDatos.widget.widget2.botonCancelarClaveNueva.setEnabled(True)
			verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarClave Cancelar1')
			if len(self.ventanaEditarDatos.widget.widget2.lineEditClave.text()) < 6:
				self.ventanaEditarDatos.widget.widget2.claveActual = 0
				self.ventanaEditarDatos.widget.widget2.labelClaveError.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setStyleSheet('background-color: #B0C4DE;')
			elif re.match(r'^[^:]*$', self.ventanaEditarDatos.widget.widget2.lineEditClave.text()) is None:
				self.ventanaEditarDatos.widget.widget2.claveActual = 0
				self.ventanaEditarDatos.widget.widget2.labelClaveError.setText("Caracter dos puntos ':' no admitido\nen la contraseña.")
				self.ventanaEditarDatos.widget.widget2.labelClaveError.setWordWrap(True)
				self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setStyleSheet('background-color: #B0C4DE;')
			else:
				self.ventanaEditarDatos.widget.widget2.claveActual = 1
				self.ventanaEditarDatos.widget.widget2.labelClaveError.setText("\n")
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setEnabled(True)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.setStyleSheet('background-color: white;')

	def ventanaEditarDatosVerificacionClaveNueva(self):
		if len(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.text()) == 0:
			self.ventanaEditarDatos.widget.widget2.claveNueva = 0
			self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("\n")
			self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setEnabled(False)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setStyleSheet('background-color: #B0C4DE;')
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.blockSignals(True)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.clear()
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.blockSignals(False)
			verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarClave Aceptar0')
		else:
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.blockSignals(True)
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.clear()
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.blockSignals(False)
			if len(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.text()) < 6:
				self.ventanaEditarDatos.widget.widget2.claveNueva = 0
				self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setStyleSheet('background-color: #B0C4DE;')
				verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarClave Aceptar0')
			elif re.match(r'^[^:]*$', self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.text()) is None:
				self.ventanaEditarDatos.widget.widget2.claveNueva = 0
				self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("Caracter dos puntos ':' no admitido\nen la contraseña.")
				self.ventanaEditarDatos.widget.widget2.labelClaveError2.setWordWrap(True)
				self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setEnabled(False)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setStyleSheet('background-color: #B0C4DE;')
				verificacion1(self.ventanaEditarDatos.widget.widget2,'EditarClave Aceptar0')
			else:
				self.ventanaEditarDatos.widget.widget2.claveNueva = 1
				self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("\n")
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setEnabled(True)
				self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.setStyleSheet('background-color: white;')
				if self.ventanaEditarDatos.widget.widget2.claveActual == 1 and self.ventanaEditarDatos.widget.widget2.claveNueva == 1 and self.ventanaEditarDatos.widget.widget2.claveNueva2 == 1:
					verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar1')
					self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(True)
				else:
					verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar0')
					self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)

	def ventanaEditarDatosVerificacionClaveNueva2(self):
		if len(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.text()) == 0:
			self.ventanaEditarDatos.widget.widget2.claveNueva2 = 0
			self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("Confirma la contraseña.")
			verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar0')
			self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
		else:
			if len(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.text()) < 6:
				self.ventanaEditarDatos.widget.widget2.claveNueva2 = 0
				self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("La contraseña debe ser mínimo de 6 caracteres.")
				self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
				verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar0')
			elif re.match(r'^[^:]*$', self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.text()) is None:
				self.ventanaEditarDatos.widget.widget2.claveNueva2 = 0
				self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("Caracter dos puntos ':' no admitido\nen la contraseña.")
				self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
				verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar0')
			else:
				if self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.text() != self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.text():
					self.ventanaEditarDatos.widget.widget2.claveNueva2 = 0
					self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("Las contraseñas no coinciden.")
					self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)
					verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar0')
				else:
					self.ventanaEditarDatos.widget.widget2.claveNueva2 = 1
					self.ventanaEditarDatos.widget.widget2.labelClaveError2.setText("\n")
					if self.ventanaEditarDatos.widget.widget2.claveActual == 1 and self.ventanaEditarDatos.widget.widget2.claveNueva == 1 and self.ventanaEditarDatos.widget.widget2.claveNueva2 == 1:
						verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar1')
						self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(True)
					else:
						verificacion1(self.ventanaEditarDatos.widget.widget2, 'EditarClave Aceptar0')
						self.ventanaEditarDatos.widget.widget2.botonAceptarClaveNueva.setEnabled(False)

	def keyPressEventLineEditClave(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget2.lineEditClave.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClave, event)
		elif event.key() == 88 or event.key() == 67:
			if self.ventanaEditarDatos.widget.widget2.lineEditClave.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClave, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClave, event)

	def keyReleaseEventLineEditClave(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget2.lineEditClave.indicador = 0

	def keyPressEventLineEditClaveNueva(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva, event)
		elif event.key() == 88 or event.key() == 67:
			if self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva, event)

	def keyReleaseEventLineEditClaveNueva(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva.indicador = 0

	def keyPressEventLineEditClaveNueva2(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2, event)
		elif event.key() == 88 or event.key() == 67:
			if self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.indicador == 1:
				event.ignore()
			else:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2, event)
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2, event)

	def keyReleaseEventLineEditClaveNueva2(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget2.lineEditClaveNueva2.indicador = 0

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

	def eventoscalendario(self, event):
		event.ignore()

	def pressKeyQDateEdit(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.indicador = 1
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.lineEdit(), event)
		elif event.key() == 65 or event.key() == 67:
			if self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.indicador == 1:
				QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.lineEdit(), event)
			else:
				event.ignore()
		else:
			event.ignore()

	def releaseKeyQDateEdit(self, event):
		if event.key() == 16777249:
			self.ventanaEditarDatos.widget.widget.dateEditFechaNacimiento.indicador = 0

	def ventanaEditarDatosVerificacionNombre(self):
		if len(self.ventanaEditarDatos.widget.widget.lineEditNombre.text()) == 0:
			self.ventanaEditarDatos.widget.widget.labelNombreError.setText("\n")
			verificacion1(self.ventanaEditarDatos.widget.widget, 'EditarNombre Aceptar0')
			verificacion1(self.ventanaEditarDatos.widget.widget, 'EditarNombre Cancelar0')
			self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setEnabled(False)
			self.ventanaEditarDatos.widget.widget.botonCancelarNombre.setEnabled(False)
		else:
			verificacion1(self.ventanaEditarDatos.widget.widget, 'EditarNombre Cancelar1')
			self.ventanaEditarDatos.widget.widget.botonCancelarNombre.setEnabled(True)
			if len(self.ventanaEditarDatos.widget.widget.lineEditNombre.text()) < 5:
				verificacion1(self.ventanaEditarDatos.widget.widget, 'EditarNombre Aceptar0')
				self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setEnabled(False)
				self.ventanaEditarDatos.widget.widget.labelNombreError.setText("Escribe tu nombre completo.")
			elif re.match(r'^[a-zA-ZÀ-ÿ\u00f1\u00d1][a-zA-Z À-ÿ\u00f1\u00d1]*$', self.ventanaEditarDatos.widget.widget.lineEditNombre.text()) is None:
				verificacion1(self.ventanaEditarDatos.widget.widget, 'EditarNombre Aceptar0')
				self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setEnabled(False)
				self.ventanaEditarDatos.widget.widget.labelNombreError.setText("El nombre no puede contener números\no caracteres especiales.")
				self.ventanaEditarDatos.widget.widget.labelNombreError.setWordWrap(True)
			else:
				self.ventanaEditarDatos.widget.widget.botonAceptarNombre.setEnabled(True)
				verificacion1(self.ventanaEditarDatos.widget.widget, 'EditarNombre Aceptar1')
				self.ventanaEditarDatos.widget.widget.labelNombreError.setText("\n")

	def ventanaEditarDatosVerificacionNombreEvento(self, event):
		if event.key() == 16777220:
			self.ventanaEditarDatos.widget.widget.botonAceptarNombre.click()
		else:
			QtWidgets.QLineEdit.keyPressEvent(self.ventanaEditarDatos.widget.widget.lineEditNombre, event)
	#-------------------------------------------------------------------------------------------------------------------------------
	#Tab Mensajes Privados
	def construirTabMensaje(self):
		self.tabMensaje = QtWidgets.QWidget()
		self.tabMensaje.setObjectName("tabMensaje")
		self.tabMensaje.setStyleSheet("""
			#tabMensaje {
				margin-top: 6px;
				background-color: rgba(35, 0, 119, 90);
				border-radius: 20px;
			}
		""")
		self.tabWidget.insertTab(1, self.tabMensaje, 'Mensajes Privados')
		self.tabWidget.setCurrentIndex(1)

	def nada(self):
		print("empaNada")

	def nada2(self,u):
		print("Arecripada",u)

def main():
	app = QtWidgets.QApplication(sys.argv)
	QtGui.QFontDatabase.addApplicationFont('Ubuntu.ttf')
	QtGui.QFontDatabase.addApplicationFont('segoeuil.ttf')

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	a = Ventana_Principal()
	QtGui.QFontDatabase.addApplicationFont('Ubuntu.ttf')
	QtGui.QFontDatabase.addApplicationFont('segoeuil.ttf')
	usuario = {'nickname':'Nectar97','nombre':'Luis David Pérez Bermúdez','sexo':'Masculino','fechaNacimiento':'05/07/1997','edad':21}
	sala = {'nombre':'Default'}
	usuariosSala = {'usuario1':{'nickname':'reydali', 'nombre':'Luis David', 'sexo':'Masculino'},
					'usuario2':{'nickname':'nectar97', 'nombre':'Hector Francisco', 'sexo':'Masculino'},
					'usuario3':{'nickname':'laburra96', 'nombre':'Laura YANETH', 'sexo':'Femenino'}}
	a.constructor(usuario,sala,usuariosSala,None,None)
	#a.construirTabSala({'Nombre':'Dede'})
	a.setIndexTab(0)
	a.show()

	#b = ClienteGUI.Ventana_Login()
	#b.show()
	sys.exit(app.exec_())
