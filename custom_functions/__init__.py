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

#para observar la matriz
print(a) 

#para "separar" la matriz como "listas"

s = a[[0,], :]
g = a[[1,], :]
n = a[[2,], :]
print("santander: ",s)
print("Guajira: ",g)
print("Nariño: ",n)

#para hallar la temperatura mas alta por departamento
s_1=(np.max(s))
s_2=(np.max(g))
s_3=(np.max(n))
print("la temperatura mayor en Santander :",(np.max(s)))
print("la temperatura mayor en Guajira:",(np.max(g)))
print("la temperatura mayor en Nariño:",(np.max(n)))

#para hallar la posicion de las temperaturas en cada departamento
np_array = np.array((s))
posicion_santan = (np.where(np.max(np_array)== np_array))
print("numero del mes en que la temperatura fue maxima en Santander: ",posicion_santan)

np_array = np.array((g))
posicion_guaji = (np.where(np.max(np_array)== np_array))
print("numero del mes en que la temperatura fue maxima en la Guajira: ",posicion_guaji)

np_array = np.array((n))
posicion_nariño = (np.where(np.max(np_array)== np_array))
print("numero del mes en que la temperatura fue maxima en Nariño: ",posicion_nariño)

#diccionario para saber el mes por posicion
meses = {"0":"enero","1":"febrero","2":"marzo","3":"abril",
         "4":"mayo","5":"junio","6":"julio","7":"agosto",
         "8":"septiembre","9":"octubre","10":"noviembre","11":"diciembre"}
print(meses)

#entrada para saber si hubo mas de 1 mes con maxima temperatura
b = int(input("digite la cantidad de meses en los que la temperatura fue maxima en Santander:"))
sb = s_1*b
print("total de la suma de los meses en los que la temperatura fue maxima en Santander: ",sb)

c = int(input("digite la cantidad de meses en los que la temperatura fue maxima en la Guajira:"))
gc = s_2*c
print("total de la suma de los meses en los que la temperatura fue maxima en la Guajira: ",gc)

d = int(input("digite la cantidad de meses en los que la temperatura fue maxima en Nariño:"))
nd = s_3*d
print("total de la suma de los meses en los que la temperatura fue maxima en Nariño ",nd)

#para sacar el promededio de los meses mas calientes de los 3 departamentos
temp_max_prom = (sb+gc+nd)/3
print("promedio de los meses mas calientes de los 3 departamentos: ",temp_max_prom)

#para saber cual de los 3 departamentos tiene el "promedio" mas alto o si hay mas de 1 con el "promedio" mas alto
if(sb > gc and sb > nd):
 print("El promedio mayor es el de Santander" + str(sb))
elif(sb == gc and sb == nd):
        print("todos tienen el mismo promedio ")
elif(gc > sb and gc > nd):
  print("El promedio mayor es el de la Guajira " + str(gc))
elif(sb == gc ):
         print("Santander y Guajira tienen los promedios mas altos ")  
elif(nd > sb and nd>gc):
  print("El promedio mayor es el de Nariño " + str(nd))
elif(sb==nd):
        print("Santander y Nariño tienen los promedios mas altos")
elif(gc == nd):
        print("Guajira y Nariño tienen los promedios mas altos")
 

#contadores



tempSan = 0 

tempGua = 0 

tempNar = 0

 
 

for i in range(3): 

    for j in range(12): 

        if(i==0): 

            tempSan += a[i][j] 

        if(i==1): 

            tempGua += a[i][j] 

        elif(i==2): 

            tempNar += a[i][j] 



promSan = tempSan/12 

promGua = tempGua/12 

promNar = tempNar/12 

promNac = (promSan+promGua+promNar)/3 



print("Promedio de la temperatura de santander: "+str(promSan)+"\n", 

      "Promedio de la temperatura de Guajira: "+str(promGua)+"\n", 

      "Promedio de la temperatura de Nariño: "+str(promNar)+"\n", 

      "Promedio de la temperatura Nacional: "+str(promNac)) 

