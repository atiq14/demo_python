# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:58:42 2019

@author: atiqurrahmb
"""

import pandas as pd

from matplotlib import pyplot as plt

sensor = pd.read_csv('Sensor_record_20190318_150727_AndroSensor.csv')

sensor.columns = ['ACCELEROMETERX', 'ACCELEROMETERY', 'ACCELEROMETERZ',
                  'GRAVITYX', 'GRAVITYY', 'GRAVITYZ',
                  'LINEARACCELERATIONX', 'LINEARACCELERATIONY',
                  'LINEARACCELERATIONZ', 'GYROSCOPEX', 'GYROSCOPEY',
                  'GYROSCOPEZ', 'LIGHTlux', 'MAGNETICX', 'MAGNETICY',
                  'MAGNETICZ', 'ORIENTATIONZ', 'ORIENTATIONX', 'ORIENTATIONY',
                  'PROXIMITYM', 'SOUNDDB', 'LOCATIONLatitude',
                  'LOCATIONLongitude', 'LOCATIONAltitude','LOCATIONAltitude',
                  'LOCATIONSpeed', 'LOCATIONAccuracy', 'LOCATIONORIENTATION',
                  'Satellitesinrange', 'Time', 'YYYY']
Time = sensor.Time * 1000
Sound_level = 0
Light_level = 0
Light_level1 = 0
Curtains_pos = 0 # means it on top, folded
sensor.head()
def noise_level():
    NOISE = sensor.SOUNDDB
    for x in NOISE:
        if x < 40:
            Sound_level = 0
        elif x > 40 and x < 60:
            Sound_level = 1
        
    return Sound_level

def room_noise_level():
    if Sound_level == 0:
        print("room noise is enough")
    elif Sound_level == 1:
        print("room has little Noise")
    else: print("Noise is high")

def noise_graph_analysis():
    NOISE = sensor.SOUNDDB
    sound = sensor.SOUNDDB -30
    plt.plot(Time, sound, 'b*-')
    plt.plot(Time, NOISE, 'r*-')
    plt.ylabel('Noise')
    plt.xlabel('Time')
    plt.draw()
# =============================================================================
# Sunlight 10,000 107,527
# Full Daylight 1,000 10,752
# Overcast Day 100 1,075
# Very Dark Day 10 107
# =============================================================================
result =[]
def light_level_in_room():
    light = sensor.LIGHTlux
    for x in light:
        if x > 500 and x < 700:
            Light_level = 1
            print("It's a workspace or Training room")
        elif x > 200 and x < 500:
            Light_level = 2
            print("It's a Stairwells or coridor room")
        elif x > 700 and x < 1500:
            Light_level = 2
            result.append(x)
            print("It's outside")
        else:
            Light_level = 3
            print("The room has very good lighting")
    return Light_level

def light_level_outside():
    light = sensor.LIGHTlux
    for x in light:
        if x > 500:
            Light_level1 = 1
        elif x > 200 and x < 500:
            Light_level1 = 2
        else:
            Light_level1 = 3
    return Light_level1
def room_determination_based_on_light_level():
    light = sensor.LIGHTlux
    for x in light:
        if x == 1:
            print("It's a workspace or Training room")
        elif x == 2:
            print("It's a Stairwells or coridor room")
        elif x == 3:
            print("The room has very good lighting")
        else:
            print("No value from Sensor")

def Curtains_pos():
    position = sensor.PROXIMITYM
    for x in position:
        if x == 0:
            print("Curtains is at top & folded")
            print(x)
        else:
            print("Curtains is at down")
            print(x)
def room_light_graph_analysis():
    light_lux = sensor.LIGHTlux
    plt.plot(Time, light_lux, 'b*-')
    plt.ylabel('LIGHT(lux)')
    plt.xlabel('Time')
    plt.draw()

acc = ((sensor.ACCELEROMETERX)**2 + 
       (sensor.ACCELEROMETERY)**2 + (sensor.ACCELEROMETERZ)**2)** 0.5
def curtain_position_graph_analysis():
    curtain_position = sensor.PROXIMITYM
    plt.plot(Time, curtain_position, 'b-')
    plt.ylabel('curtain_position')
    plt.xlabel('Time')
    plt.draw()




# =============================================================================
# room_noise_level()
# noise_graph_analysis()
# =============================================================================

dataframe = sensor[(sensor["LIGHTlux"] < 500) & (sensor["LIGHTlux"] > 200)]
dataframe.set_index = 'Time'
dataframe[['LIGHTlux']].plot(kind='bar')
print(dataframe)
#dataframe.describe()
# =============================================================================
# plt.plot(dataframe.Time, dataframe.LIGHTlux, 'b*-')
# plt.ylabel('curtain_position')
# plt.xlabel('Time')
# plt.draw()
# =============================================================================
# =============================================================================
# light_level_in_room()
# 
# print (result)
# =============================================================================

# =============================================================================
# Curtains_pos()
# =============================================================================


# =============================================================================
# print(sensor.LIGHTlux>500)
# #room_light_graph_analysis()
# #curtain_position_graph_analysis()
# plt.plot(Time, acc, 's',Time, sensor.ACCELEROMETERX, 'b', Time, sensor.ACCELEROMETERY, 'r', Time, sensor.ACCELEROMETERZ, 'g')
# plt.xlabel('X axis----->time')
# plt.ylabel('Y axis----->accelerometer')
# plt.title(' Accelerometer vs Time ')
# plt.legend('A')
# plt.show() 
# #noise_level()
# =============================================================================
#room_noise_level()
#noise_graph_analysis()
