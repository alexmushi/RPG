#liberias
from random import *

global hp
global atk
global mana
global curacion
global pociones
global xp

"""
==========Preguntas==========
"""

preguntas = [
#1    
"""¿Cuántos litros de sangre tiene una persona adulta?
1 Tiene entre 2 y 4 litros
2 Tiene entre 4 y 6 litros
3 Tiene 10 litros
4 Tiene 7 litros
5 Tiene 0,5 litros""",
#2
"""¿Quién es el autor de la frase "Pienso, luego existo"?
1 Platón
2 Galileo Galilei
3 Descartes
4 Sócrates
5 Francis Bacon""",
#3
"""¿Cuál es el país más grande y el más pequeño del mundo?
1 Rusia y Vaticano
2 China y Nauru
3 Canadá y Mónaco
4 Estados Unidos y Malta
5 India y San Marino""",
#4
"""¿Cuál es el grupo de palabras escritas correctamente?
1 Metamorfosis, extranjero, diversidac, equilivrio
2 Metaformosis, estranjero, diversidad, ekilibrio
3 Metamorfosis, extrangero, dibersidad, equilibrio
4 Metamorfosis, extranjero, diversidad, equilibrio
5 Metamórfosis, eztranjero, divérsidad, ecuilibrio""",
#5
"""¿Cuál es el libro más vendido en el mundo después de la Biblia?
1 El Señor de los Anillos
2 Don Quijote de la Mancha
3 El Principito
4 Cien años de Soledad
5 La Odisea""",
#6
"""¿Cuántos decimales tiene el número pi π?
1 Dos
2 Cien
3 Infinitos
4 Mil
5 Veinte""",
#7
"""La sal común está formada por dos elementos, ¿cuáles son?
1 Sodio y potasio
2 Sodio y cloro
3 Sodio y carbono
4 Potasio y cloro
5 Cristal y sodio.""",
#8
"""¿Cuántos jugadores por equipo participan en un partido de voleibol?
1 2 jugadores
2 3 jugadores
3 4 jugadores
4 5 jugadores
5 6 jugadores""",
#9
"""¿Cuáles son los representantes más destacados de la literatura renacentista?
1 Miguel de Cervantes, William Shakespeare, Luis de Camões.
2 Leonardo da Vinci, Miguel Angel Buonarroti, Sandro Boticelli
3 Caravaggio, Bernini, Borromini
4 Goethe, Victor Hugo, Gustavo Adolfo Bécquer
5 Jorge Isaac, José Martí, Eduardo Blanco""",
#10
"""¿Quién pintó la obra "Guernica"?
1 Paul Cézanne
2 Pablo Picasso
3 Diego Rivera
4 Salvador Dalí
5 Frida Kahlo""",
#11
"""¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra?
1 12 minutos
2 1 día
3 12 horas
4 8 minutos
5 8 segundos""",
#12
"""¿Cuál es la traducción correcta de la frase "There is a green carpet at the exit of the library"?
1 Hay una verde carpeta en la salida de la librería
2 Ahí es una verde carpeta en el éxito de la librería
3 Hay una alfombra verde a la salida de la biblioteca
4 Hay una alfombra verde a la salida de la librería
5 Hay una carpeta verde a la salida de la biblioteca""",
#13
"""¿Cuál es la nacionalidad de Jorge Mario Bergoglio?
1 Cubana
2 Italiana
3 Española
4 Mexicana
5 Argentina""",
#14
"""¿Cuáles son los tres predadores del reino animal reconocidos por: 1) habilidad de cazar en grupo, 2) camuflajearse para sorprender a su presa, 3) poseer sentidos refinados?
1 1) Hiena; 2) Oso polar; 3) Lobo gris
2 1) León; 2) tiburón blanco; 3) orca
3 1) Tigre; 2) águila; 3) gato
4 1) Tiburón blanco; 2) elefante; 3) escorpión
5 1) Cobra; 2) zorro; 3) cocodrilo""",
#15
"""¿Cuál es la altura de la red de voleibol en los juegos masculino y femenino?
1 2,4 m para ambos
2 2,5 m y 2,0 m
3 1,8 m y 1,5 m
4 2,45 m y 2,15 m
5 2,43 m y 2,24 m""",
#16
"""¿En qué orden se presentaron los modelos atómicos?
1 Thomson, Dalton, Rutherford, Bohr
2 Dalton, Thomson, Rutherford, cuántico
3 Bohr, Rutherford, cuántico, Einstein
4 Dalton, Einstein, cuántico, Sheldon Cooper
5 Rutherford, Dalton, Thomson, cuántico""",
#17
"""¿En qué periodo de la prehistoria fue descubierto el fuego?
1 Neolítico
2 Paleolítico
3 Edad de los metales
4 Edad de piedra
5 Edad media""",
#18
"""¿A quién se le atribuye la frase "Solo sé que no sé nada"?
1 Aristóteles
2 Nietszche
3 Sófocles
4 Salomón
5 Sócrates""",
#19
"""¿Cuál es la montaña más alta del continente americano?
1 Monte Everest
2 Aconcagua
3 Pico Neblina
4 Pico Bolívar
5 Monte Fuji""",
#20
"""¿Cuál es la velocidad de la luz?
1 300 000 000 metros por segundo
2 150 000 000 metros por segundo
3 199 792 458 metros por segundo
4 299 792 458 metros por segundo
5 350 000 000 metros por segundo""",
#21
"""¿En qué país de África el español es la lengua oficial?
1 Costa de Marfil
2 Sierra Leona
3 Guinea ecuatorial
4 Cabo Verde
5 Liberia""",
#22
"""¿Qué hora es en inglés "It is a quarter past six"?
1 6:15
2 3:46
3 6:45
4 5:15
5 5:45""",
#23
"""¿Quién es el autor de "El Príncipe"?
1 Antoine de Saint-Exupery
2 Charles de Gales
3 Friedrich Nietzche
4 Nicolás Maquiavelo
5 Dante Allighieri""",
#24
"""¿Cuál es la conjugación del verbo "caber" en la primera persona del singular del presente indicativo?
1 Yo quepo
2 Yo cabo
3 Nosotros cabemos
4 Nosotros quepamos
5 Yo cabé""",
#25
"""¿Cuáles de estas construcciones famosas quedan en los Estados Unidos?
1 Lincoln Memorial, Sydney Opera House, Burj Khalifa
2 Torre Eiffel, Museo Guggenheim, Abadía de Westminter
3 Estatua de la Libertad, puente Golden Gate, Empire State Building
4 Dancing House, 30 st Mary Axe, La Casa Blanca
5 La ciudad prohibida, la Sagrada Familia, el Panteón""",
#26
"""¿Cuales de las siguientes son enfermedades de transmisión sexual ETS?
1 SIDA, tricomoniasis, ébola
2 Chikunguya, malaria, herpes genital
3 Gonorrea, clamidia, sífilis
4 Botulismo, cistitis, chagas
5 Hepatitis B, fiebre tifoidea, lepra""",
#27
"""¿Cuál de estos países se extiende entre dos continentes?
1 Tanzania
2 Groenlandia
3 Egipto
4 Filipinas
5 Rusia""",
#28
"""¿En cuál de las siguientes oraciones se emplea una palabra de forma incorrecta?
1 La sabia fluyó por los conductos de la planta.
2 Mi abuela era una mujer sabia.
3 No sabía que podía hacer esto.
4 Mi mamá prepara un rico platillo con salvia.
5 Zabia es un nombre propio de niñas en árabe.""",
#29
"""¿Cuál fue el recurso utilizado inicialmente por el ser humano para explicar el origen de las cosas?
1 La filosofía
2 La biología
3 La matemática
4 La astronomía
5 La mitología""",
#30
"""¿Cuál es el orden de los planetas del sistema solar, partiendo desde su centro?
1 Sol, Mercurio, Venus, Luna, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno, Plutón
2 Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno
3 Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno, Plutón
4 Venus, Mercurio, Tierra, Júpiter, Urano, Saturno, Neptuno
5 Tierra, Venus, Mercurio, Marte, Urano, Neptuno, Plutón""",
#31
"""¿Cuáles son los dioses griegos correspondientes a los dioses romanos Júpiter y Plutón?
1 Ares y Hermes
2 Cronos y Apolo
3 Zeus y Hades
4 Dionisio y Démeter
5 Zeus y Ares""",
#32
"""¿Cuál es el animal terrestre más grande en la actualidad?
1 Jirafa
2 Tiburón blanco
3 Diplodocus
4 Ballena azul
5 Elefante africano""",
#33
"""¿Cuál es el tema del famoso discurso "I have a dream" de Martin Luther King?
1 La igualdad de las razas
2 La Justicia para los menos favorecidos
3 La intolerancia religiosa
4 El premio Nobel de la Paz
5 La lucha contra el Apartheid""",
#34
"""¿Qué líder mundial quedó conocida como "La Dama de Hierro"?
1 Dilma Rouseff
2 Angela Merkel
3 Hillary Clinton
4 Margaret Thatcher
5 Christine Lagarde""",
#353
"""¿Qué es el Acuerdo de París?
1 El acuerdo ortográfico entre países cuya lengua oficial es el francés.
2 El acuerdo entre países europeos acerca de la inmigración.
3 El acuerdo entre Francia, EE.UU y Canadá para acusar a China del calentamiento global.
4 El acuerdo de cooperación financiera internacional entre las tres mayores potencias mundiales.
5 El acuerdo entre varios países acerca de las consecuencias del calentamiento global.""",
#36
"""¿Qué es el Acuerdo de París?
1 El acuerdo ortográfico entre países cuya lengua oficial es el francés.
2 El acuerdo entre países europeos acerca de la inmigración.
3 El acuerdo entre Francia, EE.UU y Canadá para acusar a China del calentamiento global.
4 El acuerdo de cooperación financiera internacional entre las tres mayores potencias mundiales.
5 El acuerdo entre varios países acerca de las consecuencias del calentamiento global.""",
#37
"""¿Cuáles son los nombres de los tres reyes magos?
1 Gaspar, Nicolas y Nataniel
2 Gaspar, Melchor y Baltazar
3 Simon, Judas y Mateo
4 Charles, George y Louis
5 Abraham, Noé y Moises""",
#38
"""¿Cuál es la religión monoteísta que cuenta con el mayor número de adeptos en el mundo?
1 Judaísmo
2 Zoroastrismo
3 Islamismo
4 Cristianismo
5 Hinduismo""",
#39
"""¿Cuál de esta películas se basó en el plebiscito chileno de 1988?
1 NO
2 Diarios de motocicleta
3 Pinochet in Suburbia
4 Enterrados vivos
5 Ya no basta con rezar""",
#40
"""¿Quién fue el primer hombre en pisar la Luna?
1 Yuri Gagarin
2 Buzz Aldrin
3 Charles Conrad
4 Michael Collins
5 Neil Armstrong""",
#41
"""¿Quién descubrió la vacuna contra la rabia y el proceso de pasteurización?
1 Charles Darwin
2 Louis Pasteur
3 Marie Curie
4 Antoine Lavoisier
5 Edward Jenner""",
#42
"""¿Cuál es el tipo sanguíneo considerado como "donante universal"?
1 Tipo A
2 Tipo B
3 Tipo O
4 Tipo AB
5 Ninguno de los anteriores""",
#43
"""¿Cuál es el cromosoma que determina el sexo masculino?
1 El cromosoma V
2 El cromosoma X
3 El cromosoma Y
4 El cromosoma Z
5 El cromosoma M""",
#44
"""¿Cuál es la capital de Australia?
1 Canberra
2 Melbourne
3 Sydney
4 Adelaide
5 Perth""",
#45
"""¿Cuál es la organización juvenil fundada por Baden-Powell?
1 La juventud socialista
2 Los Boy scouts
3 Los testigos de Jehová
4 YMCA
5 La juventud obrera""",
#46
"""Según la leyenda de la fundación de Roma, ¿quién amamantó a los gemelos Rómulo y Remo?
1 Una cabra
2 Una vaca
3 Una oveja
4 Una gata
5 Una loba""",
#47
"""¿En el exterior de qué edificio famoso en Francia fue construida una enorme pirámide de vidrio?
Torre Eiffel
1 Arco del Triunfo
2 Museo de Louvre
3 Grand Palais
4 Petit Palais""",
#48
"""¿Cómo se llaman los vasos que transportan la sangre desde el corazón al resto del cuerpo?
1 Arterias
2 Venas
3 Capilares
4 Articulaciones
5 Uréteres""",
#49
"""¿Con qué países tiene frontera Ecuador?
1 Con Brasil y Colombia
2 Con Colombia y Venezuela
3 Con Colombia y Perú
4 Con Perú y Bolivia
5 Con Bolivia y Brasil""",
#50
"""¿Qué animal gluglutea?
1 El pato
2 La garza
3 La guacamaya
4 La cacatúa
5 El pavo""",
#51
"""¿Cuál es el mayor archipiélago de la Tierra?
1 Filipinas
2 Indonesia
3 Bahamas
4 Finlandia
5 Maldivas""",
#52
"""¿Qué sustancia es absorbida por las plantas y expirada por los animales?
1 Oxígeno
2 Nitrógeno
3 Nitrato de sodio
4 Dióxido de hierro
5 Dióxido de carbono""",
#53
"""¿En qué océano queda Madagascar?
1 Océano Índico
2 Océano Antártico
3 Océano Ártico
4 Océano Atlántico
5 Océano Pacífico""",
#54
"""¿Cuál artista es conocido como uno de los exponentes máximos del ready-made (objeto-encontrado)?
1 Pablo Picasso
2 Salvador Dalí
3 Marcel Duchamp
4 Van Gogh
5 Leonardo de Vinci""",
#55
"""¿Cuál es el metal cuyo símbolo químico es Au?
1 Aluminio
2 Arsénico
3 Antimonio
4 Actinio
5 Oro""",
#56
"""¿En qué siglo el continente europeo fue devastado por la peste bubónica?
1 En el siglo X
2 En el siglo XI
3 En el siglo XII
4 En el siglo XIII
5 En el siglo XIV""",
#57
"""¿En qué ciudad tuvo lugar la Eco-92, una conferencia de las Naciones Unidas sobre el ambiente y el desarrollo?
1 Buenos Aires
2 Rio de Janeiro
3 Montevideo
4 Asunción
5 Caracas""",
#58
"""¿Quién pintó la bóveda de la capilla sixtina?
1 Miguel Angel
2 Leonardo da Vinci
3 Rafael
4 Boticelli
5 Donatello""",
#59
"""¿Cuántos grados son necesarios para que dos ángulos sean complementarios?
1 45 º
2 60 º
3 90 º
4 80 º
5 360 º""",
#60
"""¿Quién fue el creador de la tragedia griega?
1 Esquilo
2 Eurípides
3 Homero
4 Plutarco
5 Sófocles""",
#61
"""¿De qué grupo era vocalista Jim Morrison?
1 The Police
2 The Doors
3 Pink Floyd
4 Nirvana
5 AC/DC""",
#62
"""¿Qué es el BREXIT?
1 Salida del Reino Unido de la Zona Euro
2 Salida del Reino Unido de la Unión Europea
3 Salida de Inglaterra del Reino Unido
4 Salida de la monarquía del Reino Unido
5 Salida del Reino Unido de los juegos olímpicos.""",
#63
"""¿De qué país fue primera ministro Benazir Bhuto?
1 Inglaterra
2 Israel
3 India
4 Indonesia
5 Pakistán""",
#64
"""¿Por qué es mejor reconocida Nadia Comaneci?
1 Por la película "Nadia"
2 Por su libro "Nadia"
3 Por gobernar Rumania
4 Por ser gimnasta
5 Por ser nadadora""",
#65
"""¿Por qué película recibió un premio Oscar Leonardo DiCaprio?
1 Once Upon a Time... in Hollywood (2019)
2 The revenant (2015)
3 El Lobo de Wall Street (2013)
4 Diamantes de sangre (2006)
5 Titanic (1997)""",
#66
"""¿Cuántos jugadores pueden participar por equipo en el basquetbol?
1 2
2 3
3 4
4 5
5 6""",
#67
"""¿Cuál de estos países tiene como idioma oficial el francés?
1 Haití
2 Suecia
3 Líbano
4 Andorra
5 Mauritania""",
#68
"""¿Dónde se encuentra el gran colisionador de hadrones?
1 Entre Portugal y España
2 Entre España y Francia
3 Entre Francia y Suiza
4 Entre Italia y Alemania
5 Entre EE.UU y Canadá""",
#69
"""¿Cuáles de los siguientes compuestos son polisacáridos?
1 Colesterol y triglicéridos
2 Almidón y celulosa
3 Insulina y vitamina A
4 Metano y etano
5 Glucosa y fructosa""",
#70
"""¿Qué es el quimo?
1 La masa que se forma cuando se coagula la leche
2 La masa que se forma cuando se combina el jugo gástrico y los alimentos
3 La masa que se forma cuando se combina la saliva y los alimentos
4 La masa que se forma cuando se fermentan las uvas para hacer vino
5 La masa que se forma cuando se combina harina de maíz y agua""",
#71
"""¿Cuál es el único número primo par?
1 2
2 3
3 4
4 5
5 6""",
#72
"""¿Dónde se originaron los números arábigos?
1 India
2 Grecia
3 Roma
4 Persia
5 Arabia""",
#73
"""¿Cuándo se inició la Primera Guerra Mundial?
1 11 de noviembre 1918
2 1 de septiembre de 1939
3 28 de julio de 1914
4 2 de septiembre de 1945
5 28 de junio 1919""",
#74
"""¿La revolución francesa se inició con cuál evento?
1 La toma de la Bastilla el 14 de julio de 1789
2 La crisis económica en Francia en 1780
3 La coronación de Napoleón Bonaparte como Emperador de Francia
4 La huida del rey Luis XVI en 1791
5 El fin de la monarquía del rey Luis XVI en 1792""",
#75
"""¿Cómo se llaman los lados de un triángulo rectángulo?
1 Segmento y ángulo
2 Adyacente y opuesto
3 Tangente y coseno
4 Hipatia y catesis
5 Hipotenusa y catetos""",
#76
"""¿Cuáles son las partes de una fracción?
1 Número y denominado
2 Numerador y denominador
3 Superior e inferior
4 Dependiente e independiente
5 Natural y entero""",
#77
"""El barroco fue:
1 Un movimiento científico
2 Un movimiento telúrico
3 Un movimiento revolucionario
4 Un movimiento espiritual
5 Un movimiento artístico""",
#78
"""El Sol está compuesto principalmente por:
1 Luz y energía
2 Hidrógeno y helio
3 Asteroides y cometas
4 Hierro y níquel
5 Fotones y neutrones""",
#79
"""¿Cuál es el planeta más grande del sistema solar ?
1 Júpiter
2 Saturno
3 Urano
4 Neptuno
5 Plutón""",
#80
"""La FIFA es:
1 Fundación para la Investigación de Focas Amargadas
2 Fundación Internacional de Feroces Atletas
3 Federacíón Intergubernamental de
4 Federación Internacional de Fútbol Asociación
5 Fuente Inagotable de Fuerzas Armadas""",
#81
"""La carrera de obstáculos, el lanzamiento de jabalina y el salto triple son pruebas de:
1 Estrés
2 Sobrevivencia
3 Gimnasia
4 Atletismo
5 Ubicación""",
#82
"""La crisis económica que se originó por la caída de la bolsa de valores Wall Street en 1929 se conoce como:
1 La Gran Depresión
2 La Gran Recesión
3 La Gran Rendición
4 La Gran Revolución
5 La Gran Retención""",
#83
"""Curiosity, Perseverance, Opportunity, Spirit y Sojourner son:
1 Valores humanos
2 Adjetivos en inglés
3 Nombres de mascotas
4 Nombres de estrellas
5 Nombres de rovers marcianos""",
#84
"""En la siguiente expresión: 8-2x2+6x3-3 ¿la respuesta correcta es?
1 51
2 12
3 19
4 56
5 4""",
#85
"""¿Quién es la primera persona en ganar dos premios Nobel?
1 Albert Einstein
2 Nicolas Copérnico
3 Linus Pauling
4 Richard Feynman
5 Marie Curie""",
#86
"""El autor de la obra "La metamorfosis" es:
1 Richard Hawkins
2 Franz Kafka
3 J.K. Rowling
4 William Shakesperare
5 Isabel Allende""",
#87
"""En la película "Jojo Rabbit", el niño protagonista tenía un amigo imaginario, ¿quién era?
1 Hitler
2 El niño Jesús
3 El conejo de la suerte
4 Un dinosaurio morado
5 El fantasma de su papá""",
#88
"""¿Quién fue el maestro de Platón?
1 Aristóteles
2 Zeus
3 Diógenes
4 Sócrates
5 Pirilampo""",
#89
"""¿Dónde se encuentra Machu Picchu?
1 En México
2 En Colombia
3 En Perú
4 En Brasil
5 En China""",
#90
"""Los olmecas, zapotecas y toltecas fueron pueblos indígenas pertenecientes a:
1 Mesoamérica
2 Sudamérica
3 Norteamérica
4 Patagonia
5 Amazonía""",
#91
"""Un ejemplo de la figura literaria símil es la expresión:
1 Tus dientes con perlas
2 Perlas son tus dientes
3 Tus blancos dientes de perla
4 Tus dientes son perlas
5 Tus dientes son como perlas""",
#92
"""¿A quién pertenece el poema Hombres necios que acusáis?
1 Jorge Borges
2 Sor Juana Inés de la Cruz
3 Pablo Neruda
4 Teresa de la Parra
5 Teresa Carreño""",
#93
"""El plano cartesiano se llama así en honor a:
1 Jimmy Carter
2 Olivia Cartesí
3 Horacio Cartes
4 Carles Puyol
5 René Descartes""",
#94
"""¿A qué compuesto corresponde la fórmula química O3?
1 Oxígeno
2 Ozono
3 Peróxido
4 Oro triple
5 No existe""",
#95
"""¿Dónde se encuentra el lago Titicaca?
1 América del Sur
2 Centroamérica
3 África
4 Asia
5 Oceanía""",
#96
"""El álbum musical "Like a Prayer" pertenece a:
1 Cindy Lauper
2 Britney Spears
3 Lady Gaga
4 Madonna
5 Michael Jackson""",
#97
"""¿Dónde se inventó la pólvora?
1 España
2 Francia
3 Inglaterra
4 China
5 Suecia""",
#98
"""La moneda oficial de Japón es:
1 Yen
2 Yuan
3 Yin
4 Yan
5 Yun""",
#99
"""El país ganador de la Copa Mundial de Fútbol del 2010 fue:
1 Brasil
2 Alemania
3 Uruguay
4 Italia
5 España""",
#100
"""¿De qué país fue presidente Nelson Mandela?
1 Libia
2 Guinea
3 Sudáfrica
4 Filipinas
5 Venezuela""",
#101
"""¿Cuál es el videojuego favorito del profe?
1 Total Warhammer
2 Zelda
3 Genshin Impact
4 Minecraft
5 No juega videojuegos"""
]

