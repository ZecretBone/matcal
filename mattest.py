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

    b = np.array(
        np.mat('[-97.27,47.03,-24.84,-82.13,59.61,-11.58,57.35,43.29,-73.13,-71.79,-35.61,32.12,-48.79,72.02,11.69;6.22,-69.02,42.85,-1.7,45.2,-38.71,-26.23,-77.99,-94.32,63.84,-38.65,48.27,-16.48,-29.45,81.11;69.75,86.36,29.91,-44.38,-71.54,29.32,42.38,-57.01,-97.53,70.78,33.19,87.2,-82.02,17.04,90.29;90.25,38.03,-19.8,-88.7,26.53,70.6,-33.36,92.07,-73.39,16.0,62.78,-11.33,-55.26,49.67,30.95;96.74,-20.44,-28.71,-28.26,95.74,-70.36,19.0,-2.08,35.39,-5.86,-21.88,-44.38,-11.55,19.67,36.04;-85.61,31.3,-73.22,-83.04,95.7,39.02,84.01,1.16,-84.18,-15.2,-67.12,0.53,-15.67,-46.89,-99.78;-9.31,-50.45,-20.48,45.12,-1.17,-50.67,19.8,-56.92,-21.97,-16.06,72.48,-57.31,-78.92,29.91,16.22;-27.34,-58.46,55.93,-4.18,-96.71,-1.34,43.88,68.42,-44.64,49.38,-49.53,3.04,-29.5,-22.05,7.36;-39.39,62.79,-31.55,-98.82,-42.61,44.54,-32.34,-48.74,8.25,-10.89,-31.49,-47.25,8.91,29.89,17.15;-41.58,-27.14,21.82,-24.69,-92.99,-30.84,-41.4,72.36,13.4,-46.57,43.35,-1.79,76.3,64.18,-45.42;-99.91,-27.93,-34.68,-18.36,-94.6,99.96,86.29,24.53,-80.3,-88.78,97.61,89.29,-8.06,-14.88,99.47;-51.16,-1.34,96.25,32.55,50.73,99.44,86.83,29.49,71.14,57.41,52.77,82.5,65.01,75.29,-42.15;84.16,-10.14,53.28,2.05,-0.08,48.56,-44.58,90.95,-96.54,-47.82,-74.47,-96.08,-83.9,8.8,85.22;-87.68,19.54,-93.14,67.03,77.74,80.71,77.97,-0.53,89.49,-98.74,48.74,79.54,0.68,21.78,-33.16;-28.27,-42.34,36.06,7.18,75.44,-3.79,-67.77,99.88,8.69,-19.41,78.78,-76.09,-20.37,-56.41,-18.83]'))
    an = np.array(
        np.mat('[5.0;4.0;1.0;2.0;5.0;6.0;8.0;4.0;11.0;25.0;55.0;1.0;5.0;4.0;8.0]'))

    b = np.array(
        np.mat('[8]'))
    an = np.array(
        np.mat('[9]'))

    b = np.array(np.mat('[1 2 1; 2 -1 1; 4 3 3; 2 -1 3]'))
    an = np.array(
        np.mat('[1; 2; 4; 5]'))

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
    # print(test_inv(b))
    print("done test invert")
