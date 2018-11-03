#Importar libreria random

import random

#Definir Variables

vidas = 3
movimientos = 0

#Funcion de la perdida de vidas

def perderVida():
    global vidas
    vidas=vidas-1
    print("Has perdido una vida")
    return

#Funcion de los obstaculos

def generaObstaculos(m,y,x):
    m[x][y]="*"
    m[x + 1][y]="*"
    m[x][y + 1]="*"
    m[x + 1][y + 1]="*"
    if (x%2 == 0):
        m[x][y + 2]="*"
        m[x + 1][y + 2]="*"
    else:
        m[x + 2][y]="*"
        m[x + 2][y + 1]="*"
    return

#Funcion de las direcciones en el movimiento

def traslado(m,str,numero,puntero):
    movi()
    
    if (str == "a"):
        if not(puntero[0] - numero < 0):
            for k in range(numero + 1):
                if(m[puntero[0] - k][puntero[1]] == "*"):
                    perderVida()
                    return puntero
            m[puntero[0] - numero][puntero[1]] = "M"
            m[puntero[0]][puntero[1]] = "￿"
            puntero[0] = puntero[0] - numero
            return  puntero
        else:
            perderVida()
            return puntero
        
    if (str == "b"):
        if not(puntero[0] + numero > 15):
            for k in range(numero + 1):
                if(m[puntero[0]+k][puntero[1]] == "*"):
                    perderVida()
                    return puntero
            m[puntero[0] + numero][puntero[1]] = "M"
            m[puntero[0]][puntero[1]] = "￿"
            puntero[0] = puntero[0] + numero
            return  puntero
        else:
            perderVida()
            return puntero
        
    if (str == "d"):
        if not(puntero[1] + numero > 15):
            for k in range(numero + 1):
                if(m[puntero[0]][puntero[1] + k] == "*"):
                    perderVida()
                    return puntero
            m[puntero[0]][puntero[1] + numero] = "M"
            m[puntero[0]][puntero[1]] = "￿"
            puntero[1] = puntero [1] + numero
            return  puntero
        else:
            perderVida()
            return puntero
        
    if (str == "i"):
        if not(puntero[1] - numero < 0):
            for k in range(numero + 1):
                if(m[puntero[0]][puntero[1] - k] == "*"):
                    perderVida()
                    return puntero
            m[puntero[0]][puntero[1] - numero]= "M"
            m[puntero[0]][puntero[1]] = "￿"
            puntero[1] = puntero[1] - numero
            return  puntero
        else:
            perderVida()
            return puntero

#Funciones de variables

def movi ():
    global movimientos
    movimientos = movimientos + 1
    return

def valida (puntero,meta):
    if (puntero[0] == meta[0] and puntero[1] == meta[1]):
       return False
    else :
       return True
    
def validar (matriz,palabra):
    for i in range (matriz.len):
        if (matriz[i] == palabra):
            return False
    return True

#Funcion de tamaño del tablero

print (" ")
def imprimeTablero (m):
    for i in range (16):
        for j in range( 16):
            print (m[i][j], end=" ")
        print("")
    print("")
    print("")
    return

#Definir tamaño de mapa

conti = True
matriz = []
for i in range (16):
    matriz.append ([])
    for j in range (16):
        matriz[i].append ("-")
    
#Explicacion al usuario del algoritmo

print ("Bienvenido al juego de buscar el tesoro\n")
print ("Ingrese su nombre:")
nom = input()
print ("\n¡Hola!", nom)

#Historia del juego

print ("\nNuestro amigo Esteban acaba de perder su notebook y justo")
print ("en este momento acaban de iniciar las ofertas en Steam.")
print ("Ayuda a nuestro amigo para que encuentre su notebook y gaste todo su  ")
print ("dinero en juegos que no jugara y que lo dejarán sin comer el resto del mes.")

#Preguntar al usuario si desea ver las instrucciones

print ("\n¿Deseas ver las instrucciones? [s/n]:")
resp = input()
if resp == 's':
    
#Mostrarle las instrucciones al usuario

    print ("\nEl objetivo del juego es alcanzar el tesoro en la menor cantidad")
    print ("de movimientos posibles mientras evitas los obstáculos, para ello")
    print ("debes ingresar la coordenadas d(derecha), i(izquierda), a(arriba), b(abajo)")
    print ("y el número de espacios a mover (de al 1 al 15).")
    print ("\nTienes 3 vidas, las cuales pierdes al chocar contra un obstáculo o al salir del mapa.")
    print ("\nDiviertete y buena suerte", nom)

#El usuario ingresa la posicion en la que quiere que aparezca el movil

print ("\nIngresa la posicion del movil en la que quieres comenzar [0, 15]")
x = int(input())
while x < 0 or x > 15:
    print ("\n¡ERROR! Debes ingresar un numero entre 0 a 15")
    x = int(input())

#Definir variables del tablero (movil y tesoro)

print (" ")
matriz[15][x] = "M"
puntero=[15,x]
y=random.randint (0,15)
matriz[0][y] = "T"
meta=[0,y]

#Generar los obstaculos

generaObstaculos(matriz,0,random.randint (1,3)+9)
generaObstaculos(matriz,9,random.randint (1,3)+9)
generaObstaculos(matriz,12,random.randint (1,3)+5)
generaObstaculos(matriz,4,random.randint (1,3)+5)
generaObstaculos(matriz,random.randint (1,3),random.randint (1,4))

#Imprimir el tablero

imprimeTablero(matriz)

#Preguntar al usuario la direccion

while (conti and vidas > 0):
    str = input("¿En que dirreccion se desea mover? [a(Arriba), b(Abajo),d(Derecha),i(Izquierda)]:")
    direcciones = ['a','b','d','i']
    boo = True
    while (boo):
        for i in range (4):
            if (direcciones[i] == str):
                boo=False
        if (boo):
            str = input("¡Error!, ¿En que direccion se desea mover? [a(Arriba), b(Abajo),d(Derecha),i(Izquierda)]")        

#Preguntar al usuario la cantidad de movimientos

    print ("Ingrese el numero de movimientos que desea:")
    x = int(input())
    while( x < 0):
        print ("¡Error!, Ingrese el numero de movimientos que desea:")
        x = int(input())

#Realizar el movimiento
        
    puntero = traslado(matriz,str,x,puntero)
    print (vidas, end=" vidas")
    print ()
    conti = valida(puntero,meta)
    imprimeTablero(matriz)

#Definir al ganador
    
if (vidas > 0):
       print ("¡Felicidades!", nom, "Has ganado con ",end="")
       print (movimientos,end=" Movimentos")
else:
    print ("Lo lamento,", nom, "perdiste");
    print ("\nGAME OVER :(")
