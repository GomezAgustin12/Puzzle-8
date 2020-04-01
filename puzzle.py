
import bfs
import movimiento
import sys
import Node
bfs = bfs.bfs
Nodo = Node.Nodo
movimiento = movimiento.movimiento

estadoFinal = [1, 4, 7, 2, 5, 8, 3, 6, 0]


def main():
    estadoInicial = []
    for i in range(0, 9):
        estadoInicial.append(
            int(input('Inserta el numero ' + str(i) + ': ')))

    result = bfs(estadoInicial, estadoFinal, )
    if result == None:
        print("No existe solucion")
    elif result == [None]:
        print("El nodo inicial es la meta!")
    else:
        print(result)
        print(len(result), " movimientos")


if __name__ == "__main__":
    main()
