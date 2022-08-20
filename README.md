# RPG

Los RPGs (Role Playing Games, por sus siglas en inglés) son un tipo de videojuego en los cuales el jugador toma el rol de un personaje en un mundo de fantasía. Hay varios tipos de RPGs, pero el que se va a utilizar en este código va a ser un RPG con combate basado en turnos. Algunos ejemplos de juegos así son Final Fantasy, Earthbound, Undertale, entre otros. 

# Pseudocódigo
importar random

(Información del jugador)
jHP = 100
jATK = 10
jDEF = 0
jPOT = 2

(Información del enemigo)
eHP = 100
eATK = 10

(Acciones del jugador)
Función de atacar:
	Número random 1-10
	Si el número es 10:
		Restarle al HP del enemigo jATK * 2
	Si es 1:
		Fallaste
	Si no:
		Restarle al HP del enemigo jATK
	
Función de curar:
	Sumar número random de 5-20 a jHP

Función de poción:
	Si jPOT > 0:
		subir jDEF + 20
	Si no:
		Decir que se acabaron las pociones

(Acciones del enemigo)
Función de atacar:
	Número random 1-10
	Si el número es 10:
		Restarle al jugador eATK*((100 - jDEF) / 100) * 2
	Si es 1:
		Falla
	Si no:
		Restarle al jugador eATK*((100 - jDEF) / 100)
	
(Sección de batalla)
Mientras el enemigo y el jugador tengan vida mayor a 0:
	Preguntar qué hará el jugador (atacar, curar, poción)
	Si elige atacar, función de atacar
	Si elige curar, función de curar
	Si elige poción, función de poción
	Después atacará el enemigo con su función de ataque
	Si la vida del jugador llega a 0 o menos: 
		Imprimir que perdió
	Si la vida del enemigo llega a 0 o menos:
		Imprimir que ganó
	
