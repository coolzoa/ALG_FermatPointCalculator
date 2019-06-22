
#librerias
import math
from math import sqrt,acos,pi,sin,cos,atan,degrees

import sympy
from sympy import Eq, var, solve, symbols,Line,Symbol,Point,intersection


import ast
from ast import literal_eval
import tkinter
from tkinter import*






#constantes
angulolimite = 120

#variables
x,y = symbols('x y')


#funcion distancia entre dos puntos
def distancia(A,B):
    d = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    return d


#funcion que retorna linea
def linea(A,B):
    p1 = Point(A[0],A[1])
    p2 = Point(B[0],B[1])
    return Line(A,B)

def pendiente(A,B):
    return (B[1]-A[1])/(B[0]-A[0])
    
#funcion que retorna ecuacion de recta que pasa por 2 puntos
#retorna forma mx + c - y = 0
def ecuacion0(A,B):
    m = pendiente(A,B)
    c = Symbol('c')
    ejeY = solve(m* A[0] + c - A[1], c)[0]
    return Eq(m*x+ejeY-y,0)

#retorna ecuacion de recta entre 2 puntos
def ecuacion(A,B):
    m = pendiente(A,B)
    c = Symbol('c')
    ejeY = solve(m* A[0] + c - A[1], c)[0]
    return str(m) + "*" + 'x' + '+' + str(ejeY)

def interseccion(e1,e2):
    s = str(intersection(e1,e2))
    xp = ""
    xy = ""
    indice1 = s.find(",")
    indice2 = s.find(")")
    px = float(eval(s[9:indice1]))
    py = float(eval(s[indice1+2:indice2]))
    return [px,py]
    
    
        
    

#calculo de angulo A usando regla de coseno
def angulo(a,b,c):
    angulo = ((b**2 + c**2 - a**2)/ (2*b*c))
    return degrees(acos(angulo))

#determinar si conjunto de puntos es apropiado
def apropiado(A,B,C):
    puntos = [A,B,C]
    puntos.sort()
    if puntos[0] == puntos[1] or puntos[1] == puntos[2]:
        return False
    
    else:
        a = distancia(B,C)
        b = distancia(A,C)
        c = distancia(A,B)
        if angulo(a,b,c) > angulolimite:
            messagebox.showerror(None,"< BAC es mayor que 2pi/3")
            return False
        elif angulo(b,a,c) > angulolimite:
            messagebox.showerror(None,"< ABC es mayor que 2pi/3")
            return False

        elif angulo(c,a,b) > angulolimite:
            messagebox.showerror(None,"< ACB es mayor que 2pi/3")
            return False
        else:
            return True

#funcion que retorna tercer punto para hacer un triangulo equilatero
def puntoEquilaterod(P,Q):
    dist = distancia(P,Q)
    e1 = Eq((P[0]-x)**2 + (P[1]-y)**2,dist**2)
    e2 = Eq((Q[0]-x)**2 + (Q[1]-y)**2,dist**2)
    temp = solve([e1,e2],[x,y])
    puntos = list()
    for i in temp:
        puntos.append(list(i))

    for i in puntos:
        if P[0] == Q[0] and P[1] < Q[1]:
            if i[0] < P[0]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[1] == Q[1] and P[0] < Q[0]:
            if i[1] > P[1]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[1] == Q[1] and P[0] > Q[0]:
            if i[1] < P[1]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] == Q[0] and P[1] > Q[1]:
            if i[0] > P[0]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] > Q[0] and P[1] > Q[1]:
            if i[0] > Q[0]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] < Q[0] and P[1] > Q[1]:
            if i[1] > Q[1]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] > Q[0] and P[1] < Q[1]:
            if i[1] < Q[1]: 
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] < Q[0] and P[1] < Q[1]:
            if i[0] < P[0]:
                puntos.remove(i)
                break
            else:
                pass
    return puntos[0]

def puntoEquilateroe(P,Q):
    dist = distancia(P,Q)
    e1 = Eq((P[0]-x)**2 + (P[1]-y)**2,dist**2)
    e2 = Eq((Q[0]-x)**2 + (Q[1]-y)**2,dist**2)
    temp = solve([e1,e2],[x,y])
    puntos = list()
    for i in temp:
        puntos.append(list(i))

    for i in puntos:
        if P[0] == Q[0] and P[1] < Q[1]:
            if i[0] > P[0]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[1] == Q[1] and P[0] < Q[0]:
            if i[1] < P[1]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[1] == Q[1] and P[0] > Q[0]:
            if i[1] > P[1]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] == Q[0] and P[1] < Q[1]:
            if i[0] < P[0]:
                puntos.remove(i)
                break
            else:
                pass            
        elif P[0] < Q[0] and P[1] > Q[1]:
            if i[0] < Q[0]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] > Q[0] and P[1] < Q[1]:
            if i[0] > Q[0]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] < Q[0] and P[1] < Q[1]:
            if i[0] > Q[0]:
                puntos.remove(i)
                break
            else:
                pass
        elif P[0] > Q[0] and P[1] > Q[1]:
            if i[0] < P[0]:
                puntos.remove(i)
                break
            else:
                pass
    return puntos[0]

    
    
    


