def numero_minore(lista):
    min=lista[0]
    max=lista[0]
    for x in lista:
        if x < min:
            min = x
        if x > max:
            max=x
            
    return (min,max)        

    
    
    
     
 
lista=[3,5,8,5,3,6,8,4,1,]
minore = numero_minore(lista)
print("il numeor minore e' ", minore[0],"e il maggiore e' ", minore[1])
anni=(2008,2009)