def movimiento(estado, dire):
    estadoN = estado[:]
    ind = estadoN.index(0)
    if dire == 0:
        print("up")
        if ind not in [0, 3, 6]:
            temp = estadoN[ind - 1]
            estadoN[ind - 1] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            return None
    elif dire == 1:
        print("down")
        if ind not in [2, 5, 8]:
            temp = estadoN[ind + 1]
            estadoN[ind + 1] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            return None
    elif dire == 2:
        print("right")
        if ind not in [0, 1, 2]:
            temp = estadoN[ind - 3]
            estadoN[ind - 3] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            return None
    elif dire == 3:
        print("left")
        if ind not in [6, 7, 8]:
            temp = estadoN[ind + 3]
            estadoN[ind + 3] = estadoN[ind]
            estadoN[ind] = temp
            return estadoN
        else:
            return None
