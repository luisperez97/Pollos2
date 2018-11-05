import socket  
import threading
import os
import time

#registroUsuario = True

#import Cliente.LlenarBaseCliente
#import Cliente.Interfaz.Cliente

import LlenarBaseCliente
import Interfaz.ClienteGUI

class Receive(threading.Thread):
	def __init__(self, skt):
		super(Receive, self).__init__()
		self.skt = skt

	def run(self):
		message = ''
		while True:
			if message != '':
				print(message)
			if message == 'okis':
				break
			message = self.skt.recv(1024).decode('UTF-8')

class Send(threading.Thread):
	def __init__(self, skt):
		super(Send, self).__init__()
		self.skt = skt

	def run(self):
		while True:
			masaje = input()
			if masaje == 'okis':
				masaje += '**'
			else:
				masaje += '*'
			if masaje == '#exit*':
				break
			self.skt.send(masaje.encode('UTF-8'))

			
				
def verificarDatosVentanaOlvidoClave(ventana):

	global sckt

	usuario = ventana.olvidoVentana.lineEditUsuario.text()
	respuestaSecreta = ventana.olvidoVentana.lineEditRespuesta.text()
	mensaje = '*' + 'RC'+':'+usuario+':'+respuestaSecreta
	sckt.send(mensaje.encode('UTF-8'))
	error= sckt.recv(1024).decode('UTF-8')
	if error[:5] != 'error':
		ventana.olvidoVentana.hide()
		ventana.olvidoVentana.deleteLater()
		ventana.ventana_clave_nueva()
	else:
		ventana.olvidoVentana.labelError.setText(error[5:])
		ventana.olvidoVentana.labelError.show()
	
	
				
def controladorInicioSesion(ventana):

	global sckt, chat
	
	nickname = ventana.lineEditUsuario.text()
	password = ventana.lineEditPassword.text()
	
	mensaje = '*'+'DC'+':'+nickname+':'+password
	sckt.send(mensaje.encode('UTF-8'))
	error = sckt.recv(1024).decode('UTF-8')
	if error[:5] != 'error':
		ventana.hide()
		ventana.deleteLater()
		sckt.send('*IS'.encode('UTF-8'))
		b = Interfaz.ClienteGUI.NewDialog()
		b.show()
		chat = Chat()
		chat.start()
	else:
		ventana.labelError.setText(error[5:])
		ventana.labelError.show()

def controladorRegistro(ventana):

	global sckt, chat

	nombreCompleto = ventana.ventanaRegistro.lineEditNombre.text()
	nickname = ventana.ventanaRegistro.lineEditNickname.text()
	password = ventana.ventanaRegistro.lineEditClave.text()
	respuestaSecreta = ventana.ventanaRegistro.lineEditRespuesta.text()
	fecha = ventana.ventanaRegistro.dateEditFechaNacimiento.date().toString('dd/MM/yyyy')
	sexo = None
	if ventana.ventanaRegistro.radioButtonMasculino.isChecked() == True:
		sexo ='Masculino'
	else:
		sexo='Femenino'
	mensaje = '*'+'DR'+':'+nombreCompleto+':'+nickname+':'+password+':'+respuestaSecreta+':'+sexo+':'+fecha
	sckt.send(mensaje.encode('UTF-8'))
	error = sckt.recv(1024).decode('UTF-8')
	if error[:5] != 'error':
		ventana.ventanaRegistro.hide()
		ventana.ventanaRegistro.deleteLater()
		ventana.alerta('Registro exitoso.')
	else:
		ventana.ventanaRegistro.labelError.setText(error[5:])
		ventana.ventanaRegistro.labelError.show()

def controladorNuevaClave(ventana):

	global sckt

	clave = ventana.claveNuevaVentana.lineEditClave.text()
	mensaje = '*'+'NC'+':'+clave
	sckt.send(mensaje.encode('UTF-8'))
	ventana.claveNuevaVentana.hide()
	ventana.claveNuevaVentana.deleteLater()
	ventana.alerta('Contraseña modificada con éxito.')
	#error = sckt.recv(1024).decode('UTF-8')



global rcv, snd, sckt, chat
sckt = socket.socket()
sckt.connect(("192.168.1.63", 8092))

def ensayo():
	while True:
		data = sckt.recv(1024).decode('UTF-8')
		print('mensaje:',data)

def exit_handler():
	if os.path.exists("../cliente.db"):
		os.remove("../cliente.db")
	else:
		print("No existe la base de datos")

	global sckt

	mensaje = '#exit*'
	sckt.send(mensaje.encode('UTF-8'))
	time.sleep(1)
	sckt.shutdown(socket.SHUT_RDWR)
	sckt.close()
	print("Me cerré")

class Chat(threading.Thread):
	def __init__(self):
		super(Chat, self).__init__()
		
		self.rcv = Receive(sckt)
		self.snd = Send(sckt)
	
	def run(self):
		self.rcv.start()
		self.snd.start()
		self.rcv.join()
		self.snd.join()
		exit_handler()
		
	
if __name__ == "__main__":
	Interfaz.ClienteGUI.main()