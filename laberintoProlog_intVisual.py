from pyswip import Prolog
import turtle
prolog = Prolog()
prolog.consult('laberinto.pl')

def leer(archivo):
    return [line.splitlines()for line in (open(archivo, "r"))]

def split(array):
    return[i[0].split() for i in array]

arreglo = split(leer('laberinto.txt'))

fil = len(arreglo)
col = len(arreglo[0])

e = open ('laberinto.pl','w')

# horizontal

for f in range(fil-1):
    for c in range(col-1):

        actual = arreglo[f][c]
        abyacente = arreglo[f][c+1]

        if((actual != "|") & (abyacente != "|")):
            er = 'conecta('+str(actual)+', '+str(abyacente)+').\n'
            e.write(er)

# vertical 

for f in range(fil-1):
    for c in range(col-1):

        actual = arreglo[f][c]
        abyacente = arreglo[f+1][c]

        if((actual != "|") & (abyacente != "|")):
            er = 'conecta('+str(actual)+', '+str(abyacente)+').\n'            
            e.write(er)

er = 'conectado(Pos1,Pos2) :- conecta(Pos1,Pos2).\n'
e.write(er)
er = 'conectado(Pos1,Pos2) :- conecta(Pos2,Pos1).\n'
e.write(er)
er = 'miembro(X,[X|_]).\n'
e.write(er)
er = 'miembro(X,[_|Y]) :- miembro(X,Y).\n'
e.write(er)
er = 'sol :- camino([inicio],Sol),write(Sol).\n'
e.write(er)
er = 'camino([fin|RestoDelCamino],[fin|RestoDelCamino]).\n'
e.write(er)
er = 'camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),\+miembro(PosSiguiente,RestoDelCamino),camino([PosSiguiente,PosActual|RestoDelCamino],Sol).\n'
e.write(er)
e.close()




solucion = []
for i in prolog.query('camino([inicio],Sol).'):
    for j in i['Sol']:
        solucion.append(j)

solucion.reverse()
print(solucion)

        
        



########################################## Dibujado ##########################################

listaLab = []

laberinto_dibujo = arreglo

#arreglo_sol = ["2","7","11","10","9","14","15","17","18","19","20","21","22","23"]
arreglo_sol = solucion
for w in range(len(arreglo_sol)):
    if (w != 0) and (w != len(arreglo_sol)-1):
        arreglo_sol[w]=str(arreglo_sol[w])

for w in range(len(arreglo_sol)):
    if (w != 0) or (w != len(arreglo_sol)-1):
        for f in range(fil):
            for c in range(col):
                if( (arreglo_sol[w] == laberinto_dibujo[f][c] )):
                    laberinto_dibujo[f][c] = "v"

for f in range(fil):
    for c in range(col):
        if(laberinto_dibujo[f][c] == "inicio"):
            laberinto_dibujo[f][c] = "i"
        if(laberinto_dibujo[f][c] == "fin"):
           laberinto_dibujo[f][c] = "f"
        if( (laberinto_dibujo[f][c] != "|") and (laberinto_dibujo[f][c] != "i") and (laberinto_dibujo[f][c] != "f") and (laberinto_dibujo[f][c] != "v")):      
            laberinto_dibujo[f][c] = "c"

      
aux = ""

for f in range(fil):
    aux = ""   
    for c in range(col):
        aux = aux + laberinto_dibujo[f][c]
    listaLab.append(aux)
print(listaLab)




wn = turtle.Screen()
wn.bgcolor("black")
wn.title("laberinto")
wn.setup(700,700)


# paredes

class Pen(turtle.Turtle):
    

    def __init__(self):

        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)
        self.color("white")

class Inicio(turtle.Turtle):
    

    def __init__(self):

        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.color("yellow")

class Fin(turtle.Turtle):
    

    def __init__(self):

        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.speed(0)
        self.color("red")
        
class Caminosolucion(turtle.Turtle):
    print("sopas")

    def __init__(self):
        
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.color("blue")

labe = []

labe.append(listaLab)


def iniciar_dibujo(listaLab):

    for f in range(len(listaLab)):
            for c in range(len(listaLab[f])):

                pared = listaLab[f][c]
                screen_x = -288 + (c * 24)
                screen_y =  288 - (f * 24)

                if(pared == "|"):

                    pen.goto(screen_x, screen_y)
                    pen.stamp()

                if(pared == "i"):

                    inicio.goto(screen_x, screen_y)
                    pen.stamp()

                if(pared == "f"):

                    final.goto(screen_x, screen_y)
                    pen.stamp()
                    

def dibujo_sol(listaLab):

    for f in range(len(listaLab)):
            for c in range(len(listaLab[f])):

                pared = listaLab[f][c]
                screen_x = -288 + (c * 24)
                screen_y =  288 - (f * 24)

                if(pared == "v"):

                    camino.goto(screen_x, screen_y)
                    pen.stamp()


pen = Pen()
inicio = Inicio()
final = Fin()
camino = Caminosolucion()
iniciar_dibujo(labe[0])
dibujo_sol(labe[0])
