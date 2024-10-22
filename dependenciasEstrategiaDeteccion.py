


def calcularJugadaGanadora(i, TableroImaginario):
  posicionImaginaria= i
  posicionImaginaria=int(posicionImaginaria)
  posicionImaginaria-=1
  if TableroImaginario[posicionImaginaria]== "-":
      TableroImaginario[posicionImaginaria]="O"
      GanadorImaginario= comprobar_victoria_imaginaria(TableroImaginario)
      if GanadorImaginario== "O":
         
          return posicionImaginaria
      else:
          return -1

  else:
      return -1

def calcularJugadaPerderoda(j, TableroImaginario):
    posicionImaginaria=j
    posicionImaginaria=int(posicionImaginaria)
    posicionImaginaria-=1
    if TableroImaginario[posicionImaginaria]=="-":
        TableroImaginario[posicionImaginaria]="X"
        GanadorImaginario= comprobar_derrota_imaginaria(TableroImaginario)
        if GanadorImaginario=="X":

            return posicionImaginaria
        else:
            return -1
    else:
        return -1

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

def comprobar_derrota_imaginaria(TableroImaginario):
    Ganador_fila_imaginaria = comprobar_filas(TableroImaginario)
    Ganador_columna_imaginaria = comprobar_columnas(TableroImaginario)
    Ganador_diagonal_imaginaria = comprobar_diagonales(TableroImaginario)

    if Ganador_fila_imaginaria:
      GanadorImaginario = "X"
    elif Ganador_columna_imaginaria:
     GanadorImaginario = "X"
    elif Ganador_diagonal_imaginaria:
      GanadorImaginario = "X"
    else:
      GanadorImaginario = None
    return GanadorImaginario




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


def MostrarTablero(Tablero):
  print("\n")
  print(" " +  Tablero[0] + " | " + Tablero [1] + " | " + Tablero[2]    +"            1|2|3")
  print("------------" +                                                 "          -----")
  print(" " +  Tablero[3] + " | " + Tablero [4] + " | " + Tablero[5]    +"            4|5|6")
  print("------------" +                                                 "          -----")
  print(" " +  Tablero[6] + " | " + Tablero [7] + " | " + Tablero[8]    +"            7|8|9")
  print("\n")
