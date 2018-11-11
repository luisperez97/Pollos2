from ModeloServidor import Salas
from ConfigBaseServidor import sessionservidor
"""
estado1 = Estados(Descripcion='Mensaje no llegó al servidor.')
sessionservidor.add(estado1)

estado2 = Estados(Descripcion='Mensaje llegó al servidor.')
sessionservidor.add(estado2)

estado3 = Estados(Descripcion='Mensaje no llegó al cliente.')
sessionservidor.add(estado3)

estado4 = Estados(Descripcion='Mensaje llegó al cliente.')
sessionservidor.add(estado4)"""

sala_default = Salas(Nombre='Default', Descripcion='Sala por defecto.',)
sessionservidor.add(sala_default)

sessionservidor.commit()
