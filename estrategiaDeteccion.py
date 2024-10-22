
import dependenciasEstrategiaDeteccion
import random

#comprobar si puede ganar
#    jugada ganadora
#comprobar si el rival puede ganar
#   evitar victoria rival
#comprobar esquinas libres
#   esquina aleatoria
#comprobar centro libre
#    ocupar centro
#   comprobar lados libres
#   lado aleatoria





# detecta cuando puede ganar.
#no detecta cuando perder.
# detecta bien las esquinas libres.
# pone bien las esquinas libres.
# falla al poner centro y aristas.

def jugada_ordenador_deteccion(Tablero):
    hayGanadorImaginaro=False
    print("es turno del ordenador ")
    for i in range(1,9):
        jugada = dependenciasEstrategiaDeteccion.calcularJugadaGanadora(i, Tablero[:])
        if (jugada >= 0 ):
            print ("Tenemos jugada ganadora!")
            Tablero[jugada]="O"
            hayGanadorImaginaro = True
            break
    if not hayGanadorImaginaro:
        evitarDerrota=False
        for j in range(1,9):
            jugada=dependenciasEstrategiaDeteccion.calcularJugadaPerderoda(j, Tablero[:])
            if (jugada>=0):
                print("evitamos perder!")
                Tablero[jugada]="O"
                evitarDerrota=True
                break
        if not evitarDerrota:
            esquinaLibre= detectar_esquinas(Tablero[:])
            if esquinaLibre==1:
                while True:
                    print("Colocando esquina de forma aleatoria: ")
                    jugada = colocar_esquina(Tablero)
                    if (jugada >= 0 ):
                        Tablero[jugada]="O"
                        break 
            elif esquinaLibre==-1:
                centroLibre= detectar_centro(Tablero[:])
                if centroLibre==1:
                    print("Colocando centro: ")
                    jugada=4
                    Tablero[jugada]="O"
                elif centroLibre==-1:
                    AristaLibre= detectar_arista(Tablero[:])
                    if AristaLibre==1:
                        while True:
                            print("colocando arista de forma aleatoria: ")
                            jugada= colocar_arista(Tablero)
                            if (jugada>=0):
                                Tablero[jugada]="O"
                                break
    dependenciasEstrategiaDeteccion.MostrarTablero(Tablero)
    return



def detectar_esquinas(Tablero):
    EsquinaLibre=-1
    if Tablero[0]=="-" or Tablero[2]=="-" or Tablero[6]=="-" or Tablero[8]=="-":
        EsquinaLibre=1
    return EsquinaLibre

        


def colocar_esquina(Tablero):         
        
    posicion=random.choice((0, 2, 6, 8))
    if Tablero[posicion]=="-":
        return posicion
    else:
       return -1

def detectar_centro(Tablero):
    CentroLibre=-1
    if Tablero[4]=="-":
        CentroLibre=1
    return CentroLibre

def detectar_arista(Tablero):
    AristaLibre=-1
    if Tablero[1]=="-" or Tablero[3]=="-" or Tablero[5]=="-" or Tablero[7]=="-":
        AristaLibre=1
    return AristaLibre

def colocar_arista(Tablero):         
        
    posicion=random.choice((1, 3, 5, 7))
    if Tablero[posicion]=="-":
        return posicion
    else:
       return -1