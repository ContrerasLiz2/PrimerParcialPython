#Hacer un programa que en un arreglo de 10 posiciones , en las posiciones pares
#se almacenes numeros pares y en las impares se almacenen numeros impares 
#Una serie de numeros de inicio al fin RANGO 

def validar(k):
  if a[po]==0:
    repaso(k)

def repaso(d):
  print("Esribe un numero ")
  n = int(input("Escibre un numero diferente de 0"))
  if (a[po]==0):
      if ((k%2)==0 and (n%2)==0):
        a[k]=n
        if ((k%2)==0 and (n%2)!=0):
            a[k]=n
            if a [k] ==0:
              repaso(d)

a = {0,0,0,0,0,0,0,0,0,0}
for k in range (0,10):
    repaso(k)
    if a[k]==0:
      print(x,' ' ,a[x])                                                                                                           

#Pubic void  no tiene parametros 
