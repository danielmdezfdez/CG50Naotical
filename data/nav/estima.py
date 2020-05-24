import math


"""
1. Navigation Basic Data
    a. Course
    b. Ellapsed Time
    c. Vessel Speed

2. Departure Position
    a. Latitude
    b. Longitude

3. Latitude Calculation
    a. Delta Latitude
    b. Final Latitude

4. Longitude Calculation
    a. Delta Longitude
    b. Final Longitude

5. Show Results
    a. Control Values
    b. Full Results

"""

def radians(value):
    return value*math.pi/180
    


# 1.A - COURSE
vessel_course=float(input("Course: "))

vessel_course_radians=float(radians(vessel_course))


# 1.B - ELLAPSED TIME
ellapsed_time=0

print("Ellapsed Time")
ellapsed_time_hours=float(input("Hours:"))
ellapsed_time_minutes=float(input("Minutes: "))
ellapsed_time_seconds=float(input("Seconds: "))

ellapsed_time=float(ellapsed_time_hours+(ellapsed_time_minutes/60)+(ellapsed_time_seconds/3600))

# 1.C - VESSEL SPEED
vessel_speed=0

print("Vessel Speed")
vessel_speed=float(input("Speed (kn):"))




# 2 - DEPARTURE POSITION
# 2.A - LATITUDE
latitude_inicial=0

latitude_inicial_sign=str(input("Sign:"))
latitude_inicial_degrees=float(input("Degrees: "))
latitude_inicial_minutes=float(input("Minutes: "))

if latitude_inicial_sign=="N" or latitude_inicial_sign=="+":
    latitude_inicial=float(latitude_inicial_degrees+(latitude_inicial_minutes/60))
elif latitude_inicial_sign=="S" or latitude_inicial_sign=="-":
    latitude_inicial=float(-1*(latitude_inicial_degrees+(latitude_inicial_minutes/60)))


# 2.B - LONGITUDE
print("Longitude")

longitude_inicial=0
longitude_inicial_sign=input("Sign:")
longitude_inicial_degrees=float(input("Degrees: "))
longitude_inicial_minutes=float(input("Minutes: "))

if longitude_inicial_sign=="E" or longitude_inicial_sign=="+":
    longitude_inicial=float(longitude_inicial_degrees+(longitude_inicial_minutes/60))
elif longitude_inicial_sign=="W" or longitude_inicial_sign=="-":
    longitude_inicial=float(-1*(longitude_inicial_degrees+(longitude_inicial_minutes/60)))




# 3 - LATITUDE CALCULATION
# 3.A - DELTA LATITUDE
delta_latitude=float((ellapsed_time*vessel_speed*math.cos(vessel_course_radians))/60.0)

# 3.B - FINAL LATITUDE
latitude_final=float(latitude_inicial+delta_latitude)

latitude_final_sign=0

if latitude_final>0:
    latitude_final_sign="N"
elif latitude_final<0:
    latitude_final_sign="S"

latitude_final_decimals=float(latitude_final-int(latitude_final))
latitude_final_minutes=float(latitude_final_decimals*60)

latitude_average=float((latitude_inicial+latitude_final)/2)

# 4 - LONGITUDE CALCULATION
# 4.A - DELTA LONGITUDE
apartamiento=float((ellapsed_time*vessel_speed*math.sin(vessel_course_radians))/60)

delta_longitude=float((apartamiento/math.cos(float(radians(latitude_average)))))


# 4.B - FINAL LONGITUDE
longitude_final=float(longitude_inicial+delta_longitude)

if longitude_final>0:
    longitude_final_sign="E" 
elif longitude_final<0:
    longitude_final_sign="W"

longitude_final_decimals=float(abs(longitude_final)-abs(int(longitude_final)))
longitude_final_minutes=float(longitude_final_decimals*60)



# 5 - RESULTS
# 5.A - Control Values
"""
print("Course", vessel_course)
print("Speed", vessel_speed)
print("Dela l", delta_latitude)
print("Delta L,", delta_longitude)
print("Average Latitude", latitude_average)
print("Apartamiento", apartamiento)
print("Distance", ellapsed_time*vessel_speed)
"""

"""
print("Sign")
print("Degrees")
print(int(latitude_final))
print("Minutes")
print(int(longitude_final_minutes))
"""

"""
print("Longitude")
print("Sign")
print("Degrees")
print(int(longitude_final))
print("Minutes")
print(int(longitude_final_minutes))
"""


# 5.B - RESULTS

# INITIAL DATA
print("Ellapsed Time")
print(ellapsed_time_hours,"h", ellapsed_time_minutes,"m", ellapsed_time_seconds, "s")

print("Vessel Course")
print(vessel_course,"º")

print("Sailed Distance")
print(ellapsed_time*vessel_speed)


# LATITUDE
print("Latitude")
print("Departing Latitude")
print(latitude_inicial_sign,latitude_inicial_degrees,"º",latitude_inicial_minutes,"'")

print("Δl (Dec. Degrees)")
print(delta_latitude,"º")

print("Arrival Latitude")
print(latitude_final_sign,int(latitude_final),"º",latitude_final_minutes,"'" )


# LONGITUDE
print("Longitude")
print("Departing Longitude")
print(longitude_inicial_sign,longitude_inicial_degrees,"º", longitude_inicial_minutes,"'")

print("Apartamiento (Minutes)")
print(apartamiento*60)

print("ΔL (Minutes)")
print(delta_longitude*60)

print("Arrival Longitude")
print(longitude_final_sign,int(longitude_final),"º",longitude_final_minutes,"'" )


