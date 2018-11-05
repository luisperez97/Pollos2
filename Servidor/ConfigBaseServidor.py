from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ModeloServidor import BaseServidor


#Servidor
engineservidor = create_engine('sqlite:///servidor.db')
#engineservidor = create_engine('postgresql+psycopg2://postgres:123@localhost/Pollos')
BaseServidor.metadata.create_all(engineservidor, checkfirst=True)
SessionServidor= sessionmaker(bind=engineservidor)
sessionservidor = SessionServidor()
