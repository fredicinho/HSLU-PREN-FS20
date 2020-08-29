import datetime
import threading
from numpy.random import seed
from numpy.random import randint
import time
from enum import Enum


class State(Enum):
    INITIALIZE = 1
    TURN_LEFT = 2
    TURN_RIGHT = 3
    GO_STRAIGHT_MAX = 4
    GO_STRAIGHT_HALF = 5
    GO_STRAIGHT_QUARTER = 6
    BYPASS_PYLONE = 7


class SensorType(Enum):
    DISTANCE_FRONT1 = 1
    DISTANCE_FRONT2 = 2
    DISTANCE_SIDE = 3
    MAGNET = 4
    BUTTON = 5
    CAMERA = 6
    NON_EXISTEND = 7


class derGeraet:
    def __init__(self):
        self.countOfMadeRounds = 0
        self.actualVelocity = 0.0
        self.timeStarted = datetime.datetime.now()
        self.timeFirstRoundEnded = None
        self.timeSecondRoundEnded = None
        self.timeThirdRoundEnded = None
        self.state = State.INITIALIZE
        self.pyloneAmUmfahren = False
        seed(1)

    def turnRight(self, xGrad):
        pass
        # Nach rechts drehen um xGrad (Winkel in Grad)
        # print('Turn right without speed and tilt of {} degrees!'.format(xGrad))

    def turnLeft(self, xGrad):
        pass
        # Nach links drehen um xGrad (Winkel in Grad)
        # print('Turn left without speed and tilt of {} degrees!'.format(xGrad))

    def turnRightWithSpeed(self, xGrad, speed):
        # Nach Rechts fahren mit Geschwindigkeit (Winkel in Grad, Geschwindigkeit in m/s)
        # print('Turn right with speed of {} and tilt of {}'.format(speed, xGrad))
        self.actualVelocity = speed

    def turnLeftWithSpeed(self, xGrad, speed):
        # Nach Links fahren mit Geschwindigkeit (Winkel in Grad, Geschwindigkeit in m/s)
        # print('Turn left with speed of {} and tilt of {}'.format(speed, xGrad))
        self.actualVelocity = speed

    def goStraight(self):
        # Geradeaus fahren mit Standardgeschwindigkeit
        # print('Go Straight with 2 m/s')
        self.actualVelocity = 2.0

    def goStraightWithControlledSpeed(self, speed):
        # Geradeaus fahren mit kontrollierter Geschwindigkeit
        # print('Go Straight with controlled speed of {}'.format(speed))
        self.actualVelocity = speed

    def breaking(self):
        # Ist staatisch und somit blockierend!
        # print("Breaking!!! Speed is now 0.0")
        self.actualVelocity = 0.0

    def bypassPylone(self):
        self.pyloneAmUmfahren = True
        # Ist staatisch, setze ein Flag damit Automat überprüfen kann, ob er weitermachen kann!
        # Dauer der Umfahrung = 3 Sekunden
        print(
            "Bypassing Pylone now. Going 0.5m straight, turning 30 degrees to the left and going again 0.3m straight.")
        time.sleep(8)
        self.pyloneAmUmfahren = False

    def toCloseToPylone(self):
        # Ist staatisch und somit blockierend!
        print("To Close to pylone. Going 0.3m back and turning to the right 20 degrees.")


"""
Containerobjekt für kritische Daten
Daten, welche den Threshold der Sensoren über-/unterschritten haben, werden hier gesammelt und evaluiert.

parameters:
    derGeraet: das Geräteobjekt, welches gesteuert werden soll.

@author Frederico Fischer
"""


