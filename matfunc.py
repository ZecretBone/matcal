import numpy as np
from matele import *
from matinv import *


def elemental(a, an):
    print(a)
    x = initial_element(a, an)
    return x


def inverse(a, aa, haveans):
    print(a)
    x = init_invert(a, aa, haveans)
    return x
