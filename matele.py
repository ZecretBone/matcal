import numpy as np


def multback(a):
    i = len(a)-1
    while i > 0:
        i -= 1
    return


def mult(a, b):
    return a*b


def checkzero(e):
    iszero = True
    for i in range(len(e)):
        print(i)
        for j in range(i+1):
            if e[i, j] != 0:
                iszero = False
                break

    return iszero


def notzero(e):
    index = []
    for i in range(len(e)):
        print(i)
        for j in range(i+1):
            if e[i, j] != 0:
                index = [i, j]
                break

    return index


def swapper(e, i, j):
    return e


def square(e):
    total = e.shape
    srow = total[0]
    scol = total[1]
    h1 = np.eye(srow)
    print("print identity")
    print(h1)
    answer = {}
    answer["original"] = e
    answer["eye"] = []
    if e[0, 0] == 0:
        i = 0
        swap = False
        while e[i, 0] == 0 and i != srow:
            i += 1
        if e[i, 0] != 0:
            swap = True
        if swap:
            print(i)
            e[(0, i)] = e[(i, 0)]
            print(e)
            print("end swap")
            answer["swapped"] = e
    while not checkzero(e):
        x = notzero(e)

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