class sensorData:
    def __init__(self, derGeraet, breiteDesBilder=300, thresholdOfDistanceToQuarter=500, thresholdOfDistanceToHalf=1000, thresholdOfPyloneDistance=100):
        self.startTime = time.perf_counter()
        print("Starting Timer is: {}".format(self.startTime))
        self.derGeraet = derGeraet
        self.criticalDataOfDistance1 = []
        self.criticalDataOfDistance2 = []
        self.criticalDataOfDistancePylone = []
        self.criticalDataOfMagnet = []
        self.standingPylons = []
        self.lyingPylons = []
        # TODO: Breite des Bildes wird in Kamera festgelegt. Muss irgendwie noch dem SensorData übergeben werden. Evt. über derGeraet?
        self.breiteDesBildes = breiteDesBilder
        self.linkesDrittel = self.breiteDesBildes // 3
        self.thresholdOfPyloneDistance = thresholdOfPyloneDistance
        self.thresholdOfDistanceToQuarter = thresholdOfDistanceToQuarter
        self.thresholdOfDistanceToHalf = thresholdOfDistanceToHalf


    def evaluateData(self):
        time.sleep(0.5)
        if self.derGeraet.state is State.INITIALIZE:
            if self.standingPylons:
                if self.standingPylons.pop() > self.linkesDrittel:
                    self.standingPylons.clear()
                    self.derGeraet.state = State.TURN_RIGHT
                    print("Wechsle zum Zustand: {}".format(State.TURN_RIGHT))
                    self.derGeraet.turnRight(20)
                else:
                    self.standingPylons.clear()
                    self.derGeraet.state = State.GO_STRAIGHT_MAX
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_MAX))
                    self.derGeraet.goStraight()
            else:
                self.derGeraet.state = State.TURN_LEFT
                print("Wechsle zum Zustand: {}".format(State.TURN_LEFT))
                self.derGeraet.turnLeft(20)

        elif self.derGeraet.state is State.TURN_LEFT:
            if self.standingPylons:
                if self.standingPylons.pop() > self.linkesDrittel:
                    self.standingPylons.clear()
                    self.derGeraet.state = State.TURN_RIGHT
                    print("Wechsle zum Zustand: {}".format(State.TURN_RIGHT))
                    self.derGeraet.turnRight(20)
                else:
                    self.standingPylons.clear()
                    self.derGeraet.state = State.GO_STRAIGHT_MAX
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_MAX))
                    self.derGeraet.goStraight()
            else:
                self.derGeraet.turnLeft(20)

        elif self.derGeraet.state is State.TURN_RIGHT:
            if self.standingPylons:
                if self.standingPylons.pop() > self.linkesDrittel:
                    self.standingPylons.clear()
                    self.derGeraet.turnRight(20)
                else:
                    self.standingPylons.clear()
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_MAX))
                    self.derGeraet.state = State.GO_STRAIGHT_MAX
                    self.derGeraet.goStraight()
            else:
                # TODO: Was ist wenn keine Pylone erkannt wird bzw. die erkannte Pylone verloren geht?
                # Evt. in State.TURN_LEFT wechseln?
                pass

        elif self.derGeraet.state is State.GO_STRAIGHT_MAX:
            # TODO: Prioritäten der Sensoren festlegen
            # Vorschlag: 1. Distanz Seite 1, 2. Distanz Vorne 1, 3. Bild event 2, 4. Bild event 1
            if self.criticalDataOfDistancePylone:
                print("Wechsle zum Zustand: {}".format(State.BYPASS_PYLONE))
                self.derGeraet.state = State.BYPASS_PYLONE
                criticalDataPylone = self.criticalDataOfDistancePylone.pop()
                self.criticalDataOfDistancePylone.clear()
                # Wenn Abstand kleiner 100mm, fahre zurück und drehe 20 Grad nach rechts.
                if criticalDataPylone < self.thresholdOfPyloneDistance:
                    self.derGeraet.toCloseToPylone()
                    # TODO: Setting timer because Method toCloseToPylone is Static?
                    self.derGeraet.bypassPylone()
                else:
                    self.derGeraet.bypassPylone()
            elif self.criticalDataOfDistance1:
                criticalData = self.criticalDataOfDistance1.pop()
                self.criticalDataOfDistance1.clear()
                if criticalData < self.thresholdOfDistanceToQuarter:
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_QUARTER))
                    self.clearData()
                    self.derGeraet.state = State.GO_STRAIGHT_QUARTER
                    self.derGeraet.goStraightWithControlledSpeed(0.5)
                elif criticalData < self.thresholdOfDistanceToHalf:
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_HALF))
                    self.derGeraet.state = State.GO_STRAIGHT_HALF
                    self.derGeraet.goStraightWithControlledSpeed(1.0)
            elif self.criticalDataOfDistance2:
                criticalData = self.criticalDataOfDistance2.pop()
                self.criticalDataOfDistance2.clear()
                if criticalData < self.thresholdOfDistanceToQuarter:
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_QUARTER))
                    self.derGeraet.state = State.GO_STRAIGHT_QUARTER
                    self.derGeraet.goStraightWithControlledSpeed(0.5)
                elif criticalData < self.thresholdOfDistanceToHalf:
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_HALF))
                    self.derGeraet.state = State.GO_STRAIGHT_HALF
                    self.derGeraet.goStraightWithControlledSpeed(1.0)
            elif self.standingPylons:
                if self.standingPylons.pop() > self.linkesDrittel:
                    self.standingPylons.clear()
                    print("Wechsle zum Zustand: {}".format(State.TURN_RIGHT))
                    self.derGeraet.state = State.TURN_RIGHT
                    # Need to break and then turning Right
                    self.derGeraet.breaking()
                    self.derGeraet.turnRight(20)
                else:
                    self.standingPylons.clear()
            elif not self.standingPylons:
                print("Wechsle zum Zustand: {}".format(State.TURN_LEFT))
                self.derGeraet.state = State.TURN_LEFT

        elif self.derGeraet.state is State.GO_STRAIGHT_HALF:
            # Prioritäten: 1. Neigung, 2. Bild event, 3. Distanz
            if self.criticalDataOfMagnet:
                # TODO: Werte vom Magnet werden zwischen -1 und 1 abgespeichert. Bei 0 hat er keine Neigung.
                # TODO: Soll der Wert noch überprüft werden? Eher nein?
                self.criticalDataOfMagnet.pop()
                self.criticalDataOfMagnet.clear()
                print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_QUARTER))
                self.derGeraet.state = State.GO_STRAIGHT_QUARTER
                self.derGeraet.goStraightWithControlledSpeed(0.5)
            elif self.criticalDataOfDistancePylone:
                print("Wechsle zum Zustand: {}".format(State.BYPASS_PYLONE))
                self.derGeraet.state = State.BYPASS_PYLONE
                # Wenn Abstand kleiner 10, fahre zurück und drehe 20 Grad nach rechts.
                criticalData = self.criticalDataOfDistancePylone.pop()
                self.criticalDataOfDistancePylone.clear()
                if criticalData < self.thresholdOfPyloneDistance:
                    self.derGeraet.toCloseToPylone()
                    self.derGeraet.bypassPylone()
                else:
                    self.derGeraet.bypassPylone()
            elif self.standingPylons:
                if self.standingPylons.pop() > self.linkesDrittel:
                    self.standingPylons.clear()
                    print("Wechsle zum Zustand: {}".format(State.TURN_RIGHT))
                    self.derGeraet.state = State.TURN_RIGHT
                    self.derGeraet.breaking()
                    self.derGeraet.turnRight(20)
                else:
                    self.standingPylons.clear()

        elif self.derGeraet.state is State.GO_STRAIGHT_QUARTER:
            if self.criticalDataOfMagnet:
                # Lösche Liste und warte kurz um zu sehen ob ein neuer kritischer Wert erfasst wird
                self.criticalDataOfMagnet.clear()
                time.sleep(1)
                if not self.criticalDataOfMagnet:
                    self.clearData()
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_MAX))
                    self.derGeraet.state = State.GO_STRAIGHT_MAX
                    self.derGeraet.goStraight()
                else:
                    # Schwellwert wurde nicht verlassen. Gerät ist Hinderniss immer noch am überwinden.
                    self.criticalDataOfMagnet.clear()
            else:
                time.sleep(1)
                if not self.criticalDataOfMagnet:
                    self.clearData()
                    print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_MAX))
                    self.derGeraet.state = State.GO_STRAIGHT_MAX
                else:
                    self.criticalDataOfMagnet.clear()

        elif self.derGeraet.state is State.BYPASS_PYLONE:
            # Überprüfe mit dem Flag ob Pylonenumfahrung abgeschlossen ist.
            # Else: bleibe im Zustand BYPASS_PYLONE
            if not self.derGeraet.pyloneAmUmfahren:
                self.clearData()
                print("Wechsle zum Zustand: {}".format(State.GO_STRAIGHT_MAX))
                self.derGeraet.state = State.GO_STRAIGHT_MAX
                self.derGeraet.goStraight()
            else:
                print("Bleibe im Zustand: {}".format(State.BYPASS_PYLONE))

    def clearData(self):
        self.criticalDataOfDistance1.clear()
        self.criticalDataOfDistance2.clear()
        self.criticalDataOfDistancePylone.clear()
        self.criticalDataOfMagnet.clear()
        self.standingPylons.clear()
        self.lyingPylons.clear()
        print("All lists are empty now!")


