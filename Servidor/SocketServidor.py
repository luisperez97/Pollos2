import socket
import threading
import time

from ModeloServidor import *
from ConfigBaseServidor import sessionservidor
#import sys
#sys.path.append('..')
#import Cliente.SocketCliente

class enviarMensajePrivado(threading.Thread):
	def __init__(self, emisor, receptor, clientes):
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
	def __init__(self, cliente, clientes, excluirCliente):
		super(enviarMensajeSala, self).__init__()
		self.cliente = cliente
		self.clientes = clientes
		self.excluirCliente = excluirCliente

	def run(self):
		sala = self.cliente.sala
		mensaje = self.cliente.mensaje[:-1]
		name = self.cliente.name
		for cli in self.clientes:
			if cli.sala == sala:
				# Guardar los mensajes de la sala
				# modelo.guardarMensajeSala('mensaje')
				if not (cli.name == name and self.excluirCliente):
					if self.excluirCliente:
						cli.enviar(mensaje)
					else:
						cli.enviar(name+': '+mensaje)

class Observer(threading.Thread):
	def __init__(self):
		super(Observer, self).__init__()
		self.clientes = []
		#self.activos = []
		self.desconectados = []
		self.salir = False

	def add_client(self, client):
		self.clientes.append(client)

	def desconectar(self, cli):
		self.clientes.remove(cli)
		self.desconectados.append(cli)

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
								cli.updateInfo()
								cli.enviar('bien')
					elif cli.mensaje[1:3] == 'DR':
						# El cliente envió los datos para registrarse
						datos = cli.mensaje.split(':')
						busquedaNickname = sessionservidor.query(Usuarios).filter_by(Nickname=str(datos[2])).first()
						if busquedaNickname is None:							
							usuario = Usuarios(Nickname=datos[2], Nombre=datos[1], Estado=False, Sala_Actual='Default', Sexo=datos[5], Fecha_Nacimiento=datos[6])
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
						cli.enviartodos('Redya puta')

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
						cli.sala = 'default'
						cli.enviar('Ahora estás en la sala '+cli.sala+', Bienvenido')
						cli.mensaje = 'El usuario '+cli.name+' se ha unido a la sala'
						self.notificar(cli,True)

					elif cli.mensaje[1:-1] == 'exit':
						# Eliminar las salas y demás cosas creadas por el cliente
						# modelo.desconectarCliente('nombre cliente')
						cli.mensaje = 'El usuario '+cli.name+' ha abandonado la sala'
						self.notificar(cli,True)
						cli.enviar('okis')
						cli.cerrarConexion()
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
					self.notificar(cli)
				cli.mensaje = ''
			if cli.fin:
				self.desconectar(cli)

	def notificar(self, cliente, excluirCliente = False, receptor = ''):
		if not receptor:
			enviarMensajeSala(cliente, self.clientes, excluirCliente).start()
		else:
			enviarMensajePrivado(cliente, receptor, self.clientes).start()

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
	
	def updateInfo(self):
		self.name = self.user.Nickname
		
	def enviar(self, mensaje):
		self.conexion.send(mensaje.encode('UTF-8'))
	
	def enviartodos(self, mensaje):
		self.conexion.sendall(mensaje.encode('UTF-8'))

	def cerrarConexion(self):
		#self.conexion.shutdown(socket.SHUT_WR)
		self.conexion.close()

	def run(self):
		print("se ha unido "+self.name)
		while not self.fin:
			self.mensaje = self.conexion.recv(1024).decode('UTF-8')
			if self.mensaje[1:-1] == 'exit':
				self.fin = True
		print("ha salido "+self.name)

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