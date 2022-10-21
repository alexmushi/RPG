#Liberia de random, la cual permitira agregarle numeros aleatorios al juego
from random import *

"""
==========Preguntas==========
"""

preguntas = [
# 1    
    """¿Cuántos litros de sangre tiene una persona adulta?
    1 Tiene entre 2 y 4 litros
    2 Tiene entre 4 y 6 litros
    3 Tiene 10 litros
    4 Tiene 7 litros
    5 Tiene 0,5 litros""",
# 2
    """¿Quién es el autor de la frase "Pienso, luego existo"?
    1 Platón
    2 Galileo Galilei
    3 Descartes
    4 Sócrates
    5 Francis Bacon""",
# 3
    """¿Cuál es el país más grande y el más pequeño del mundo?
    1 Rusia y Vaticano
    2 China y Nauru
    3 Canadá y Mónaco
    4 Estados Unidos y Malta
    5 India y San Marino""",
# 4
    """¿Cuál es el grupo de palabras escritas correctamente?
    1 Metamorfosis, extranjero, diversidac, equilivrio
    2 Metaformosis, estranjero, diversidad, ekilibrio
    3 Metamorfosis, extrangero, dibersidad, equilibrio
    4 Metamorfosis, extranjero, diversidad, equilibrio
    5 Metamórfosis, eztranjero, divérsidad, ecuilibrio""",
# 5
    """¿Cuál es el libro más vendido en el mundo después de la Biblia?
    1 El Señor de los Anillos
    2 Don Quijote de la Mancha
    3 El Principito
    4 Cien años de Soledad
    5 La Odisea""",
# 6
    """¿Cuántos decimales tiene el número pi π?
    1 Dos
    2 Cien
    3 Infinitos
    4 Mil
    5 Veinte""",
# 7
    """La sal común está formada por dos elementos, ¿cuáles son?
    1 Sodio y potasio
    2 Sodio y cloro
    3 Sodio y carbono
    4 Potasio y cloro
    5 Cristal y sodio.""",
# 8
    """¿Cuántos jugadores por equipo participan en un partido de voleibol?
    1 2 jugadores
    2 3 jugadores
    3 4 jugadores
    4 5 jugadores
    5 6 jugadores""",
# 9
    """¿Cuáles son los representantes más destacados de la literatura renacentista?
    1 Miguel de Cervantes, William Shakespeare, Luis de Camões.
    2 Leonardo da Vinci, Miguel Angel Buonarroti, Sandro Boticelli
    3 Caravaggio, Bernini, Borromini
    4 Goethe, Victor Hugo, Gustavo Adolfo Bécquer
    5 Jorge Isaac, José Martí, Eduardo Blanco""",
# 10
    """¿Quién pintó la obra "Guernica"?
    1 Paul Cézanne
    2 Pablo Picasso
    3 Diego Rivera
    4 Salvador Dalí
    5 Frida Kahlo""",]

"""
==========Respuestas==========
"""

respuestas = [
# 1
    2,
# 2
    3,
# 3
    1,
# 4
    4,
# 5
    2,
# 6
    3,
# 7
    2,
# 8
    5,
# 9
    1,
# 10
    2,]

"""
==========Acciones==========
"""

def ataque(atk, hp):
    randnum = randrange(0,10)
    print(preguntas[randnum])
    respuesta = int(input())
    if respuesta == respuestas[randnum]:
        print("¡Correcto!", "Le hiciste ", atk * 2, " daño al boss")
        nhp = hp - 2 * atk
    else:
        print("La respuesta correcta era", respuestas[randnum], "Le hiciste ", atk, " daño al boss")
        nhp = hp - atk
    return nhp

def curar(hp, poder_curacion):
    nhp = hp + randrange(5,20) * poder_curacion
    return nhp
         
"""
==========Stats clases==========
"""

# Caballero
HPCaballero = 100
AtkCaballero = 10
ManaCaballero = 50
CuracionCaballero = 1
pociones_m_c = ["Pocion_m"]
pociones_d_c = ["Pocion_d"]
InvCaballero = [pociones_m_c, pociones_d_c]

# Alquimista
HPAlqui = 60
AtkAlqui = 5
ManaAlqui = 100
CuracionAlqui = 1.5
pociones_m_a = ["Pocion_m", "Pocion_m", "Pocion_m"]
pociones_d_a = ["Pocion_d", "Pocion_d", "Pocion_d"]
InvAlqui = [pociones_m_a, pociones_d_a]

# Tanque
HPTanque = 150
AtkTanque = 15
ManaTanque = 10
CuracionTanque = 0.5
pociones_m_t = []
pociones_d_t = []
InvTanque = [pociones_m_t, pociones_d_t]

# Curandero
HPCurandero = 75
AtkCurandero = 7
ManaCurandero = 125
CuracionCurandero = 2
pociones_m_cr = ["Pocion_m", "Pocion_m", "Pocion_m", "Pocion_m", "Pocion_m", "Pocion_m"]
pociones_d_cr = []
InvCurandero = [pociones_m_cr, pociones_d_cr]

