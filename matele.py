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


def getfree(n):
    v = ""
    free = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    if n >= 12:
        v = "r"*n
    else:
        v = free[n]
    return v


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
    answer["isconsist"] = True
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
        print("appending entire")
        answer["entire"].append(e)
        e, answer = ridzero(e, x[0], x[1], answer)
        print("NEW")
        print(e)
        print("IDENT")
        print(answer["eye"][-1])
        print("appending entire")
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


def isconsist(e, a):
    carrier = {}
    total = e.shape
    srow = total[0]
    scol = total[1]
    # [tzero, getswap, stayrow]
    carrier["gather"] = []
    carrier["eye"] = []
    carrier["consist"] = True
    carrier["freevar"] = []
    # three results
    # loop col
    i = 0
    tr = 0
    while i < scol:
        gather = [False, False, False]
        j1 = tr
        print("checking row,col: "+str(j1)+", "+str(i))
        if 0 == e[j1, i]:
            gather[0] = True
            while j1 < srow:
                gather[1] = False
                if 0 != e[j1, i]:
                    y = np.eye(srow, scol)
                    y[(j1, tr)] = y[(tr, j1)]
                    carrier["eye"].append(y)
                    e = np.matmul(y, e)
                    a = np.matmul(y, a)
                    print("swapped: ")

                    print(e)
                    gather[1] = True

                if gather[1]:
                    break
                j1 += 1
            if not gather[1]:
                gather[2] = True
            if gather[2]:
                carrier["freevar"].append(i)

        else:
            gather[0] = False

        if not gather[0] or not gather[2]:
            # run mul
            j2 = tr+1
            while j2 < srow:
                # tomult = -1*(e[j2, i]/e[tr, i])
                tomult = (e[j2, i]/e[tr, i])
                print(tomult)
                # y = np.eye(srow, scol)
                # y[j2, i] = tomult
                # newsave = e[j2]-(e[tr]*tomult)
                e[j2] = e[j2]-(e[tr]*tomult)
                a[j2] = a[j2]-(a[tr]*tomult)
                # print(y)
                # carrier["eye"].append(y)
                # e = np.matmul(y, e)
                # print("after mult e: ")
                # print(e)
                j2 += 1
            tr += 1
        print("END ROW")
        print(e)

        carrier["gather"].append(gather)
        i += 1
    # print("multback eye")
    # newa = []
    # if len(carrier["eye"]) <= 0:
    #     newa = []
    # elif len(carrier["eye"]) == 1:
    #     # a["entire2"].append(a["eye"][0])
    #     newa = carrier["eye"][0]
    # else:
    #     print("more than 1")
    #     i = len(carrier["eye"])-1
    #     print(i)
    #     n = carrier["eye"][i]
    #     # a["entire2"].append(n)
    #     while i > 0:
    #         n = np.matmul(n, carrier["eye"][i-1])
    #         # a["entire2"].append(a["eye"][i-1])
    #         # a["entire2"].append(n)
    #         print(n)
    #         i -= 1
    #     newa = n
    # if newa != []:
    #     a = np.matmul(newa, a)
    print("time for consistency")
    print("check every row")
    print("current MAT")
    print(e)
    print("current ANS")
    print(a)
    carrier["out"] = -999
    k = 0
    while k < srow:
        l = 0
        stack = 0
        while l < scol:
            if e[k, l] == 0:
                stack += 1
            l += 1
        if stack == scol:
            if a[k] != 0:
                carrier["consist"] = False
                break
            else:
                if carrier["out"] == -999:
                    carrier["out"] = k
        if not carrier["consist"]:
            break
        k += 1
    print("check consistency done")

    print("isconsist: "+str(carrier["consist"]))
    print("freevar: "+str(carrier["freevar"]))

    if carrier["consist"] and len(carrier["freevar"]) > 0:
        print("finding var")
        o = carrier["out"]-1
        while o >= 0:
            p = 0
            while p > 100:
                if p in carrier["freevar"]:
                    print("free var replace")
            o -= 1

    return carrier


def rectangle(e):
    return e


def initial_element(e, an):
    print(e)

    total = e.shape
    srow = total[0]
    scol = total[1]
    fakeE = np.array(e)
    fakeAN = np.array(an)
    print("row: "+str(srow)+" col: "+str(scol))
    consist = isconsist(fakeE, fakeAN)
    if not consist["consist"]:
        print("done with inconsist")
        return consist
    if len(consist["freevar"]) > 0:
        print("done with consist but have free var")
        return consist
    print("calculating consist and no free var")
    print(e)
    if srow == scol:
        print("SQUARE VERSION INIT")
        result = square(e, an)
    else:
        print("RECTANGLE VERSION INIT")
        result = rectangle(e)

    return result
