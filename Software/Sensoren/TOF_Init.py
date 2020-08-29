import RPi.GPIO as GPIO
import qwiic_vl53l1x
import time
import os


"""
Tof Initialisierung mit Libary von SparkFun.
  
Die ToF sollen auf verschiednene IIC Addressen verschoben werden.
ToF Nr. 1 -> 0x33 
ToF Nr. 2 -> 0x34
ToF Nr. 3 -> 0x35

und anschliessend abwechselnd zu Messen beginnen
"""

print('\n\n\n****START DER TOF INITIALISIERUNG****\n\n\n')

#Addressen der ToF
addr_current = 0x29
addr_desired_tof1 = 0x33
addr_desired_tof2 = 0x34
addr_desired_tof3 = 0x35

print('\nI2C Overview: Vor der Initialisierung\n')
os.system('i2cdetect -y 1')

#GPIO PIn Nummerierung und Zuweisung. 
#XSHUT (Shutdown Pin) der TOF auf HIGH -> ToF wird abgeschalten
#XSHUT der TOF auf LOW -> Normaler Betrieb  
GPIO.setmode(GPIO.BCM)

XSHUT_tof1 = 23
XSHUT_tof2 = 24
XSHUT_tof3 = 25

#Interrupt Pin der TOF
INT_tof1 = 17
INT_tof2 = 27
INT_tof3 = 22

GPIO.setup(XSHUT_tof1, GPIO.OUT)
GPIO.setup(XSHUT_tof2, GPIO.OUT)
GPIO.setup(XSHUT_tof3, GPIO.OUT)

GPIO.setup(INT_tof1, GPIO.IN)
GPIO.setup(INT_tof2, GPIO.IN)
GPIO.setup(INT_tof3, GPIO.IN)

GPIO.output(XSHUT_tof1, GPIO.LOW)
GPIO.output(XSHUT_tof2, GPIO.LOW)
GPIO.output(XSHUT_tof3, GPIO.LOW)

print('\nI2C Overview: Alle TOF abgeschaltet\n')
os.system('i2cdetect -y 1')



#####################################################################################################

distance_mode = 1 # 1 = short, 2 = long
polarity_mode = 0 # 0 = active low, 1 = active high

#Initialisierung ToF Nr. 1
print('\n\n*************************\nTOF Nr. 1 Init\n0x29 -> 0x33\n')
GPIO.setup(XSHUT_tof1,GPIO.IN)
tof1 = qwiic_vl53l1x.QwiicVL53L1X()
tof1.set_i2c_address(addr_desired_tof1)
tof1.sensor_init()
if (tof1.sensor_init() == None):		# Begin returns 0 on a good init
	print("Sensor tof1 online! I2C Address %s !\n" % hex(tof1.address))
	tof1.set_distance_mode(distance_mode)
	print("Distance Mode tof1(1 = short, 2 = long): %s" % tof1.get_distance_mode())
	print("Distance Threshold High: %s" % tof1.get_distance_threshold_high())
	print("Distance Threshold Low: %s" % tof1.get_distance_threshold_low())
	tof1.set_interrupt_polarity(polarity_mode)
	tof1.clear_interrupt()
	print("Interrupt Polarity: %s" % tof1.get_interrupt_polarity())
print('\n*************************\n')



#Initialisierung ToF Nr. 2
print('\n\n*************************\nTOF Nr. 2 Init\n0x29 -> 0x34\n')
GPIO.setup(XSHUT_tof2,GPIO.IN)
tof2 = qwiic_vl53l1x.QwiicVL53L1X()
tof2.set_i2c_address(addr_desired_tof2)
tof2.sensor_init()
if (tof2.sensor_init() == None):		# Begin returns 0 on a good init
	print("Sensor tof2 online! I2C Address %s !\n" % hex(tof2.address))
	tof2.set_distance_mode(distance_mode)
	print("Distance Mode (1 = short, 2 = long): %s" % tof2.get_distance_mode())
	print("Distance Threshold High: %s" % tof2.get_distance_threshold_high())
	print("Distance Threshold Low: %s" % tof2.get_distance_threshold_low())
	tof2.set_interrupt_polarity(polarity_mode)
	tof2.clear_interrupt()
	print("Interrupt Polarity: %s" % tof2.get_interrupt_polarity())
print('\n*************************\n')


#Initialisierung ToF Nr. 3
print('\n\n*************************\nTOF Nr. 3 Init\n0x29 -> 0x35\n')
GPIO.setup(XSHUT_tof3,GPIO.IN)
tof3 = qwiic_vl53l1x.QwiicVL53L1X()
tof3.set_i2c_address(addr_desired_tof3)
tof3.sensor_init()
if (tof3.sensor_init() == None):		# Begin returns 0 on a good init
	print("Sensor tof3 online! I2C Address %s !\n" % hex(tof3.address))
	tof3.set_distance_mode(distance_mode)
	print("Distance Mode (1 = short, 2 = long): %s" % tof3.get_distance_mode())
	print("Distance Threshold High: %s" % tof3.get_distance_threshold_high())
	print("Distance Threshold Low: %s" % tof3.get_distance_threshold_low())
	tof3.set_interrupt_polarity(polarity_mode)
	tof3.clear_interrupt()
	print("Interrupt Polarity: %s" % tof3.get_interrupt_polarity())
print('\n*************************\n')


print('\nI2C Overview: TOF Initialisiert\n')
os.system('i2cdetect -y 1')

#####################################################################################################



time.sleep(1)



#####################################################################################################

	
interrupt_distance_low = 1500
interrupt_distance_high = 3000
interrupt_mode = 0 #0 = below, 1=above, 2=out, 3=in

tof1.set_distance_threshold(interrupt_distance_low,interrupt_distance_high,interrupt_mode,1) #Interrupt ab 500mm
tof2.set_distance_threshold(interrupt_distance_low,interrupt_distance_high,interrupt_mode,1) #Interrupt ab 500mm
tof2.set_distance_threshold(interrupt_distance_low,interrupt_distance_high,interrupt_mode,1) #Interrupt ab 500mm


"""
tof1.set_inter_measurement_in_ms(100) 	#This function programs the intermeasurement period in ms. Default = 100ms
tof1.set_timing_budget_in_ms(15) 	#This function programs the timing budget in ms. Default = 100ms
"""

while True:
	tof1.start_ranging()
	"""
	tof2.start_ranging()
	tof3.start_ranging()
	"""
	distancetof1 = tof1.get_distance()
	print("Distance(mm) tof1: %s" % distancetof1)
	time.sleep(0.2)
	
	"""
	if GPIO.input(17) == GPIO.LOW:
		tof1.clear_interrupt()
		distancetof1 = tof1.get_distance()	 # Get the result of the measurement from the sensor
		if distancetof1 <= interrupt_distance_low:
			print("Distance(mm) tof1: %s" % distancetof1)
			time.sleep(0.2)
			
	elif GPIO.input(27) == GPIO.LOW:
		tof2.clear_interrupt()
		distancetof2 = tof2.get_distance()
		if distancetof2 <= interrupt_distance_low:
			print("Distance(mm) tof2: %s" % distancetof2)
			time.sleep(0.2)
	
	elif GPIO.input(22) == GPIO.LOW:
		tof3.clear_interrupt()
		distancetof3 = tof3.get_distance()
		if distancetof3 < interrupt_distance_low:
			print("Distance(mm) tof3: %s" % distancetof3)
			time.sleep(0.2)
	"""
		
    
    
	


