from math import pi, tan, cos, sin
from math import radians
import numpy as np
import matplotlib.pyplot as plt

while True:
   try:
       vi = float(input("Introduzca la velocidad inicial en (m/s): "))
       break
   except ValueError:
       print("Cantidad Incorrecta")
print("Se le agrega a un objeto una velocidad de:",vi,"m/s")

while True:
   try:
       angulo = int(input("Introduzca el ángulo en grados: "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")

print("Y se lanza a un angulo de",angulo,"°")#no es necesario, lo uso para que vayamos viendo el resultado
grados = ((angulo*pi)/180)

g = float( "9.81")       

#Posicionamiento en el plano cartesiano
while True:
   try:
       x = float(input("En la posición horizontal inicial(Eje X): "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")
while True:
   try:
       y = float(input("Y posición vertical inicial(Eje Y): "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")


#Formulas
a = tan(grados)
b = ((g)/((2*vi*2)*cos(grados)*2))

#print()

ymax=(vi**2)*(np.sin(grados)*sin(grados))/(2*g)
xmax=(vi**2)*(np.sin(2*grados))/(g)
vho = vi*(cos(radians(angulo)))
vver = vi*(sin(radians(angulo)))

print ("\nAngulo de grados en radianes:",format(grados ,".2f")) #no es necesario, lo uso para que vayamos viendo el resultado, se usará en las formulas de abajo

print("\nUn proyectil lanzado con una velocidad inicial(Vi) de:",vi,"m/s a un ángulo de:",angulo,"°")
print("Iniciará su trayectoria con una velocidad horizontal de (Vxi):",format(vho,".3f"),"m/s,")
print("y una velocidad vertical de(Vyi):",format(vver,".3f"),"m/s.")

print("\nLos parámetros más relevantes de su trayectoria son:")

tmax=(vi*sin(grados))/(g)
tv=2*(tmax)

#print(str("La altura máxima  alcanzada por el proyectil es(Ymax): ")+str(ymax)+"m")
#print(str("El alcance máximo horizontal  del proyectil es(Xmax): ")+str(xmax)+"m")

print("La altura máxima alcanzada por el proyectil es(Ymax):",format(ymax,".2f"))
print("El alcance máximo horizontal del proyectil es(Xmax):",format(xmax,".2f"))

#Tiempo
print("El tiempo máximo TiMax(s) que alcanza el proyectil para el ángulo x es:",format(tmax,".2f"))
#Representa el tiempo total que tarda el proyectil en alcanzar su altura máxima y luego regresar al suelo
print("El tiempo de vuelo TiV(s) que alcanza el proyectil para el angulo x es:",format(tv,".2f"))
#Representa el tiempo total que el proyectil está en el aire desde el momento del lanzamiento hasta el momento en que impacta en el suelo

#Creación de la ventana del plano
#Definimos la ecuación de la trayectoria
def f(x):
   return(a*x-b*x**2)
x=np.linspace(0,xmax,500)       
#añadimos el subtitulo
plt.suptitle("Evento fisico simulado: Tiro parabolico.",fontsize=20,color="blue")

#añadimos las etiquetas de los ejes
plt.xlabel("Eje X",fontsize=20,color="red")                                      
plt.ylabel("Eje Y",fontsize=20,color="red")
#añadimos texto
plt.text(((np.argmax(f(x)))/2),np.max(f(x))+1,"vi=",fontsize=10)
plt.text(((np.argmax(f(x)))/2)+11,np.max(f(x))+1,(str(vi)+"m/s"),fontsize=10)
#Añadimos la rejilla en la gráfica
plt.grid(True)                                                              
plt.grid(color = '0.5', linestyle = '--', linewidth = 1)
#Añadimos los ejes
#Dibujamos y ponemos etiquetas a la gráfica
plt.text(3,1,angulo,fontsize=10)
plt.plot(x, f(x), "red", linewidth = 1, label = (str(angulo)+("°")))

plt.show()