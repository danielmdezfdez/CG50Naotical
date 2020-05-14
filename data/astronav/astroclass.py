
class position():
    def __init__(self):

        self.position=[]

        self.latitude=0.0
        self.latitude_sign=0.0
        self.latitude_degrees=0.0
        self.latitude_minutes_dec=0.0
        self.latitude_minutes_sex=0.0

        self.longitude=0.0
        self.longitude_sign=0.0
        self.longitude_degrees=0.0
        self.longitude_minute_dec=0.0
        self.longitude_minutes_sex=0.0



    def introduce_position_dec(self, name):
        print("Introduce  Latitude:")
        self.latitude_sign=input("Sign:")
        self.latitude_degrees=input("Degrees:")

        if self.latitude_sign=="+":
            self.latitude=self.latitude_degrees

        elif self.latitude_sign=="-":
            self.latitude=-1*(self.latitude_degrees)



        print("Introduce la Longitud:")
        self.longitude_sign=input("Signo:")
        self.longitude_degrees=input("Degrees:")

        if self.longitude_sign=="+":
            self.longitude=self.longitude_degrees

        elif self.longitude_sign=="-":
            self.longitude=-1*(self.longitude_degrees)

        
        # Define position within a list.
        self.position=[name, self.latitude, self.longitude]


    def introduce_position_sex(self):
        print("Introduce la Latitud:")
        self.latitude_sign=input("Signo:")
        self.latitude_degrees=input("Degrees:")
        self.latitude_minutes_sex=input("Minutes 1/60:")



        if self.latitude_sign=="+":
            self.latitude=self.latitude_degrees+(self.latitude_minutes_sex/60)

        elif self.latitude_sign=="-":
            self.latitude=-1*(self.latitude_degrees+(self.latitude_minutes_sex/60))

        print("Introduce la Longitud:")
        self.longitude_sign=input("Signo:")
        self.longitude_degrees=input("Degrees:")
        self.longitude_minutes_sex=input("Minutes 1/60:")

        if self.longitude_sign=="+":
            self.longitudee=self.longitude_degrees+(self.longitude_minutes_sex/60)

        if self.longitude_sign=="-":
            self.longitude=-1*(self.longitude_degrees+(self.longitude_minutes_sex/60))

        # Define position within a list
       # self.position=name, [self.latitude, self.longitude]


class angle():
    def __init__(self):
        self.angle=0.0
        self.sign=0
        self.degrees=0.0
        self.minutes_sex=0.0
        self.minutes_dec=0.0

    def introduce_angle_dec(self):
        self.sign=input("Signo:")
        self.degrees=float(input("Grados:"))

        if self.sign=="+":
            self.angle=self.degrees
            return(self.angle)
        if self.sign=="-":
            self.angle=-1*self.degrees
            return(self.angle)

    def introduce_angle_sex(self):
        self.sign=input("Signo:")
        self.degrees=float(input("Grados:"))
        self.minutes_sex=float(input("Minutos (1/60):"))

        if self.sign=="+":
            self.angle=self.degrees+(self.minutes_sex/60) 
            return(self.angle)

        if self.sign=="-":
            self.angle=-1*(self.degrees+(self.minutes_sex/60))
            return(self.angle)

    def angle_addition(self, angulo_primero, angulo_segundo):

        self.angle=angulo_primero+angulo_segundo
        return(self.angle)
        

class time():
    def __init__(self):
        self.year=0
        self.month=0
        self.day=0
        self.hour=0
        self.minute=0
        self.seconds=0
    
    def introduce_time(self):
        print("Introduce Time: ")
        self.year=input("Year:")
        self.month=input("Month:")
        self.day=input("Day:")
        self.hour=input("Hour:")
        self.minute=input("Minute:")
        self.seconds=input("Seconds:")

"""
# Fecha Inicial
print("Local Time:")
local_init_time=introduce_time()

# Starting Position
print("Choose an option:")
print ("1. DEG")
print ("2. SEX")

option=input("Option:")

if option==1:
    initial_position=introduce_position_dec()

elif option==2:
    initial_position=introduce_position_sex()






"""
# Recta de Alturas
AlturaInstrumental=angle()
AlturaInstrumental.introduce_angle_sex()

ErrorInstrumental=angle()
ErrorInstrumental.introduce_angle_sex()

AlturaObservada=angle()
AlturaObservada.angle_addition(AlturaInstrumental, ErrorInstrumental)


CorrecionSemidiametroParalaje=angle()
CorreccionAdicional=angle()
AlturaVerdadera=angle()