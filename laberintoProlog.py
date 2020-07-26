
# f = open ("holamundo.txt","w")
# f.write("hola mundo\n")
# f.write("hola mundo2\n")
# f.close()

from pyswip import Prolog

#prolog = Prolog()
#prolog.consult("laberinto.pl")


def leer(archivo):
    return [line.splitlines()for line in (open(archivo, "r"))]

def arreglar(array):
    return[i[0].split() for i in array]


arreglo = arreglar(leer('laberinto.txt'))

fil = len(arreglo)
col = len(arreglo[0])

e = open ("conecta.txt","w")

####### horizontal #######

for f in range(fil-1):
    for c in range(col-1):

        actual = arreglo[f][c]
        abyacente = arreglo[f][c+1]

        if((actual != "|") & (abyacente != "|")):
            er = "conecta("+str(actual)+", "+str(abyacente)+").\n"

            
            
            e.write(er)

#######  vertical  ########

for f in range(fil-1):
    for c in range(col-1):

        actual = arreglo[f][c]
        abyacente = arreglo[f+1
                            ][c]

        if((actual != "|") & (abyacente != "|")):
            er = "conecta("+str(actual)+", "+str(abyacente)+").\n"
            #prolog.assertz("conecta("+str(actual)+", "+str(abyacente)+").")
            
            e.write(er)

###############

e.close()



camino = []



##for i in  prolog.query("camino([inicio],Sol)"):










