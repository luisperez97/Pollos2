import socket
import threading
import time
import json
import pickle

from ModeloServidor import *
import ModeloServidor as modelo
from ConfigBaseServidor import sessionservidor

#import sys
#sys.path.append('..')
#import Cliente.SocketCliente

class enviarMensajePrivado(threading.Thread):
	def __init__(self, emisor, receptor, clientes, server, folder):
		super(enviarMensajePrivado, self).__init__()
		self.emisor = emisor
		self.receptor = receptor
		self.clientes = clientes

	def run(self):
		mensaje = self.emisor.mensaje
		name = self.emisor.name
		receptor = False
		for cli in self.clientes:
			if cli.name == self.receptor:
				# Guardar los mensajes privados
				# modelo.guardarMensajePrivado('mensaje')
				cli.enviar('private :'+name+': '+mensaje)
				self.emisor.enviar('Se ha enviado el mensaje a '+cli.name)
				receptor = True
				break
		if not receptor:
			self.emisor.enviar('No se ha encontrado el usuario '+self.receptor)

class enviarMensajeSala(threading.Thread):
	def __init__(self, cliente, clientes, excluirCliente, server, folder):
		super(enviarMensajeSala, self).__init__()
		self.cliente = cliente
		self.clientes = clientes
		self.excluirCliente = excluirCliente
		self.server = server
		self.folder = folder

	def run(self):
		sala = self.cliente.sala
		if self.server:
			if type(self.cliente.mensaje).__name__ == 'bytes':
				mensaje = 'sv:'.encode() + self.cliente.mensaje
			else:
				mensaje = 'sv:' + self.cliente.mensaje
		else:
			mensaje = self.cliente.mensaje[:-1]
		name = self.cliente.name
		for cli in self.clientes:
			if cli.sala == sala:
				# Guardar los mensajes de la sala
				# modelo.guardarMensajeSala('mensaje')
				if not (cli.name == name and self.excluirCliente):
					if self.folder:
						listmensaje = mensaje.split(':')
						mensaje = ':'.join(listmensaje[:4]) + ':' + cli.name
						print('\n\n', mensaje, '\n\n')
					if self.excluirCliente:
						cli.enviar(mensaje)
					else:
						if self.server:
							cli.enviar(mensaje)
						else:
							cli.enviar(name+': '+mensaje)

class guardarArchivo(threading.Thread):
	def __init__(self, cliente):
		super(guardarArchivo, self).__init__()
		self.owner = cliente
		self.ext = None
		self.size = 0
		self.file = None
		self.finished = False
		self.nbuffer = 0

	def update(self, info):
		info = info.split('uwu'.encode())
		self.file.write(info)
		self.nbuffer += 1
		#print('voy en : ', self.nbuffer)
		if self.nbuffer == self.size:
			self.file.close()
			self.finished = True

	def run(self):
		datos = self.cliente.mensaje.split(':')
		self.ext = datos[1]
		self.size = datos[2]
		path = './archivosCompartidos'
		if not os.path.exists(path):
			os.makedirs(path)
		self.name = path + '/' + self.name[-1] +'.'+ self.ext
		self.file = open(self.name, 'wb')

