# Importando las librerías necesarias
from math import tan, cos, sin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Solicitando los datos al usuario
try:
    # Solicitando al usuario la velocidad inicial, ángulo, y las posiciones iniciales en los ejes x e y.
    vi = float(input("Introduce la velocidad inicial en m/s: "))
    angulo = float(input("Introduce el ángulo en grados: "))
    x0 = float(input("Introduce la posición horizontal inicial (Eje X): "))
    y0 = float(input("Introduce la posición vertical inicial (Eje Y): "))
except ValueError:
    # En caso de que el usuario introduzca un valor no numérico, se mostrará un mensaje de error y se terminará el programa.
    print("Por favor, introduce solo números.")
    exit()

# Conversión del ángulo a radianes para usar en cálculos trigonométricos.
angulo_rad = np.radians(angulo)

# Constante de gravedad
g = 9.81



# Cálculo de los parámetros de la trayectoria
# Se utilizan las ecuaciones de la física para calcular los parámetros del movimiento parabólico.
a = tan(angulo_rad)
b = g / (2 * vi ** 2 * cos(angulo_rad) ** 2)
xmax = (vi ** 2 * sin(2 * angulo_rad)) / g
tmax = 2 * vi * sin(angulo_rad) / g
ymax = vi**2 * sin(angulo_rad)**2 / (2*g)
vho = vi * cos(angulo_rad)
vver = vi * sin(angulo_rad)

# Imprimiendo los resultados
# Se muestran los resultados en un formato legible, con una precisión de dos decimales.
print("\nUn proyectil es lanzado con una velocidad inicial (Vi) de {0:.2f} m/s a un ángulo de {1:.2f}°".format(vi, angulo))
print("La velocidad horizontal inicial (Vxi) es: {0:.2f} m/s".format(vho))
print("La velocidad vertical inicial (Vyi) es: {0:.2f} m/s".format(vver))
print("\nLos parámetros más relevantes de su trayectoria son:")
print("Altura máxima alcanzada por el proyectil (Ymax): {0:.2f} m".format(ymax))
print("Alcance máximo horizontal del proyectil (Xmax): {0:.2f} m".format(xmax))
print("El tiempo de vuelo que alcanza el proyectil para el angulo x (TiV): {0:.2f} s".format(tmax))

# Definiendo la ecuación de la trayectoria
# Esta función define la trayectoria del proyectil en función de la distancia horizontal.
def f(x):
   return a * x - b * x ** 2

# Creando la gráfica
# Iniciamos una figura y un objeto de ejes para la gráfica.
fig, ax = plt.subplots()

# Variables para almacenar los datos de la trayectoria del proyectil.
xdata, ydata = [], []

# Creamos un objeto Line2D vacío para la animación del proyectil.
ln, = plt.plot([], [], 'ro')

# Creamos un objeto de texto para mostrar la posición y el tiempo actuales del proyectil.
ln_txt = ax.text(0, 0, '', fontsize=10)

# Función para inicializar el gráfico.
def init():
    # Configuramos los límites de los ejes.
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax + 10)
    
    # Configuramos el título y las etiquetas de los ejes.
    ax.set_title("Evento físico simulado: Tiro parabólico", fontsize=20, color="blue")
    ax.set_xlabel("Eje X", fontsize=20, color="red")
    ax.set_ylabel("Eje Y", fontsize=20, color="red")
    
    # Activamos la rejilla de la gráfica.
    ax.grid(True)
    ax.grid(color = '0.5', linestyle = '--', linewidth = 1)
    
    return ln, ln_txt,

# Función para actualizar el gráfico en cada frame de la animación.
def update(frame):
    # Calculamos la posición actual del proyectil.
    x = frame
    y = f(x)
    
    # Calculamos el tiempo actual en la simulación.
    t = frame / xmax * tmax
    
    # Añadimos los datos actuales a las listas de datos.
    xdata.append(x)
    ydata.append(y)
    
    # Actualizamos la posición del proyectil en el gráfico.
    ln.set_data(xdata, ydata)
    
    # Actualizamos el texto de la posición y el tiempo actuales.
    ln_txt.set_text('Tiempo: {0:.2f} s, Posición: ({1:.2f}, {2:.2f})'.format(t, x, y))
    ln_txt.set_position((x, y))
    
    return ln, ln_txt,

# El número de frames es proporcional a la velocidad inicial.
frames = int(vi)

# Creamos la animación usando FuncAnimation.
# La animación se actualizará 'frames' veces, y no se repetirá.
ani = FuncAnimation(fig, update, frames=np.linspace(0, xmax, frames),
                    init_func=init, blit=True, repeat=False)

# Mostramos la gráfica.
plt.show()
