#Hacer un programa que pida un dato (un estring o cadena )y si dicha cadena comienza con un numero entonces se pasara a un areglo .El programa no termina hasta que el arreglo este lleno 5 posic
#Ejemplo 1 de como resolverlo 
p=0
while(p<=4):
a = input("Escribe una cadena")
r =True
ar=["-1","-1","-1","-1","-1","-1"]


nu=["1","2","3","4","5","6","7","8","9"]
while(r==True):
    for x in nu: 
        if a[0]==x:
            r = False
            if arr[p]=="-1":
                ar[p]=a
                p+1

#Recursividad Cuando un metodo se llama asi mismo para cumplir una comdicion


