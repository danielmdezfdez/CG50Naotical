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
            self.DF=int(0)

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
            self.DF=int(input("¿Tiene DF? True=1:"))

            if self.DF==1:
                self.DFHeight=float(input("Altura DF: "))
            elif self.DF==0:
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
    def __init__(self, DamagedTankName):
        # Obtener Nombre del Tanque
        self.TankName=DamagedTankName

        # Recuperar datos del Buque
        self.DFHeight=Ship().DFHeight
        self.Heel=barco.HeelRad
        self.CaladoCorregidoAsiento=barco.CaladoCorregidoAsiento
        
        # Pregunta si es DF
        self.DobleFondo=input("¿DF? (YES=1;NO=0) ")
        
        self.EsloraTanque=float(input("Eslora TK: "))
        self.MangaTanque=float(input("Manga TK:"))
        self.AlturaTanque=float(input("Altura TK:"))
        self.CoeficientePermeabilidad=float(input("C. Permeabilidad: "))
        self.DensidadCarga=float(input("Densidad Carga: "))
        self.MaestraGTanque=float(input("MaestraG:"))
        self.LineaCentralGTanque=float(input("LCg Tk:"))

        self.AsientoTotalTanque=0.0
        self.CaladoInicialGdelTanque=0.0

        self.EmpujePerdidoTanque=0.0

    def asiento_longitudinal(self):
     self.AsientoLongitudinalTanque=float(self.MaestraGTanque*barco.AsientoInicial/barco.LOA)

     if self.DobleFondo==1:
         self.AsientoLongitudinalTanque=0
            
     print("Asiento Longitudinal del TK")
     return(self.AsientoLongitudinalTanque)

    def asiento_transversal(self):
         self.AsientoTransversalTanque=float(self.LineaCentralGTanque*math.tan(self.Heel))

         if self.DobleFondo==1:
             self.AsientoTransversalTanque=0

         print("Asiento Transversal del TK")
         return(self.AsientoTransversalTanque)

    def asiento_total(self):
     self.AsientoTotalTanque=float(self.AsientoLongitudinalTanque+self.AsientoTransversalTanque)

     if self.DobleFondo==1:
            self.AsientoTotalTanque=0

     print("Asiento Total del TK:")
     return(self.AsientoTotalTanque)

    def caladoinicialgdeltanque(self):
    
     self.CaladoInicialGdelTanque=self.CaladoCorregidoAsiento+self.AsientoTotalTanque-(barco.DFHeight)

     if self.DobleFondo==1:
         self.AsientoLongitudinalTanque=0

     print("C.I. en g del TK:")
     return(self.CaladoInicialGdelTanque)

    def lostbuoyancy(self):

        self.LostBuoyancy=float(self.EsloraTanque*self.MangaTanque*(self.CaladoInicialGdelTanque-self.DFHeight)*self.DensidadCarga*self.CoeficientePermeabilidad)
        print("Empuje Perdido:")

        return(self.LostBuoyancy)


# BARCO

# Nombramos Barco
barco=Ship()

# Ejecutamos funciones del barco
barco.ship_particulars()
barco.double_hull()
barco.asiento_inicial(barco.AftDraft, barco.ForwardDraft)
barco.medium_draft(barco.AftDraft, barco.ForwardDraft)
barco.maestra_f()


# TANQUES
DamagedTanks=int(input("Tanques Damaged Number: "))
DamagedTanksCounter=DamagedTanks

while DamagedTanksCounter>0:
    DamagedTankName=input("Damaged Tank Name: ")
    DamagedTankName=Tank(DamagedTankName)
    print(DamagedTankName.asiento_longitudinal())
    print(DamagedTankName.asiento_transversal())
    print(DamagedTankName.asiento_total())
    print(DamagedTankName.caladoinicialgdeltanque())
    print(DamagedTankName.lostbuoyancy())

    DamagedTanksCounter=DamagedTanksCounter-1

