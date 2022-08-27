#Liberias
from random import *

"""
==========Acciones==========
"""

def ataque(atk, hp):
    nhp = hp - atk
    return nhp

def curar(hp):
    nhp = hp + randrange(5,20)
    return nhp

"""
==========Stats jugador==========
"""

HPJugador = 100
AtkJugador = 10


"""
==========Stats boss==========
"""

HPBoss = 100
AtkBoss = 10

"""
==========Pelea==========
"""

while HPBoss > 0:
    accion = input("Ataque = A o Curar = C ")
    if accion == "A" or accion == "a":
        HPBoss = ataque(AtkJugador, HPBoss)
    elif accion == "C" or accion == "c":
        HPJugador = curar(HPJugador)
    else:
        print("Elige una acción válida")
    HPJugador = HPJugador - randrange(1,20)
    print(" HP Jugador: ", HPJugador, "\n HP Boss: ", HPBoss)

print("Mataste al boss")
        
        
    

    
    

