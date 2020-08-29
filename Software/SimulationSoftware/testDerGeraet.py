import unittest

from SimulationSoftware.derGeraet import *
import datetime


class derGeraetTest(unittest.TestCase):

    def testKonstruktor(self):
        self.gerät = derGeraet()
        self.assertEqual(self.gerät.countOfMadeRounds, 0)
        self.assertEqual(self.gerät.actualVelocity, 0.0)
        self.assertTrue(self.gerät.timeStarted <= datetime.datetime.now())
        self.assertIsNone(self.gerät.timeFirstRoundEnded)
        self.assertIsNone(self.gerät.timeSecondRoundEnded)
        self.assertIsNone(self.gerät.timeThirdRoundEnded)


class distanceTest(unittest.TestCase):

    def setUp(self):
        self.gerät = derGeraet()
        self.sensorDataTest = sensorData(self.gerät)

    def testKonstruktor1(self):
        self.distanceSensor = distance(self.sensorDataTest, SensorType.DISTANCE_FRONT1)
        self.assertEqual(self.distanceSensor.sensorType, SensorType.DISTANCE_FRONT1)
        self.assertEqual(self.distanceSensor.threshold, 1000)
        self.assertTrue(self.distanceSensor.sensorDataList is self.sensorDataTest.criticalDataOfDistance1)

    def testKonstruktor2(self):
        distanceSensor = distance(self.sensorDataTest, SensorType.DISTANCE_FRONT2, 20)
        self.assertEqual(distanceSensor.sensorType, SensorType.DISTANCE_FRONT2)
        self.assertEqual(distanceSensor.threshold, 20)
        self.assertTrue(distanceSensor.sensorDataList is self.sensorDataTest.criticalDataOfDistance2)

    def testKonstruktor3(self):
        distanceSensor = distance(self.sensorDataTest, SensorType.DISTANCE_SIDE, 20)
        self.assertEqual(distanceSensor.sensorType, SensorType.DISTANCE_SIDE)
        self.assertEqual(distanceSensor.threshold, 20)
        self.assertTrue(distanceSensor.sensorDataList is self.sensorDataTest.criticalDataOfDistancePylone)

    def testKonstruktor4(self):
        distanceSensor = distance(self.sensorDataTest, SensorType.MAGNET)
        self.assertTrue(distanceSensor.sensorType is SensorType.NON_EXISTEND)


class compassTest(unittest.TestCase):
    def setUp(self):
        self.gerät = derGeraet()
        self.sensorData = sensorData(self.gerät)

    def testKonstruktor1(self):
        self.compass = compass(self.sensorData)
        self.assertTrue(self.compass.sensorDataList is self.sensorData.criticalDataOfMagnet)
        self.assertTrue(self.compass.sensorType is SensorType.MAGNET)
        self.assertTrue(self.compass.threshold == 0)

    def testKonstruktor2(self):
        self.compass = compass(self.sensorData, 10)
        self.assertTrue(self.compass.threshold == 10)


class knopfTest(unittest.TestCase):
    def setUp(self):
        self.gerät = derGeraet()

    def testKonstruktor1(self):
        self.knopf = knopf(self.gerät)
        self.assertTrue(self.knopf.sensorType is SensorType.BUTTON)
        self.assertFalse(self.knopf.eingeschaltet)
        self.assertTrue(self.knopf.derGeraet is self.gerät)

    def testDrücken1(self):
        self.knopf = knopf(self.gerät)
        self.knopf.drücken()
        self.assertTrue(self.knopf.eingeschaltet)

    def testDrücken2(self):
        self.knopf = knopf(self.gerät)
        self.knopf.drücken()
        self.knopf.drücken()
        self.assertFalse(self.knopf.eingeschaltet)


class cameraTest(unittest.TestCase):

    def setUp(self):
        self.gerät = derGeraet()
        self.sensorData = sensorData(self.gerät)

    def testKonstruktor1(self):
        self.camera = camera(self.sensorData)
        self.assertTrue(self.camera.sensorType is SensorType.CAMERA)
        self.assertTrue(self.camera.standingPylons is self.sensorData.standingPylons)
        self.assertTrue(self.camera.lyingPylons is self.sensorData.lyingPylons)


