import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

resolution = width, height = 2*(2500,)

xmin, xmax = -1.5, 1.5
xwidth = xmax - xmin

ymin, ymax = -1.5, 1.5
yheight = ymax - ymin

x,y = np.ogrid[xmin:xmax:1j*width, ymin:ymax:1j*height]

complex_plane = (x + 1j*y).T


def f(z, c):
    return z**2 + c

N = 500
c = complex(-0.8, 0.156)

max_m = 10
ns = np.zeros((height,width))
counter = 0

for i in range(N):
    T = abs(complex_plane)<=max_m
    complex_plane[T] = f(complex_plane[T], c)
    ns[T] += 1
    counter += 1
    print(f'{counter}/{N}')


julia = ns/N
#julia = 1-np.sqrt(ns/N)

fig = plt.figure()

ax = fig.add_subplot(111)
im = ax.pcolormesh(julia, cmap = cm.jet)

cbar = fig.colorbar(ax=ax, mappable=im, orientation='vertical')

xtick_labels = np.linspace(xmin, xmax, int((xwidth) / 0.5), endpoint=True)
ax.set_xticks([(x-xmin)*(width)/(xwidth) for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])

ytick_labels = np.linspace(ymin, ymax, int((yheight) / 0.5), endpoint=True)
ax.set_yticks([(y-ymin)*(height)/(yheight) for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])

plt.subplots_adjust(left=0.23, right=0.843, top=0.967, bottom=0.06)

plt.show()