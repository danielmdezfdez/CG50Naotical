#Inicialización de Variables
#Anotation
import math

import math

def sen(grados):
    return math.sin(math.radians(grados))


def cos(grados):
    return math.sin(math.radians(grados)) 

def tan(grados):
    return math.tan(math.radians(grados))



####
# 
# Position=Lat and Longitud
# Lat=00"º"00","0"'"
# Long=000"º"00","0"'"
# 
# 
# 
# 






Norte="N"
South="S"
Este="E"
Oeste="W"


#Posición Inicial


print("Introduce tu posición en el siguuiente formato:")
20
SignoLatitudInicial=(0)
Latitud=float(0)

SignoLongitudInicial=(0)
Longitud=float(0)

#Variables para el cálculo de la Hora Civil del Orto/Ocaso


LatSupAlmanaque=float(0)
HoraCivilLatSupAlmanaque=float(0)
MinutosCivilLatSupAlmanaque=float(0)


LatInfAlmanaque=float(0)
HoraCivilLatInfAlmanaque=float(0)
MinutosCivilLatInfAlmanaque=float(0)

DiferenciaGradosAlmanaque=float(0)
DiferenciaGradosReal=float(0)



print("Hola, bienvenido a Navegación Astronómica. Vamos a empezar por introducir la situación de estima del buque: ")

Latitud = float(input("Latitud del Buque: "))
CardinalLatitudInicial=input("Latitud N/S? ")

if South == CardinalLatitudInicial:
    Latitud=-Latitud




Longitud = float(input("Longitud de Estima: "))
CardinalLongitudInicial=input("Introduce E/W: ")

if CardinalLatitudInicial == Oeste:
    Longitud=-Longitud


print(Latitud, Longitud)

## Cálculo de la Hora Civil de lugar del Orto
##
##

print("Ahora realizaremos la interpolación de la hora civil del orto. Introduce los valores pedidos: ")


# Datos del Almanaque - Latitud Superior a la de Estima

LatSupAlmanaque = float(input("Introduce la latitud superior (de mayor valor absoluto) del almanque: "))
HoraCivilLatSupAlmanaque = float(input("Introduce las horas del orto/ocaso para la Latitud Superior: "))
MinutosCivilLatSupAlmanaque = float(input("Introduce los minutos del orto/ocaso para la Latitud Superior: "))


# Datos del Almanaque - Latitud Inferior a la de Estima

LatInfAlmanaque = float(input("Introduce la latitud inferior (de menor valor absoluto) del almanque: "))
HoraCivilLatInfAlmanaque = float(input("Introduce las horas del orto/ocaso para la Latitud Inferior: "))
MinutosCivilLatInfAlmanaque = float(input("Introduce los minutos del orto/ocaso para la Latitud Inferior: "))

# Comprobación de Integridad de los Datos

while LatSupAlmanaque<LatInfAlmanaque :
    print("Los valores introducidos no son correctos. Repita la operación.")
    LatSupAlmanaque = float(input("Introduce la latitud superior (de mayor valor absoluto) del almanque: "))
    LatInfAlmanaque = float(input("Introduce la latitud inferior (de menor valor absoluto) del almanque: "))




#Interpolación
##


# Transformación de la Hora Civil (SEXAGESIMAL) a Hora Civil (CENTESIMAL)
HoraCivilOrtoLatSupCentesimal=float(float(HoraCivilLatSupAlmanaque))+((float(MinutosCivilLatSupAlmanaque)/60))
HoraCivilOrtoLatInfCentesimal=float(float(HoraCivilLatInfAlmanaque))+((float(MinutosCivilLatInfAlmanaque)/60))


# Calculo de la Diferencia de Tiempo entre las dos latitudes del Almanaque
DiferenciaHorasAlmanaqueCentesimal=float(float(HoraCivilOrtoLatSupCentesimal)-float(HoraCivilOrtoLatInfCentesimal))
print("La diferencia en tiempo entre ambas latitudes del alamanque es de: ",DiferenciaHorasAlmanaqueCentesimal)


# Cálculo de la Diferencia en Grados entre los valores de entrada en el Almanaque
DiferenciaGradosAlmanaque=float(float(LatSupAlmanaque)-float(LatInfAlmanaque))
print("La diferencia en grados entre ambas entradas es de: ", DiferenciaGradosAlmanaque)

# Diferencia en Grados entre la Latitud de Estima y la Latitud Inferior del Almanaque
DiferenciaGradosReal=float(float(Latitud)-float(LatInfAlmanaque))

# Cálculo de Parte Proporcional correspondiente

DiferenciaenTiempo=float(float((float(DiferenciaHorasAlmanaqueCentesimal)/float(DiferenciaGradosAlmanaque))*float(DiferenciaGradosReal)))

HoraCivildeLugar=float(float(HoraCivilLatInfAlmanaque)+float(DiferenciaenTiempo))
HCivilLugar=int(HoraCivildeLugar)
MCivilLugar=math.modf(HoraCivildeLugar)

MCivilLugarMinutos=(MCivilLugar*60)



HoraCivildeLugar=(HCivilLugar+","MCivilLugarMinutos,)


print("Hora civil del lugar es", HoraCivildeLugar)




#Variables para el cálculo de LT (Longitud en Tiempo)
LongitudEnTiempo=(Longitud/15)


#Expresión de resultados finales


DeclinacionSol=input(float("Introduce el valor de la declinación del Sol: "))



Azimut=(math.acos(math.sin(DeclinacionSol)))

CorreciondelAzimut=(math.radians(0.9)*(math.tan(Latitud)/math.sin(Azimut)))
