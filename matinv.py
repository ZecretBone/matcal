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
                    a["detlog"].append(str(np.array(m)))
                    print("Row swapped")
                    jj = srow + 1
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
                tomult = (m[j, i]/m[nr, i])
                print(tomult)
                m[j] = m[j]-(m[nr]*tomult)
                a["detlog"].append(str(np.array(m)))
                j += 1
            i += 1
            nr += 1
    dettext = ""
    if not invertible:
        det = 0
        dettext = "determinant = 0"
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
        dettext += "= "+str(det)
    a["detlog"].append(dettext)
    a["det"] = det

    return a


def make_rref():
    print("rrefing...")


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
    if ans["det"] != 0:
        ans["invertible"] = False
        ans["reason"] = "Since determinant equal to 0 so it is not invertible"
        return ans
