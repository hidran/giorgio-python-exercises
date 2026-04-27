result = 0
numero = ""
for i in range(0,8):
    bit = 2;
    while bit != 1 and bit !=0:
        bit = int(input(f"inserire il digito {i+1} digito"))
        if bit != 1 and bit !=0:
            print("${bit} non e' un bit")
    result = result + (bit*(2**i))
    numero = numero + str(bit);
numero_decimal = ''
for c in numero:
    print(numero_decimal)
    numero_decimal =c + numero_decimal
print(f"il numero {numero_decimal} in decimale e' {result}")  
