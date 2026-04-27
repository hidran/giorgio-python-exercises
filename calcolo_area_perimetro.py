main=input ("mettere A per calcolare l'area, P per il perimetro") 
while main != "A" and main !="P":
    int(input("mettere A per calcolare l'area, P per il perimetro")) 
def area_rettangolo(base,altezza):
    area = base*altezza
    return area
def perimetro_rettangolo(base,altezza):
    perimetro = 2*(base+altezza)
    return perimetro
def main():
    base=int(input("valore base:"))
    altezza=int(input("valore altezza:"))
    if main=="A":
        risultatoA=area_rettangolo(base,altezza)
        print("l' area e uguale a",risultatoA)
    if main=="P":
        risultatoP=perimetro_rettangolo(base,altezza)
        print("il perimetro e uguale a ",risultatoP)
main()