
"""
Program for Seakeeping General Calculations

Includes IMO Criteria and General Analysis
"""

"""
Here we ask for all Ship Particulars needed for ship calculations:
LOA:
Beam:
Displacement:
Balance_Factor:
Balance_K_Factor:
GMT_CSL:
Vessel Speed
"""
# Python Math Module Imported
import math

# Ship's Particulars
loa=float(input("LOA:")) # LOA
beam=float(input("Beam:")) # Ships Construction Beam (Manga de Trazado)
displacement=float(input("Displacement:")) # Desplazamiento del Buque
GMT_CSL=float(input("GMt CSL: ")) # Distance from G to M (Transversal)

side=str(input("Side: ")) # S
balance_k_factor=float(input("Balance K: "))
balance_f_factor=float(input("Balance F (0.77): "))

# Vessel Speed
vessel_speed_knots=float(input("Speed (Kn): "))
vessel_speed_ms=float(vessel_speed_knots*1852/3600)

# Waves Angle
waves_angle_degrees=float(input("Angle (0 to 180):"))
waves_angle_radians=float(math.radians(waves_angle_degrees))

# Observers Data
distance_AB=float(input("Distance AB:"))
time=float(input("Time (s): "))




"""
WAVES CALCULATIONS
"""

# Wave Apparent Speed
wave_apparent_speed=float(abs((distance_AB*math.cos(waves_angle_radians))/time))

# Wave Speed
wave_speed=float(wave_apparent_speed-(vessel_speed_ms*math.cos(waves_angle_radians)))

# Wave Length
wave_length=float((wave_speed/1.25)**2)

# Projected Wave Lenght
projected_wave_lenght=float(wave_length/math.cos(waves_angle_radians))

# Wave Period
wave_period=float(0.8*math.sqrt(wave_length))

# Wave Heigth
wave_height=float(wave_length/20)

# Apparent Period
wave_apparent_period=float(wave_length/(wave_speed+vessel_speed_ms*math.cos(waves_angle_radians)))

# Transversal Speed
wave_transversal_speed=float(wave_apparent_speed*math.sin(waves_angle_radians))

# Longitudinal Speed
wave_longitudinal_speed=float(wave_apparent_speed*math.cos(waves_angle_radians))


# Wave Calculations Results
print("Waves Particulars:")

print("Wave Apparent Speed:", wave_apparent_speed, " m/s")
print("Wave Speed:", wave_speed, " m/s")
print("Wave Length", wave_length, " m")
print("Projected Wave Lenght", projected_wave_lenght, " m")
print("Wave Period", wave_period, " s")
print("Wave Height", wave_height, " m")
print("Apparent Period", wave_apparent_period, " s")
print("Apparent Speed", wave_transversal_speed, " m/s")
print("Transversal Speed", wave_transversal_speed, " m/s")
print("Longitudinal Speed", wave_longitudinal_speed, "m/s")


"""
Now we will make ship calculations between waves.
"""
# Vessel Harmonic Periods
vessel_roll_period=float(balance_f_factor*beam/(math.sqrt(GMT_CSL)))
vessel_pitch_period=float(0.6*vessel_roll_period)

heel_average_degrees=float(5)
heel_average_radians=math.radians(heel_average_degrees)
heel_calculated=heel_average_radians*math.sin(waves_angle_radians)/(1-(vessel_roll_period/wave_apparent_period)**2)


# Vessel Displacements
vessel_displacement_crest=float(displacement*1+((math.pi*wave_height)/wave_length))
vessel_displacement_trough=float(displacement*1-((math.pi*wave_height)/wave_length))


print("Vessel Roll Period:", vessel_roll_period, "s")
print("Vessel Pitch Period:", vessel_pitch_period, " s")
print("Vessel Heel Angle:", heel_calculated, " deg")


"""
VESSELs SEAKEEPING CONDITIONS
1. Longitudinal Synchronism
    a. Condition 1 - Roll Period == Apparent Period
    b. Condition 2 - Projected Wave Lenght == 2x LOA

2. Transversal Synchronism
    a. Condition 1 - Pitch Period == Apparent Period
    b. Condition 2 - 0.5 Roll Period == Apparent Period

3. Surfing Effect
    a. Condition 1 - Angle Between 135 and 225.
    b. Condition 2 - Speed greater than

"""

# 1. Longitudinal Syncronism
print("Condition 1: ")
print("If Vessel Roll Period is approximately equal to Sea Apparent Period, there is Longitudinal Synchronism.")
print("Roll Period:", vessel_roll_period)
print("Pitch Period:", vessel_pitch_period)

print("Condition 2: ")
print("If wave apparent period is similar to 0.5 vessel pitch period, there will be longitudinal synchronism.")
print("2x LOA:", loa*2)
print("Projected Wave Lenght: ", projected_wave_lenght, " m")


# Transversal Synchronism
print("Condition 1: ")
print("If 2x Vessel LOA is similar to projected wave length, there will be longitudinal synchronism.")
print("2x LOA:", loa*2)


print("Condition 2: ")
print("If wave apparent period is similar to 0.5 vessel pitch period, there will be longitudinal synchronism.")
print("2x LOA:", loa*2)
print("Projected Wave Lenght: ", projected_wave_lenght, " m")