def ricerca_sequenziale4(insieme, dimensione, cognome):
    i = 0
    trovato = False
    superato = False  # Nuova bandierina: indica se abbiamo "superato" il target
    
    # Continuiamo finché NON abbiamo superato il bersaglio E non siamo alla fine
    while not superato and i <= dimensione - 1:
        
        if insieme[i] == cognome:
            # L'ho trovato!
            print("Cognome trovato in posizione:", i)
            trovato = True
            i += 1  # Vado avanti per cercare altri eventuali duplicati
            
        else:
            # Se NON è uguale, devo capire se sono andato "troppo oltre"
            if insieme[i] > cognome:
                # Es: sto cercando "Chiera" e leggo "Gallo". Gallo > Chiera.
                # Alzo la bandierina 'superato' a True. 
                # Questo farà terminare il ciclo while immediatamente!
                superato = True
            else:
                # Es: sto cercando "Chiera" e leggo "Bianchi". Bianchi < Chiera.
                # Non l'ho ancora trovato, ma posso continuare a cercare.
                i += 1
                
    if not trovato:
        print("Cognome non trovato")