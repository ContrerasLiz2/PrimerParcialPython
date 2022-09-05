#  arreglos Solos Numeros 

# Todo tiene que llevar una sangria espacios dentro de cada tema separado por temas 

from curses.ascii import isdigit

def validarNumeros (a):
    c = 0
    x = 0
    for i in  a : 
        if isdigit (a[x]):
            c+1
        x +=1
        if c == len(a):
            return True 
        else: 
            return False 



def arreglod ( ):
    res = 's'
    po= 0;
    while res == 's' or res =='s ':
            a =  input('valor')
            if validarNumeros (a):
                ar[po]=int (a)
                po +=1
            else: 
                print('Error solo se pediran numeros ')

            if po> len(ar): 
                res = input('Deseas otro valor s/n ')
            else : 
                mostrar ( )



    
    def mostrar ( ): 
        for x in ar :
            for x in ar : 
                if (x != 0):
                    print(x, ' ')
                    
    ar = [0,0,0,0,0,0,0,0,0,0]
    arreglo ()
    mostrar ( )
