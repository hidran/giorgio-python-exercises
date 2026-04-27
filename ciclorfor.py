#for x in range (1,21,1) :
#    print(x)
#for x in range (0,42,2):
#    print(x)
for x in range (101):
    cont = 0 # 9 ,3
    for y in range (2,x):
        if x%y==0:
            cont = cont +1
    if cont == 0:
        print(x)    
    
for x in range (101):
    primo = True # 9 ,3
    if x != 1 and x!=2:
        for y in range (2,x):
            if x%y==0:
                primo = False
                break
    else:
        print(x)      
    if primo:
        print(x)  