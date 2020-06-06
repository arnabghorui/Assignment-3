import numpy as np
import matplotlib.pyplot as plt 
import math

def sinc(x):
	if x == 0:
		return 1
	else:
		return np.sin(x)/x

x_min = -100
x_max = 100

N = 200
m = 2*N + 1
f = np.zeros(m)
x = np.linspace(x_min, x_max, m)
dx = (x_max - x_min) / (2*N)

for i in range(m):
	f[i] = sinc(x_min + i*dx)

# Fourier Transform using np.fft
FT_f = np.fft.fft(f, norm = 'ortho')
k = 2*np.pi*np.fft.fftfreq(m, d = dx)
FT_f = dx*np.exp(-1j*k*x_min)*FT_f*np.sqrt(m/(2*np.pi))

# Fourier transform calculated analytically
def rect(k):
	if abs(k) <= 1:
		return np.sqrt(np.pi/2)
	else:
		return 0

FT_f_ana = np.zeros(m)
for i in range(m):
	FT_f_ana[i] = rect(k[i])

####################################################
plt.plot(k, FT_f, label = 'Numerically calculated')
plt.plot(k, FT_f_ana, label = 'Analytically calculated')
plt.xlabel("k")
plt.ylabel("Fourier transformed sinc(x): g(k)")
plt.legend()

plt.show()