"""
==========Respuestas==========
"""

respuestas = [
#1
2,
#2
3,
#3
1,
#4
4,
#5
2,
#6
3,
#7
2,
#8
5,
#9
1,
#10
2,
#11
4,
#12
3,
#13
5,
#14
1,
#15
5,
#16
2,
#17
2,
#18
5,
#19
2,
#20
4,
#21
3,
#22
1,
#23
4,
#24
1,
#25
3,
#26
3,
#27
5,
#28
1,
#29
5,
#30
2,
#31
3,
#32
5,
#33
1,
#34
4,
#35
5,
#36
4,
#37
2,
#38
4,
#39
1,
#40
5,
#41
2,
#42
3,
#43
3,
#44
1,
#45
2,
#46
5,
#47
3,
#48
1,
#49
3,
#50
5,
#51
2,
#52
5,
#53
1,
#54
3,
#55
5,
#56
5,
#57
2,
#58
1,
#59
3,
#60
1,
#61
2,
#62
2,
#63
5,
#64
4,
#65
2,
#66
4,
#67
1,
#68
3,
#69
2,
#70
2,
#71
1,
#72
1,
#73
3,
#74
1,
#75
5,
#76
2,
#77
5,
#78
2,
#79
1,
#80
4,
#81
4,
#82
1,
#83
5,
#84
3,
#85
5,
#86
2,
#87
1,
#88
4,
#89
3,
#90
1,
#91
5,
#92
2,
#93
5,
#94
2,
#95
1,
#96
4,
#97
4,
#98
1,
#99
5,
#100
3,
#101
1
]

"""
==========Acciones==========
"""

def ataque(atk, hp):
    randnum = randrange(0,101)
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
==========Overworld==========
"""




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
        
        
#Preguntas de cultura general sacadas de https://www.todamateria.com/preguntas-de-cultura-general/