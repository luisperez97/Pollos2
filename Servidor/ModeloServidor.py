from sqlalchemy.ext.declarative import declarative_base

BaseServidor = declarative_base()

from datetime import date, datetime #timedelta
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, Boolean #Table String
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash


#Servidor
class Usuarios(BaseServidor):
    __tablename__ = 'usuarios'
    Nickname = Column(Text, primary_key=True)
    Nombre = Column(Text, nullable=False)
    Estado = Column(Boolean, nullable=False)
    Clave = Column(Text, nullable=False)
    Sexo = Column(Text, nullable=False)
    Respuesta_Secreta = Column(Text, nullable=False)
    Sala_Actual = Column(Text, ForeignKey('salas.Nombre'), nullable=False)
    Fecha_Nacimiento = Column(Text, nullable=False)
    Edad = Column(Integer, nullable=False)

    Sala_Relacion = relationship("Salas", backref=backref("Sala"), foreign_keys=[Sala_Actual])

    def set_edad(self, born):
        today = date.today()
        born = born.split('/')
        self.Edad= today.year - int(born[2]) - ((today.month, today.day) < (int(born[1]), int(born[0])))

    def set_password(self, password):
        self.Clave = generate_password_hash(password)

    def set_respuesta(self, respuesta):
        self.Respuesta_Secreta = generate_password_hash(respuesta)

    def check_password(self, password):
        return check_password_hash(self.Clave, password)

    def check_respuesta(self, respuesta):
        return check_password_hash(self.Respuesta_Secreta, respuesta)

    def __repr__(self):
        return '<Usuario {}>'.format(self.Nickname)

class Mensajes_Privados(BaseServidor):
    __tablename__ = 'mensajes_privados'
    id = Column(Integer, primary_key=True)
    Hora = Column(DateTime, default=datetime.now, nullable=False)
    Cuerpo = Column(Text, nullable=False)
    #Estado_id = Column(Integer, ForeignKey('estados.id'), nullable=False)
    Emisor_FK = Column(Text, ForeignKey('usuarios.Nickname'), nullable=False)
    Receptor_FK = Column(Text, ForeignKey('usuarios.Nickname'), nullable=False)
    #HELOW dsdsd

    #Relaciones-----------
    #Estados_Relacion = relationship("Estados", backref=backref("Estado"), foreign_keys=[Estado_id])
    Emisor_Relacion = relationship("Usuarios", backref=backref("Emisor"), foreign_keys=[Emisor_FK])
    Receptor_Relacion = relationship("Usuarios", backref=backref("Receptor"), foreign_keys=[Receptor_FK])
    #---------------------
    def __repr__(self):
        return '<Mensaje Privado {}>'.format(self.Cuerpo)
"""
class Estados(BaseServidor):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True)
    Descripcion = Column(Text, nullable=False)

    def __repr__(self):
        return '<Estado {}>'.format(self.Descripcion)
"""
class Salas(BaseServidor):
    __tablename__ = 'salas'
    Nombre = Column(Text, primary_key=True)
    Descripcion = Column(Text)
    Owner_FK = Column(Text, ForeignKey('usuarios.Nickname'), nullable=True)

    Owner_Relacion = relationship("Usuarios", backref=backref("Creador"), foreign_keys=[Owner_FK])

    def toDict(self):
        info = {}
        info['nombre'] = self.Nombre
        info['descripcion'] = self.Descripcion
        info['owner'] = self.Owner_FK
        return info

    def __repr__(self):
        return '<Sala {}>'.format(self.Nombre)
