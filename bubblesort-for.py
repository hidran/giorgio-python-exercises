def ordinamento_scambio_con_for(insieme, dimensione):
    # Il ciclo 'for' esterno gestisce automaticamente l'indice 'i'.
    # 'i' andrà da 0 fino al penultimo elemento (dimensione - 1 esclusa).
    for i in range(dimensione - 1):
        
        # All'inizio di ogni nuovo passaggio, reimpostiamo la variabile a False
        scambio = False
        
        # Il ciclo interno è identico a quello del libro: 
        # parte dal penultimo elemento e scorre all'indietro fino a 'i'
        for j in range(dimensione - 2, i - 1, -1):
            
            # Se l'elemento corrente è maggiore di quello alla sua destra...
            if insieme[j] > insieme[j + 1]:
                # ...effettuiamo lo scambio
                insieme[j], insieme[j + 1] = insieme[j + 1], insieme[j]
                scambio = True
                
        print(f"Passo {i + 1}:")
        print(insieme)
        
        # L'ottimizzazione dell'uscita anticipata:
        # Se 'scambio' è ancora False dopo il ciclo interno, significa che
        # non è stato spostato nulla. L'array è già ordinato.
        if not scambio:
            print("--> Nessuno scambio effettuato in questo passo. L'ordinamento è completo. Uscita anticipata.")
            break 

# --- BLOCCO DI TEST ---

insieme = ["Barbara", "Alberto", "Paola", "Domenico", "Vincenzo", "Beatrice"]

print("Insieme iniziale:")
print(insieme)
print("-" * 40)

ordinamento_scambio_con_for(insieme, len(insieme))

print("-" * 40)
print("Risultato finale:")
print(insieme)