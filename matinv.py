import numpy as np

# square only
# det != 0


def make_det(m, a):
    print("deting...")
    det = 1
    a["det"] = det
    return


def make_rref():
    print("rrefing...")


def init_invert(e):
    print("checking mat if it's invertible")
    print('copy original mat')
    ans = {}
    ans["det"] = 0
    fakeE = np.array(e)
    ans = make_det(fakeE, ans)
    if ans["det"] != 0:
        return ans
