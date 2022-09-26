#Hacer un programa que pida un numero comprendido entre 5 y 20 , de lo contrario se volvera a pedir el programa mostrara todos los numeros pares
#que se encuntran entre  y el numero que se escribio 



num1= int(input("Dijita un numero:"))
num2 = int(input("Dijita un numero:"))
if num1%2==0 and num2%2==0:
 print("Ambos numeros son par")
elif num1%2==0 and num2%2!=0:
 print(f"{num1}es par")
elif num1%2!=0 and num2%2==0:
      print(f"{num2}es par")
else:
     print("Ambos son impares")
    


 