# Random
HPRandom = randrange(20, 200, 10)
AtkRandom = randrange(2, 20)
ManaRandom = randrange(2, 200, 10)
CuracionRandom = randrange(1,3)
PocionesMRandom = randrange(0,7)
PocionesDRandom = randrange(0,7)
pociones_m_r = []
pociones_d_r = []
while PocionesMRandom > 0:
    pociones_m_r.append("Pocion_m")
    PocionesMRandom -= 1
while PocionesDRandom > 0:
    pociones_d_r.append("Pocion_d")
    PocionesDRandom -= 1
InvRandom = [pociones_m_r, pociones_d_r]

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
    Pociones de maná = 1\n
    Pociones de daño = 1\n
    \n
    Alquimista (A):\n
    HP = 60\n
    Atk = 5\n
    Mana = 100\n
    Pociones de maná = 3\n
    Pociones de daño = 3\n
    \n
    Tanque (T):\n
    HP = 150\n
    Atk = 15\n
    Mana = 10\n
    Pociones de maná = 0\n
    Pociones de daño = 0\n 
    \n
    Curandero (CR)\n
    HP = 75\n
    Atk = 7\n
    Mana = 125\n
    Pociones de maná = 6\n
    Pociones de daño = 0\n
    \n
    Random (R):\n
    HP = ???\n
    Atk = ???\n
    Mana = ???\n
    Pociones de maná = ???\n
    Pociones de daño = ???\n''')

clase = str(input("Escribe la inicial de tu clase "))

if clase == "C":
    hp = HPCaballero
    atk = AtkCaballero
    mana = ManaCaballero
    curacion = CuracionCaballero
    pociones_m = pociones_m_c
    pociones_d = pociones_d_c
    inv = InvCaballero
elif clase == "A":
    hp = HPAlqui
    atk = AtkAlqui
    mana = ManaAlqui
    curacion = CuracionAlqui
    pociones_m = pociones_m_a
    pociones_d = pociones_d_a
    inv = InvAlqui
elif clase == "T":
    hp = HPTanque
    atk = AtkTanque
    mana = ManaTanque
    curacion = CuracionTanque
    pociones_m = pociones_m_t
    pociones_d = pociones_d_t
    inv = InvTanque
elif clase == "CR":
    hp = HPCurandero
    atk = AtkCurandero
    mana = ManaCurandero
    curacion = CuracionCurandero
    pociones_m = pociones_m_cr
    pociones_d = pociones_d_cr
    inv = InvCurandero
elif clase == "R":
    hp = HPRandom
    atk = AtkRandom
    mana = ManaRandom
    curacion = CuracionRandom
    pociones_m = pociones_m_r
    pociones_d = pociones_d_r
    inv = InvRandom

# Aqui se guarda el nombre del usuario
nombre = str(input("Escribe el nombre del guerrero: "))

"""
==========Stats boss==========
"""

HPBoss = 100
AtkBoss = 10

"""
==========Pelea==========
"""

print(" HP ", nombre, ": ", hp, "\n HP Boss: ", HPBoss, "\n Mana: ", mana)

# Menu
while HPBoss > 0 and hp > 0:
    accion = input("Ataque = A, Curar = C, Pocion mana = PM, Pocion daño = PD, Inventario = I ")

# Inventario
    while accion == "I" or accion == "i":
        print("Tu inventario: " , inv)
        accion = input("Ataque = A, Curar = C, Pocion mana = PM, Pocion daño = PD, Inventario = I ")
        
# Ataque
    if accion == "A" or accion == "a":
        HPBoss = ataque(atk, HPBoss)
  
# Curar
    elif accion == "C" or accion == "c":
        if mana >= 10:
            hp = curar(hp, curacion)
            mana = mana - 10
        else:
            print("¡Necesitas mana para curarte!")

# Pocion mana
    elif accion == "PM" or accion == "pm":
        if "Pocion_m" in pociones_m:
            mana = mana + 20
            pociones_m.remove("Pocion_m")
            print("Te regeneraste 20 mana")
        else:
            print("¡Ya no te quedan pociones!")

# Pocion daño
    elif accion == "PD" or accion == "pd":
        if "Pocion_d" in pociones_d:
            HPBoss = HPBoss - 20
            pociones_d.remove("Pocion_d")
            print("Le hiciste 20 daño al boss")
        else:
            print("¡Ya no te quedan pociones!")

# Daño boss
    dañoboss = randrange(1, 20)
    print("¡El boss te hizo ", dañoboss, " de daño!")
    hp = hp - dañoboss
    print(" HP ", nombre, ": ", hp, "\n HP Boss: ", HPBoss, "\n Mana: ", mana)

# Fin del combate
if HPBoss < 0:
    print("Mataste al boss")
elif hp < 0:
    print("YOU DIED")
        
        
#Preguntas de cultura general sacadas de https://www.todamateria.com/preguntas-de-cultura-general/
                                                                                          