lista = [3,3,4,44,44]

campione = lista[0]
omogena = True
for x in lista:
    print(x, campione,"\n")
    if x != campione:
        omogena = False
        break
if omogena != True:
    print("lista non omogena")
else:
     print("lista omogena")