# Inicialitation
import math


# Variables
# Ship's Particulars
Eslora=0.0
Manga=0.0
EscoraInicial=0.0
DF=True
AlturaDobleFondo=0.0
CaladoProa=0.0
CaladoPopa=0.0
AsientoInicial=float(CaladoPopa-CaladoProa)
MaestraF=0.0

# Calculos Iniciales
CorreccionAsiento=(AsientoInicial*MaestraF)/Eslora
CaladoMedioInicial=float((CaladoPopa+CaladoProa)/2)
CaladoCorregidoAsiento=CaladoMedioInicial+CorreccionAsiento

CaladoInicialGdelTanque=0

# DamagedTKs
Tanques=[]
DamagedTKsNumber=0

NombreTanque=str()
DobleFondo=bool()
SobreDF=bool()
EsloraTanque=float()
MangaTanque=float()
AlturaTanque=float()
MaestraGTanque=float()
LineaCentralGTanque=float()
DensidadCarga=float()
CoeficientePermeabilidad=float()
CaladoInicialGdelTanque=0.0


# Datos Iniciales del Buque
def datos_iniciales():
    Eslora=float(input("Eslora: "))
    Manga=float(input("Manga: "))
    EscoraInicial=float(input("Escora: "))
    DF=bool(input("¿DF?:"))

    if DF==True:
        AlturaDobleFondo=float(input("Altura DF: "))


    CaladoProa=float(input("CPr: "))
    CaladoPopa=float(input("CPp: "))

    AsientoInicial=float(CaladoPopa-CaladoProa)

    print("Asiento:", AsientoInicial)
    MaestraF=float(input("MaestraF: "))


    print("Asiento I:",AsientoInicial)
    print("C/A",CorreccionAsiento)
    print("Calado C/A:", CaladoCorregidoAsiento)


# Compartimentos Dañados:
def damaged_tanks():
    DamagedTKsNumber=int(input("No. Damaged TKs:"))
    TanquesRestantes=DamagedTKsNumber

    while TanquesRestantes>0:

        TanqueNumero=(DamagedTKsNumber-TanquesRestantes)+1

        print("Tanque No.",TanqueNumero)
        NombreTanque=input("Nombre del TK:")
        DobleFondo=bool(input("DF=1 WBT=0"))
        SobreDF=bool(input("YES=1; NO=0"))
        EsloraTanque=float(input("Eslora TK: "))
        MangaTanque=float(input("Manga TK:"))
        AlturaTanque=float(input("Altura TK:"))
        MaestraGTanque=float(input("MaestraG:"))
        LineaCentralGTanque=float(input("LCg Tk:"))
        DensidadCarga=float(input("Densidad Carga:"))
        CoeficientePermeabilidad=float(input("Permeabilidad:"))
        CaladoInicialGdelTanque=0.0

        AsientoLongitudinalTanque=float((MaestraGTanque*AsientoInicial)/Eslora) 
        AsientoTransversalTanque=float(LineaCentralGTanque*math.tan(EscoraInicial))
        AsientoTotalTanque=float(AsientoLongitudinalTanque+AsientoTransversalTanque)

        CaladoInicialGdelTanque=CaladoCorregidoAsiento+AsientoTotalTanque-AlturaDobleFondo

        if DobleFondo==1:
            AsientoLongitudinalTanque=0
            AsientoTransversalTanque=0
            AsientoTotalTanque=0
            CaladoInicialGdelTanque=0


        EmpujePerdidoTanque=float(EsloraTanque*MangaTanque*(CaladoInicialGdelTanque-AlturaDobleFondo)*DensidadCarga*CoeficientePermeabilidad)


        print("A.Long.=",AsientoLongitudinalTanque)
        print("A.Transv.=",AsientoTransversalTanque)
        print("A.Total Tk.=",AsientoTotalTanque)
        print("C.I.G del TK.:",CaladoInicialGdelTanque)
        print("Empuje Perd.:", EmpujePerdidoTanque)

        TanqueNumero=[TanqueNumero,NombreTanque,DobleFondo, EsloraTanque, MangaTanque, AlturaTanque, MaestraGTanque, LineaCentralGTanque, AsientoLongitudinalTanque, AsientoTransversalTanque, AsientoTotalTanque, CaladoInicialGdelTanque, EmpujePerdidoTanque]


        TanquesRestantes=TanquesRestantes-1




    

# Empuje Perdido en los Tanques










