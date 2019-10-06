import numpy as np  

import random  

 
 

a= np.zeros((3,12)) 



 

for i in range(len(a)): 

    for j in range(len(a[i])): 

        if(i == 0): 

            dep = "Santander" 

        elif(i == 1): 

            dep  = "Guajira" 

        else: 

            dep = "Nariño" 

        a[i][j] = (random.randint(18,28))




#para encontrar el valor mayor dentro de cada fila que corresponde a cada departamento
print(a) 

#para hallar la temperatura mayor en cada departamento
max_temp_dep = (a.max(axis=1))

#contadores

santander = 0
guajira = 0
nariño = 0
#para "separar" la matriz como una lista"
s= for i in range(len(a)): 
    print("departamento"),(i+1)
    if (santander == 0):
        santander =+ s
    elif (guajira == 0):
         guajira =+ s
    elif(nariño == 0):
        nariño =+ s

    for j in range(len(a[i])): 
         print(a[i][j])
print(max_temp_dep )
print(santander)
print(guajira)
print(nariño)