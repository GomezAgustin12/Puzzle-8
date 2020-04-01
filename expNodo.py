
import movimiento
import crarNodo
movimiento = movimiento.movimiento
crarNodo = crarNodo.crarNodo


def expNode(nodo, nodos):
    """Returns a list of expanded nodos"""
    expNodos = []
    expNodos.append(crarNodo(movimiento(nodo.estado, 0),
                             nodo, "u", nodo.pro + 1, 0))
    expNodos.append(crarNodo(movimiento(nodo.estado, 1),
                             nodo, "d", nodo.pro + 1, 0))
    expNodos.append(crarNodo(movimiento(nodo.estado, 2),
                             nodo, "l", nodo.pro + 1, 0))
    expNodos.append(crarNodo(movimiento(nodo.estado, 3),
                             nodo, "r", nodo.pro + 1, 0))
    expNodos = [nodo for nodo in expNodos if nodo.estado != None]
    return expNodos
