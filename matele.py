import numpy as np


def varback(x, y, a):
    a["var"] = []
    n = len(y)
    i = 0
    xr = len(x)-1
    xc = len(x[0])-1
    while i < n:
        j = 0
        m = len(a["var"])
        equalto = y[n-(1+i), 0]
        xc = len(x[0])-1
        while j < m:
            equalto -= a["var"][j]*x[xr, xc]
            xc -= 1
            j += 1
        newv = equalto/x[xr, xc]
        a["var"].append(newv)
        i += 1
        xr -= 1
    return a


def multback(a):
    print("len multback")
    print(a["eye"])
    if len(a["eye"]) <= 0:
        return []
    elif len(a["eye"]) == 1:
        a["entire2"].append(a["eye"][0])
        return a["eye"][0]
    else:
        print("more than 1")
        i = len(a["eye"])-1
        print(i)
        n = a["eye"][i]
        a["entire2"].append(n)
        while i > 0:
            n = np.matmul(n, a["eye"][i-1])
            a["entire2"].append(a["eye"][i-1])
            a["entire2"].append(n)
            print(n)
            i -= 1
        return n


def mult(a, b):
    return a*b


def checkzero(e):
    iszero = True
    for i in range(len(e[0])-1):
        print("i deep")
        print(i)
        print(len(e[0])-2)
        print("end i")
        d = False
        for j in range(i+1, len(e)):
            print("j deep ")
            print(j)
            print(len(e)-1)
            print("end j ")
            if e[j, i] != 0:
                iszero = False
                d = True
                print("pos row: "+str(j)+" col: "+str(j) +
                      " which is "+str(e[j, i])+"is not zero yet")
                break
        if d:
            break

    return iszero


def notzero(e):
    index = []
    for i in range(len(e[0])-1):
        print(i)
        tobreak = False
        for j in range(i+1, len(e)):
            if e[j, i] != 0:
                index = [j, i]
                print("NOTZERO pos row: "+str(j)+" col: "+str(j) +
                      " which is "+str(e[j, i])+"is not zero yet")
                tobreak = True
                break
        if tobreak:
            break

    return index


def swapper(e, i, j, a):
    srow = a["allr"]
    scol = a["allc"]
    m = i
    # notswap = True
    # print(e[m, j])
    # return
    while e[m, j] == 0 or srow <= i:
        swap = False
        if e[m, j] != 0:
            # e[(i, m)] = e[(m, i)]
            # emerge row,col in eye
            y = np.eye(srow)
            y[(i, m)] = y[(m, i)]
            a["eye"].append(y)
            e = np.matmul(y, e)
            print("swapped")
            swap = True
            print(e)
            break
        m += 1
        if swap:
            break

    return e, a


def ridzero(e, i, j, a):
    tomult = -1*(e[i, j]/e[j, j])
    print("multer")
    print(e[i, j])
    print(e[j, j])
    print("to mult: ")
    print(tomult)
    srow = a["allr"]
    scol = a["allc"]
    y = np.eye(srow)
    y[i, j] = tomult
    print(y)
    a["eye"].append(y)
    e = np.matmul(y, e)
    print(e)

    return e, a


def findval(e, n, a):
    sr = a["allr"]
    sc = a["allc"]
    # i =


def square(e, an):
    total = e.shape
    srow = total[0]
    scol = total[1]
    h1 = np.eye(srow)
    print("print identity")
    print(h1)
    answer = {}
    answer["original"] = e
    answer["eye"] = []
    answer["entire"] = []
    answer["allr"] = srow
    answer["allc"] = scol
    answer["entire2"] = []
    ccol = -1
    print("start")
    while not checkzero(e):
        x = notzero(e)
        if x[1] != ccol:
            ccol = x[1]
            e, answer = swapper(e, x[1], x[1], answer)
        answer["entire"].append(e)
        e, answer = ridzero(e, x[0], x[1], answer)
        print("NEW")
        print(e)
        print("IDENT")
        print(answer["eye"][-1])
        answer["entire"].append(answer["eye"][-1])
        answer["entire"].append(e)

    print("nearly")
    print(e)
    tom = multback(answer)
    answer["togetans"] = []
    if tom == []:
        print("same bp")
        bp = an
    else:
        print("new bp")
        answer["togetans"] = tom
        bp = np.matmul(tom, an)
    print(bp)
    answer["firstans"] = an
    answer["newans"] = bp
    answer["newone"] = e
    answer = varback(e, bp, answer)
    print("all var backward")
    print(answer["var"])
    answer["havenan"] = False
    for c in answer["var"]:
        if np.isnan(c):
            answer["havenan"] = True

    return answer


def isconsist(e):
    carrier = {}
    total = e.shape
    srow = total[0]
    scol = total[1]
    # [tzero, getswap, stayrow]
    carrier["gather"] = []
    carrier["eye"] = []
    carrier["consist"] = True
    # three results
    # loop col
    i = 0
    tr = 0
    while i < scol:
        gather = [False, False, False]
        j1 = tr
        if 0 == e[j1, i]:
            gather[0] = True
            while j1 < srow:
                gather[1] = False
                if 0 != e[j1, i]:
                    y = np.eye(srow, scol)
                    y[(j1, tr)] = y[(tr, j1)]
                    carrier["eye"].append(y)
                    e = np.matmul(y, e)
                    gather[1] = True

                if gather[1]:
                    break
                j1 += 1
            if not gather[1]:
                gather[2] = True
        else:
            gather[0] = False

        if not gather[0] or not gather[2]:
            # run mul
            j2 = tr+1
            while j2 < srow:
                j2 += 1
            tr += 1

        carrier["gather"].append(gather)
        i += 1

    return


def rectangle(e):
    return e


def initial_element(e, an):
    print(e)
    total = e.shape
    srow = total[0]
    scol = total[1]
    print("row: "+str(srow)+" col: "+str(scol))

    if srow == scol:
        result = square(e, an)
    else:
        result = rectangle(e)

    return result
