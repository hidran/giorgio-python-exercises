def ricerca_sequenziale3(insieme, dimensione, cognome):
    # Usiamo una "bandierina" (flag booleano) per ricordarci se abbiamo 
    # trovato l'elemento almeno una volta. All'inizio è False.
    trovato = False
    
    # Usiamo un ciclo FOR perché sappiamo di dover scorrere TUTTA 
    # la lista, dall'inizio alla fine, senza scappatoie.
    for i in range(dimensione):
        
        # Se il nome corrente è quello che cerco...
        if insieme[i] == cognome:
            print("Cognome trovato in posizione:", i)
            # Alzo la bandierina! 
            trovato = True
            
            # NOTA BENE: Qui NON c'è nessun "break". Il ciclo continua
            # per controllare anche i nomi successivi.

    # Alla fine di tutto il ciclo, guardo la bandierina. 
    # Se è ancora False, vuol dire che non ho mai trovato quel nome.
    if not trovato:
        print("Cognome non trovato")