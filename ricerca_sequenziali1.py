def ricerca_sequenziale1(insieme, dimensione, cognome):
    # Partiamo dalla prima posizione in assoluto (indice 0)
    i = 0
    
    # Continuiamo a scorrere l'array FINCHÉ si verificano DUE condizioni:
    # 1. Il nome nella casella attuale è DIVERSO da quello che cerco (!=)
    # 2. Non sono ancora arrivato all'ultima casella disponibile
    while insieme[i] != cognome and i != dimensione - 1:
        # Se non l'ho trovato e non sono alla fine, passo alla casella successiva
        i += 1
        
    # Quando il ciclo "while" finisce, dobbiamo capire PERCHÉ è finito.
    # Se il nome nella casella in cui ci siamo fermati è proprio quello cercato...
    if insieme[i] == cognome:
        print("Cognome trovato in posizione:", i)
    else:
        # ...altrimenti significa che siamo arrivati alla fine senza successo.
        print("Cognome non trovato")