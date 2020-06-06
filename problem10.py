import numpy as np 
import matplotlib.pyplot as plt 
import math
import urllib.request

with urllib.request.urlopen('http://theory.tifr.res.in/~kulkarni/noise.txt') as response:
	data = []
	for line in response:
		data.append(float(line))

Noise = np.array(data)
x = np.linspace(1,len(Noise), len(Noise))

plt.subplots()
plt.plot(x,Noise)
plt.xlabel('n')
plt.ylabel('Noise')
plt.title('Noise vs data-count graph')


dft = np.fft.fft(Noise, norm ='ortho')
k = 2*np.pi*np.fft.fftfreq(len(Noise), d = 1)

plt.subplots()
plt.plot(k, Noise)
plt.xlabel('k')
plt.ylabel('DFT of Noise')
plt.title('DFT of Noise vs K graph')
   

power_spec = np.zeros(len(k))
for i in range(len(k)):
	power_spec[i]=abs(dft[i])**2/len(k)

plt.subplots()
plt.plot(k, power_spec)
plt.xlabel('k')
plt.ylabel('Power spectrum')
plt.title('Power spectrum vs k graph')

k_min, k_max = min(k), max(k)

plt.subplots()
plt.title("Plot of binned power spectrum")
plt.hist(power_spec, range = (k_min, k_max), bins = 10, density = True)
plt.xlabel(r"bins")
plt.ylabel(r"$|\tilde{f}(k)|^2 / N$")

plt.show()

