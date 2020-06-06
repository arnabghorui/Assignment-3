import numpy as np 
import matplotlib.pyplot as plt 
import math
import time

def TIMER_DFT(arr):	# Manually calculating
	length = len(arr)
	
	start = time.time()
	E = np.zeros(length)

	for p in range(length):
		for r in range(length):
			E[p] = E[p] + arr[r]*np.exp(-2*np.pi*1j*p*r/length)
	
		E[p] = E[p] / np.sqrt(length)
	
	end = time.time()
	return end - start

def TIMER_FFT(arr):	# Direct computation using fft
	start = time.time()

	E = np.fft.fft(arr, norm = 'ortho')

	end = time.time()
	return end - start

N = 100
arr_size = np.zeros(N)
dft_time = np.zeros(N)
fft_time = np.zeros(N)
j = 4
for i in range(N):
	arr_size[i] = j
	num = np.linspace(1,j,j)


	dft_time[i] = TIMER_DFT(num)
	fft_time[i] = TIMER_FFT(num)

	j+=1

plt.plot(arr_size, dft_time, label = "Direct")
plt.plot(arr_size, fft_time, label = "Using np.fft", color = 'r')

plt.xlabel('Size of array')
plt.ylabel('Time')
plt.legend()
plt.grid()
plt.show()








