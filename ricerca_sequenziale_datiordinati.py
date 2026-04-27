def ricerca_sequenziale2(insieme, dimensione, cognome):
    i = 0
    
    # ATTENZIONE ALLA MAGIA QUI:
    # Invece di controllare se è "diverso" (!=), controlliamo se è "minore" (<).
    # Finché i nomi che leggiamo vengono PRIMA in ordine alfabetico di quello
    # che cerchiamo, continuiamo ad andare avanti.
    while insieme[i] < cognome and i != dimensione - 1:
        i += 1
        
    # Appena leggiamo un nome UGUALE o MAGGIORE, il ciclo si rompe.
    # A questo punto controlliamo se ci siamo fermati perché lo abbiamo 
    # trovato, o se ci siamo fermati per "uscita anticipata".
    if insieme[i] == cognome:
        print("Cognome trovato in posizione:", i)
    else:
        print("Cognome non trovato")