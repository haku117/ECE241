import numpy as np
from timeit import Timer

pi2 = np.pi * 2


def DFT(x):
    N = len(x)
    FmList = []
    for m in range(N):
        Fm = 0.0
        for n in range(N):
            Fm += x[n] * np.exp(- 1j * pi2 * m * n / N)
        FmList.append(Fm / N)
    return FmList


N = 1000
x = np.arange(N)
t = Timer(lambda: DFT(x))
print('Elapsed time: {} s'.format(str(t.timeit(number=1))))