class sensorDataTest(unittest.TestCase):
    def setUp(self):
        self.gerät = derGeraet()
        self.sensorData = sensorData(self.gerät)

    def testKonstruktor1(self):
        self.assertTrue(self.sensorData.derGeraet is self.gerät)
        self.assertTrue(len(self.sensorData.criticalDataOfDistance1) == 0)
        self.assertTrue(len(self.sensorData.criticalDataOfDistance2) == 0)
        self.assertTrue(len(self.sensorData.criticalDataOfMagnet) == 0)
        self.assertTrue(len(self.sensorData.criticalDataOfDistancePylone) == 0)
        self.assertTrue(len(self.sensorData.standingPylons) == 0)
        self.assertTrue(len(self.sensorData.lyingPylons) == 0)

    def testEvaluateDataInitializeToRight(self):
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel + 100)
        self.sensorData.evaluateData()
        self.assertTrue(self.sensorData.derGeraet.state is State.TURN_RIGHT)

    def testEvaluateDataInitializeToStraight(self):
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel)
        self.sensorData.evaluateData()
        self.assertTrue(self.sensorData.derGeraet.state is State.GO_STRAIGHT_MAX)

    def testEvaluateDataInitializeToLeft(self):
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.TURN_LEFT)

    def testEvaluateDataLeftToRight(self):
        self.gerät.state = State.TURN_LEFT
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel + 100)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.TURN_RIGHT)

    def testEvaluateDataLeftToStraight(self):
        self.gerät.state = State.TURN_LEFT
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_MAX)

    def testEvaluateDataLeftToLeft(self):
        self.gerät.state = State.TURN_LEFT
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.TURN_LEFT)

    def testEvaluateDataRightToRight(self):
        self.gerät.state = State.TURN_RIGHT
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.TURN_RIGHT)

    def testEvaluateDataRightToRight2(self):
        self.gerät.state = State.TURN_RIGHT
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel + 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.TURN_RIGHT)

    def testEvaluateDataRightToStraight(self):
        self.gerät.state = State.TURN_RIGHT
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel - 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_MAX)

    def testEvaluateDataStraightMaxToStraightMax(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_MAX)

    def testEvaluateDataStraightMaxToBypassPyloneWithToCloseToPylone(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.criticalDataOfDistancePylone.append(self.sensorData.thresholdOfPyloneDistance - 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.BYPASS_PYLONE)

    def testEvaluateDataStraightMaxToBypassPyloneWithoutToCloseToPylone(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.criticalDataOfDistancePylone.append(self.sensorData.thresholdOfPyloneDistance)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.BYPASS_PYLONE)

    def testEvaluateDataStraightMaxToStraightQuarter(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.criticalDataOfDistance1.append(self.sensorData.thresholdOfDistanceToQuarter - 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_QUARTER)

    def testEvaluateDataStraightMaxToStraightHalf(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.criticalDataOfDistance1.append(self.sensorData.thresholdOfDistanceToHalf - 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_HALF)

    def testEvaluateDataStraightMaxToStraightQuarter2(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.criticalDataOfDistance2.append(self.sensorData.thresholdOfDistanceToQuarter - 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_QUARTER)

    def testEvaluateDataStraightMaxToStraightHalf2(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.criticalDataOfDistance2.append(self.sensorData.thresholdOfDistanceToHalf - 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_HALF)

    def testEvaluateDataStraightMaxToTurnRight(self):
        self.gerät.state = State.GO_STRAIGHT_MAX
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel + 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.TURN_RIGHT)

    def testEvaluateDataStraightHalfToStraightQuarter(self):
        self.gerät.state = State.GO_STRAIGHT_HALF
        self.sensorData.criticalDataOfMagnet.append(1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_QUARTER)

    def testEvaluateDataStraightHalfToBypassPylone(self):
        self.gerät.state = State.GO_STRAIGHT_HALF
        self.sensorData.criticalDataOfDistancePylone.append(self.sensorData.thresholdOfPyloneDistance - 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.BYPASS_PYLONE)

    def testEvaluateDataStraightHalfToTurnRight(self):
        self.gerät.state = State.GO_STRAIGHT_HALF
        self.sensorData.standingPylons.append(self.sensorData.linkesDrittel + 1)
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.TURN_RIGHT)

    def testEvaluateDataStraightQuarterToStraightQuarter(self):
        self.gerät.state = State.GO_STRAIGHT_QUARTER
        self.sensorData.criticalDataOfMagnet.append(1)
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_QUARTER)

    def testEvaluateDataBypassPylone(self):
        self.gerät.state = State.BYPASS_PYLONE
        self.gerät.pyloneAmUmfahren = False
        self.sensorData.evaluateData()
        self.assertTrue(self.gerät.state is State.GO_STRAIGHT_MAX)


















    
if __name__ == "__main__": 
    unittest.main()

