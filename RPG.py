#liberias
from random import *

global hp
global atk
global mana
global curacion
global pociones

"""
==========Acciones==========
"""

def ataque(atk, hp):
    nhp = hp - atk
    return nhp

def curar(hp, poder_curacion):
        nhp = hp + randrange(5,20) * poder_curacion
        return nhp

            
"""
==========Stats clases==========
"""

#Caballero

HPCaballero = 100
AtkCaballero = 10
ManaCaballero = 50
CuracionCaballero = 1
PocionesCaballero = 1

#Alquimista

HPAlqui = 60
AtkAlqui = 5
ManaAlqui = 100
CuracionAlqui = 1.5
PocionesAlqui = 5

#Tanque

HPTanque = 150
AtkTanque = 15
ManaTanque = 10
CuracionTanque = 0.5
PocionesTanque = 0

#Curandero

HPCurandero = 75
AtkCurandero = 7
ManaCurandero = 125
CuracionCurandero = 2
PocionesCurandero = 3

#Random

HPRandom = randrange(20, 200, 10)
AtkRandom = randrange(2, 20)
ManaRandom = randrange(2, 200, 10)
CuracionRandom = randrange(1,3)
PocionesRandom = randrange(0,7)

"""
==========Elegir clase==========
"""

print('''
Elige tu clase \n
\n
Caballero (C):\n
HP = 100\n
Atk = 10\n
Mana = 50\n
Pociones = 1\n
\n
Alquimista (A):\n
HP = 60\n
Atk = 5\n
Mana = 100\n
Pociones = 5\n
\n
Tanque (T):\n
HP = 150\n
Atk = 15\n
Mana = 10\n
Pociones = 0\n  
\n
Curandero (CR)\n
HP = 75\n
Atk = 7\n
Mana = 125\n
Pociones = 3\n
\n
Random (R):\n
''')

clase = str(input("Escribe la inicial de tu clase "))
#caballero
if clase == "C":
    hp = HPCaballero
    atk = AtkCaballero
    mana = ManaCaballero
    curacion = CuracionCaballero
    pociones = PocionesCaballero
#alquimista
elif clase == "A":
    hp = HPAlqui
    atk = AtkAlqui
    mana = ManaAlqui
    curacion = CuracionAlqui
    pociones = PocionesAlqui
#tanque
elif clase == "T":
    hp = HPTanque
    atk = AtkTanque
    mana = ManaTanque
    curacion = CuracionTanque
    pociones = PocionesTanque
#curandero
elif clase == "CR":
    hp = HPCurandero
    atk = AtkCurandero
    mana = ManaCurandero
    curacion = CuracionCurandero
    pociones = PocionesCurandero
#random
elif clase == "R":
    hp = HPRandom
    atk = AtkRandom
    mana = ManaRandom
    curacion = CuracionRandom
    pociones = PocionesRandom


"""
==========Stats boss==========
"""

HPBoss = 100
AtkBoss = 10

"""
==========Pelea==========
"""

print(" HP Jugador: ", hp, "\n HP Boss: ", HPBoss, "\n Mana: ", mana, "\n Pociones: ", pociones)

while HPBoss > 0 and hp > 0:
    accion = input("Ataque = A, Curar = C, Pocion = P ")
    
#ataque

    if accion == "A" or accion == "a":
        HPBoss = ataque(atk, HPBoss)
        print("Le hiciste ", atk, " daño al boss")

#curar

    elif accion == "C" or accion == "c":
        if mana >= 10:
            hp = curar(hp, curacion)
            mana = mana - 10
        else:
            print("¡Necesitas mana para curarte!")

#pocion

    elif accion == "P" or accion == "p":
        if pociones >= 1:
            mana = mana + 20
            pociones = pociones - 1
        elif pociones == 0:
            print("¡Ya no te quedan pociones!")

#daño boss

    dañoboss = randrange(1, 20)
    print("¡El boss te hizo ", dañoboss, " de daño!")
    hp = hp - dañoboss

    print(" HP Jugador: ", hp, "\n HP Boss: ", HPBoss, "\n Mana: ", mana, "\n Pociones: ", pociones)


#fin del combate
if HPBoss < 0:
    print("Mataste al boss")
elif hp < 0:
    print("YOU DIED")
else:
    print("ehh empate, a ver si luego implemento el stat de speed")
        
        
    