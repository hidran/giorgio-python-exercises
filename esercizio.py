#calcola la media dele materie dell'utente, chiedere per quante materie vuole fare la media, 
#per ogni materia chiedere il voto, ridare la media in valore decimale
def media_voti(n_materie,totale):
    risultato=totale/n_materie
    return risultato
n_materie=int(input("numero di materie di cui calcolare la media:"))
while n_materie<=0:
    n_materie=int(input("numero di materie di cui calcolare la media:"))

counter=0
totale=0
while counter<n_materie:
    voto=float( input("immetti voto materia:"))
    totale=totale+voto
    counter=counter+1
media=media_voti(n_materie,totale)
print("la media e ", media)
