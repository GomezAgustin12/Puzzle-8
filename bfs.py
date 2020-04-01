
import crarNodo
import expNodo
expNode = expNodo.expNode
crarNodo = crarNodo.crarNodo


def bfs(inicial, meta):
    nodos = []
    nodos.append(crarNodo(inicial, None, None, 0, 0))
    while True:
        if len(nodos) == 0:
            return None
        nodo = nodos.pop(0)
        if nodo.estado == meta:
            moves = []
            temp = nodo
            while True:
                moves.insert(0, temp.op)
                if temp.pro == 1:
                    break
                temp = temp.padre
            return moves
        nodos.extend(expNode(nodo, nodos))
