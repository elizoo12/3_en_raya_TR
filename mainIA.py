import random
import estrategiaDeteccion
import EstrategiaBuscarVictoria
import estrategiaRandom

# --------- variables goblales -----------

# esto es la matriz donde trabajaremos, en este caso tan solo es una tupla
Tablero = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

TableroImaginario=["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

# Esta variable indicara si el juego debe seguir o ha finalizado
el_juego_funciona = True

# Esta variable nos indicara quien es el ganador si lo hay, sino permanecera en estado None
Ganador = None

#  Esta variable indica de quien es el turno, de forma predeterminada empezaran las cruces 
jugador_humano="X"
ordenador="O"
Jugador_del_Turno = jugador_humano
# ------------- funciones ---------------

# Jugar al 3 en ralla
def JugarPVE(Tablero, dificultad):

  # reiniciar el tablero
  MostrarTablero()

  # bucle principal, el bucle cerrara cuando haya ganador o tablas
  while el_juego_funciona:

    #Jugada de cada jugador
    #*************
    Jugada(Jugador_del_Turno, Tablero, dificultad)

    # comprobamos victoria y empate
    Comprobar_fin_juego()

    # cambiamos de X a O y viceversa
    Cambiar_jugador()
  
  # Cuando el bucle principal termina indicamos quien ha ganado
  if Ganador == "X" or Ganador == "O":
    print(Ganador + " ha ganado. ")
  elif Ganador == None:
    print("Tablas.")


# aqui mostramos el tablero de pantalla, en un lado tendremos nuestro propio tablero y en el otro una indicacion numerica
def MostrarTablero():
  print("\n")
  print(" " +  Tablero[0] + " | " + Tablero [1] + " | " + Tablero[2]    +"            1|2|3")
  print("------------" +                                                 "          -----")
  print(" " +  Tablero[3] + " | " + Tablero [4] + " | " + Tablero[5]    +"            4|5|6")
  print("------------" +                                                 "          -----")
  print(" " +  Tablero[6] + " | " + Tablero [7] + " | " + Tablero[8]    +"            7|8|9")
  print("\n")


# funcion usada para las jugadas, ambos jugadores comparten funcion
def Jugada(Jugador, Tablero, dificultad):

    if Jugador=="X":
        jugada_humana()
    elif Jugador=="O":
        jugada_ordenador(Tablero, dificultad)


def jugada_ordenador(Tablero, dificultad):
  if dificultad==1:
    estrategiaRandom.jugada_ordenador_Random(Tablero)
  elif dificultad==2:
    EstrategiaBuscarVictoria.jugada_ordenador_Ganar(Tablero)
  elif dificultad==3:
    estrategiaDeteccion.jugada_ordenador_deteccion(Tablero)
  return



def jugada_humana():
    # pedimos una jugada
  print("es el turno del Jugador ")
  posicion = input("elige una casilla entre 1-9: ")

  # valido sera un valor para generar un bucle que solo se abrira cuando se de una jugada valida
  valido = False
  while not valido:

    # Nos aseguramos de que juegan dentro del tablero
    while posicion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      posicion = input("Input invalido. elige una casilla entre 1-9: ")
 
    # corregimos la posicion para que el ordenador la entienda
    posicion = int(posicion) - 1

    # Nos aseguramos que se coloca en una casilla no escogida previamente
    if Tablero[posicion] == "-":
      valido = True
    else:
      print("casilla ocupada, piensa otra opcion. ")

  # colocamos la pieza en nuestra "matriz"
  Tablero[posicion] = "X"

  # refrescamos el tablero con la nueva jugada
  MostrarTablero()

# funcion para comprobar el final de juego
def Comprobar_fin_juego():
  comprobar_victoria()
  comprobar_tablas()


# funcion para comrpobar si hay una victoria
def comprobar_victoria():
  # Set global variables
  global Ganador
  # traemos las variables globales necesarias
  ganador_fila = comprobar_filas(Tablero)
  ganador_columna = comprobar_columnas(Tablero)
  ganador_diagonal = comprobar_diagonales(Tablero)
  # Obtenemos el jugador victorioso
  if ganador_fila:
    Ganador = ganador_fila
  elif ganador_columna:
    Ganador = ganador_columna
  elif ganador_diagonal:
    Ganador = ganador_diagonal
  else:
    Ganador = None


# comprobacion de cada fila
def comprobar_filas(Tablero):
  # traemos las variables globales necesarias
  global el_juego_funciona
  # comprobamos que todos los valores en una fila sean iguales y no esten vacios
  fila_1 =Tablero[0] ==Tablero[1] ==Tablero[2] != "-"
  fila_2 =Tablero[3] ==Tablero[4] ==Tablero[5] != "-"
  fila_3 =Tablero[6] ==Tablero[7] ==Tablero[8] != "-"
  # si hay linea hay victoria
  if fila_1 or fila_2 or fila_3:
    el_juego_funciona = False
  # obtenemos el ganador
  if fila_1:
    return Tablero[0] 
  elif fila_2:
    return Tablero[3] 
  elif fila_3:
    return Tablero[6] 
  # seguimos el codigo si no hay fila
  else:
    return None


# comprobamos las columnas para ganar
def comprobar_columnas(Tablero):
  # traemos las variables globales necesarias
  global el_juego_funciona
  # comprobamos que tienen el mismo valor y no estan vacias
  columna_1 =Tablero[0] ==Tablero[3] ==Tablero[6] != "-"
  columna_2 =Tablero[1] ==Tablero[4] ==Tablero[7] != "-"
  columna_3 =Tablero[2] ==Tablero[5] ==Tablero[8] != "-"
  # si hay columna hay victoria
  if columna_1 or columna_2 or columna_3:
    el_juego_funciona = False
  #  obtenemos el ganador
  if columna_1:
     return Tablero[0] 
  elif columna_2:
    return Tablero[1] 
  elif columna_3:
    return Tablero[2] 
  # seguimos el codigo si no hay columna
  else:
    return None


# comprobamos las diagonales para ganar
def comprobar_diagonales(Tablero):
  # traemos las variables globales necesarias
  global el_juego_funciona
  # comprobamos que tengan el mismo valor y no sea vacio
  diagonal_1 =Tablero[0] ==Tablero[4] ==Tablero[8] != "-"
  diagonal_2 =Tablero[2] ==Tablero[4] ==Tablero[6] != "-"
  # si hay diagonal hay victoria
  if diagonal_1 or diagonal_2:
    el_juego_funciona = False
  # obtenemos el ganador
  if diagonal_1:
    return Tablero[0] 
  elif diagonal_2:
    return Tablero[2]
  #continuamos el codigo
  else:
    return None


# funcion para comprobar si hay tablas
def comprobar_tablas():
  # traemos las variables globales necesarias
  global el_juego_funciona
  # si el tablero esta lleno hay tablas
  if "-" not in Tablero:
    el_juego_funciona = False
    return True
  # De otra forma no hay tablas
  else:
    return False


def comprobar_victoria_imaginaria(TableroImaginario):
    Ganador_fila_imaginaria = comprobar_filas(TableroImaginario)
    Ganador_columna_imaginaria = comprobar_columnas(TableroImaginario)
    Ganador_diagonal_imaginaria = comprobar_diagonales(TableroImaginario)

    if Ganador_fila_imaginaria:
      GanadorImaginario = "O"
    elif Ganador_columna_imaginaria:
     GanadorImaginario = "O"
    elif Ganador_diagonal_imaginaria:
      GanadorImaginario = "O"
    else:
      GanadorImaginario = None
    return GanadorImaginario


#  funcion para cambiar jugador en cada turno
def Cambiar_jugador():
  # traemos las variables globales necesarias
  global Jugador_del_Turno
  #si el jugador es X pasamos a O
  if Jugador_del_Turno == jugador_humano:
    Jugador_del_Turno = ordenador
  #  si el jugador es O pasamos a X
  elif Jugador_del_Turno == ordenador:
    Jugador_del_Turno = jugador_humano





####JugarPVE(Tablero, dificultad)