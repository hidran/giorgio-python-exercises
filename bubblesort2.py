def bubble_sort_classico(insieme, dimensione):
    # Ripetiamo il processo per un numero massimo di volte pari alla dimensione dell'array
    for i in range(dimensione):
        scambio = False
        
        # Il ciclo interno parte dall'inizio (indice 0) e va in avanti.
        # Ci fermiamo a 'dimensione - i - 1' perché a ogni passaggio 'i' 
        # l'elemento più grande viene spinto in fondo, quindi gli ultimi 'i' 
        # elementi sono già ordinati e non serve ricontrollarli.
        for j in range(0, dimensione - i - 1):
            
            # Se l'elemento a sinistra è maggiore di quello a destra...
            if insieme[j] > insieme[j + 1]:
                # ...li scambiamo
                insieme[j], insieme[j + 1] = insieme[j + 1], insieme[j]
                scambio = True
                
        # Se in un intero passaggio non abbiamo fatto scambi, l'array è ordinato
        if not scambio:
            break
        
        
# Insieme iniziale di partenza
insieme = ["Barbara", "Alberto", "Paola", "Domenico", "Vincenzo", "Beatrice"]

print("Visualizzazione dell'insieme da ordinare:")
print(insieme)

# Richiamiamo la funzione passando l'array e la sua lunghezza
bubble_sort_classico(insieme, len(insieme))

print("Visualizzazione dell'insieme ordinato:")
print(insieme)