class Observer(threading.Thread):
	def __init__(self):
		super(Observer, self).__init__()
		self.clientes = []
		#self.activos = []
		self.desconectados = []
		self.salir = False
		self.listFiles = []

	def add_client(self, client):
		self.clientes.append(client)

	def desconectar(self, cli):
		self.clientes.remove(cli)
		self.desconectados.append(cli)

	def crearArchivo(self, cliente):
		newFile = guardarArchivo(cliente)
		newFile.start()
		listFiles.append(newFile)
		cliente.archivoPosition = len(listFiles)-1
		newFile.join()
		'''
		cliente.mensaje = 'sv:fileReceived:'+newFile.name.split('/')[2]
		self.notificar(cliente)
		'''

	def observar(self):
		for cli in self.clientes:
			if cli.mensaje != '':
				if cli.mensaje[0] == '*' and not cli.mensaje[-1] == '*':
					if cli.mensaje[1:3] == 'DC':
						# El cliente envió los datos para iniciar sesión (nickname, password)
						datos = cli.mensaje.split(':')
						busquedaNickname = sessionservidor.query(Usuarios).filter_by(Nickname=str(datos[1])).first()
						if busquedaNickname is None:
							cli.enviar('error'+'El usuario no existe.')
						else:
							if not busquedaNickname.check_password(datos[2]):
								cli.enviar('error'+'Contraseña incorrecta.')
							else:
								cli.user = busquedaNickname
								datosCliente = cli.updateInfo()
								datosSala = sessionservidor.query(Salas).filter_by(Nombre=cli.info['salaActual']).first().toDict()
								mensaje = json.dumps(datosCliente) + '<>' + json.dumps(datosSala)
								print(mensaje)
								cli.enviar(mensaje)
					elif cli.mensaje[1:3] == 'DR':
						# El cliente envió los datos para registrarse
						datos = cli.mensaje.split(':')
						busquedaNickname = sessionservidor.query(Usuarios).filter_by(Nickname=str(datos[2])).first()
						if busquedaNickname is None:
							usuario = modelo.Usuarios(Nickname=datos[2], Nombre=datos[1], Estado=False, Sala_Actual='Default', Sexo=datos[5], Fecha_Nacimiento=datos[6])
							usuario.set_password(datos[3])
							usuario.set_respuesta(datos[4])
							usuario.set_edad(datos[6])
							sessionservidor.add(usuario)
							sessionservidor.commit()
							cli.enviar("Usuario registrado con éxito.")
						else:
							cli.enviar('error'+'Nickname no disponible.')
					elif cli.mensaje[1:3] == 'RC':
						# El cliente envió los datos para recuperar contraseña
						datos = cli.mensaje.split(':')
						busquedaUsuario = sessionservidor.query(Usuarios).filter_by(Nickname=datos[1]).first()
						if busquedaUsuario is None:
							cli.enviar('error'+'El usuario no existe.')
						else:
							if not busquedaUsuario.check_respuesta(datos[2]):
								cli.enviar('error'+'Respuesta secreta incorrecta.')
							else:
								cli.user = busquedaUsuario
								cli.enviar('bien')
					elif cli.mensaje[1:3] == 'NC':
						# El cliente envió los datos para cambiar contraseña
						datos = cli.mensaje.split(':')
						cli.user.set_password(datos[1])
						sessionservidor.commit()
						cli.enviar("Contraseña modificada con éxito.")
					elif cli.mensaje[1:3] == 'IS':
						cli.mensaje = 'inicio sesion '+cli.name
						self.notificar(cli, True)
					elif cli.mensaje[1:3] == 'EN':
						datos = cli.mensaje.split(':')
						cli.mensaje = 'fileInfo:' + datos[1] + ':' + datos[2]
						#Guardar en el Servidor
						self.crearArchivo(cli)
						#self.notificar(cli, True, server=True, folder=True)
					elif cli.mensaje[1:5] == 'PART':
						#cli.mensaje = 'rf:'.encode() + cli.infoBytes
						archivoRecibiendo = self.listFiles[cli.archivoPosition]
						archivoRecibiendo.update(cli.infoBytes)
						if archivoRecibiendo.finished:
							cli.mensaje = 'sv:flieReceived:'+archivoRecibiendo.name
							self.notificar(cliente)
						#print(len(cli.mensaje))
						#self.notificar(cli, True, server=True)

				elif cli.mensaje[0] == '#' and cli.mensaje[-1] == '*':
					if cli.mensaje[1:4] == 'cR ':
						# Pedir al modelo que cree la sala con la información del cliente
						# if not modelo.buscarSala('nombre sala') then
						# 	 modelo.crearSala('nombre sala','datos del cliente')
						cli.sala = cli.mensaje[4:-1]
						cli.enviar('Ahora estás en la sala '+cli.sala+', Bienvenido')
					elif cli.mensaje[1:4] == 'gR ':
						# Verificar que la sala existe
						# if modelo.buscarSala('nombre sala') then
						# 	 mover al cliente a la sala por defecto
						# 	 modelo.moverCliente('nombre sala')
						cli.sala = cli.mensaje[4:-1]
						cli.enviar('Ahora estás en la sala '+cli.sala+', Bienvenido')
						cli.mensaje = 'El usuario '+cli.name+' se ha unido a la sala'
						self.notificar(cli,True)

					elif cli.mensaje[1:-1] == 'eR':
						# Mover al cliente a la sala por defecto
						# modelo.moverCliente('default')
						cli.mensaje = 'El usuario '+cli.name+' ha abandonado la sala'
						self.notificar(cli,True)
						time.sleep(0.1)
						cli.sala = 'Default'
						cli.enviar('Ahora estás en la sala '+cli.sala+', Bienvenido')
						cli.mensaje = 'El usuario '+cli.name+' se ha unido a la sala'
						self.notificar(cli,True)

					elif cli.mensaje[1:-1] == 'exit':
						# Eliminar las salas y demás cosas creadas por el cliente
						# modelo.desconectarCliente('nombre cliente')
						cli.mensaje = 'El usuario '+cli.name+' ha abandonado la sala'
						self.notificar(cli,True)
						cli.fin = True
						#cli.cerrarConexion()
					elif cli.mensaje[1:-1] == 'lR':
						# Mostrar al cliente todas las salas disponibles
						# y la cantidad de clientes en cada una
						# modelo.listarSalas() -> devuelve la lista de salas y numero de clientes
						print('Aún no disponible por culpa de Bermeja')
					elif cli.mensaje[1:4] == 'dR ':
						sala = cli.mensaje[4:-1]
						# Verificar que la sala existe
						# if modelo.buscarSala('nombre sala') then
						#	 si el cliente está en la sala que va a eliminar
						# 	 se debe mover al cliente a la sala por defecto
						if cli.sala == sala:
							cli.sala = 'default'
							cli.enviar('Ahora estás en la sala '+cli.sala+', Bienvenido')
							cli.mensaje = 'El usuario '+cli.name+' se ha unido a la sala'
							self.notificar(cli,True)
						#	 	 modelo.moverCliente('default')
						#	 se deben de mover todos los clientes de la sala, a la por defecto
						#	 modelo.eliminarSala()
						cli.enviar('Se ha eliminado la sala con exito')
					elif cli.mensaje[1:-1] == 'show users':
						# Mostrar todos los clientes (¿disponibles o registrados?) en TODO el sistema
						# modelo.listarClientes() -> devuelve la lista con TODOS los clientes
						print('Aún no disponible por culpa de Bermeja')
					elif cli.mensaje[1:10] == r'\private ':
						msj = cli.mensaje[10:-1].split(':',1)
						receptor = msj[0]
						#cli.mensaje = cli.mensaje[len(receptor)+11:]
						cli.mensaje = msj[1]
						#print(receptor, msj)
						self.notificar(cli,receptor=receptor)
						# Envia el mensaje al receptor si éste existe
						# modelo.enviarMensajePrivado('from', 'to', 'message',..)
				else:
					# Envia el mensaje a todos los usuarios dentro de la sala
					# modelo.enviarMensajeSala('informacion necesaria')
					print('Mensaje : '+str(cli.mensaje))
					self.notificar(cli)
				cli.mensaje = ''
			if cli.fin:
				self.desconectar(cli)

	def notificar(self, cliente, excluirCliente = False, receptor = '', server = False, folder = False):
		if not receptor:
			enviarMensajeSala(cliente, self.clientes, excluirCliente, server, folder).start()
		else:
			enviarMensajePrivado(cliente, receptor, self.clientes, server, folder).start()

	def run(self):
		while not self.salir:
			self.observar()

