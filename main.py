import numpy as np
import matplotlib.pyplot as plt

mmax = 1200
ko = 10**6

#step one: peak force, fpeak(N), for a given distance, x(m)

def fp(x):
    return (1000 + 9 * (x**2) - 183 * x) * 1000


#step two: load duration, td(s), for a given distance x(m)

def td(x):
    return (20 - 0.12 * (x**2) + 4.2 * x) / 1000


#step three: maximum displacement zmax (m)

def disp(x, k, m, g=0):

    w = np.sqrt(k / m)

    Tmax = 2 * np.pi * np.sqrt(mmax / ko)
    tmax = 2 * Tmax

    t = 0
    i = 0.001

    zmax = 0

    F = fp(x)
    T = td(x)

    if g == 1:
        times = []
        zvalues = []

    while t <= tmax:

        if t <= T:
            z = (F/k * (1 - np.cos(w*t)) + F/(k*T) * (np.sin(w*t)/w - t))

        else:
            z = (F/(k*w*T) * (np.sin(w*t) - np.sin(w*(t-T))) - F/k * np.cos(w*t))

        zmax = max(zmax, z)

        if g == 1:
            times.append(t)
            zvalues.append(z)

        t += i

    if g == 1:

        fig = plt.figure(figsize=(8,5))
        axes = fig.add_subplot(111)

        axes.set_title('Blast Wall Displacement Response')
        axes.set_xlabel('Time (s)')
        axes.set_ylabel('Displacement (m)')

        axes.grid(color=(0.8,0.8,0.8), linestyle=':')
        axes.minorticks_on()

        axes.plot(times, zvalues, color='red', label='Displacement')

        axes.axhline(y=0.1, color='blue', linestyle='--', label='Failure limit (100 mm)')

        axes.legend()

        plt.show()

    return zmax

#step four: bisector method to find the distance x(m) that gives approximately 0.1m displacement, z(m)

def bisector(xL, xU, k, m):

    while (xU - xL) > 0.001:

        x = (xL + xU) / 2
        z = disp(x, k, m)

        if z > 0.1:
            xL = x
        else:
            xU = x

    return (xL + xU) / 2

#step five: find the minimum-cost design

def mincost(xL, xU):

    d = []

    for k in range(365 * 10**4, 370 * 10**4, 1000):
        for m in range(690, 710, 1):

            x = bisector(xL, xU, k, m)

            ck = 900 + 825 * ((k / 10**6) ** 2) - 1725 * (k / 10**6)
            cm = 10 * m - 2000
            cx = 2400 * ((x**2) / 4)

            d.append([ck + cm + cx, k, m, x])

    d = sorted(d)

    print("Solution:")
    print(f"Cost: £{d[0][0]:,.2f}")
    print(f"Stiffness: {d[0][1] / 10**6:.2f} MN/m")
    print(f"Mass: {d[0][2]:,.0f} kg")
    print(f"Distance: {d[0][3]:.3f} m")
    print(f"Displacement: {disp(d[0][3], d[0][1], d[0][2]) * 1000:.2f} mm")

mincost(0, 10)