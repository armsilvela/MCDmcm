'''
Escribir una función que calcule el máximo común divisor de dos números y otra
que calcule el mínimo común múltiplo.

MCD es el máximo común divisor es el mayor número que los divide sin dejar resto.

mcm es el número positivo más pequeño que es multiplo de dos o mas números
'''


def mcd(n1,n2):
    rest = 0
    while n2 > 0:
        rest = n2
        n2 = n1 % n2#El mcd es el numero mayor modulo del menor
        n1 = rest
    return n1
print("El máximo común divisor es: ",mcd(225,300))


#tarea minimo comun multiplo
def mcm(n1,n2):
    res = max(n1,n2)#Se asigna a res el dato mas grande
    while True:
        if res % n1 == 0 and res % n2 == 0:#Cuando el reciduo de res entre los
        #dos numeros es cero quiere decir que encontro el primer(minimo) común nmultiplo
        #y ahi se detiene el bucle
            return res
        else:
            res += 1#Se aumenta el valor, se podría mejorar usando numeros primos
            # aunque seria mas lineas de codigo pero menos tiempo de procesamiento
print("El minimo común multiplo es: ",mcm(5,3))
