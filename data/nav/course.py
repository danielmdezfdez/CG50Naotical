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
 
    print ("1. Desde Rumbo de Aguja a Rumbo de Superficie")
    print ("2. Desde Rumbo Verdadero a Rumbo de Superficie")
    print ("3. Rumbo de Superficie")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print("1. Desde Rumbo de Aguja a Rumbo de Superficie")
        RumbodeAguja=float(input("Introduce el Rumbo de Aguja: "))
        CorreccionTotal=float(input("Introduce la Corrección Total: "))
        RumboVerdadero=RumbodeAguja+CorreccionTotal
        DirecciondelViento=float(input("Introduce la dirección del viento: "))
        Abatimiento=float(input("Introduce el Abatimiento (positivo): "))
        if RumboVerdadero-DirecciondelViento>180:
            RumbodeSuperficie=RumboVerdadero+Abatimiento
        if RumboVerdadero-DirecciondelViento<180:
            RumbodeSuperficie=RumboVerdadero-Abatimiento
       

        print("El Rumbo Verdadero es: ",RumboVerdadero)
        print("El Rumbo de Superficie es: ",RumbodeSuperficie)
        salir=True
    
    
    elif opcion == 2:
        print("2. Desde Rumbo Verdadero a Rumbo de Superficie")
        RumboVerdadero=float(input("Introduce el Rumbo Verdadero: "))
        DireccionViento=float(input("Introduce la dirección del viento: "))
        Abatimiento=float(input("Introduce el Abatimiento (positivo): "))
        
        # Comparación de los Valores

        if RumboVerdadero-DireccionViento>180: # Caso 1: Abatimiento a Estribor (Positivo)
            RumbodeSuperficie=RumboVerdadero+Abatimiento
        if RumboVerdadero-DireccionViento<180: # Caso 2: Abatimiento Babor (Negativo)
            RumbodeSuperficie=RumboVerdadero-Abatimiento
       

        print("El Rumbo Verdadero es: ",RumboVerdadero)
        print("El Rumbo de Superficie es: ",RumbodeSuperficie)
        salir=True

    elif opcion == 3:
         print("1. Desde Rumbo de Aguja a Rumbo Efectivo")
         RumbodeAguja=float(input("Introduce el Rumbo de Aguja: "))
         CorreccionTotal=float(input("Introduce la Corrección Total: "))
         RumboVerdadero=RumbodeAguja+CorreccionTotal
         DireccionViento=float(input("Introduce la dirección del viento: "))
         Abatimiento=float(input("Introduce el Abatimiento (positivo): "))
         if RumboVerdadero-DireccionViento>180:
                RumboSuperficie=RumboVerdadero-Abatimiento
         if RumboVerdadero-DireccionViento<180:
                RumboSuperficie=RumboVerdadero+Abatimiento


         VelocidadMaquinas=float(input("Introduce la velocidad de máquinas: "))
         IHC=float(input("Introduce la intensidad horaria de la corriente: "))
         RumboCorriente=float(input("Introduce el rumbo de la corriente: "))
         Alfa=RumboCorriente-RumboSuperficie

    
         if Alfa<0:
             Alfa=Alfa+180
         elif Alfa>180:
             Alfa=Alfa-180

         Alfa=math.radians(float(Alfa))

         # Calculo de la Velocidad Efectiva
         VelocidadEfectiva=float(math.sqrt(VelocidadMaquinas*VelocidadMaquinas+IHC*IHC-2*VelocidadMaquinas*IHC*math.cos(Alfa)))


         # Calculo del Ángulo de Deriva
         AnguloDeriva=float(math.asin((float(math.sin(Alfa))*float(IHC))/float(VelocidadEfectiva)))  
         
         # Transformamos la Deriva de Radianes a Grados
         AnguloDeriva=math.degrees(AnguloDeriva)    

         if AnguloDeriva<0:
             RumboEfectivo=RumboSuperficie-AnguloDeriva
         if AnguloDeriva>0:
             RumboEfectivo=RumboSuperficie+AnguloDeriva

         Beta=180-Alfa-AnguloDeriva


         Alfa=math.degrees(Alfa) 
         

        ### Impresión de Resultados
         print("El Rumbo Verdadero es: ", RumboVerdadero)
         print("El abatimiento es de: ", Abatimiento, "grados")
         print("El Rumbo de Superficie es: ", RumboSuperficie)
         print("El Rumbo de la Corriente es: ", RumboCorriente)
         print("La Velocidad de Máquinas es: ", VelocidadMaquinas)
         print("La Intensidad Horaria de la corriente es: ", IHC)
         print("El Angulo de Deriva es: ",AnguloDeriva)
         print("Alfa: ", Alfa)
         print(Beta)
         print("El Rumbo Efectivo es: ",RumboEfectivo)
         print("La Velocidad Efectiva es: ", VelocidadEfectiva)
         salir=True

### Introducir tabla con los valores calculados

print ("Fin de la Estima")