"""
Distanzobjekt für Distanzsensoren

parameters:
    sensorData = Container in dem Daten abgespeichert werden welche den Threshold über-/ bzw. unterschreiten
    sensorType = Sensor Typ (siehe Enum Typen "sensorType")
    threshold (optional) = unter/über diesem Wert wird Data in Container eingefügt.
    
@author Frederico Fischer
"""


class distance(threading.Thread):
    def __init__(self, sensorData, sensorType, threshold=1000):
        threading.Thread.__init__(self)
        self.sensorData = sensorData
        if sensorType != SensorType.DISTANCE_FRONT1 and sensorType != SensorType.DISTANCE_FRONT2 and sensorType != SensorType.DISTANCE_SIDE:
            print("SensorTyp of Distance is not settet correctly!")
            self.sensorType = SensorType.NON_EXISTEND
        else:
            self.sensorType = sensorType
        self.threshold = threshold
        if sensorType.value == 1:
            self.sensorDataList = sensorData.criticalDataOfDistance1
        elif sensorType.value == 2:
            self.sensorDataList = sensorData.criticalDataOfDistance2
        elif sensorType.value == 3:
            self.sensorDataList = sensorData.criticalDataOfDistancePylone
        else:
            print("Sensor is not of Type Distance! Will not send Data to SensorData-Object!")
        self.testData = 0
        # This array contains Data of the specified Sensor. Not used in the simulation!
        self.dataOfSensor = []

    def run(self):
        print("Sensor {} is starting now".format(self.sensorType.name))
        while True:
            # If counter > 11 Seconds, add Data to Sensor.
            difference = time.perf_counter() - self.sensorData.startTime
            if self.sensorType is SensorType.DISTANCE_FRONT1 or self.sensorType is SensorType.DISTANCE_FRONT2:
                if 28 > difference > 24:
                    self.testData = 999
                    if self.testData < self.threshold:
                        self.sensorDataList.append(self.testData)
                elif 30 > difference > 28:
                    self.testData = 499
                    if self.testData < self.threshold:
                        self.sensorDataList.append(self.testData)
            # Else sensorType is DISTANCE_SIDE
            else:
                if 8 < difference < 10:
                    self.testData = 110
                    self.sensorDataList.append(self.testData)
                elif difference >= 44:
                    self.testData = 110
                    self.sensorDataList.append(self.testData)


