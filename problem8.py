import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
fig = plt.figure()

x_min = -100
x_max = 100
y_min = -100
y_max = 100

n = 200
m = 2*n + 1
x = np.linspace(x_min,x_max,m)
y = np.linspace(y_min,y_max,m)

dx = (x_max - x_min)/(2*n)
dy = (y_max - y_min)/(2*n)

x, y = np.meshgrid(x,y)

z = np.exp(-x**2 - y**2) #given function
#######################################################

kx = 2*np.pi*np.fft.fftfreq(m,d = dx)
ky = 2*np.pi*np.fft.fftfreq(m,d = dy)
kx, ky = np.meshgrid(kx, ky)

# Fourier Transform using np.fft.fft2
FT = dx*dy*np.exp(-1j*kx*x_min)*np.exp(-1j*ky*y_min)*(m/2/np.pi)*np.fft.fft2(z, norm = 'ortho')

# Fourier transform calculated analytically
FT_ana = 0.5*np.exp(-(kx**2+ky**2)/4)
#######################################################
ax1 = fig.add_subplot(121, projection = '3d')
ax1.plot_surface(kx,ky,np.real(FT), cmap = cm.hot,linewidth = 1)
ax1.set_xlabel('$k_x$')
ax1.set_ylabel('$k_y$')
ax1.set_zlabel(r'$\tilde{f}$ : Numerically')



ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(kx,ky,FT_ana,cmap=cm.cool,linewidth=1)
ax2.set_xlabel('$k_x$')
ax2.set_ylabel('$k_y$')
ax2.set_zlabel(r'$\tilde{f}$ : Analytically')



plt.tight_layout()
plt.show()
