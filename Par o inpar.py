#Hacer un programa que lleve un programa de 10 posiciones nada mas numeros 1 a 50 
#El programa mostrara cuantos pares e impares se introdujieron 



num1= int(input("Dijita un numero:"))
num2 = int(input("Dijita un numero "))

if num1%2==0 and num2%2==0:
 print("Ambos numeros son par")
elif num1%2==0 and num2%2!=0:
 print(f"{num1}es par")
elif num1%2!=0 and num2%2==0:
      print(f"{num2}es par")
else:
     print("Ambos son impares")
    

   