def puntoFermat(A,B,C):
    plt.ion()
    plt.close()
    if apropiado(A,B,C):
        a = distancia(B,C)
        b = distancia(A,C)
        c = distancia(A,B)
        
        lbdatos.grid_forget()
        lbdatos.delete(1,END)
        #mostrar distancias triangulo original
        lbdatos.insert(END,"Distancias entre puntos de triangulo ABC")
        lbdatos.insert(END,"Distancia BC -> " + str(a))
        lbdatos.insert(END,"Distancia AC -> " + str(b))
        lbdatos.insert(END,"Distancia AB -> " + str(c))
        lbdatos.insert(END,"--------------")

        #mostrar coordenadas de puntos equilateros
        d = puntoEquilaterod(A,B)
        lbdatos.insert(END,"Triangulo ABD")
        lbdatos.insert(END,"Coordenadas punto D: " + str(d))
        lbdatos.insert(END,"Distancia AD -> " + str(distancia(A,d)))
        lbdatos.insert(END,"Distancia BD -> " + str(distancia(B,d)))

        lbdatos.insert(END,"--------------")
        e = puntoEquilateroe(A,C)
        lbdatos.insert(END,"Triangulo ACE")
        lbdatos.insert(END,"Coordenadas punto E: " + str(e))
        lbdatos.insert(END,"Distancia AE -> " + str(distancia(A,e)))
        lbdatos.insert(END,"Distancia CE -> " + str(distancia(C,e)))

        #mostrar ecuaciones
        e1 = linea(d,C)
        e2 = linea(e,B)

        lbdatos.insert(END,"Ecuaciones:")
        lbdatos.insert(END,"Ecuacion recta DC -> " + str(e1))
        lbdatos.insert(END,"Ecuacion recta EB -> " + str(e2))

        puntoFer = interseccion(e1,e2)
        lbdatos.insert(END,"Punto de Fermat:")
        lbdatos.insert(END,"Punto F -> " + str(puntoFer))

        lbdatos.insert(END,"Distancia minimia de punto F a vertices de triangulo ABC:")
        distanciaF = distancia(puntoFer,A) + distancia(puntoFer,B) + distancia(puntoFer,C)
        lbdatos.insert(END,str(distanciaF))        
        lbdatos.grid(row=7,column=0,columnspan=2)
      
        valoresx = list()
        valoresy = list()

        listapuntos = [A,B,C,d,e,puntoFer]
        nombrespuntos = ['A','B','C','D','E','F']

        indice = 0
        for i in listapuntos:
            valoresx.append(i[0])
            valoresy.append(i[1])
            plt.text(i[0],i[1],nombrespuntos[indice])
            indice += 1

        plt.axis([-50,50,-50,50])
        plt.plot(valoresx,valoresy,'ro')
        plt.show()
        
    else:
        messagebox.showerror(None,"Los puntos no son apropiados")
        return
    


#funciones GUI
    
def verificar():
    try:
        A = [float(eax.get()),float(eay.get())]
        B = [float(ebx.get()),float(eby.get())]
        C = [float(ecx.get()),float(ecy.get())]
        puntoFermat(A,B,C)
        return
        


    except ValueError:
        messagebox.showerror(None,"Verifique que las coordenadas esten bien")
        return

app = tkinter.Tk()
import matplotlib.pyplot as plt
app.geometry('600x400')
lb1 = Label(app,text='Ingrese los puntos A B y C',font=("Times New Roman",16)).grid(row=0,column=1,columnspan=2)
lbx = Label(app,text='X',font=("Times New Roman",14)).grid(row=1,column=1)
lby = Label(app,text='Y',font=("Times New Roman",14)).grid(row=1,column=2)
lba = Label(app,text='A',font=("Times New Roman",14)).grid(row=2,column=0)
lbb = Label(app,text='B',font=("Times New Roman",14)).grid(row=3,column=0)
lbc = Label(app,text='C',font=("Times New Roman",14)).grid(row=4,column=0)
eax = Entry(app)
eax.grid(row=2,column=1)
eay = Entry(app)
eay.grid(row=2,column=2)

ebx = Entry(app)
ebx.grid(row=3,column=1)
eby = Entry(app)
eby.grid(row=3,column=2)

ecx = Entry(app)
ecx.grid(row=4,column=1)
ecy = Entry(app)
ecy.grid(row=4,column=2)

bingreso = Button(app,text="calcuar punto fermat",font=("Times New Roman",14),command=verificar)
bingreso.grid(row=5,column=1)

lbn = Label(app,text="").grid(row=6,column=0,columnspan=2)

lbdatos = Listbox(app)
lbdatos.insert(END,("Informacion sobre el triangulo"))
lbdatos.grid(row=7,column=0,columnspan=2)
lbdatos.config(height=10,width=40)










    
