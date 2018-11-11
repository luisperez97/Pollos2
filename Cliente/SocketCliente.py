import socket
import threading
import os
import time
import datetime
import math
import json
import pickle

#registroUsuario = True

#import Cliente.LlenarBaseCliente
#import Cliente.Interfaz.Cliente

import LlenarBaseCliente
import Interfaz.Login
import Interfaz.Chat


global rcv, snd, sckt, chat, ventanaChat, ventanaLogin
sckt = socket.socket()
sckt.connect(("192.168.1.63", 8092))


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
		print('finalizo el chat')
		#exit_handler()

class Archivo():
	def __init__(self, ext, packages, name):
		self.packages = packages
		self.ext = ext
		self.file = None
		self.name = ''
		self.nbuffer = 0
		self.name = name
		self.iniciarBuffer()


	def iniciarBuffer(self, folder = r'./archivosCompartidos'):
		newpath = folder + '/' + self.name
		print(newpath)
		if not os.path.exists(newpath):
			os.makedirs(newpath)
		self.name = newpath + '/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.'+self.ext
		self.file = open(self.name, 'wb')
		print('me he creado', newpath)

	def actualizarInfo(self, info):
		self.file.write(info)
		self.nbuffer += 1
		print('voy en : ', self.nbuffer)
		if self.nbuffer == int(self.packages):
			self.file.close()
			print('Ya tengo todos los paquetes, soy : ', self.name)
			print('\n\n##############################################################################\n\n')

class Receive(threading.Thread):
	def __init__(self, skt):
		super(Receive, self).__init__()
		self.skt = skt
		self.archi = None

	def recibirArchivo(self, message):
		message = message.split('uwu'.encode())
		#byte:232323:png:3
		print('archi: ',self.archi.packages, self.archi.nbuffer)
		print('mes: ', message)

		if self.archi:
			if self.archi.packages == message[1].decode() and self.archi.ext == message[2].decode() and self.archi.nbuffer == int(message[3].decode()):
				self.archi.actualizarInfo(message[0])

	def run(self):
		message = ''
		while True:
			message = self.skt.recv(1024)
			#serv:typeOfService:[info]
			if message:
				print('Ha llegado un mensaje: \t')
				data = message.split(':'.encode(), 2)
				print('\t',data)
				owner = data[0]
				if owner.decode() == 'sv':
					typeOfService = data[1].decode()
					if typeOfService == 'rf':
						self.recibirArchivo(data[2])
					elif typeOfService == 'fileInfo':
						message = data[2].decode().split(':')
						self.archi = Archivo(message[0],message[1],message[2])
						#print('instancia de archi')
					elif typeOfService == 'fileReceived':
						message = data[2].decode()
						if ventanaChat:
							#mostrar el link de descarga en la vista de chat
						 	pass
					elif typeOfService == 'exitAccepted':
						break
				else:
					message =':'.encode().join(data).decode()
					print(message)

		print('deje de recibir')

class Send(threading.Thread):
	def __init__(self, skt):
		super(Send, self).__init__()
		self.skt = skt

	def run(self):
		while True:
			masaje = input()
			if masaje == 'okis':
				# se añaden ':' para hacer split
				masaje += ':**'
			else:
				masaje += ':*'
			self.skt.send(masaje.encode('UTF-8'))
			#enviar la informacion del archivo adjunto
			if masaje == '#exit*':
				break
		print('deje de enviar')


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
		ventana.ventana_clave_nueva(usuario)
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
	if error[:5] != 'error': #Si no hay error llegan los datos en el error
		datos = error.split('<>')
		print(datos)
		user = json.loads(datos[0])
		room = json.loads(datos[1])
		ventana.hide()
		ventana.deleteLater()
		sckt.send('*IS'.encode('UTF-8'))
		#Interfaz.Chat.main()
		ventanaChat = Interfaz.Chat.Ventana_Principal()
		ventanaChat.constructor(user,room,None,None,None) #--Enviar Parámetros. (usuario-->dict, sala-->dict, usuariosSala, usuariosMensajesPrivados, mensajesPrivados):
		ventanaChat.setIndexTab(0)
		ventanaChat.show()
		#b.show()
		chat = Chat()
		chat.start()
	else:
		ventana.labelError.setText(error[5:])
		ventana.labelError.show()

def controladorRegistro(ventana):

	global sckt, chat

	nombreCompleto = ventana.ventanaRegistro.widget.widget.lineEditNombre.text()
	nickname = ventana.ventanaRegistro.widget.widget.lineEditNickname.text()
	password = ventana.ventanaRegistro.widget.widget2.lineEditClave.text()
	respuestaSecreta = ventana.ventanaRegistro.widget.widget2.lineEditRespuesta.text()
	fecha = ventana.ventanaRegistro.widget.widget.dateEditFechaNacimiento.date().toString('dd/MM/yyyy')
	sexo = None
	if ventana.ventanaRegistro.widget.widget.radioButtonMasculino.isChecked() == True:
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
		ventana.ventanaRegistro.widget.widget.labelErrorNickname.setText(error[5:])
		ventana.ventanaRegistro.widget.widget.labelErrorNickname.show()

def controladorNuevaClave(ventana):

	global sckt

	clave = ventana.claveNuevaVentana.lineEditClave.text()
	mensaje = '*'+'NC'+':'+clave
	sckt.send(mensaje.encode('UTF-8'))
	ventana.claveNuevaVentana.hide()
	ventana.claveNuevaVentana.deleteLater()
	ventana.alerta('Contraseña modificada con éxito.')
	#error = sckt.recv(1024).decode('UTF-8')

def controladorEnviarArchivos(archivo):
	global sckt

	#enviar byte por byte con el tamaño total, el tipo de archivo, y que parte se envía
	#byte:232323:png:3
	print('\n\n##############################################################################\n\n')
	archi = open(archivo,'rb')
	info = archi.read()
	size = len(info)
	tipo = archivo.split('.')[-1]
	total = 6 + 5 + len(tipo) + len('uwu'*3) + 5 #solo se pueden enviar archivos de máximo 100mb
	step = 1024 - total
	nsends = math.ceil(size/step)
	#sckt.send('*PART:'.encode() + info)
	mensajeArchivo = '*EN:'+tipo+':'+str(nsends)
	#print(mensajeArchivo)
	print('Tengo el mensaje listo para enviar')
	sckt.send(mensajeArchivo.encode())
	print('Se ha enviado el mensaje de informacion')
	time.sleep(0.5)
	print('Hey :', nsends, step)
	for i in range(nsends):
		encd = '*PART:'.encode() + info[i*step:(i+1)*step] + 'uwu'.encode() + str(nsends).encode() + 'uwu'.encode() + tipo.encode() + 'uwu'.encode() + str(i).encode()
		#print(encd.split('uwu'.encode()))
		time.sleep(0)
		sckt.send(encd)
	print('Se han enviado todas las partes')
	print('\n\n##############################################################################\n\n')
	archi.close()
	print('se ha cerrado el archivo')

def controladorRecibirArchivos(archivo):
	pass

def solicitarDatosUsuario(nombre):
	pass

'''
def ensayo():
	while True:
		data = sckt.recv(1024).decode('UTF-8')
		print('mensaje:',data)
'''

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
