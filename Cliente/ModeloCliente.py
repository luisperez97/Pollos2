from sqlalchemy.ext.declarative import declarative_base

BaseCliente = declarative_base()

from datetime import datetime #timedelta
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, Boolean #Table String
from sqlalchemy.orm import relationship, backref

#Cliente
class Mensajes(BaseCliente):
    __tablename__ = 'mensajes'
    id = Column(Integer, primary_key=True)
    Hora = Column(DateTime, default=datetime.utcnow, nullable=False)
    Cuerpo = Column(Text, nullable=False)
    Estado_id = Column(Integer, ForeignKey('estados.id'), nullable=False)
    Emisor_FK = Column(Text, nullable=False)

    #Relaciones-----------
    Estados_Relacion = relationship("Estados", backref=backref("Estado"), foreign_keys=[Estado_id])
    #---------------------
    def __repr__(self):
        return '<Mensaje Privado {}>'.format(self.Cuerpo)

class Estados(BaseCliente):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True)
    Descripcion = Column(Text, nullable=False)

    def __repr__(self):
        return "<Estado {}>".format(self.Descripcion)