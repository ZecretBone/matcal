import numpy as np

# square only
# det != 0


def make_det(m, a):
    print("deting...")
    total = m.shape
    srow = total[0]
    scol = total[1]
    swap = 0
    i = 0
    nr = 0
    invertible = True
    det = 0
    a["detlog"] = []
    while i < scol:
        # check for swap
        if m[nr, i] == 0:
            print("Current pivot is zero... finding row to swap")
            jj = nr
            swapped = False
            while jj < srow:
                if m[jj, i] != 0:
                    swapped = True
                    y = np.eye(srow)
                    y[(nr, jj)] = y[(jj, nr)]
                    m = np.matmul(y, m)
                    swap += 1
                    print("swapped: "+str(swap))
                    a["detlog"].append(np.array(m))
                    print("Row swapped")
                    jj = srow + 1
                if swapped:
                    break
                jj += 1
            if not swapped:
                invertible = False
                print("No row to swap so it's not invertible")

        if not invertible:
            i = scol + 1
            break
        else:
            j = nr+1
            while j < srow:
                # np.append(m[j],m[j,i])
                # m[j] += m[j,i]
                if m[j, i] != 0:
                    tomult = (m[j, i]/m[nr, i])
                    print(tomult)
                    m[j] = m[j]-(m[nr]*tomult)
                    a["detlog"].append(np.array(m))
                j += 1
            i += 1
            nr += 1
    dettext = ""
    if not invertible:
        det = 0
        dettext = "determinant = 0"
        a["reason"] = "No row to swap so it's not invertible"
    else:
        l = 0
        dettext = "determinant = "
        det = 1
        while l < scol:
            dettext += str(m[l, l])
            det *= m[l, l]
            if l != scol-1:
                dettext += "*"
            l += 1

        if swap % 2 == 1:
            print("Row swapped odd times so det = det*(-1)")
            dettext += "* (-1)"
            det = det*(-1)
        if det == 0:
            a["reason"] = "Since determinant equal to 0 so it is not invertible"
        dettext += "= "+str(det)
    a["detresult"] = dettext
    print("printing detlog")
    print(a["detresult"])
    a["det"] = det

    return a


# def make_rref(e, a):
#     print("rrefing...")
#     a["rreflog"] = []


def inverter(e, a):
    print("adding E")

    total = e.shape
    srow = total[0]
    scol = total[1]
    y = np.eye(srow)
    print(y)
    e = np.concatenate((e, y), axis=1)
    a["invlog"].append(e)
    print(e)
    total = e.shape
    srow = total[0]
    scol = total[1]
    print("rrefing...")
    a["rreflog"] = []
    # loop up to down have swap row
    print("loop up to down have swap row")

    i = 0
    nr = 0
    while i < (scol/2):
        print("run col/2")
        if e[nr, i] == 0:
            jj = nr
            swapped = False
            while jj < srow:
                if e[jj, i] != 0:
                    swapped = True
                    y = np.eye(srow)
                    y[(nr, jj)] = y[(jj, nr)]
                    e = np.matmul(y, e)
                    a["rreflog"].append(np.array(e))
                if swapped:
                    break
                jj += 1
        j = nr+1
        while j < srow:
            if e[j, i] != 0:
                tomult = (e[j, i]/e[nr, i])
                print(tomult)
                e[j] = e[j]-(e[nr]*tomult)
                a["rreflog"].append(np.array(e))
            j += 1
        if e[nr, i] != 1:
            e[nr] = e[nr]/e[nr, i]
            a["rreflog"].append(np.array(e))
        nr += 1
        i += 1

    print("loop down to up no swap row")
    print(e)
    i = int((scol/2)-1)
    nr = srow-1
    while i > -1:
        j = nr-1
        print(j)
        print("i")
        print(i)
        while j > -1:
            print("print j")
            print(j)
            if e[j, i] != 0:
                tomult = (e[j, i]/e[nr, i])
                print(tomult)
                e[j] = e[j]-(e[nr]*tomult)
                a["rreflog"].append(np.array(e))
            j -= 1
        nr -= 1
        i -= 1
    print("end invert")
    print(e)
    inv = np.array(e[0:srow, int(scol/2):int(scol)])
    print("inverted")
    print(inv)
    a["inverted"] = inv

    return a


def init_invert(e):
    print("checking mat if it's invertible")
    print('copy original mat')
    ans = {}
    ans["invlog"] = []
    total = e.shape
    srow = total[0]
    scol = total[1]
    if srow != scol:
        ans["invertible"] = False
        ans["reason"] = "Since it is rectangle matrix so it is not invertible"
        return ans
    ans["det"] = 0
    fakeE = np.array(e)
    ans = make_det(fakeE, ans)
    print(ans)
    if ans["det"] == 0:
        ans["invertible"] = False
        return ans
    print("inverting...")
    ans = inverter(e, ans)
