#EL OBJETIVO DE ESTE FICHERO ES SER EL EJECUTADO, POR LO QUE TODOS LOS OTROS DEBEN VENIR A PARAR AQUI
import mainIA
import main






def seleccionarmodalidad(Tablero):
    modalidad= input("Para jugar al 3 en raya con un amigo pulsa 1, para jugar solo pulsa 2: \n" )
    modalidadvalida=False

    while modalidadvalida==False:
        if modalidad=="1":
            main.JugarPVP()
            modalidadvalida=True
        elif modalidad=="2":
            seleccionardificultad(Tablero)
            modalidadvalida=True
        else:
            modalidad= input("valor invalido. Para jugar al 3 en raya con un amigo pulsa 1, para jugar solo pulsa 2" )



def seleccionardificultad(Tablero):
    print("Seleciona un nivel de dificultad para enfrentarlo entre 1 y 3 siendo 1 el mas facil: \n")

    dificultad= input()
    dificultad=int(dificultad)
    while dificultad<1 or dificultad>3:
        print("valor invalido, introduce un numero del 1 al 3: ")
        dificultad=input()
        dificultad= int(dificultad)

    mainIA.JugarPVE(Tablero, dificultad)
    return


seleccionarmodalidad(mainIA.Tablero)

input("pulsa enter para finalizar el programa: ")