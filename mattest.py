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
    b = np.array(np.mat('2,1,1;6,4,5;4,1,3'))
    an = np.array(np.mat('2;8;11'))
    print(test_element(b, an))
