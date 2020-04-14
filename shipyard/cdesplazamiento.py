# Parte Inicial
# Anotation

import math

EsloraPerpendiculares=float(input("Eslora PP: "))
Manga=float(input("Manga: "))
DesplazamientoInicial=float(input("Desplazamiento I: "))
EscoraInicial=float(input("Escora Inicial: "))

CaladoInicialProa=float(input("Calado Inicial Pr: "))
CaladoInicialPopa=float(input("Calado Inicial Pp: "))

CaladoMedio=(CaladoInicialProa+CaladoInicialPopa)/2
AsientoInicial=CaladoInicialPopa-CaladoInicialProa

print("Calado Medio:", CaladoMedio)
print("Asiento: ",Asiento)

MaestraFlotacionInicial=float(input("Maestra F Ini: "))

CorreccionAsientoInicial=(AsientoInicial*MaestraFlotacionInicial)/EsloraPerpendiculares

CaladoMedioInicialCA=CaladoMedioInicial+CorreccionAsiento

print("C/A: ", CorreccionAsiento)
print("CmC/A: ", CaladoMedioInicialCA)

# FUNCTION THAT 1. ASKS FOR VALUES AND 2. LETS YOU CALCULATE THEM

DesplazamientoInicial=DesplazamientoInicial
KMTInicial=KMTInicial
MaestraC=0.0
MaestraFlotacionInicial=0.0
ToneladasCentimetroInicial=0.0
SuperficieFlotacionInicil=0.0
MomentoAsientoUnitarioInicial=0.0





def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Datos Enunciado")
    print ("2. Curvas Hidrost.")
    print ("3. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Datos Enunciado: ")
        DesplazamientoInicial=DesplazamientoInicial
        KMTInicial=KMTInicial
        MaestraC=float(input("MaestraC: "))
        MaestraFlotacionInicial=float(input("MaestraF: "))
        ToneladasCentimetroInicial=float(input("TCm: "))
        SuperficieFlotacionInicil=float(input("SF: "))
        MomentoAsientoUnitarioInicial=float(input("Mto. U: "))
    elif opcion == 2:
        print ("Curvas Hidrost: ")
        CaladoInf=input("Calado Inf: ")
        CaladoSup=input("Calado Sup: ")
        DesplazamientoInf=input("Desplz. Inf: ")
        DesplazamientoSup=input("Desplz. Sup: ")
        DifDesplazamientos=DesplazamientoSup-DesplazamientoInf
        KMTInf=input("KMTInf: ")
        KMTSup=input("KMTSup: ")
        DifKMTs=KMTSup-KMTInf
        MaestraCInf=input("Maestra C Inf:")
        MaestraCSup=input("Maestra C Sup:")
        MaestraFInf=input("Maestra F Inf: ")
        MaestraFSup=input("Maestra F Sup:")
        TCmInf=input("TCm Inf:")
        TCmSup=input("TCm Sup:")
        SuperficieFlotacionIni=input("SupFlot Inf:")
        SuperificieFlotacionSup=input("SupFlot Sup:")
        MomentoAsientoUnitarioInf=input("Mto. U Inf:")
        MomentoAsientoUnitarioSup=input("Mto. U Sup:")


    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")

KGInicial=float(input("KG Inicial: "))
MomentosInerciaTransversalesInicial=float(input("Id Transv: "))
CorreccionSuperficiesLibresInicial=MomentosInerciaTransversales/DesplazamientoInicial
KGInicialCSLibres=KGInicial+CorreccionSuperficiesLibres


print("KGInicial: ", KGInicialCSLibres)
print("CSLibres: ", CorreccionSuperficiesLibres)
print("KGiCSL: ", KGInicialCSLibres)


GMTCSLibres=KMTInicial-KGInicialCSLibres
print("KMTInicial:", KMTInicial)
print("KGi CSL: ", KGInicialCSLibres)
print("GMTCSLibres:", GMTCSLibres)



EscoraInicialRadianes=math.radians(EscoraInicial)
LineaCentralGInicial=GMTCSLibres+math.tan(EscoraInicial)

print("LC G: ", LineaCentralGInicial)


# Número de TKs Dañados
def(pedirNumeroEntero)

NumeroTanquesDañados=int(input("No. TKs Dañados: "))


salir = False
opcion = 0
 
while not salir:
 
    print ("No. Damaged TKs ")

 
    opcion = pedirNumeroEntero()
