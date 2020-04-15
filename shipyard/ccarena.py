# Inicialitation
import math
# ListaTKs
Tanques=[0,1,2,3,4,5,6]

Eslora=float(input("Eslora: "))
Manga=float(input("Manga: "))
EscoraInicial=float(input("Escora: "))


CaladoProa=float(input("CPr: "))
CaladoPopa=float(input("CPp: "))

AsientoInicial=float(CaladoPopa-CaladoProa)

print("Asiento:", AsientoInicial)
MaestraF=float(input("MaestraF: "))

CorreccionAsiento=(AsientoInicial*MaestraF)/Eslora
CaladoMedioInicial=float((CaladoPopa+CaladoProa)/2)
CaladoCorregidoAsiento=CaladoMedioInicial+CorreccionAsiento

print("Asiento I:",AsientoInicial)
print("C/A",CorreccionAsiento)
print("Calado C/A:", CaladoCorregidoAsiento)

# Correccion por Asientos:

NumeroTanquesDamaged=input("No. Damaged TKs: ")
TanquesRestantes=float(NumeroTanquesDamaged)

print("Calculo de Asientos: ")

while TanquesRestantes>0:

    TanqueNumero=0

    print("Tanque No.",[1])
    MaestraGTanque=float(input("MaestraG:"))
    AsientoLongitudinalTanque=float((MaestraGTanque*AsientoInicial)/Eslora)

    LineaCentralGTanque=float(input("LCg Tk:"))
    AsientoTransversalTanque=float(LineaCentralGTanque*math.tan(EscoraInicial))

    AsientoTotalTanque=AsientoLongitudinalTanque+AsientoTransversalTanque
    CaladoInicialGdelTanque=CaladoCorregidoAsiento+AsientoTotalTanque

    print("A.Long.=",AsientoLongitudinalTanque)
    print("A.Transv.=",AsientoTransversalTanque)
    print("A.Total Tk.=", AsientoTotalTanque)
    print("C.I. en g del TK.:", CaladoInicialGdelTanque)



    TanquesRestantes=TanquesRestantes-1


    










