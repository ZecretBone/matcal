import numpy as np
from matfunc import *


def test_element(e, an):
    x = elemental(e, an)
    return x


def test_inv(e):
    x = inverse(e)
    return x


if __name__ == '__main__':
    # for i in range(2):
    #     for j in range(i+1, 3):
    #         print("i")
    #         print(i)
    #         print("j")
    #         print(j)

    print("a"*7)

    b = np.array(
        np.mat('[2,1,1;6,4,5;4,1,3]'))
    an = np.array(np.mat('[2; 8; 11]'))

    # incon
    # b = np.array(
    #     np.mat('[1 1 1 1 1;-1 -1 0 0 1;-2 -2 0 0 3; 0 0 1 1 3;1 1 2 2 4]'))
    # an = np.array(np.mat('[1; -1; 1; -1; 1]'))

    # con but free var
    # b = np.array(
    #     np.mat('[1 1 1 1 1; -1 -1 0 0 1; -2 -2 0 0 3; 0 0 1 1 3; 1 1 2 2 4]'))
    # an = np.array(np.mat('[1; -1; 1; 3; 4]'))

    # con but free var2
    # b = np.array(
    #     np.mat('[1 1 1 1 1; 0 0 1 1 2; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0]'))
    # an = np.array(np.mat('[1; 0; 0; 0; 0]'))

    # con but free var 3
    # b = np.array(
    #     np.mat('[1 2 0 0; 0 3 0 0]'))
    # an = np.array(np.mat('[5; 3]'))

    # rectangle row > col
    # b = np.array(
    #     np.mat('[2 0 0;2 3 0;2 0 -3; 2 0 0]'))
    # an = np.array(np.mat('[2; -3; 3; 2]'))

    # b = np.array(
    #     np.mat('[2 0 0;2 3 0;2 0 -3]'))
    # an = np.array(np.mat('[2; -3; 3; 2]'))

    print(str(b))

    print("init MAT")
    print(b)
    print("init ANS")
    print(an)
    print("done init")
    print("testing element")
    print(test_element(b, an))
    print("done test element")
    print("testing invert")
    print(test_inv(b))
    print("done test invert")
