voto=int(input("inserire voto verifica: "))
if voto<5:
    print("bocciato")
elif voto>=6 and voto<=7 :
        print("sufficiente")
elif voto>=8 and voto<=10:
        print("eccellente")
else:
        print("valore non valido") 
        
