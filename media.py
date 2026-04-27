#per un numero di materie che non sappiamo facciamo la media generale se minore di 6 bocciato
numero_materie= int(input("inserisci numero di materie scolastiche:"))
counter=0
totale=0
while counter<numero_materie:
    voto_materia=int(input("inserisci_voto materia:"))
    counter=counter+1
    totale=totale+voto_materia
media=totale/numero_materie
if media<6:
    print("la media e"+str(media)+", sei bocciato")
else:
    print("la media e"+str(media)+", sei promosso")


