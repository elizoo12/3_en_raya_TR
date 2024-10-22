import random
import dependenciasGanar



def jugada_ordenador_Ganar(Tablero):

    hayGanadorImaginaro=False
    print("es turno del ordenador ")
    for i in range(1,9):
      jugada = calcularJugada(i, Tablero[:])
      if (jugada >= 0 ):
        print ("Tenemos jugada ganadora")
        Tablero[jugada]="O"
        hayGanadorImaginaro = True
        break
       
    if not hayGanadorImaginaro:
        valido=False
        while not valido:
          print("#1 El ordenador esta calculando una jugada aleatoria ")
          jugada = calcularJugadaAleatoria(Tablero[:])
          if (jugada >= 0 ):
            Tablero[jugada]="O"
            hayGanadorImaginaro = True
            break 
    dependenciasGanar.MostrarTablero(Tablero)
    return



def calcularJugada(i, TableroImaginario):
  posicionImaginaria= i
  posicionImaginaria=int(posicionImaginaria)
  posicionImaginaria-=1
  if TableroImaginario[posicionImaginaria]== "-":
      TableroImaginario[posicionImaginaria]="O"
      GanadorImaginario= dependenciasGanar.comprobar_victoria_imaginaria(TableroImaginario)
      if GanadorImaginario== "O":
         
          return posicionImaginaria
      else:
          return -1

  else:
      return -1

def calcularJugadaAleatoria(TableroImaginario):
  posicion= random.randint(1,9)
  posicion= int(posicion) -1
  # Nos aseguramos que se coloca en una casilla no escogida previamente
  if TableroImaginario[posicion] == "-":
    return posicion
  else:
     return -1


