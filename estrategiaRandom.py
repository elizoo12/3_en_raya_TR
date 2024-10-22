
import dependenciasRandom
import random

def jugada_ordenador_Random(Tablero):
    print("es turno del ordenador ")

    valido=False
    while not valido:
        posicion= random.randint(1,9)
        posicion= int(posicion) -1
         # Nos aseguramos que se coloca en una casilla no escogida previamente
        if Tablero[posicion] == "-":
            valido = True
        else:
            print("El ordenador esta pensando ")

  # colocamos la pieza en nuestra "matriz"
    Tablero[posicion] = "O"

  # refrescamos el tablero con la nueva jugada
    dependenciasRandom.MostrarTablero(Tablero)

