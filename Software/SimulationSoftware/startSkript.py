#!/usr/bin/python
from SimulationSoftware.derGeraet import SensorType
from SimulationSoftware.derGeraet import derGeraet
from SimulationSoftware.derGeraet import distance
from SimulationSoftware.derGeraet import compass
from SimulationSoftware.derGeraet import knopf
from SimulationSoftware.derGeraet import camera
from SimulationSoftware.derGeraet import sensorData
import time

# Erzeuge Knopfobjekt
geraet = derGeraet()
knopf = knopf(geraet)

# Wird nur zum testen ausgeführt
knopf.drücken()

# Warte solange Knopf nicht gedrückt wurde
while not knopf.eingeschaltet:
    time.sleep(1)

# Sensorobjekte erstellen
sensorData = sensorData(geraet)
sensorVorne1 = distance(sensorData, SensorType.DISTANCE_FRONT1)
sensorVorne2 = distance(sensorData, SensorType.DISTANCE_FRONT2)
sensorSeite = distance(sensorData, SensorType.DISTANCE_SIDE, 100)
magnet = compass(sensorData)
camera = camera(sensorData)


# Sensoren und Kamera in eigenen Threads starten
if __name__ == '__main__':
    camera.start()
    sensorVorne1.start()
    sensorVorne2.start()
    sensorSeite.start()
    magnet.start()


while knopf.eingeschaltet:
    sensorData.evaluateData()
    if time.perf_counter() - sensorData.startTime > 55:
        knopf.drücken()


print('Job finished')
    

















