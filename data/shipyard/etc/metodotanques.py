import math



class Ship():
        def __init__(self):
            self.LOA=float(input("Eslora:"))
            self.Beam=float(input("Manga: "))
            self.Heel=float(input("Escora: "))
            self.ForwardDraft=float(input("CPr: "))
            self.AftDraft=float(input("CPp: "))
            self.Draft=float((CaladoProa+CaladoPopa)/2)

            # Doble Fondo
            self.DFHeight=0.0
            self.DF=bool(input("¿Tiene DF?:"))
            if self.DF==True:
                AlturaDobleFondo=float(input("Altura DF: "))
            else:
                AlturaDobleFondo=0.0
class Ship_Particulars1(CaladoPopa, CaladoProa):
    AsientoInicial=float(CaladoPopa-CaladoProa)
    MaestraF=float(input("MaestraF: "))
    CorreccionAsiento=(AsientoInicial*MaestraF)/Eslora

    CaladoCorregidoAsiento=CaladoMedioInicial+CorreccionAsiento

    print("Asiento I:",AsientoInicial)
    print("C/A",CorreccionAsiento)
    print("Calado C/A:", CaladoCorregidoAsiento)



"""
Creo una clase para los TKs dañados.

"""

        self.NombreTanque=input("Nombre del TK:")
        self.DobleFondo=bool(input("DF=1 WBT=0"))
        self.EsloraTanque=float(input("Eslora TK: "))
        self.MangaTanque=float(input("Manga TK:"))
        self.AlturaTanque=float(input("Altura TK:"))
        self.MaestraGTanque=float(input("MaestraG:"))
        self.LineaCentralGTanque=float(input("LCg Tk:"))
        self.AsientoLongitudinalTanque=float(input("Densidad Carga:"))
        self.AsientoTransversalTanque=float(LineaCentralGTanque*math.tan(EscoraInicial))
        self.AsientoTotalTanque=float(AsientoLongitudinalTanque+AsientoTransversalTanque)



class Tank():
    def __init__(self):
        self.NombreTanque=input("Nombre del TK:")
        self.DobleFondo=bool(input("DF=1 WBT=0"))
        self.EsloraTanque=float(input("Eslora TK: "))
        self.MangaTanque=float(input("Manga TK:"))
        self.AlturaTanque=float(input("Altura TK:"))
        self.MaestraGTanque=float(input("MaestraG:"))
        self.LineaCentralGTanque=float(input("LCg Tk:"))
        self.AsientoLongitudinalTanque=float(input("Densidad Carga:"))
        self.AsientoTransversalTanque=float(LineaCentralGTanque*math.tan(EscoraInicial))
        self.AsientoTotalTanque=float(AsientoLongitudinalTanque+AsientoTransversalTanque)

        self.CaladoInicialGdelTanque=CaladoCorregidoAsiento+AsientoTotalTanque-AlturaDobleFondo

        if DobleFondo==1:
            AsientoLongitudinalTanque=0
            AsientoTransversalTanque=0
            AsientoTotalTanque=0
            CaladoInicialGdelTanque=0

        self.EmpujePerdidoTanque=float(EsloraTanque*MangaTanque*(CaladoInicialGdelTanque-AlturaDobleFondo)*DensidadCarga*CoeficientePermeabilidad)
