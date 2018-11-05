#from Cliente.ModeloCliente import *
#from Cliente.ConfigBaseCliente import sessioncliente
from ModeloCliente import *
from ConfigBaseCliente import sessioncliente

estado1 = Estados(Descripcion='Mensaje no llegó al servidor.')
sessioncliente.add(estado1)

estado2 = Estados(Descripcion='Mensaje llegó al servidor.')
sessioncliente.add(estado2)

estado3 = Estados(Descripcion='Mensaje no llegó al cliente.')
sessioncliente.add(estado3)

estado4 = Estados(Descripcion='Mensaje llegó al cliente.')
sessioncliente.add(estado4)

sessioncliente.commit()