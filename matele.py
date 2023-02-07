import numpy as np


def square(e):
    total = e.shape
    srow = total[0]
    scol = total[1]
    h1 = np.eye(srow)
    print("print identity")
    print(h1)
    if e[0, 0] == 0:
        i = 0
        swap = False
        while e[i, 0] == 0 and i != srow:
            i += 1
        if e[i, 0] != 0:
            swap = True
        print(swap)
        if swap:
            print(i)
            e[(0, i)] = e[(i, 0)]
            print(e)
            print("end swap")

    return e


def rectangle(e):
    return e


def initial_element(e):
    print(e)
    total = e.shape
    srow = total[0]
    scol = total[1]
    print("row: "+str(srow)+" col: "+str(scol))

    if srow == scol:
        result = square(e)
    else:
        result = rectangle(e)

    return result
