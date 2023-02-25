import numpy as np
from matfunc import *


def test_element(e, an):
    x = elemental(e, an)
    return x


if __name__ == '__main__':
    # for i in range(2):
    #     for j in range(i+1, 3):
    #         print("i")
    #         print(i)
    #         print("j")
    #         print(j)

    # incon
    b = np.array(
        np.mat('[1 1 1 1 1;-1 -1 0 0 1;-2 -2 0 0 3; 0 0 1 1 3;1 1 2 2 4]'))
    an = np.array(np.mat('[1; -1; 1; -1; 1]'))

    # con but free var
    b = np.array(
        np.mat('[1 1 1 1 1; -1 -1 0 0 1; -2 -2 0 0 3; 0 0 1 1 3; 1 1 2 2 4]'))
    an = np.array(np.mat('[1; -1; 1; 3; 4]'))

    print("init MAT")
    print(b)
    print("init ANS")
    print(an)
    print("done init")
    print(test_element(b, an))
