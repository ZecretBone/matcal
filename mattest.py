import numpy as np
from matfunc import *


def test_element(e):
    x = elemental(e)
    return x


if __name__ == '__main__':
    b = np.array(np.mat('0,2,0;0,1,3;2,2,1'))
    print(test_element(b))
