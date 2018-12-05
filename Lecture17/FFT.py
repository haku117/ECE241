# Recursive FFT function

import numpy as np
from timeit import Timer

def FFT(x):
    N = len(x)
    if N <= 1: return x
    even = FFT(x[0::2])
    odd = FFT(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]


N = 1024
x = np.random.random(N)
t = Timer(lambda: FFT(x))
print('Elapsed time: {} s'.format(str(t.timeit(number=1))))


# FFT example using the Numpy fftpack

import numpy as np
from timeit import Timer

N = 10000
x = np.arange(N)
t = Timer(lambda: np.fft.fft(x))
print('Elapsed time: {} s'.format(str(t.timeit(number=1))))

# FFT example using the SciPy fftpack

import scipy
from scipy.fftpack import fft
from timeit import Timer

N = 10000
x = scipy.arange(N)
t = Timer(lambda: fft(x))
print('Elapsed time: {} s'.format(str(t.timeit(number=1))))