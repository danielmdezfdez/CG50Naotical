# Anotation

ListaValores=["Signo", "Grados (Dec)", "Grados", "Minutos"]

def pedirNumeroEntero():
 
    correcto=False
    num=(0)
    while(not correcto):
        try:
            num = int(input("Choose: "))
            correcto=True
        except ValueError:
            print('Error. Choose: ')
     
    return num
 
salir = False
opcion = 0
 

while not salir:
 
    print ("1. Limbo Inferior")
    print ("2. Limbo Superior")
    print ("3. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print("Limbro Inferior")
        ListaValores=["Signo", "Grados (Dec)", "Grados", "Minutos"]


        # AlturaInstrumental
        # ENTRADA
        print("Altura Instrumental")

        AlturaInstrumentalSigno=((input("Signo: ")))
        AlturaInstrumentalGrados=float(input("Grados: "))
        AlturaInstrumentalMinutosSex=float((input("Minutos: ")))
        AlturaInstrumentalMinutosDec=float(float(AlturaInstrumentalMinutosSex)/60)

        AlturaInstrumentalTotal=float()

        if AlturaInstrumentalSigno=="+":
            AlturaInstrumentalTotal=float(AlturaInstrumentalGrados+AlturaInstrumentalMinutosDec)
        elif AlturaInstrumentalSigno=="-":
            AlturaInstrumentalTotal=float(-1*(AlturaInstrumentalGrados+AlturaInstrumentalMinutosDec))

        # CALCULOS

        ListaAlturaInstrumental=[]
        ParteEnteraAlturaInstrumental=int(abs(int(AlturaInstrumentalTotal)))
        ParteDecimalAlturaInstrumental=(AlturaInstrumentalTotal-int(ParteEnteraAlturaInstrumental))
        ParteDecimalAlturaInstrumentalSexagesimal=float(ParteDecimalAlturaInstrumental*60)
        ParteDecimalAlturaInstrumentalSexagesimal=round(ParteDecimalAlturaInstrumentalSexagesimal, 2)

        # RESULTADOS
        ListaAlturaInstrumental.append(AlturaInstrumentalTotal) #0
        ListaAlturaInstrumental.append(ParteEnteraAlturaInstrumental) #1
        if AlturaInstrumentalTotal>=0:
            AlturaInstrumentalSigno="+" 
            ListaAlturaInstrumental.append(AlturaInstrumentalSigno) #2
        elif ParteEnteraAlturaInstrumental<0:
            AlturaInstrumentalSigno="-"
            ListaAlturaInstrumental.append(AlturaInstrumentalSigno) #2
        ListaAlturaInstrumental.append(ParteDecimalAlturaInstrumentalSexagesimal) #3
        ListaAlturaInstrumental.append(round(AlturaInstrumentalTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaAlturaInstrumental[2], ListaAlturaInstrumental[4],ListaAlturaInstrumental[1],ListaAlturaInstrumental[3])




        # ErrorInstrumental
        # ENTRADA
        print("Error Instrumental")

        ErrorInstrumentalSigno=((input("Signo: ")))
        ErrorInstrumentalGrados=float(input("Grados: "))
        ErrorInstrumentalMinutosSex=float((input("Minutos: ")))
        ErrorInstrumentalMinutosDec=float(float(ErrorInstrumentalMinutosSex)/60)

        ErrorInstrumentalTotal=float()

        if ErrorInstrumentalSigno=="+":
            ErrorInstrumentalTotal=float(ErrorInstrumentalGrados+ErrorInstrumentalMinutosDec)
        elif ErrorInstrumentalSigno=="-":
            ErrorInstrumentalTotal=float(-1*(ErrorInstrumentalGrados+ErrorInstrumentalMinutosDec))

        # CALCULOS

        ListaErrorInstrumental=[]
        ParteEnteraErrorInstrumental=int(abs(int(ErrorInstrumentalTotal)))
        ParteDecimalErrorInstrumental=(ErrorInstrumentalTotal-int(ParteEnteraErrorInstrumental))
        ParteDecimalErrorInstrumentalSexagesimal=float(ParteDecimalErrorInstrumental*60)
        ParteDecimalErrorInstrumentalSexagesimal=round(ParteDecimalErrorInstrumentalSexagesimal, 2)

        # RESULTADOS
        ListaErrorInstrumental.append(ErrorInstrumentalTotal) #0
        ListaErrorInstrumental.append(ParteEnteraErrorInstrumental) #1
        if ErrorInstrumentalTotal>=0:
            ErrorInstrumentalSigno="+" 
            ListaErrorInstrumental.append(ErrorInstrumentalSigno) #2
        elif ErrorInstrumentalTotal<0:
            ErrorInstrumentalSigno="-"
            ListaErrorInstrumental.append(ErrorInstrumentalSigno) #2
        ListaErrorInstrumental.append(ParteDecimalErrorInstrumentalSexagesimal) #3
        ListaErrorInstrumental.append(round(ErrorInstrumentalTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaErrorInstrumental[2],ListaErrorInstrumental[4],ListaErrorInstrumental[1],ListaErrorInstrumental[3])







        #AlturaObservada

        # ENTRADA
        print("AlturaObservada")


        AlturaObservadaTotal=AlturaInstrumentalTotal+ErrorInstrumentalTotal


        # CALCULOS

        ListaAlturaObservada=[]
        ParteEnteraAlturaObservada=int(abs(int(AlturaObservadaTotal)))
        ParteDecimalAlturaObservada=(AlturaObservadaTotal-int(ParteEnteraAlturaObservada))
        ParteDecimalAlturaObservadaSexagesimal=float(ParteDecimalAlturaObservada*60)
        ParteDecimalAlturaObservadaSexagesimal=round(ParteDecimalAlturaObservadaSexagesimal, 2)

        # RESULTADOS
        ListaAlturaObservada.append(AlturaObservadaTotal) #0
        ListaAlturaObservada.append(ParteEnteraAlturaObservada) #1
        if AlturaObservadaTotal>=0:
            AlturaObservadaSigno="+" 
            ListaAlturaObservada.append(AlturaObservadaSigno) #2
        elif AlturaObservadaTotal<0:
            AlturaObservadaSigno="-"
            ListaAlturaObservada.append(AlturaObservadaSigno)
        ListaAlturaObservada.append(ParteDecimalAlturaObservadaSexagesimal) #3
        ListaAlturaObservada.append(round(AlturaObservadaTotal, 2)) #4

        # SALIDA
        print("AlturaObservada")
        "print(AlturaObservadaSigno, AlturaObservadaTotal, ParteEnteraAlturaObservada, ParteDecimalAlturaObservadaSexagesimal)"
        print(ListaValores)
        print(ListaAlturaObservada[2], ListaAlturaObservada[4],ListaAlturaObservada[1],ListaAlturaObservada[3])


        # CDPH
        # ENTRADA
        print("CDPH")

        CDPHSigno=((input("Signo: ")))
        CDPHGrados=float(input("Grados: "))
        CDPHMinutosSex=float((input("Minutos: ")))
        CDPHMinutosDec=float(float(CDPHMinutosSex)/60)

        CDPHTotal=float()

        if CDPHSigno=="+":
            CDPHTotal=float(CDPHGrados+CDPHMinutosDec)
        elif CDPHSigno=="-":
            CDPHTotal=float(-1*(CDPHGrados+CDPHMinutosDec))

        # CALCULOS

        ListaCDPH=[]
        ParteEnteraCDPH=int(abs(int(CDPHTotal)))
        ParteDecimalCDPH=(CDPHTotal-int(ParteEnteraCDPH))
        ParteDecimalCDPHSexagesimal=float(ParteDecimalCDPH*60)
        ParteDecimalCDPHSexagesimal=round(ParteDecimalCDPHSexagesimal, 2)

        # RESULTADOS
        ListaCDPH.append(CDPHTotal) #0
        ListaCDPH.append(ParteEnteraCDPH) #1
        if CDPHTotal>=0:
            CDPHSigno="+" 
            ListaCDPH.append(CDPHSigno) #2
        elif CDPHTotal<0:
            CDPHSigno="-"
            ListaCDPH.append(CDPHSigno) #2
        ListaCDPH.append(ParteDecimalCDPHSexagesimal) #3
        ListaCDPH.append(round(CDPHTotal, 2)) #4

        # SALIDA
        print("CDPH")
        "print(CDPHSigno, CDPHTotal, ParteEnteraCDPH, ParteDecimalCDPHSexagesimal)"
        print(ListaValores)
        print(ListaCDPH[2], ListaCDPH[4],ListaCDPH[1],ListaCDPH[3])



        #AlturaAparente

        # ENTRADA
        print("AlturaAparente")


        AlturaAparenteTotal=AlturaObservadaTotal+CDPHTotal


        # CALCULOS

        ListaAlturaAparente=[]
        ParteEnteraAlturaAparente=int(abs(int(AlturaAparenteTotal)))
        ParteDecimalAlturaAparente=(AlturaAparenteTotal-int(ParteEnteraAlturaAparente))
        ParteDecimalAlturaAparenteSexagesimal=float(ParteDecimalAlturaAparente*60)
        ParteDecimalAlturaAparenteSexagesimal=round(ParteDecimalAlturaAparenteSexagesimal, 2)

        # RESULTADOS
        ListaAlturaAparente.append(AlturaAparenteTotal) #0
        ListaAlturaAparente.append(ParteEnteraAlturaAparente) #1
        if AlturaAparenteTotal>=0:
            AlturaAparenteSigno="+" 
            ListaAlturaAparente.append(AlturaAparenteSigno) #2
        elif AlturaAparenteTotal<0:
            AlturaAparenteSigno="-"
            ListaAlturaAparente.append(AlturaAparenteSigno) #2
        ListaAlturaAparente.append(ParteDecimalAlturaAparenteSexagesimal) #3
        ListaAlturaAparente.append(round(AlturaAparenteTotal, 2)) #4

        # SALIDA
        print("AlturaAparente")
        "print(AlturaAparenteSigno, AlturaAparenteTotal, ParteEnteraAlturaAparente, ParteDecimalAlturaAparenteSexagesimal)"
        print(ListaValores)
        print(ListaAlturaAparente[2], ListaAlturaAparente[4],ListaAlturaAparente[1],ListaAlturaAparente[3])



        # CSRP
        # ENTRADA
        print("CSRP")

        CSRPSigno=((input("Signo: ")))
        CSRPGrados=float(input("Grados: "))
        CSRPMinutosSex=float((input("Minutos: ")))
        CSRPMinutosDec=float(float(CSRPMinutosSex)/60)

        CSRPTotal=float()

        if CSRPSigno=="+":
            CSRPTotal=float(CSRPGrados+CSRPMinutosDec)
        elif CSRPSigno=="-":
            CSRPTotal=float(-1*(CSRPGrados+CSRPMinutosDec))

        # CALCULOS

        ListaCSRP=[]
        ParteEnteraCSRP=int(abs(int(CSRPTotal)))
        ParteDecimalCSRP=(CSRPTotal-int(ParteEnteraCSRP))
        ParteDecimalCSRPSexagesimal=float(ParteDecimalCSRP*60)
        ParteDecimalCSRPSexagesimal=round(ParteDecimalCSRPSexagesimal, 2)

        # RESULTADOS
        ListaCSRP.append(CSRPTotal) #0
        ListaCSRP.append(ParteEnteraCSRP) #1
        if CSRPTotal>=0:
            CSRPSigno="+" 
            ListaCSRP.append(CSRPSigno) #2
        elif CSRPTotal<0:
            CSRPSigno="-"
            ListaCSRP.append(CSRPSigno) #2
        ListaCSRP.append(ParteDecimalCSRPSexagesimal) #3
        ListaCSRP.append(round(CSRPTotal, 2)) #4

        # SALIDA
        print("CSRP")
        "print(CSRPSigno, CSRPTotal, ParteEnteraCSRP, ParteDecimalCSRPSexagesimal)"
        print(ListaValores)
        print(ListaCSRP[2], ListaCSRP[4],ListaCSRP[1],ListaCSRP[3])


        # CorreccionAdicional
        # ENTRADA
        print("CorreccionAdicional")

        CorreccionAdicionalSigno=((input("Signo: ")))
        CorreccionAdicionalGrados=float(input("Grados: "))
        CorreccionAdicionalMinutosSex=float((input("Minutos: ")))
        CorreccionAdicionalMinutosDec=float(float(CorreccionAdicionalMinutosSex)/60)

        CorreccionAdicionalTotal=float()

        if CorreccionAdicionalSigno=="+":
            CorreccionAdicionalTotal=float(CorreccionAdicionalGrados+CorreccionAdicionalMinutosDec)
        elif CorreccionAdicionalSigno=="-":
            CorreccionAdicionalTotal=float(-1*(CorreccionAdicionalGrados+CorreccionAdicionalMinutosDec))

        # CALCULOS

        ListaCorreccionAdicional=[]
        ParteEnteraCorreccionAdicional=int(abs(int(CorreccionAdicionalTotal)))
        ParteDecimalCorreccionAdicional=(CorreccionAdicionalTotal-int(ParteEnteraCorreccionAdicional))
        ParteDecimalCorreccionAdicionalSexagesimal=float(ParteDecimalCorreccionAdicional*60)
        ParteDecimalCorreccionAdicionalSexagesimal=round(ParteDecimalCorreccionAdicionalSexagesimal, 2)

        # RESULTADOS
        ListaCorreccionAdicional.append(CorreccionAdicionalTotal) #0
        ListaCorreccionAdicional.append(ParteEnteraCorreccionAdicional) #1
        if CorreccionAdicionalTotal>=0:
            CorreccionAdicionalSigno="+" 
            ListaCorreccionAdicional.append(CorreccionAdicionalSigno) #2
        elif CorreccionAdicionalTotal<0:
            CorreccionAdicionalSigno="-"
            ListaCorreccionAdicional.append(CorreccionAdicionalSigno) #2
        ListaCorreccionAdicional.append(ParteDecimalCorreccionAdicionalSexagesimal) #3
        ListaCorreccionAdicional.append(round(CorreccionAdicionalTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaCorreccionAdicional[2], ListaCorreccionAdicional[4],ListaCorreccionAdicional[1],ListaCorreccionAdicional[3])


        # ENTRADA
        print("AlturaVerdadera")


        AlturaVerdaderaTotal=AlturaAparenteTotal+CorreccionAdicionalTotal+CSRPTotal


        # CALCULOS

        ListaAlturaVerdadera=[]
        ParteEnteraAlturaVerdadera=int(abs(int(AlturaVerdaderaTotal)))
        ParteDecimalAlturaVerdadera=(AlturaVerdaderaTotal-int(ParteEnteraAlturaVerdadera))
        ParteDecimalAlturaVerdaderaSexagesimal=float(ParteDecimalAlturaVerdadera*60)
        ParteDecimalAlturaVerdaderaSexagesimal=round(ParteDecimalAlturaVerdaderaSexagesimal, 2)

        # RESULTADOS
        ListaAlturaVerdadera.append(AlturaVerdaderaTotal) #0
        ListaAlturaVerdadera.append(ParteEnteraAlturaVerdadera) #1
        if AlturaVerdaderaTotal>=0:
            AlturaVerdaderaSigno="+" 
            ListaAlturaVerdadera.append(AlturaVerdaderaSigno) #2
        elif AlturaVerdaderaTotal<0:
            AlturaVerdaderaSigno="-"
            ListaAlturaVerdadera.append(AlturaVerdaderaSigno) #2
        ListaAlturaVerdadera.append(ParteDecimalAlturaVerdaderaSexagesimal) #3
        ListaAlturaVerdadera.append(round(AlturaVerdaderaTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaAlturaVerdadera[2], ListaAlturaVerdadera[4],ListaAlturaVerdadera[1],ListaAlturaVerdadera[3])





        print(ListaValores)
        print(ListaAlturaInstrumental[2], ListaAlturaInstrumental[4],ListaAlturaInstrumental[1],ListaAlturaInstrumental[3])
        print(ListaErrorInstrumental[2], ListaErrorInstrumental[4],ListaErrorInstrumental[1],ListaErrorInstrumental[3])
        print(ListaAlturaObservada[2], ListaAlturaObservada[4],ListaAlturaObservada[1],ListaAlturaObservada[3])
        print(ListaCDPH[2], ListaCDPH[4],ListaCDPH[1],ListaCDPH[3])
        print(ListaCSRP[2], ListaCSRP[4],ListaCSRP[1],ListaCSRP[3])
        print(ListaAlturaVerdadera[2], ListaAlturaVerdadera[4],ListaAlturaVerdadera[1],ListaAlturaVerdadera[3])

        salir=True

        
    elif opcion == 2:
        ListaValores=["Signo", "Grados (Dec)", "Grados", "Minutos"]


        # AlturaInstrumental
        # ENTRADA
        print("Altura Instrumental")

        AlturaInstrumentalSigno=((input("Signo: ")))
        AlturaInstrumentalGrados=float(input("Grados: "))
        AlturaInstrumentalMinutosSex=float((input("Minutos: ")))
        AlturaInstrumentalMinutosDec=float(float(AlturaInstrumentalMinutosSex)/60)

        AlturaInstrumentalTotal=float()

        if AlturaInstrumentalSigno=="+":
            AlturaInstrumentalTotal=float(AlturaInstrumentalGrados+AlturaInstrumentalMinutosDec)
        elif AlturaInstrumentalSigno=="-":
            AlturaInstrumentalTotal=float(-1*(AlturaInstrumentalGrados+AlturaInstrumentalMinutosDec))

        # CALCULOS

        ListaAlturaInstrumental=[]
        ParteEnteraAlturaInstrumental=int(abs(int(AlturaInstrumentalTotal)))
        ParteDecimalAlturaInstrumental=(AlturaInstrumentalTotal-int(ParteEnteraAlturaInstrumental))
        ParteDecimalAlturaInstrumentalSexagesimal=float(ParteDecimalAlturaInstrumental*60)
        ParteDecimalAlturaInstrumentalSexagesimal=round(ParteDecimalAlturaInstrumentalSexagesimal, 2)

        # RESULTADOS
        ListaAlturaInstrumental.append(AlturaInstrumentalTotal) #0
        ListaAlturaInstrumental.append(ParteEnteraAlturaInstrumental) #1
        if AlturaInstrumentalTotal>=0:
            AlturaInstrumentalSigno="+" 
            ListaAlturaInstrumental.append(AlturaInstrumentalSigno) #2
        elif ParteEnteraAlturaInstrumental<0:
            AlturaInstrumentalSigno="-"
            ListaAlturaInstrumental.append(AlturaInstrumentalSigno) #2
        ListaAlturaInstrumental.append(ParteDecimalAlturaInstrumentalSexagesimal) #3
        ListaAlturaInstrumental.append(round(AlturaInstrumentalTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaAlturaInstrumental[2], ListaAlturaInstrumental[4],ListaAlturaInstrumental[1],ListaAlturaInstrumental[3])




        # ErrorInstrumental
        # ENTRADA
        print("Error Instrumental")

        ErrorInstrumentalSigno=((input("Signo: ")))
        ErrorInstrumentalGrados=float(input("Grados: "))
        ErrorInstrumentalMinutosSex=float((input("Minutos: ")))
        ErrorInstrumentalMinutosDec=float(float(ErrorInstrumentalMinutosSex)/60)

        ErrorInstrumentalTotal=float()

        if ErrorInstrumentalSigno=="+":
            ErrorInstrumentalTotal=float(ErrorInstrumentalGrados+ErrorInstrumentalMinutosDec)
        elif ErrorInstrumentalSigno=="-":
            ErrorInstrumentalTotal=float(-1*(ErrorInstrumentalGrados+ErrorInstrumentalMinutosDec))

        # CALCULOS

        ListaErrorInstrumental=[]
        ParteEnteraErrorInstrumental=int(abs(int(ErrorInstrumentalTotal)))
        ParteDecimalErrorInstrumental=(ErrorInstrumentalTotal-int(ParteEnteraErrorInstrumental))
        ParteDecimalErrorInstrumentalSexagesimal=float(ParteDecimalErrorInstrumental*60)
        ParteDecimalErrorInstrumentalSexagesimal=round(ParteDecimalErrorInstrumentalSexagesimal, 2)

        # RESULTADOS
        ListaErrorInstrumental.append(ErrorInstrumentalTotal) #0
        ListaErrorInstrumental.append(ParteEnteraErrorInstrumental) #1
        if ErrorInstrumentalTotal>=0:
            ErrorInstrumentalSigno="+" 
            ListaErrorInstrumental.append(ErrorInstrumentalSigno) #2
        elif ErrorInstrumentalTotal<0:
            ErrorInstrumentalSigno="-"
            ListaErrorInstrumental.append(ErrorInstrumentalSigno) #2
        ListaErrorInstrumental.append(ParteDecimalErrorInstrumentalSexagesimal) #3
        ListaErrorInstrumental.append(round(ErrorInstrumentalTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaErrorInstrumental[2],ListaErrorInstrumental[4],ListaErrorInstrumental[1],ListaErrorInstrumental[3])







        #AlturaObservada

        # ENTRADA
        print("AlturaObservada")


        AlturaObservadaTotal=AlturaInstrumentalTotal+ErrorInstrumentalTotal


        # CALCULOS

        ListaAlturaObservada=[]
        ParteEnteraAlturaObservada=int(abs(int(AlturaObservadaTotal)))
        ParteDecimalAlturaObservada=(AlturaObservadaTotal-int(ParteEnteraAlturaObservada))
        ParteDecimalAlturaObservadaSexagesimal=float(ParteDecimalAlturaObservada*60)
        ParteDecimalAlturaObservadaSexagesimal=round(ParteDecimalAlturaObservadaSexagesimal, 2)

        # RESULTADOS
        ListaAlturaObservada.append(AlturaObservadaTotal) #0
        ListaAlturaObservada.append(ParteEnteraAlturaObservada) #1
        if AlturaObservadaTotal>=0:
            AlturaObservadaSigno="+" 
            ListaAlturaObservada.append(AlturaObservadaSigno) #2
        elif AlturaObservadaTotal<0:
            AlturaObservadaSigno="-"
            ListaAlturaObservada.append(AlturaObservadaSigno)
        ListaAlturaObservada.append(ParteDecimalAlturaObservadaSexagesimal) #3
        ListaAlturaObservada.append(round(AlturaObservadaTotal, 2)) #4

        # SALIDA
        print("AlturaObservada")
        "print(AlturaObservadaSigno, AlturaObservadaTotal, ParteEnteraAlturaObservada, ParteDecimalAlturaObservadaSexagesimal)"
        print(ListaValores)
        print(ListaAlturaObservada[2], ListaAlturaObservada[4],ListaAlturaObservada[1],ListaAlturaObservada[3])


        # CDPH
        # ENTRADA
        print("CDPH")

        CDPHSigno=((input("Signo: ")))
        CDPHGrados=float(input("Grados: "))
        CDPHMinutosSex=float((input("Minutos: ")))
        CDPHMinutosDec=float(float(CDPHMinutosSex)/60)

        CDPHTotal=float()

        if CDPHSigno=="+":
            CDPHTotal=float(CDPHGrados+CDPHMinutosDec)
        elif CDPHSigno=="-":
            CDPHTotal=float(-1*(CDPHGrados+CDPHMinutosDec))

        # CALCULOS

        ListaCDPH=[]
        ParteEnteraCDPH=int(abs(int(CDPHTotal)))
        ParteDecimalCDPH=(CDPHTotal-int(ParteEnteraCDPH))
        ParteDecimalCDPHSexagesimal=float(ParteDecimalCDPH*60)
        ParteDecimalCDPHSexagesimal=round(ParteDecimalCDPHSexagesimal, 2)

        # RESULTADOS
        ListaCDPH.append(CDPHTotal) #0
        ListaCDPH.append(ParteEnteraCDPH) #1
        if CDPHTotal>=0:
            CDPHSigno="+" 
            ListaCDPH.append(CDPHSigno) #2
        elif CDPHTotal<0:
            CDPHSigno="-"
            ListaCDPH.append(CDPHSigno) #2
        ListaCDPH.append(ParteDecimalCDPHSexagesimal) #3
        ListaCDPH.append(round(CDPHTotal, 2)) #4

        # SALIDA
        print("CDPH")
        "print(CDPHSigno, CDPHTotal, ParteEnteraCDPH, ParteDecimalCDPHSexagesimal)"
        print(ListaValores)
        print(ListaCDPH[2], ListaCDPH[4],ListaCDPH[1],ListaCDPH[3])




        # D
        # ENTRADA
        print("DiametroSol")

        DiametroSolSigno=((input("Signo: ")))
        DiametroSolGrados=float(input("Grados: "))
        DiametroSolMinutosSex=float((input("Minutos: ")))
        DiametroSolMinutosDec=float(float(DiametroSolMinutosSex)/60)

        DiametroSolTotal=float()

        if DiametroSolSigno=="+":
            DiametroSolTotal=float(2.5*(DiametroSolGrados+DiametroSolMinutosDec))


        # CALCULOS

        ListaDiametroSol=[]
        ParteEnteraDiametroSol=int(abs(int(DiametroSolTotal)))
        ParteDecimalDiametroSol=(DiametroSolTotal-int(ParteEnteraDiametroSol))
        ParteDecimalDiametroSolSexagesimal=float(ParteDecimalDiametroSol*60)
        ParteDecimalDiametroSolSexagesimal=round(ParteDecimalDiametroSolSexagesimal, 2)

        # RESULTADOS
        ListaDiametroSol.append(DiametroSolTotal) #0
        ListaDiametroSol.append(ParteEnteraDiametroSol) #1
        if DiametroSolTotal>=0:
            DiametroSolSigno="+" 
            ListaDiametroSol.append(DiametroSolSigno) #2
        elif DiametroSolTotal<0:
            DiametroSolSigno="-"
            ListaDiametroSol.append(DiametroSolSigno) #2
        ListaDiametroSol.append(ParteDecimalDiametroSolSexagesimal) #3
        ListaDiametroSol.append(round(DiametroSolTotal, 2)) #4

        # SALIDA
        print("DiametroSol")
        "print(DiametroSolSigno, DiametroSolTotal, ParteEnteraDiametroSol, ParteDecimalDiametroSolSexagesimal)"
        print(ListaValores)
        print(ListaDiametroSol[2], ListaDiametroSol[4],ListaDiametroSol[1],ListaDiametroSol[3])


        #AlturaAparente

        # ENTRADA
        print("AlturaAparente")


        AlturaAparenteTotal=AlturaObservadaTotal+CDPHTotal-(2.5*DiametroSolTotal)


        # CALCULOS

        ListaAlturaAparente=[]
        ParteEnteraAlturaAparente=int(abs(int(AlturaAparenteTotal)))
        ParteDecimalAlturaAparente=(AlturaAparenteTotal-int(ParteEnteraAlturaAparente))
        ParteDecimalAlturaAparenteSexagesimal=float(ParteDecimalAlturaAparente*60)
        ParteDecimalAlturaAparenteSexagesimal=round(ParteDecimalAlturaAparenteSexagesimal, 2)

        # RESULTADOS
        ListaAlturaAparente.append(AlturaAparenteTotal) #0
        ListaAlturaAparente.append(ParteEnteraAlturaAparente) #1
        if AlturaAparenteTotal>=0:
            AlturaAparenteSigno="+" 
            ListaAlturaAparente.append(AlturaAparenteSigno) #2
        elif AlturaAparenteTotal<0:
            AlturaAparenteSigno="-"
            ListaAlturaAparente.append(AlturaAparenteSigno) #2
        ListaAlturaAparente.append(ParteDecimalAlturaAparenteSexagesimal) #3
        ListaAlturaAparente.append(round(AlturaAparenteTotal, 2)) #4

        # SALIDA
        print("AlturaAparente")
        "print(AlturaAparenteSigno, AlturaAparenteTotal, ParteEnteraAlturaAparente, ParteDecimalAlturaAparenteSexagesimal)"
        print(ListaValores)
        print(ListaAlturaAparente[2], ListaAlturaAparente[4],ListaAlturaAparente[1],ListaAlturaAparente[3])



        # CSRP
        # ENTRADA
        print("CSRP")

        CSRPSigno=((input("Signo: ")))
        CSRPGrados=float(input("Grados: "))
        CSRPMinutosSex=float((input("Minutos: ")))
        CSRPMinutosDec=float(float(CSRPMinutosSex)/60)

        CSRPTotal=float()

        if CSRPSigno=="+":
            CSRPTotal=float(CSRPGrados+CSRPMinutosDec)
        elif CSRPSigno=="-":
            CSRPTotal=float(-1*(CSRPGrados+CSRPMinutosDec))

        # CALCULOS

        ListaCSRP=[]
        ParteEnteraCSRP=int(abs(int(CSRPTotal)))
        ParteDecimalCSRP=(CSRPTotal-int(ParteEnteraCSRP))
        ParteDecimalCSRPSexagesimal=float(ParteDecimalCSRP*60)
        ParteDecimalCSRPSexagesimal=round(ParteDecimalCSRPSexagesimal, 2)

        # RESULTADOS
        ListaCSRP.append(CSRPTotal) #0
        ListaCSRP.append(ParteEnteraCSRP) #1
        if CSRPTotal>=0:
            CSRPSigno="+" 
            ListaCSRP.append(CSRPSigno) #2
        elif CSRPTotal<0:
            CSRPSigno="-"
            ListaCSRP.append(CSRPSigno) #2
        ListaCSRP.append(ParteDecimalCSRPSexagesimal) #3
        ListaCSRP.append(round(CSRPTotal, 2)) #4

        # SALIDA
        print("CSRP")
        "print(CSRPSigno, CSRPTotal, ParteEnteraCSRP, ParteDecimalCSRPSexagesimal)"
        print(ListaValores)
        print(ListaCSRP[2], ListaCSRP[4],ListaCSRP[1],ListaCSRP[3])


        # CorreccionAdicional
        # ENTRADA
        print("CorreccionAdicional")

        CorreccionAdicionalSigno=((input("Signo: ")))
        CorreccionAdicionalGrados=float(input("Grados: "))
        CorreccionAdicionalMinutosSex=float((input("Minutos: ")))
        CorreccionAdicionalMinutosDec=float(float(CorreccionAdicionalMinutosSex)/60)

        CorreccionAdicionalTotal=float()

        if CorreccionAdicionalSigno=="+":
            CorreccionAdicionalTotal=float(CorreccionAdicionalGrados+CorreccionAdicionalMinutosDec)
        elif CorreccionAdicionalSigno=="-":
            CorreccionAdicionalTotal=float(-1*(CorreccionAdicionalGrados+CorreccionAdicionalMinutosDec))

        # CALCULOS

        ListaCorreccionAdicional=[]
        ParteEnteraCorreccionAdicional=int(abs(int(CorreccionAdicionalTotal)))
        ParteDecimalCorreccionAdicional=(CorreccionAdicionalTotal-int(ParteEnteraCorreccionAdicional))
        ParteDecimalCorreccionAdicionalSexagesimal=float(ParteDecimalCorreccionAdicional*60)
        ParteDecimalCorreccionAdicionalSexagesimal=round(ParteDecimalCorreccionAdicionalSexagesimal, 2)

        # RESULTADOS
        ListaCorreccionAdicional.append(CorreccionAdicionalTotal) #0
        ListaCorreccionAdicional.append(ParteEnteraCorreccionAdicional) #1
        if CorreccionAdicionalTotal>=0:
            CorreccionAdicionalSigno="+" 
            ListaCorreccionAdicional.append(CorreccionAdicionalSigno) #2
        elif CorreccionAdicionalTotal<0:
            CorreccionAdicionalSigno="-"
            ListaCorreccionAdicional.append(CorreccionAdicionalSigno) #2
        ListaCorreccionAdicional.append(ParteDecimalCorreccionAdicionalSexagesimal) #3
        ListaCorreccionAdicional.append(round(CorreccionAdicionalTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaCorreccionAdicional[2], ListaCorreccionAdicional[4],ListaCorreccionAdicional[1],ListaCorreccionAdicional[3])


        # ENTRADA
        print("AlturaVerdadera")


        AlturaVerdaderaTotal=AlturaAparenteTotal+CorreccionAdicionalTotal+CSRPTotal


        # CALCULOS

        ListaAlturaVerdadera=[]
        ParteEnteraAlturaVerdadera=int(abs(int(AlturaVerdaderaTotal)))
        ParteDecimalAlturaVerdadera=(AlturaVerdaderaTotal-int(ParteEnteraAlturaVerdadera))
        ParteDecimalAlturaVerdaderaSexagesimal=float(ParteDecimalAlturaVerdadera*60)
        ParteDecimalAlturaVerdaderaSexagesimal=round(ParteDecimalAlturaVerdaderaSexagesimal, 2)

        # RESULTADOS
        ListaAlturaVerdadera.append(AlturaVerdaderaTotal) #0
        ListaAlturaVerdadera.append(ParteEnteraAlturaVerdadera) #1
        if AlturaVerdaderaTotal>=0:
            AlturaVerdaderaSigno="+" 
            ListaAlturaVerdadera.append(AlturaVerdaderaSigno) #2
        elif AlturaVerdaderaTotal<0:
            AlturaVerdaderaSigno="-"
            ListaAlturaVerdadera.append(AlturaVerdaderaSigno) #2
        ListaAlturaVerdadera.append(ParteDecimalAlturaVerdaderaSexagesimal) #3
        ListaAlturaVerdadera.append(round(AlturaVerdaderaTotal, 2)) #4

        # SALIDA
        print(ListaValores)
        print(ListaAlturaVerdadera[2], ListaAlturaVerdadera[4],ListaAlturaVerdadera[1],ListaAlturaVerdadera[3])





        print(ListaValores)
        print(ListaAlturaInstrumental[2], ListaAlturaInstrumental[4],ListaAlturaInstrumental[1],ListaAlturaInstrumental[3])
        print(ListaErrorInstrumental[2], ListaErrorInstrumental[4],ListaErrorInstrumental[1],ListaErrorInstrumental[3])
        print(ListaAlturaObservada[2], ListaAlturaObservada[4],ListaAlturaObservada[1],ListaAlturaObservada[3])
        print(ListaCDPH[2], ListaCDPH[4],ListaCDPH[1],ListaCDPH[3])
        print(ListaDiametroSol[2], ListaDiametroSol[4],ListaDiametroSol[1],ListaDiametroSol[3])
        print(ListaCSRP[2], ListaCSRP[4],ListaCSRP[1],ListaCSRP[3])
        print(ListaAlturaVerdadera[2], ListaAlturaVerdadera[4],ListaAlturaVerdadera[1],ListaAlturaVerdadera[3])
        salir=True

    elif opcion == 3:
        print("Salir.")
        salir = True

