'''
Created on 11/03/2013

@author: Alumno
'''

def main():
    fin = True
    x = int(input("Introduzca un numero:"))
    y = int(input("Introduzca otro numero:"))
    while(fin):
        op = input("Introduzca el tipo de operacion: ")
        
        if op == "+":
            print ("La suma es: "+str(sumar(x,y)))
            fin = False
        elif op == "-":
            print ("La resta es: "+str(restar(x,y)))
            fin = False
        elif op == "*":
            print ("La multiplicacion es: "+str(multiplicar(x,y)))
            fin = False
        elif op == "/":
            print ("La division es: "+str(dividir(x,y)))
            fin = False
        else:
            print ("Introduzca una operacion valida")
        


def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b
  
def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

main()



    