import math



def pedirNumeroEntero():
 
    correcto=False
    num=(0)
    while(not correcto):
        try:
            num = int(input("Choose an option: "))
            correcto=True
        except ValueError:
            print('Error. Choose an option: ')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. One Weight")
    print ("2. Two Equal Weights")
    print ("3. Rumbo de Superficie")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:

# Ship Data
LOA=float(input("LOA:"))
LCG=float(input("LCG:"))
TCG=float(input("TCG:"))
KG_Inicial_FreeFloatingSurfaces

HeightDatumHigh=float(input("Datum High Height:"))
HeightDatumGrounding=float(input("Datum Grounding Height:"))
TideHeight=float(HeightDatumHigh-HeightDatumGrounding)
print("Tide Height:", TideHeight)