class Cliente(threading.Thread):
	def __init__(self,conexion):
		super(Cliente, self).__init__()
		self.conexion = conexion
		self.mensaje = ''
		self.sala = 'Default'
		self.fin = False
		self.user = None
		self.infoBytes = None
		self.info = {}
		self.archivoPosition = 0

	def updateInfo(self):
		#devolver un diccionario
		self.info['nickname'] = self.user.Nickname
		self.info['nombre'] = self.user.Nombre
		self.info['estado'] = self.user.Estado
		self.info['sexo'] = self.user.Sexo
		self.info['salaActual'] = self.user.Sala_Actual
		self.info['fechaNacimiento'] = self.user.Fecha_Nacimiento
		self.info['edad'] = self.user.Edad
	    #self.info['clave'] = self.user.Clave
	    #self.info['respuestaSecreta'] = self.user.Respuesta_Secreta

		return self.info


	def toString(self):
		return

	def enviar(self, mensaje):
		if type(mensaje).__name__ == 'bytes':
			self.conexion.send(mensaje)
		else:
			self.conexion.send(mensaje.encode('UTF-8'))

	def cerrarConexion(self):
		#self.conexion.shutdown(socket.SHUT_WR)
		self.enviar('sv:exitAccepted')
		self.conexion.close()

	def run(self):
		print("se ha unido "+self.name)
		while not self.fin:
			newmensaje = self.conexion.recv(1024)
			#print(newmensaje)
			if newmensaje:
				newmensaje = newmensaje.split(':'.encode())
				print(newmensaje)
				if not newmensaje[-1][-1] == 42:
					if newmensaje[0][0] == 42:
						if newmensaje[0] == '*PART'.encode():
							self.mensaje = newmensaje[0].decode()
							self.infoBytes = ':'.encode().join(newmensaje[1:])
							print(self.infoBytes, len(self.infoBytes))
						else:
							self.mensaje = ':'.encode().join(newmensaje).decode()
				else:
					self.mensaje = ':'.encode().join(newmensaje).decode()
			#añadir verificación para salir
		print("ha salido "+self.name)
		self.cerrarConexion()

Mi_socket=socket.socket()
Mi_socket.bind(("192.168.1.63", 8092))
Mi_socket.listen(0)
listclientes = []
observador = Observer()
observador.start()
#print('soy Observer '+observador.name)

while True:
	conexion, addr = Mi_socket.accept()
	if conexion:
		listclientes.append(Cliente(conexion))
		listclientes[-1].start()
		observador.add_client(listclientes[-1])

observador.salir = True
Mi_socket.close()
