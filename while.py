#chiede un numero di una tabellina, mostrare la tabellina
numero = int(input("inserisci numero:"))
moltiplicatore = 0
while numero*moltiplicatore<=numero*10:
    prodotto=numero*moltiplicatore
    print(prodotto)
    moltiplicatore=moltiplicatore+1
