def ordinamento_selezione(insieme, dimensione):
    # Il ciclo esterno scorre le posizioni dell'array da riempire.
    # Ci fermiamo al penultimo elemento (dimensione - 1), perché quando 
    # avremo sistemato il penultimo, l'ultimo sarà per forza al suo posto.
    for i in range(0, dimensione - 1):
        
        # All'inizio di ogni giro, supponiamo temporaneamente che l'elemento 
        # più piccolo sia quello che si trova nella posizione attuale 'i'.
        posizione_minimo = i
        
        # Il ciclo interno serve a "esplorare" il resto dell'array alla 
        # ricerca di un elemento ancora più piccolo. 
        # Partiamo da 'i + 1' (l'elemento subito dopo) fino alla fine.
        for j in range(i + 1, dimensione):
            
            # Confrontiamo l'elemento che attualmente consideriamo il minimo
            # con l'elemento nella posizione 'j' che stiamo analizzando.
            # (Trattandosi di stringhe, il '>' valuta l'ordine alfabetico).
            if insieme[posizione_minimo] > insieme[j]:
                
                # Se troviamo un elemento "più piccolo", ci annotiamo la sua 
                # nuova posizione. Attenzione: qui NON spostiamo i dati, ci 
                # limitiamo a memorizzare DOVE si trova il nuovo minimo.
                posizione_minimo = j
                
        # Finito di esplorare la parte rimanente dell'array, controlliamo 
        # se il minimo che abbiamo trovato si trova in una posizione diversa 
        # da quella di partenza 'i'.
        if posizione_minimo != i:
            
            # Se è così, significa che abbiamo trovato un elemento più piccolo
            # e dobbiamo scambiarli di posto usando la variabile 'appoggio'.
            appoggio = insieme[i]
            insieme[i] = insieme[posizione_minimo]
            insieme[posizione_minimo] = appoggio
            
        # Stampa per farci vedere lo stato dell'array dopo ogni passaggio.
        print("Passo:", i + 1)
        print(insieme)

# --- BLOCCO DI TEST ---

# Insieme iniziale disordinato
insieme = ["Carlo", "Alberto", "Beatrice", "Domenico", "Paola", "Vincenzo"]

print("Visualizzazione dell'insieme da ordinare:")
print(insieme)

# Avviamo l'ordinamento
ordinamento_selezione(insieme, len(insieme))

print("Visualizzazione dell'insieme ordinato:")
print(insieme)