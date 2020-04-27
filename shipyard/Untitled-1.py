import math


# Definimos las caracteristicas del barco

class Ship():
        def __init__(self):
            # Ships Particulars
            self.LOA=0.0
            self.Beam=0.0
            self.HeelDeg=0.0
            self.HeelRad=0.0
            self.ForwardDraft=0.0
            self.AftDraft=0.0
            self.MediumDraft=0.0

            # Doble Fondo            
            self.DFHeight=0.0
            self.DF=bool(0)

            # Condicion del Doble Fondo
            if self.DF==True:
                self.DFHeight=0.0
            else:
                self.DFHeight=0.0

            # Draft Correction
            self.AsientoInicial=0.0
            self.MaestraF=0.0
            self.CorreccionAsiento=0.0
            self.CaladoCorregidoAsiento=0.0

        # Ships Particulars
        def ship_particulars(self):
            self.LOA=float(input("Eslora:"))
            self.Beam=float(input("Manga: "))
            self.HeelDeg=float(input("Escora: "))
            self.HeelRad=float(math.radians(self.HeelDeg))
            self.ForwardDraft=float(input("CPr: "))
            self.AftDraft=float(input("CPp: "))

        def double_hull(self):

            # Doble Fondo
                     
            self.DFHeight=0.0
            self.DF=bool(input("¿Tiene DF?:"))

            if self.DF==True:
                self.DFHeight=float(input("Altura DF: "))
            else:
                self.DFHeight=0.0

        def asiento_inicial(self, AftDraft, ForwardDraft):
            self.AsientoInicial=float(self.AftDraft-self.ForwardDraft)

        def medium_draft(self,AftDraft,ForwardDraft):
            self.MediumDraft=float((ForwardDraft+AftDraft)/2)
            print("Calado Medio:",self.MediumDraft,"m")

        def maestra_f(self):
            self.MaestraF=float(input("MaestraF: "))
            self.CorreccionAsiento=(self.AsientoInicial*self.MaestraF)/self.LOA
            self.CaladoCorregidoAsiento=self.MediumDraft+self.CorreccionAsiento

            print("C/A:",self.CorreccionAsiento)
            print("C C/A:", self.CaladoCorregidoAsiento)





class Tank():
    def __init__(self):
        # Obtener Nombre del Tanque
        self.Nombre=DamagedTankName

        # Recuperar datos del Buque
        self.DFHeight=getattr(barco.DFHeight)
        self.Heel=getattr(barco.HeelRad)
        self.CaladoCorregidoAsiento=getattr(barco.CaladoCorregidoAsiento)
        # Pregunta si es DF
        self.DobleFondo=bool(input("¿DF? YES=1"))

        if self.DobleFondo==1:

        elif self.DobleFondo==0:
        self.EsloraTanque=float(input("Eslora TK: "))
        self.MangaTanque=float(input("Manga TK:"))
        self.AlturaTanque=float(input("Altura TK:"))
        self.CoeficientePermeabilidad=float(input("C. Permeabilidad: "))
        self.DensidadCarga=float(input("Densidad Carga: "))
        self.MaestraGTanque=float(input("MaestraG:"))
        self.LineaCentralGTanque=float(input("LCg Tk:"))
        self.AsientoLongitudinalTanque=float(input("Densidad Carga:"))
        self.AsientoTransversalTanque=float(self.LineaCentralGTanque*math.tan(self.Heel))
        self.AsientoTotalTanque=float(self.AsientoLongitudinalTanque+self.AsientoTransversalTanque)
        self.CaladoInicialGdelTanque=self.CaladoCorregidoAsiento+self.AsientoTotalTanque-(Ship.__init__(self).DFHeight)

        if self.DobleFondo==1:
            self.AsientoLongitudinalTanque=0
            self.AsientoTransversalTanque=0
            self.AsientoTotalTanque=0
            self.CaladoInicialGdelTanque=0

        self.EmpujePerdidoTanque=float(self.EsloraTanque*self.MangaTanque*(self.CaladoInicialGdelTanque-self.DFHeight)*self.DensidadCarga*self.CoeficientePermeabilidad)


































barco=Ship()

barco.ship_particulars()
barco.double_hull()
barco.asiento_inicial(barco.AftDraft, barco.ForwardDraft)
barco.medium_draft(barco.AftDraft, barco.ForwardDraft)
barco.maestra_f()




DamagedTanks=int(input("Tanques Damaged Number: "))
DamagedTanksCounter=DamagedTanks

while DamagedTanksCounter>0:
    DamagedTankName=input("Damaged Tank Name: ")
    DamagedTank=Tank()

    DamagedTanksCounter=DamagedTanksCounter-1


"""Tank.__self__.EmpujePerdidoTanque"""


"""class Flooding():
    def __init__(self):
        self.EmpujePerdidtoTotal=
        self.IPTotal=
"""