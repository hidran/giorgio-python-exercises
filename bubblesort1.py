def ordinamento_scambio(insieme, dimensione):
    # 'i' rappresenta il limite tra la parte di array già ordinata e quella da ordinare.
    # Inizia a -1 perché al primo giro (quando viene incrementato a 0) indica che stiamo 
    # cercando l'elemento più piccolo da mettere in prima posizione (indice 0).
    i = -1
    
    # Inizializziamo 'scambio' a True per forzare il primo ingresso nel ciclo while.
    scambio = True

    # Il ciclo continua finché non abbiamo posizionato quasi tutti gli elementi 
    # (i != dimensione - 2) E finché nell'ultimo passaggio c'è stato almeno uno scambio.
    while i != dimensione - 2 and scambio:
        # Incrementiamo 'i' per spostare in avanti il limite della parte ordinata
        i += 1
        
        # All'inizio di ogni passaggio, presumiamo che l'array sia ordinato (nessuno scambio)
        scambio = False
        
        # Ciclo interno: scorre l'array dal fondo verso l'inizio.
        # - Parte dal penultimo elemento (dimensione - 2) perché il confronto è con j+1.
        # - Si ferma all'indice 'i' (usando i - 1 come limite esclusivo del range) perché 
        #   gli elementi prima di 'i' sono già al loro posto definitivo.
        # - Usa un passo di -1 per scorrere all'indietro.
        for j in range(dimensione - 2, i - 1, -1):
            
            # Se l'elemento corrente è "maggiore" (alfabeticamente) di quello successivo...
            if insieme[j] > insieme[j + 1]:
                
                # ...li scambiamo di posto usando una variabile temporanea ('appoggio')
                appoggio = insieme[j]
                insieme[j] = insieme[j + 1]
                insieme[j + 1] = appoggio
                
                # Segnaliamo che è avvenuto almeno uno scambio in questo passaggio.
                # Questo comunicherà al ciclo while di fare un altro giro.
                scambio = True
                
        # Mostra lo stato dell'array alla fine di ogni singolo passaggio (passo I, passo II, ecc.)
        print("Passo", i + 1)
        print(insieme)

# --- BLOCCO DI TEST PRINCIPALE ---

# Insieme iniziale di partenza
insieme = ["Barbara", "Alberto", "Paola", "Domenico", "Vincenzo", "Beatrice"]

print("Visualizzazione dell'insieme da ordinare:")
print(insieme)

# Richiamiamo la funzione passando l'array e la sua lunghezza
ordinamento_scambio(insieme, len(insieme))

print("Visualizzazione dell'insieme ordinato:")
print(insieme)