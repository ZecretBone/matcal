import numpy as np


def varback(x, y, a):
    a["var"] = []
    n = len(y)
    nn = len(y)
    i = 0
    xr = len(x)-1
    xc = len(x[0])-1
    # cleaning row all zero
    l = 0
    print("var finding")
    print(nn)
    while l < nn:
        # print("row run")
        stack = 0
        ll = 0
        while ll < len(x[0]):
            # print("col run")
            if x[l, ll] == 0:
                stack += 1
            ll += 1
        # print("stack: "+str(stack))
        # print("len col: "+str(len(x[0])))
        if stack != len(x[0]):
            # print("switch to row: "+str(l))
            xr = l
            n = l+1
        l += 1
    print("var back from row: "+str(n))
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
    e = np.round(e, 30)
    for i in range(len(e[0])-1):
        print("i deep")
        print(i)
        # print(len(e[0])-2)
        print("end i")
        d = False
        for j in range(i+1, len(e)):
            print("j deep ")
            print(j)
            # print(len(e)-1)
            print("end j ")
            if e[j, i] != 0:
                iszero = False
                d = True
                print("pos row: "+str(j)+" col: "+str(i) +
                      " which is "+str(e[j, i])+"is not zero yet")
                break
        if d:
            break

    return iszero


def notzero(e):
    index = []
    e = np.round(e, 30)
    for i in range(len(e[0])-1):
        print(i)
        tobreak = False
        for j in range(i+1, len(e)):
            if e[j, i] != 0:
                index = [j, i]
                print("NOTZERO pos row: "+str(j)+" col: "+str(i) +
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
    e = np.round(e, 30)
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
    e = np.round(e, 30)
    print("mult tester: ")
    print(str(e[i, j]/e[j, j]))
    tomult = -1*(e[i, j]/e[j, j])
    print("my mult : -1*"+str(e[i, j])+"/"+str(e[j, j]))
    print("multer")
    # print(e[i, j])
    # print(e[j, j])
    print("to mult: ")
    print(tomult)
    srow = a["allr"]
    scol = a["allc"]
    y = np.eye(srow)
    y[i, j] = tomult
    # print(y)
    a["eye"].append(y)
    e = np.matmul(y, e)
    # print(e)

    return e, a


def findval(e, n, a):
    sr = a["allr"]
    sc = a["allc"]
    # i =


def square(e, an, answer):
    total = e.shape
    srow = total[0]
    scol = total[1]
    h1 = np.eye(srow)
    print("print identity")
    print(h1)
    # answer = {}
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


# def iscolzero(e, a):
#     total = e.shape
#     srow = total[0]
#     scol = total[1]
#     i = 0
#     while i < scol:

#         i += 1

def getvar(n, t):
    i = 0
    s = 0
    while i < len(n):
        if n[i][0] == t:
            s = n[i][1]
            break
        i += 1
    return s


def isconsist(e, a, carrier):
    carrier = {}
    total = e.shape
    srow = total[0]
    scol = total[1]
    # [tzero, getswap, stayrow]
    carrier["gather"] = []
    carrier["eye"] = []
    carrier["consist"] = True
    carrier["freevar"] = []
    carrier["novar"] = []
    carrier["consistlog"] = []
    # three results
    # loop col
    carrier["consistlog"].append(np.array(e))
    carrier["consistlog"].append(np.array(a))
    pout = False
    i = 0
    tr = 0
    while i < scol:
        print("running col")
        if not pout:
            gather = [False, False, False]
            j1 = tr
            print("checking row,col: "+str(j1)+", "+str(i))
            if 0 == e[j1, i]:
                gather[0] = True
                while j1 < srow:
                    gather[1] = False
                    if 0 != e[j1, i]:
                        y = np.eye(srow)
                        y[(j1, tr)] = y[(tr, j1)]
                        carrier["eye"].append(y)
                        e = np.matmul(y, e)
                        a = np.matmul(y, a)
                        print("swapped: ")

                        carrier["consistlog"].append(np.array(e))
                        carrier["consistlog"].append(np.array(a))
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
                if j2 == srow:
                    pout = True
                while j2 < srow:
                    # tomult = -1*(e[j2, i]/e[tr, i])
                    print("running row")
                    tomult = (e[j2, i]/e[tr, i])
                    print(tomult)
                    # y = np.eye(srow, scol)
                    # y[j2, i] = tomult
                    # newsave = e[j2]-(e[tr]*tomult)
                    e[j2] = e[j2]-(e[tr]*tomult)
                    a[j2] = a[j2]-(a[tr]*tomult)
                    carrier["consistlog"].append(np.array(e))
                    carrier["consistlog"].append(np.array(a))
                    # print(y)
                    # carrier["eye"].append(y)
                    # e = np.matmul(y, e)
                    # print("after mult e: ")
                    # print(e)
                    j2 += 1
                tr += 1
            print("END ROW")
            # print(e)

            carrier["gather"].append(gather)
            i += 1
        else:
            carrier["freevar"].append(i)
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
    print("print consistlog")
    print(carrier["consistlog"])
    carrier["consistresult"] = []
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
        if (stack == scol) and (a[k]) != 0:
            carrier["consist"] = False
        elif stack != scol:
            carrier["out"] = k
        if not carrier["consist"]:
            break
        k += 1
    print("check consistency done")

    consist_text = "It is "
    if carrier["consist"]:
        consist_text += "consistent"
        if len(carrier["freevar"]) == 1:
            consist_text += " but have 1 free variable"
        elif len(carrier["freevar"]) > 1:
            consist_text += " but have " + \
                str(len(carrier["freevar"]))+" free variables"
    else:
        consist_text += "inconsistent"
    carrier["consistresult"].append(consist_text)
    print("check all no var")
    i = 0
    while i < scol:
        j = 0
        allzero = True
        while j < srow:
            if e[j, i] != 0:
                allzero = False
            j += 1
        if allzero:
            carrier["novar"].append(i)
        i += 1

    print("isconsist: "+str(carrier["consist"]))
    print("freevar: "+str(carrier["freevar"]))
    print("novar: "+str(carrier["novar"]))
    print("current MAT: "+str(e))
    carrier["result_text"] = ""
    carrier["answer_opt"] = 1
    carrier["firster"] = 0
    carrier["colpos"] = []
    carrier["vardict"] = []

    if carrier["consist"] and len(carrier["freevar"]) > 0:
        carrier["answer_opt"] = 2
        print("finding var")
        l = 0
        while l < scol:
            if l in carrier["freevar"]:
                carrier["colpos"].append(False)
            else:
                carrier["colpos"].append(True)
                carrier["firster"] = l
            l += 1
        ll = scol-1
        while ll > carrier["firster"]:
            carrier["result_text"] += "\n"

            if ll in carrier["novar"]:
                carrier["vardict"].append([ll, "0"])
                carrier["result_text"] += "x"+str(ll+1)+" = 0"
            else:
                carrier["vardict"].append([ll, getfree(ll)])
                carrier["result_text"] += "x"+str(ll+1)+" = "+str(getfree(ll))
            ll -= 1
        o = carrier["out"]
        cl = carrier["firster"]
        print("checking all var")
        print("first not all zero for var: "+str(cl))
        print("first row not all zero: "+str(o))
        while o >= 0:
            carrier["result_text"] += "\n"
            if not cl in carrier["freevar"]:
                carrier["result_text"] += "x"+str(cl+1)+" = "
                cd = e[o, cl]
                ci = cl+1
                carrier["result_text"] += str(a[o, 0]/cd)
                current_text = str(a[o, 0]/cd)
                print(a[o, 0]/cd)
                while ci < scol:
                    if ci in carrier["novar"]:
                        print("current var = 0")
                    else:
                        carrier["result_text"] += "-"
                        carrier["result_text"] += str(e[o, ci])
                        carrier["result_text"] += "("
                        carrier["result_text"] += str(getvar(
                            carrier["vardict"], ci))
                        carrier["result_text"] += ")/"
                        carrier["result_text"] += str(cd)

                        current_text += "-("
                        current_text += str(e[o, ci])
                        current_text += "("
                        current_text += str(getvar(carrier["vardict"], ci))
                        current_text += ")/"
                        current_text += str(cd)

                    # elif carrier["colpos"][ci]:
                    #     if e[o, ci]/cd < 0:
                    #         mark = "+"
                    #         carrier["result_text"] += mark + \
                    #             str(abs(e[o, ci]/cd))
                    #     elif e[o, ci]/cd > 0:
                    #         mark = "-"
                    #         carrier["result_text"] += mark + \
                    #             str(abs(e[o, ci]/cd))

                    # else:
                    #     if e[o, ci]/cd < 0:
                    #         mark = "+"
                    #         carrier["result_text"] += mark + \
                    #             str(abs(e[o, ci]/cd))+str(getfree(ci))
                    #     elif e[o, ci]/cd > 0:
                    #         mark = "-"
                    #         carrier["result_text"] += mark + \
                    #             str(abs(e[o, ci]/cd))+str(getfree(ci))
                    ci += 1
                current_text = "("+current_text+")"
                carrier["vardict"].append([cl, current_text])
                o -= 1

            else:
                if cl in carrier["novar"]:
                    carrier["result_text"] += "x"+str(cl+1)+" = 0"
                    carrier["vardict"].append([cl, str(0)])
                else:
                    carrier["result_text"] += "x" + \
                        str(cl+1)+" = "+str(getfree(cl))
                    carrier["vardict"].append([cl, str(getfree(cl))])
            cl -= 1

        print("printing result...")
        print(carrier["result_text"])

    return carrier


def rectangle(e):
    return e


def initial_element(e, an):
    print(e)
    output = {}
    total = e.shape
    srow = total[0]
    scol = total[1]
    output["allc"] = scol
    output["allr"] = srow
    fakeE = np.array(e)
    fakeAN = np.array(an)
    print("row: "+str(srow)+" col: "+str(scol))
    output = isconsist(fakeE, fakeAN, output)
    if not output["consist"]:
        output["allc"] = scol
        output["allr"] = srow
        print("done with inconsist")
        return output
    if len(output["freevar"]) > 0:
        output["allc"] = scol
        output["allr"] = srow
        print("done with consist but have free var")
        return output
    print("calculating consist and no free var")
    print(e)
    if srow == scol:
        print("SQUARE VERSION INIT")
        output = square(e, an, output)
    else:
        print("RECTANGLE VERSION INIT")
        print("row > col only")
        output = square(e, an, output)
        # result = rectangle(e,an)
    print("all var checker: ")
    print(output["var"])
    return output
