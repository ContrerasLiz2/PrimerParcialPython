def llenar(x):
    a = int (input("Escribeun numero"))
    arr.append(a)
    x +=1
    if x < 10 :
        llenar(x)


def mostrar():
     for x in arr:
       print(x,"\n")

def pila():  #Del ultimo al primero 
    aux = len(arr)-1
    for x in range(0,len(arr)): #Esto va a ser que te muestre un arreglo cada qure elimen una posicion 
     arr.pop(aux)
    mostrar()
    aux -=1  #Para ir eliminado las posiciones
    print("Elimina otro valor")
    
#El primero que entre es el primero que sale 

def cola(): # Del primero al Ultimo 
    for x in range(0,len(arr)):
        print("x:",x," ",len(arr))
        sleep(2)
        arr.pop(0)
        print("cola")
        print(arr)


def liberarArreglo():
    valor = int(input("Esccribe la posicion a eliminar:"))
    if valor>=0 and  valor<len(ar):
        arr.pop(valor)
    else:
        print('Eliman otro valor')


# Se manejan dos tipos introducir y sacar Datos 
x = 0
arr =[]
res = "si "
llenar(x)
mostrar()
#pila()
cola()
while(res=="si"):
    liberarArreglo()
    mostrar()
    res = input("Deseas otra ejecucion si/no")

 #Utilizamos una parte logica  que es append 
 #   #arr.append  Es para alamcenar un espacio y poderlos acomodar 
 #pop eliminar # label agregar 



