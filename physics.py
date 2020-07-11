
import math
import matplotlib.pyplot as ply
import numpy as np

from mpl_toolkits.mplot3d import Axes3D #important
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#global constants
n_total = 8             # needs to be changed
D = 0.02                # distance between speakers
frequency = 10000        # frequency of output wave
velocity = 340           # velocity of wave. constant which is dependant on the space
amplitude = 1/n_total            # amplitude of the wave
length = velocity / frequency


def sin_time_amplitude(cx, cy, tx, ty, velocity, frequency, t):
    distance = ((tx - cx)**2 + (ty - cy)**2)**0.5
    phase = 2 * math.pi * frequency * t
    return np.sin(2 * math.pi * distance * frequency / velocity - phase)


def get_wave_strength(x, y, sx, t):
    #print(sin_time_amplitude(0, n*d, x, y, speed, f, t))
    return amplitude * sin_time_amplitude(0, sx, x, y, velocity, frequency, t)


def n_sum(x, y, t, split=False):
    sum = 0
    for n in np.arange(-(n_total-1)/2 ,(n_total-1)/2+0.1, 1):
        sum += get_wave_strength(x, y, n * D, t)
    return sum


def get_amplitude(x, y):
    return np.max((np.dstack((n_sum(x, y ,t) for t in np.linspace(0, 1/frequency, 100)))),axis=2)


def area():
    for cy in range(-2, 2, 1):
        for cx in range(3, 5, 1):
            print(n_sum(cx,cy,0), end=" ")
        print("")

# RESULTS
def wave():
    time = np.arange(0, 1 / frequency, 0.1 / frequency)
    ply.plot(time, [n_sum(1, 0, t) for t in time])


def colorGraph3D(mdist, Mdist, mwidth, Mwidth, fidelity = 0.01, ret = False):

    x = np.arange(mdist, Mdist, fidelity)
    y = np.arange(mwidth, Mwidth, fidelity)
    X, Y = np.meshgrid(x, y)
    zs = np.array(np.power(get_amplitude(np.ravel(X), np.ravel(Y)), 2))
    Z = zs.reshape(X.shape)

    if ret:
        return np.array([X, Y, Z])
    #return np.array([X, Y, Z])

    fig = ply.figure()
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Relative energy')
    # Customize the z axis.
    ax.set_zlim(0, 1.2)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_title("Sound energy from several sources")
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)


def polar(r, fidelity = np.pi/360):
    THETA = np.arange(-np.pi/2, np.pi/2, fidelity)
    rs = get_amplitude(np.ravel(r * np.cos(THETA)), np.ravel(r * np.sin(THETA)))
    ax = ply.subplot(122, projection='polar')
    ax.plot(THETA, 2*10*np.log(rs[0]))
    ax.grid(True)
    ax.set_xlabel('Intensity [db]')
    ax.set_rlabel_position(220)
    ax.set_title("Relative sound intensity at radius " + str(r) + "[m]", va='bottom')


def radialNonPolar(r):
    THETA = np.arange(-np.pi / 2, np.pi / 2, np.pi / 360)
    rs = get_amplitude(np.ravel(r * np.cos(THETA)), np.ravel(r * np.sin(THETA)))
    ax = ply.subplot(121)
    ax.plot(THETA, rs[0])
    ax.grid(False)
    ax.set_xlabel("Theta[radians]")
    ax.set_ylabel("Amplitude (relative to max amp)")
    ax.set_title("sound amplitude at radius " + str(r) + "[m]", va='bottom')


if __name__ != "__main__":
    #animationGraph()
    ply.show()
else:
    polar(2)
    radialNonPolar(2)
    colorGraph3D(-0.2, 3.8, -1, 1)
    ply.show()
