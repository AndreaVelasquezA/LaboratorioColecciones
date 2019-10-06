import numpy as np

np_array = np.array((1, 5, 20, 10, 7, 2, 20))
print(np.where(max(np_array)== np_array))


#numero mayor de una lista o matriz

print(a.max(axis=1))

#separar cada fila

for i in range(len(a)): 
    print("departamento"),(i+1)
    for j in range(len(a[i])): 
         print(a[i][j])

#diccionario

meses = {"0":enero,"1":febrero,"2":marzo,"3":abril,
         "4":mayo,"5":junio,"6":julio,"7":agosto,
         "8":septiembre,"9":octubre,"10":noviembre,"11"diciembre,}

#funcion para hallar el numero mayor
def Maximo(lista):
    grande=0
    for numero in lista:
        if numero>grande:
            grande=numero
    return grande
 
lista1=[7,8,4]
Masgrande=Maximo(lista1)
print(Masgrande)

#funcion para el promedio de valores
def promedio(valores):
	sumaParcial=0
	for valor in valores:
		sumaParcial+=valor
	#La funcion len calcula la longitud del arreglo, que va a ser el valor por el cual habra que dividir para obtener un promedio
	cantidadValores = len(valores)
	#En el calculo del promedio, le digo a Python que inteprete a cantidadValores como decimal y no como entero, para que me devuelva un resultado decimal. Esto lo hago poniendo la funcion float()
	return sumaParcial/float(cantidadValores)

#Llamamos a la funcion de impresion por consola (print) para que muestre el resultado de llamar a la funcion "promedio" con el arreglo "valores" como argumento
valores= (a.max(axis=1))
print(promedio(valores))





