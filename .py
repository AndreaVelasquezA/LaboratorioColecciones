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

        a[i][j] = int(input("Ingrese la temperatura del departamento "+ str(dep)+":")) 

 
 

print(a) 

 
 

tempSan = 0 

tempGua = 0 

tempNar = 0 

 
 

for i in range(3): 

    for j in range(12): 

        if(i==0): 

            tempSan += a[i][j] 

        if(i==1): 

            tempGua += a[i][j] 

        else: 

            tempNar += a[i][j] 

 
 

promSan = tempSan/12 

promGua = tempGua/12 

promNar = tempNar/12 

promNac = (promSan+promGua+promNar)/3 

print("Promedio de la temperatura de santander: "+str(promSan)+"\n", 

      "Promedio de la temperatura de Guajira: "+str(promGua)+"\n", 

      "Promedio de la temperatura de Nariño: "+str(promNar)+"\n", 

      "Promedio de la temperratura Nacional: "+str(promNac)) 