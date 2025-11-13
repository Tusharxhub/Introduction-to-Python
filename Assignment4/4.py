#Write a Python program using SciPy to find the Fourier Transform of a 1D signal [1, 2, 1, 0].(Hint: Use scipy.fft.fft()).

import numpy as np
from scipy.fft import fft

signal = np.array([1, 2, 1, 0], dtype=float)
spectrum = fft(signal)

print("Signal:", signal)
print("Fourier Transform:", spectrum)