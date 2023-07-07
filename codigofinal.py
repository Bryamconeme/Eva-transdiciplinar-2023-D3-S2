from math import tan, cos, sin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

try:
    vi = float(input("Introduce la velocidad inicial en m/s: "))
    angulo = float(input("Introduce el ángulo en grados: "))
    x0 = float(input("Introduce la posición horizontal inicial (Eje X): "))
    y0 = float(input("Introduce la posición vertical inicial (Eje Y): "))
except ValueError:
    print("Por favor, introduce solo números.")
    exit()

angulo_rad = np.radians(angulo)

g = 9.81
a = tan(angulo_rad)
b = g / (2 * vi ** 2 * cos(angulo_rad) ** 2)
xmax = (vi ** 2 * sin(2 * angulo_rad)) / g
tmax = 2 * vi * sin(angulo_rad) / g
ymax = vi**2 * sin(angulo_rad)**2 / (2*g)
vho = vi * cos(angulo_rad)
vver = vi * sin(angulo_rad)

print("\nUn proyectil es lanzado con una velocidad inicial (Vi) de {0:.2f} m/s a un ángulo de {1:.2f}°".format(vi, angulo))
print("La velocidad horizontal inicial (Vxi) es: {0:.2f} m/s".format(vho))
print("La velocidad vertical inicial (Vyi) es: {0:.2f} m/s".format(vver))
print("\nLos parámetros más relevantes de su trayectoria son:")
print("Altura máxima alcanzada por el proyectil (Ymax): {0:.2f} m".format(ymax))
print("Alcance máximo horizontal del proyectil (Xmax): {0:.2f} m".format(xmax))
print("El tiempo de vuelo que alcanza el proyectil para el angulo x (TiV): {0:.2f} s".format(tmax))

def f(x):
   return a * x - b * x ** 2

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')
ln_txt = ax.text(0, 0, '', fontsize=10)

def init():
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax + 10)
    ax.set_title("Evento físico simulado: Tiro parabólico", fontsize=20, color="blue")
    ax.set_xlabel("Eje X", fontsize=20, color="red")
    ax.set_ylabel("Eje Y", fontsize=20, color="red")
    ax.grid(True)
    ax.grid(color = '0.5', linestyle = '--', linewidth = 1)
    return ln, ln_txt,

def update(frame):
    x = frame
    y = f(x)
    t = frame / xmax * tmax
    xdata.append(x)
    ydata.append(y)
    ln.set_data(xdata, ydata)
    ln_txt.set_text('Tiempo: {0:.2f} s, Posición: ({1:.2f}, {2:.2f})'.format(t, x, y))
    ln_txt.set_position((x, y))
    return ln, ln_txt,

frames = int(vi)
ani = FuncAnimation(fig, update, frames=np.linspace(0, xmax, frames),
                    init_func=init, blit=True, repeat=True)

plt.show()
