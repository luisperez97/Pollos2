from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from Cliente.ModeloCliente import BaseCliente
from ModeloCliente import BaseCliente

enginecliente = create_engine('sqlite:///../cliente.db')
BaseCliente.metadata.create_all(enginecliente, checkfirst=True)
SessionCliente= sessionmaker(bind=enginecliente)
sessioncliente = SessionCliente()