"""
Kompassobjekt für Kompasssensor

parameters:
    sensorData = Container in dem Daten abgespeichert werden welche den Threshold über-/ bzw. unterschreiten
    sensorType = Sensor Typ (siehe Enum Typen "sensorType")
    threshold = unter/über diesem Wert wird Data in Container eingefügt
    
@author Frederico Fischer
"""


class compass(threading.Thread):
    def __init__(self, sensorData, threshold=0.0):
        threading.Thread.__init__(self)
        self.sensorData = sensorData
        self.sensorDataList = sensorData.criticalDataOfMagnet
        self.sensorType = SensorType.MAGNET
        self.threshold = threshold
        # This List will contain the collected Data. Not used in the SimulationSoftware
        self.dataOfCompass = []
        self.testData = 0

    def run(self):
        print("Sensor {} is starting now".format(self.sensorType.name))
        while True:
            # Sensor Reads Data in this Part. --> Add here your specified array!
            difference = time.perf_counter() - self.sensorData.startTime
            if 33 > difference > 29:
                self.testData = 0.5
                if self.testData != self.threshold:
                    self.sensorDataList.append(self.testData)



"""
Knopfobjekt für den Startknopf

parameters:
    sensorData = Container in dem Daten abgespeichert werden welche den Threshold über-/ bzw. unterschreiten
    sensorType = Sensor Typ (siehe Enum Typen "sensorType")
    threshold = unter/über diesem Wert wird Data in Container eingefügt
    
@author Frederico Fischer
"""


class knopf:
    def __init__(self, derGeraet):
        self.sensorType = SensorType.BUTTON
        self.eingeschaltet = False
        self.derGeraet = derGeraet

    def drücken(self):
        if self.eingeschaltet:
            self.eingeschaltet = False
            self.derGeraet.breaking()
        else:
            self.eingeschaltet = True


"""
Kameraobjekt für die Kamera

parameters:
    sensorData = Container in dem Daten abgespeichert werden welche den Threshold über-/ bzw. unterschreiten
    sensorType = Sensor Typ (siehe Enum Typen "sensorType")

@author Frederico Fischer
"""


class camera(threading.Thread):
    def __init__(self, sensorData):
        threading.Thread.__init__(self)
        self.sensorData = sensorData
        self.sensorType = SensorType.CAMERA
        seed(1)
        self.standingPylons = sensorData.standingPylons
        self.lyingPylons = sensorData.lyingPylons
        # These arrays contains the Testdata. Not used in the SimulationSoftware
        self.randomNumbersOfFoundedPyloneStanding = []
        self.randomNumbersOfFoundedPyloneLying = []
        # TestData is just used for SimulationSoftware
        self.testData = 0

    def run(self):
        print("Sensor {} is starting now".format(self.sensorType.name))
        while True:
            # randint(0, 300, 2) generiert zwei Zufallszahlen zwischen 0 und 300
            # self.randomNumbersOfFoundedPyloneStanding = randint(0, 300, 2)
            # self.randomNumbersOfFoundedPyloneLying = randint(0, 300, 1)
            difference = time.perf_counter() - self.sensorData.startTime
            if difference < 4 or 17 < difference < 20 or 42 > difference > 41:
                self.standingPylons.clear()
                # do nothing because no pylone found
            elif 37 > difference > 34:
                self.testData = 200
                self.standingPylons.append(self.testData)
            else:
                self.testData = 50
                self.standingPylons.append(self.testData)
            # LyingPylons are not used in this SimulationSoftware
            # self.lyingPylons.append()
