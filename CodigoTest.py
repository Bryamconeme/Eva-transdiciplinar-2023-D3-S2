#Librerias que usaremos
from math import pi, tan, cos, sin
from math import radians
import numpy as np
import matplotlib.pyplot as plt

#Variables que utilizaremos
#Velocidad del objeto
while True:
   #Usé el try en todos para que solo se puedan igresar valores correctos para que siga el codigo, osea en este caso un numero flotante
   try:
       vi = float(input("Introduzca la velocidad inicial en (m/s): "))
       break
   except ValueError:
       print("Cantidad Incorrecta")
print("Se le agrega a un objeto una velocidad de:",vi,"m/s")
#Angulo lanzado
while True:
   try:
       angulo = int(input("Introduzca el ángulo en grados: "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")
print("Y se lanza a un angulo de",angulo,"°")#no es necesario, lo uso para que vayamos viendo el resultado
#Paso los grados a radianes para usarlo en las formulas
grados = ((angulo*pi)/180)
#Gravedad
g = float( "9.81")       

#Posicionamiento en el plano cartesiano 
#Eje x
while True:
   try:
       x = float(input("En la posición horizontal inicial(Eje X): "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")
#Eje Y
while True:
   try:
       y = float(input("Y posición vertical inicial(Eje Y): "))
       break
   except ValueError:
       print("\nCantidad Incorrecta\n")

#Formulas
#Para definir la ecuacion de la trayectoria
a = tan(grados)#Calcula la tangente del ángulo en radianes
b = ((g)/((2*vi*2)*cos(grados)*2))#Calcula un valor utilizando la constante g(9.81), la velocidad inicial (vi) y el coseno del ángulo en radianes (grados)
#print()

ymax=(vi**2)*(np.sin(grados)*sin(grados))/(2*g)
#Calcula la altura máxima (ymax) alcanzada por el proyectil utilizando la velocidad inicial (vi), el seno del ángulo en radianes (grados) y la constante de la gravedad(g)
xmax=(vi**2)*(np.sin(2*grados))/(g)
#Calcula el alcance máximo horizontal (xmax) del proyectil utilizando la velocidad inicial (vi), el seno del doble del ángulo en radianes (grados) y la constante de la gravedad (g).
vho = vi*(cos(radians(angulo)))
#Calcula la velocidad horizontal inicial (vho) del proyectil multiplicando la velocidad inicial (vi) por el coseno del ángulo en radianes (angulo convertido a radianes utilizando radians())
vver = vi*(sin(radians(angulo)))
#alcula la velocidad vertical inicial (vver) del proyectil multiplicando la velocidad inicial (vi) por el seno del ángulo en radianes (angulo convertido a radianes utilizando radians())

#Uso los print() para ir describiendo el problema
#Uso el ,format() para que los numeros que me de no sean tan largos
print ("\nAngulo de grados en radianes:",format(grados ,".2f")) #no es necesario, lo uso para que vayamos viendo el resultado, se usará en las formulas de abajo

print("\nUn proyectil lanzado con una velocidad inicial(Vi) de:",vi,"m/s a un ángulo de:",angulo,"°")
print("Iniciará su trayectoria con una velocidad horizontal de (Vxi):",format(vho,".3f"),"m/s,")
print("y una velocidad vertical de(Vyi):",format(vver,".3f"),"m/s.")

print("\nLos parámetros más relevantes de su trayectoria son:")

tmax=(vi*sin(grados))/(g)#Este valor representa el tiempo máximo de vuelo del proyectil
tv=2*(tmax)#Este valor representa el tiempo de vuelo total del proyectil

#print(str("La altura máxima  alcanzada por el proyectil es(Ymax): ")+str(ymax)+"m")
#print(str("El alcance máximo horizontal  del proyectil es(Xmax): ")+str(xmax)+"m")

print("La altura máxima alcanzada por el proyectil es(Ymax):",format(ymax,".2f"))
print("El alcance máximo horizontal del proyectil es(Xmax):",format(xmax,".2f"))

#Tiempo
print("El tiempo máximo TiMax(s) que alcanza el proyectil para el ángulo x es:",format(tmax,".2f"))
#Representa el tiempo total que tarda el proyectil en alcanzar su altura máxima y luego regresar al suelo
print("El tiempo de vuelo TiV(s) que alcanza el proyectil para el angulo x es:",format(tv,".2f"))
#Representa el tiempo total que el proyectil está en el aire desde el momento del lanzamiento hasta el momento en que impacta en el suelo

#Definimos la ecuación de la trayectoria
def f(x):
   return(a*x-b*x**2)
#Creación de la ventana del plano
#Con la libreria de matplotlib
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
#Se muestra la ventana
plt.show()